# Prompt: Formula Risk Review

## Inputs

- Workbook description or extracted workbook structure.
- Source packet.
- XLSX control map.

## Task

Review workbook risk so the human owner knows where deterministic checks are needed.

## Process

1. Identify hardcoded numbers.
2. Identify formula-heavy sheets or ranges.
3. Identify missing checks.
4. Identify external links.
5. Identify hidden sheets, hidden rows, or hidden columns when surfaced.
6. Identify manual overrides.
7. Identify assumptions without owner or date.
8. Identify output tabs that do not clearly trace to source or calculation tabs.
9. Label risks as `formula_drift`, `static_model`, `mixed_actuals_plan`, `untraceable_chart`, or `assumption_as_fact` where applicable.

## Output

Use `_templates/xlsx-control-map.md` for the control review and summarize warnings by severity.

## Rules

- Do not certify the workbook.
- Do not become the calculation owner.
- State where Excel, a script, the source platform, or a human owner must run the exact check.
