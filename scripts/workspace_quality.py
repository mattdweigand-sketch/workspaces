"""Deterministic quality checks for Workspaces markdown contracts."""

from __future__ import annotations

import re
from pathlib import Path


ALLOWED_AUTHORITIES = {"authoritative", "supporting", "background", "superseded", ""}
ALLOWED_CONFIDENCE = {"high", "medium", "low", "unverified", ""}
ALLOWED_REVIEW_STATUS = {"pass", "warning", "blocked", ""}
ALLOWED_OVERALL_STATUS = {"pass", "pass with warnings", "blocked pending human review"}
ALLOWED_CONTROL_STATUS = {"pass", "warning", "blocked", "open", ""}
ALLOWED_APPROVAL_STATE = {"approved", "approved with conditions", "not approved"}
SOURCE_REQUIRED_CLAIM_TYPES = {"number", "date", "chart", "commitment"}


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def rel(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def issue(root: Path, severity: str, check: str, path: Path, message: str) -> dict:
    return {
        "severity": severity,
        "check": check,
        "path": rel(root, path),
        "message": message,
    }


def normalize_header(value: str) -> str:
    value = value.strip().lower()
    value = value.replace(" or ", " ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def markdown_tables(text: str) -> list[dict]:
    lines = text.splitlines()
    tables = []
    index = 0
    while index < len(lines) - 1:
        if "|" not in lines[index] or not is_separator(lines[index + 1]):
            index += 1
            continue
        headers = split_table_row(lines[index])
        normalized = [normalize_header(header) for header in headers]
        rows = []
        index += 2
        while index < len(lines) and "|" in lines[index]:
            cells = split_table_row(lines[index])
            if len(cells) < len(headers):
                cells.extend([""] * (len(headers) - len(cells)))
            row = {normalized[i]: cells[i].strip() for i in range(len(headers))}
            rows.append(row)
            index += 1
        tables.append({"headers": normalized, "rows": rows})
    return tables


def table_with_headers(text: str, required_headers: set[str]) -> dict | None:
    for table in markdown_tables(text):
        if required_headers.issubset(set(table["headers"])):
            return table
    return None


def check_required_paths(root: Path, check: str, paths: list[Path]) -> list[dict]:
    results = []
    for path in paths:
        if not path.exists():
            results.append(issue(root, "error", check, path, "required file is missing"))
    return results


def parse_source_ids(path: Path) -> set[str]:
    text = read_text(path)
    source_ids = set()
    for table in markdown_tables(text):
        if "source_id" not in table["headers"]:
            continue
        for row in table["rows"]:
            source_id = row.get("source_id", "").strip()
            if source_id:
                source_ids.add(source_id)
    return source_ids


def source_scope_base(root: Path, path: Path) -> Path:
    parts = path.parts
    if "examples" in parts:
        index = parts.index("examples")
        if len(parts) > index + 1:
            return Path(*parts[: index + 2])
    if "Archive" in parts:
        index = parts.index("Archive")
        if len(parts) > index + 1:
            return Path(*parts[: index + 2])
    if "workspaces" in parts:
        index = parts.index("workspaces")
        if len(parts) > index + 1:
            return Path(*parts[: index + 2])
    return path.parent


def nearby_source_ids(root: Path, path: Path) -> set[str]:
    base = source_scope_base(root, path)
    source_ids = set()
    for candidate in base.rglob("*.md"):
        if "source-packet" in candidate.name or "verified-facts" in candidate.name:
            source_ids.update(parse_source_ids(candidate))
    return source_ids


def validate_source_packet(root: Path, path: Path) -> list[dict]:
    results = []
    required = {
        "source_id",
        "file_link",
        "type",
        "date",
        "owner",
        "source_system",
        "version",
        "authority",
    }
    table = table_with_headers(read_text(path), required)
    if not table:
        return [issue(root, "error", "source_packet", path, "source register table is missing required columns")]

    seen = set()
    for index, row in enumerate(table["rows"], start=1):
        source_id = row.get("source_id", "").strip()
        if not source_id:
            results.append(issue(root, "error", "source_packet", path, f"row {index} is missing Source ID"))
        elif source_id in seen:
            results.append(issue(root, "error", "source_packet", path, f"duplicate Source ID `{source_id}`"))
        elif not re.fullmatch(r"S[0-9]+", source_id):
            results.append(issue(root, "warning", "source_packet", path, f"Source ID `{source_id}` does not use S-number format"))
        seen.add(source_id)

        for field in ("file_link", "type", "date", "owner", "source_system", "version"):
            if not row.get(field, "").strip():
                results.append(issue(root, "error", "source_packet", path, f"`{source_id or 'row ' + str(index)}` is missing {field}"))
        authority = row.get("authority", "").strip().lower()
        if authority not in ALLOWED_AUTHORITIES:
            results.append(issue(root, "error", "source_packet", path, f"`{source_id}` has invalid authority `{authority}`"))
    return results


def validate_claim_map(root: Path, path: Path) -> list[dict]:
    results = []
    required = {
        "claim_id",
        "artifact_location",
        "claim_text",
        "claim_type",
        "source_id",
        "evidence_note",
        "source_authority",
        "confidence",
        "open_issue",
        "review_status",
        "human_owner",
    }
    table = table_with_headers(read_text(path), required)
    if not table:
        return [issue(root, "error", "claim_map", path, "claim evidence map table is missing required columns")]

    source_ids = nearby_source_ids(root, path)
    seen = set()
    for index, row in enumerate(table["rows"], start=1):
        claim_id = row.get("claim_id", "").strip()
        source_id = row.get("source_id", "").strip()
        claim_type = row.get("claim_type", "").strip().lower()
        authority = row.get("source_authority", "").strip().lower()
        confidence = row.get("confidence", "").strip().lower()
        status = row.get("review_status", "").strip().lower()
        owner = row.get("human_owner", "").strip()
        open_issue = row.get("open_issue", "").strip()

        if not claim_id:
            results.append(issue(root, "error", "claim_map", path, f"row {index} is missing Claim ID"))
        elif claim_id in seen:
            results.append(issue(root, "error", "claim_map", path, f"duplicate Claim ID `{claim_id}`"))
        seen.add(claim_id)

        if not row.get("claim_text", "").strip():
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id or 'row ' + str(index)}` is missing Claim Text"))
        if not status:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id or 'row ' + str(index)}` is missing Review Status"))
        elif status not in ALLOWED_REVIEW_STATUS:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` has invalid Review Status `{status}`"))
        if not owner:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id or 'row ' + str(index)}` is missing Human Owner"))
        if authority not in ALLOWED_AUTHORITIES:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` has invalid Source Authority `{authority}`"))
        if confidence not in ALLOWED_CONFIDENCE:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` has invalid Confidence `{confidence}`"))

        if claim_type in SOURCE_REQUIRED_CLAIM_TYPES and not source_id and status != "blocked":
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` is a {claim_type} claim without Source ID"))
        if source_id and source_ids and source_id not in source_ids:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` cites unknown Source ID `{source_id}`"))
        if not source_id and status != "blocked":
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` has no Source ID but is not blocked"))
        if not source_id and not open_issue:
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` has no Source ID and no Open Issue"))
        if authority == "superseded" and status != "blocked":
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` rests on a superseded source but is not blocked"))
        if claim_type == "assumption" and not (owner or open_issue):
            results.append(issue(root, "error", "claim_map", path, f"`{claim_id}` assumption lacks owner or approval path"))
    return results


def status_line(text: str) -> str:
    match = re.search(r"^Status:\s*`?([^`\n]+)`?", text, flags=re.M)
    if not match:
        return ""
    return match.group(1).strip().lower()


def validate_review_report(root: Path, path: Path) -> list[dict]:
    results = []
    text = read_text(path)
    status = status_line(text)
    if not status:
        results.append(issue(root, "error", "artifact_review", path, "Overall Status is missing"))
    elif status not in ALLOWED_OVERALL_STATUS:
        results.append(issue(root, "error", "artifact_review", path, f"invalid Overall Status `{status}`"))
    if "## Recommended Next Action" not in text:
        results.append(issue(root, "error", "artifact_review", path, "Recommended Next Action section is missing"))
    if status == "blocked pending human review" and "Required Owner" not in text and "Missing Human Confirmations" not in text:
        results.append(issue(root, "error", "artifact_review", path, "blocked report does not name required owners or confirmations"))
    return results


def validate_xlsx_control_map(root: Path, path: Path) -> list[dict]:
    results = []
    text = read_text(path)
    table = table_with_headers(text, {"control", "status"})
    if not table:
        return [issue(root, "error", "xlsx_control_map", path, "Required Controls table is missing")]
    for row in table["rows"]:
        control = row.get("control", "").strip() or "unnamed control"
        status = row.get("status", "").strip().lower()
        if status not in ALLOWED_CONTROL_STATUS:
            results.append(issue(root, "error", "xlsx_control_map", path, f"`{control}` has invalid Status `{status}`"))
    return results


def validate_human_approval_note(root: Path, path: Path) -> list[dict]:
    results = []
    text = read_text(path)
    status = status_line(text)
    if not status:
        return [issue(root, "error", "human_approval", path, "approval Status is missing")]
    if status not in ALLOWED_APPROVAL_STATE:
        results.append(issue(root, "error", "human_approval", path, f"invalid approval Status `{status}`"))
    if "approved use" not in text.lower() and "stated use" not in text.lower():
        results.append(issue(root, "warning", "human_approval", path, "approved use is not explicit"))
    return results


def check_architecture_contracts(root: Path, toolkit: Path, registry_rows: list[dict]) -> list[dict]:
    results = []
    for row in registry_rows:
        architecture = row.get("architecture")
        if not architecture or architecture == "none":
            continue
        arch_dir = toolkit / "architectures" / architecture
        results.extend(
            check_required_paths(
                root,
                "architecture_contract",
                [
                    arch_dir / "AGENTS.md",
                    arch_dir / "CONTEXT.md",
                    arch_dir / "_config" / "platform-boundary.md",
                    arch_dir / "_config" / "before-you-trust-this.md",
                ],
            )
        )
        context = read_text(arch_dir / "CONTEXT.md")
        if context and "## Platform Boundary" not in context:
            results.append(issue(root, "error", "architecture_contract", arch_dir / "CONTEXT.md", "Platform Boundary section is missing"))
    return results


def check_artifact_trust_contracts(root: Path) -> list[dict]:
    module = root / "modules" / "artifact-trust-layer"
    required = [
        module / "README.md",
        module / "_config" / "artifact-boundary.md",
        module / "_config" / "review-severity.md",
        module / "_config" / "office-risk-taxonomy.md",
        module / "_operating-model" / "architecture-attachment-guide.md",
        module / "_operating-model" / "workspace-output-conventions.md",
        module / "_operating-model" / "human-approval.md",
        module / "_templates" / "source-packet.md",
        module / "_templates" / "claim-evidence-map.md",
        module / "_templates" / "artifact-review-report.md",
        module / "_templates" / "human-approval-note.md",
        module / "_templates" / "xlsx-control-map.md",
        module / "_prompts" / "hostile-review.md",
        module / "_prompts" / "stale-number-review.md",
        module / "_prompts" / "formula-risk-review.md",
    ]
    results = check_required_paths(root, "artifact_trust_contract", required)
    severity_text = read_text(module / "_config" / "review-severity.md")
    for status in ALLOWED_OVERALL_STATUS:
        if status and status not in severity_text:
            results.append(issue(root, "error", "artifact_trust_contract", module / "_config" / "review-severity.md", f"status `{status}` is missing"))
    conventions = read_text(module / "_operating-model" / "workspace-output-conventions.md")
    for token in ("source-packet", "claim-evidence-map", "artifact-review-report", "human-approval-note"):
        if token not in conventions:
            results.append(issue(root, "error", "artifact_trust_contract", module / "_operating-model" / "workspace-output-conventions.md", f"`{token}` output convention is missing"))
    return results


def is_completed_artifact(path: Path) -> bool:
    parts = set(path.parts)
    return "examples" in parts or "output" in parts or "deliverables" in parts


def files_matching(root: Path, patterns: tuple[str, ...], completed_only: bool = False) -> list[Path]:
    files = []
    for path in root.rglob("*.md"):
        if completed_only and not is_completed_artifact(path):
            continue
        name = path.name
        if any(pattern in name for pattern in patterns):
            files.append(path)
    return sorted(files)


def add_check(checks: list[dict], name: str, files_checked: int, issues: list[dict]) -> None:
    errors = sum(1 for item in issues if item["severity"] == "error")
    warnings = sum(1 for item in issues if item["severity"] == "warning")
    checks.append(
        {
            "name": name,
            "files_checked": files_checked,
            "errors": errors,
            "warnings": warnings,
            "status": "fail" if errors else "pass",
        }
    )


def run_quality_checks(root: Path, toolkit: Path, registry_rows: list[dict]) -> dict:
    checks = []
    issues = []

    architecture_issues = check_architecture_contracts(root, toolkit, registry_rows)
    issues.extend(architecture_issues)
    add_check(checks, "architecture_contracts", len(registry_rows), architecture_issues)

    module_issues = check_artifact_trust_contracts(root)
    issues.extend(module_issues)
    add_check(checks, "artifact_trust_contracts", 1, module_issues)

    source_packets = files_matching(root, ("source-packet",), completed_only=True)
    source_issues = []
    for path in source_packets:
        source_issues.extend(validate_source_packet(root, path))
    issues.extend(source_issues)
    add_check(checks, "source_packets", len(source_packets), source_issues)

    claim_maps = files_matching(root, ("claim-evidence-map",), completed_only=True)
    claim_issues = []
    for path in claim_maps:
        claim_issues.extend(validate_claim_map(root, path))
    issues.extend(claim_issues)
    add_check(checks, "claim_maps", len(claim_maps), claim_issues)

    review_reports = files_matching(root, ("review-report", "hostile-review"), completed_only=True)
    review_issues = []
    for path in review_reports:
        review_issues.extend(validate_review_report(root, path))
    issues.extend(review_issues)
    add_check(checks, "artifact_review_reports", len(review_reports), review_issues)

    control_maps = files_matching(root, ("xlsx-control-map",), completed_only=True)
    control_issues = []
    for path in control_maps:
        control_issues.extend(validate_xlsx_control_map(root, path))
    issues.extend(control_issues)
    add_check(checks, "xlsx_control_maps", len(control_maps), control_issues)

    approval_notes = files_matching(root, ("human-approval-note",), completed_only=True)
    approval_issues = []
    for path in approval_notes:
        approval_issues.extend(validate_human_approval_note(root, path))
    issues.extend(approval_issues)
    add_check(checks, "human_approval_notes", len(approval_notes), approval_issues)

    return {
        "status": "fail" if any(item["severity"] == "error" for item in issues) else "pass",
        "check_count": len(checks),
        "error_count": sum(1 for item in issues if item["severity"] == "error"),
        "warning_count": sum(1 for item in issues if item["severity"] == "warning"),
        "checks": checks,
        "issues": issues,
    }
