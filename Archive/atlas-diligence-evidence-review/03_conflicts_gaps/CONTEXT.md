# Stage 03: Conflicts And Gaps

## Purpose

Find conflicts, unsupported claims, stale versions, and missing context.

## Inputs

- `02_authority/output/authority-map-[name]-[date].md`
- Source set
- `_config/conflict-rules.md`

## Process

1. Compare key claims, numbers, dates, and decisions across sources.
2. Flag direct conflicts with both sources named.
3. Identify claims that lack support.
4. Identify source types that appear missing.
5. Escalate conflicts to a human or source-of-record owner.

## Output

Write to `03_conflicts_gaps/output/conflict-gap-log-[name]-[date].md`.

## Done Looks Like

No unsupported or conflicting claim can slip into the next stage invisibly.
