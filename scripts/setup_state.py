#!/usr/bin/env python3
"""Small setup state helper for Kit."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "_shared-config"
SESSION = SHARED / "setup-session.json"
PROGRESS = SHARED / "setup-progress.md"
AGENTS = ROOT / "AGENTS.md"
SETUP = ROOT / "SETUP.md"


SESSION_TEMPLATE = {
    "current_phase": "organization_orientation",
    "current_step": "start",
    "organization_orientation": {},
    "value_triage": {},
    "selected_workflow": None,
    "current_question": None,
    "answers": {},
    "open_confirmations": [],
    "updated_at": None,
}


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now()
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_session():
    if not SESSION.exists():
        return dict(SESSION_TEMPLATE)
    try:
        data = json.loads(SESSION.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        data = {}
    merged = dict(SESSION_TEMPLATE)
    merged.update(data)
    return merged


def profile_paths():
    return [SHARED / "org-profile.md"]


def placeholder_hits():
    hits = []
    pattern = re.compile(r"\[[^\]\n]+\]")
    for path in profile_paths():
        if not path.exists():
            continue
        text = read_text(path)
        matches = sorted(set(pattern.findall(text)))
        if matches:
            hits.append({"path": rel(path), "placeholders": matches})
    return hits


def has_profile_placeholders():
    return bool(placeholder_hits())


def is_bootstrap_agents():
    text = read_text(AGENTS)
    return "# Kit" in text and "What this project is" in text and "Run setup" in text


def session_has_orientation(session):
    orientation = session.get("organization_orientation") or {}
    return any(str(value).strip() for value in orientation.values())


def session_has_selected_workflow(session):
    return bool(session.get("selected_workflow"))


def builder_questions_complete(session):
    answers = session.get("answers") or {}
    return bool(answers.get("builder_questions_complete"))


def status_value():
    session = load_session() if SESSION.exists() else {}
    if PROGRESS.exists() and not is_bootstrap_agents():
        return "complete"
    if SESSION.exists():
        if (
            session_has_orientation(session)
            and session_has_selected_workflow(session)
            and not builder_questions_complete(session)
        ):
            return "ready_to_build"
        return "in_progress"
    if not PROGRESS.exists() and not SESSION.exists() and has_profile_placeholders():
        return "not_started"
    if PROGRESS.exists():
        return "in_progress"
    return "not_started"


def parse_registry_rows():
    text = read_text(SETUP)
    match = re.search(
        r"## Workflow Registry\n(?P<body>.*?)(?:\n## |\Z)",
        text,
        flags=re.S,
    )
    if not match:
        return []
    rows = []
    for line in match.group("body").splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or "Business job" in line:
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) >= 3:
            rows.append(
                {
                    "business_job": cells[0],
                    "architecture": cells[1],
                    "builder": cells[2],
                }
            )
    return rows


def constraint_numbers_from_setup():
    text = read_text(SETUP)
    nums = set(re.findall(r"(?:^|[\s+(])([0-9]{2}) \(", text, flags=re.M))
    nums.update(re.findall(r"\b([0-9]{2})-", "\n".join(p.name for p in (ROOT / "constraints").glob("*.md"))))
    return sorted(nums)


def registry_report():
    rows = parse_registry_rows()
    missing = []
    for row in rows:
        arch = row["architecture"]
        builder = row["builder"]
        if arch != "none" and not (ROOT / "architectures" / arch).exists():
            missing.append({"business_job": row["business_job"], "missing": "architecture", "value": arch})
        if builder and not (ROOT / builder).exists():
            missing.append({"business_job": row["business_job"], "missing": "builder", "value": builder})
    constraint_files = sorted(p.name for p in (ROOT / "constraints").glob("*.md"))
    return {
        "registry_rows": len(rows),
        "architecture_rows": sum(1 for row in rows if row.get("architecture")),
        "builder_rows": sum(1 for row in rows if row.get("builder")),
        "constraint_files": len(constraint_files),
        "constraint_numbers": constraint_numbers_from_setup(),
        "missing_registry_references": missing,
    }


def doctor_report():
    checks = {
        "status": status_value(),
        "placeholders": placeholder_hits(),
        "setup_progress_exists": PROGRESS.exists(),
        "workspaces_exists": (ROOT / "workspaces").exists(),
        "bootstrap_agents": is_bootstrap_agents(),
        "registry": registry_report(),
    }
    checks["issues"] = []
    if checks["placeholders"]:
        checks["issues"].append("placeholders_detected")
    if not checks["setup_progress_exists"]:
        checks["issues"].append("setup_progress_missing")
    if not checks["workspaces_exists"]:
        checks["issues"].append("workspaces_missing")
    if checks["bootstrap_agents"]:
        checks["issues"].append("bootstrap_agents_map")
    if checks["registry"]["missing_registry_references"]:
        checks["issues"].append("registry_mismatch")
    return checks


def rel(path):
    return str(path.relative_to(ROOT))


def text_status(data):
    return data["status"]


def text_doctor(data):
    lines = [f"status: {data['status']}"]
    if data["issues"]:
        lines.append("issues: " + ", ".join(data["issues"]))
    else:
        lines.append("issues: none")
    registry = data["registry"]
    lines.append(
        "registry: "
        f"{registry['registry_rows']} workflows, "
        f"{registry['builder_rows']} builders, "
        f"{registry['constraint_files']} constraints"
    )
    return "\n".join(lines)


def emit(data, as_json, command):
    if as_json:
        print(json.dumps(data, indent=2, sort_keys=True))
    elif command == "doctor":
        print(text_doctor(data))
    elif command == "status":
        print(text_status(data))
    else:
        print("ok")


def command_status(args):
    return {"status": status_value()}


def command_doctor(args):
    return doctor_report()


def command_init_session(args):
    data = load_session()
    if args.phase and not data.get("current_phase"):
        data["current_phase"] = args.phase
    elif args.phase:
        data["current_phase"] = data.get("current_phase") or args.phase
    write_json(SESSION, data)
    return {"ok": True, "session": rel(SESSION), "status": status_value()}


def set_dotted(data, key, value):
    parts = key.split(".")
    target = data
    for part in parts[:-1]:
        current = target.get(part)
        if not isinstance(current, dict):
            current = {}
            target[part] = current
        target = current
    target[parts[-1]] = value


def command_record(args):
    data = load_session()
    if args.phase:
        data["current_phase"] = args.phase
    if args.step:
        data["current_step"] = args.step
    if args.workflow:
        data["selected_workflow"] = args.workflow
    if args.question:
        data["current_question"] = args.question
    for key_value in args.set or []:
        key, value = key_value
        set_dotted(data, key, value)
    for key_value in args.answer or []:
        key, value = key_value
        data.setdefault("answers", {})[key] = value
    for confirmation in args.confirmation or []:
        if confirmation not in data.setdefault("open_confirmations", []):
            data["open_confirmations"].append(confirmation)
    write_json(SESSION, data)
    return {"ok": True, "session": rel(SESSION), "status": status_value()}


def command_clear_session(args):
    if not SESSION.exists():
        return {"ok": True, "removed": False, "status": status_value()}
    if not (PROGRESS.exists() or args.restart):
        return {
            "ok": False,
            "removed": False,
            "error": "Refusing to clear setup-session.json before setup completes unless --restart is passed.",
            "status": status_value(),
        }
    SESSION.unlink()
    return {"ok": True, "removed": True, "status": status_value()}


def build_parser():
    parser = argparse.ArgumentParser(description="Kit setup state helper")
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("status", "doctor"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--json", action="store_true")

    init = sub.add_parser("init-session")
    init.add_argument("--json", action="store_true")
    init.add_argument("--phase", default="organization_orientation")

    record = sub.add_parser("record")
    record.add_argument("--json", action="store_true")
    record.add_argument("--phase")
    record.add_argument("--step")
    record.add_argument("--workflow")
    record.add_argument("--question")
    record.add_argument("--set", nargs=2, action="append", metavar=("KEY", "VALUE"))
    record.add_argument("--answer", nargs=2, action="append", metavar=("KEY", "VALUE"))
    record.add_argument("--confirmation", action="append")

    clear = sub.add_parser("clear-session")
    clear.add_argument("--json", action="store_true")
    clear.add_argument("--restart", action="store_true")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    commands = {
        "status": command_status,
        "doctor": command_doctor,
        "init-session": command_init_session,
        "record": command_record,
        "clear-session": command_clear_session,
    }
    data = commands[args.command](args)
    emit(data, args.json, args.command)
    if data.get("ok") is False:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
