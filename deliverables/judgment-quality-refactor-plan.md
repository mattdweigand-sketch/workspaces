# Judgment Quality Refactor Plan

## Goal

Turn the judgment audit into a repo-native quality layer.

The refactor adds deterministic checks first. LLM judges stay as a documented next layer because the repo does not yet have enough recurring real-output signal to justify a judge runner.

## Scope

- Extend `scripts/setup_state.py doctor --json` with quality checks.
- Add reusable markdown validators for Workspaces contracts and Artifact Trust Layer outputs.
- Validate the existing sample and archived artifacts.
- Keep setup materialization unchanged. `scripts/setup_state.py` still tracks state and reports readiness. It does not copy module files or create workspaces.

## Layer 1: Deterministic Checks

Add checks for:

- Architecture contract shape.
- Artifact Trust Layer required files.
- Source packet completeness.
- Claim evidence map integrity.
- Artifact review report status and next action.
- Workbook control map status values.
- Human approval note status values when approval notes exist.

These checks catch missing structure, blank required fields, unknown source IDs, missing review statuses, invalid statuses, and missing owners.

## Layer 2: Judge Candidates

Do not implement these yet. Keep them as the next layer once deterministic checks produce clean evidence bundles:

- Architecture fit.
- Platform boundary.
- Authority and conflict handling.
- Hostile artifact review.
- Severity classification.

## Implementation Steps

1. Add `scripts/workspace_quality.py`.
2. Import it from `scripts/setup_state.py`.
3. Add `quality` to the doctor JSON payload.
4. Add `quality_checks_failed` to doctor issues only when deterministic checks produce errors.
5. Run `python3 scripts/setup_state.py doctor --json`.
6. Commit and publish through the Workspaces subtree remote.

## Done Criteria

- `python3 scripts/setup_state.py doctor --json` runs.
- Doctor output includes a `quality` object.
- Existing Artifact Trust examples pass deterministic checks.
- The archived Atlas diligence workspace passes deterministic checks.
- No LLM judge runner is added.
