# Stage 04: Evidence Brief

## Purpose

Explain what the source set supports, what it does not support, and what needs human resolution.

## Inputs

- `01_inventory/output/source-inventory-[name]-[date].md`
- `01_inventory/output/source-packet-[name]-[date].md`
- `02_authority/output/authority-map-[name]-[date].md`
- `03_conflicts_gaps/output/conflict-gap-log-[name]-[date].md`
- `../../modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `../../modules/artifact-trust-layer/_prompts/hostile-review.md`
- `_templates/artifact-trust/claim-evidence-map.md`
- `_templates/artifact-trust/artifact-review-report.md`

## Process

1. Summarize the source set.
2. List supported claims with source references.
3. List unsupported claims and gaps.
4. List conflicts requiring resolution.
5. Recommend the next architecture or human review step.

## Output

Write to `04_evidence_brief/output/evidence-brief-[name]-[date].md`.

When Artifact Trust Layer is attached, also write:

- `04_evidence_brief/output/claim-evidence-map-[name]-[date].md`
- `04_evidence_brief/output/artifact-review-report-[name]-[date].md`

## Done Looks Like

The next team can draft, decide, or respond knowing exactly what the evidence supports, which claims are blocked, and which human owners must resolve open issues.
