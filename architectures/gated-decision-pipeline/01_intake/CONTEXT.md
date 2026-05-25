# Stage 01: Intake

## Purpose
Turn an inbound item — however it arrived — into a standard snapshot the evaluate stage can assess on the same terms as every other item. Extract the facts; do not yet judge them.

## Inputs
- **The item**: brief, request, inbound note, intro, or listing. Paste or reference it here.
- **Source data** (your CRM, ERP, accounting platform, or data warehouse, if available): details, comparables, ownership.
- **_config/decision-criteria.md**: Referenced only to know which facts matter for the evaluation (so intake pulls the right fields), not to judge fit yet.

## Process
1. Read the item in full. If it came with a fuller data set, note provenance and which document is authoritative for each fact (Constraint 10, Source Provenance) — but do not deep-dive; this is still triage.
2. Extract the standard fields the evaluation needs: type, scope, size, the requester's stated plan, timeline, and how the item was sourced.
3. Pull comparable context from the data sources where available, tagged to source.
4. Note what is missing. An inbound note rarely has everything; flag the gaps the evaluation will have to reason around or request.
5. Produce the snapshot. State facts and their source. Do not editorialize on fit — that is the evaluate stage.

## Output
Write to: 01_intake/output/snapshot-[item-name]-[date].md

Format:
```
# Item Snapshot: [Item Name]

Source: [referrer / inbound / listing], received [date]
Sourced by: [name / relationship]

## The Item
[Type, scope, size, condition, key attributes.]

## The Ask
[What is being requested or proposed, structure, timeline.]

## Current State
[The facts as presented, each tagged to its source.]

## Requester's Plan
[What the requester says the opportunity is. Their case, captured as theirs.]

## Comparable Context
[Comparables and recent activity from the data sources, tagged to source.]

## Gaps
[What the materials do not say that the evaluation will need.]
```

## Done Looks Like
A snapshot that lets the evaluate stage assess this item on the same standard fields as every other item, with facts tagged to source and gaps named. No fit judgment yet.

## Common Failure Modes
- **Evaluating while capturing.** The job here is extraction, not judgment. Mixing them means the snapshot is shaped by an early opinion, which is exactly what consistent decisions are meant to avoid.
- **Repeating the requester's framing as fact.** The headline numbers and the "upside" are the requester's claims. Capture them as the requester's, not as established figures.
- **Over-investing.** This is a snapshot-level capture, not the full analysis. Pull the standard fields and the obvious comparables; stop there.

## Layer Annotation
L2 stage contract. The item materials and pulled data are L4 (this item). The decision criteria from _config/ are L3, referenced here only to know which fields to capture.
