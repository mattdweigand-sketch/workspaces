# Prompt: Stale Number Review

## Inputs

- Artifact.
- Source packet.
- Claim evidence map.

## Task

Review all numbers, dates, charts, and tables for source support and freshness.

## Process

1. Extract every number, date, chart, and table reference.
2. Map each item to a source ID where possible.
3. Record the source date or freshness date.
4. Flag figures from superseded, background, unknown, or stale sources.
5. Flag figures with no source.
6. Flag mixed-period comparisons.
7. Flag numbers that appear recomputed without a deterministic owner.
8. Label risk as `stale_number`, `mixed_actuals_plan`, `untraceable_chart`, or `polished_but_unsupported` where applicable.

## Output

Return a review table with item, location, source ID, risk type, freshness issue, severity, and owner.

## Rules

- Do not compute corrected values.
- Do not decide which conflicting number is right.
- Route unresolved issues to the source owner.
