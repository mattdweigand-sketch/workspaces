# Stage 03: Distribution

## Purpose
Finalize the draft for delivery to readers. This stage handles the constraint pass, formatting, and preparation for each reader. It does NOT rewrite the narrative. If significant rewriting is needed, return to stage 02.

## Inputs
- **02_draft/output/draft-[report-type]-[account]-[period].md**: The approved draft.
- **_config/constraints.md**: The never-do list, including disclosure rules. Final pass to catch any remaining violations. The same file used in stage 02 — it must specify the required disclosures, footers, and forward-looking language this stage confirms are present.
- **Distribution requirements** (provided at task time): Reader list, per-reader figures source, delivery channel (portal, email), required disclosures or footers.

## AI vs. Platform
Per-reader figures merged at distribution come from the platform source, not from the model. AI formats and assembles; it does not generate or adjust a reader's numbers. Sign-off and approval before anything reaches a reader are human steps, not AI steps. See Constraint 09 (Platform Boundary).

## Process
1. Read the draft.
2. Read constraints.
3. Constraint pass: read the constraints file line by line and verify the report violates none of them. Confirm required disclosures, footers, and forward-looking language are present and correct. This is a checklist pass, not a creative pass.
4. Polish pass: tighten language and transitions. Do not add content. Do not restructure.
5. Format for delivery: apply the team's template, merge per-reader figures where the report is reader-specific, and prepare the file for the delivery channel.
6. Write final output.

## Output
Write to: 03_distribution/output/final-[report-type]-[account]-[period].md

Include delivery metadata:
```
# [Title]
Report type: [type]
Account: [name]   Period: [period/date]
Delivery channel: [reader portal / email]
Constraint pass: [pass / list any unresolved items]
Per-reader merge: [required: yes/no]

---

[Final content here]

---

## Delivery Notes (if applicable)
Disclosures/footers: [confirmed present]
Distribution list source: [reference]
Send date: [date]
```

## Done Looks Like
A communication that is ready to send through the reader portal or email. No further editing should be needed. If you find yourself editing the output of this stage before sending, either the constraint pass was insufficient or the draft stage produced something not ready for distribution.

## Common Failure Modes
- **Rewriting the narrative in a constraint pass.** This stage finalizes; it does not re-draft. If the report needs real rewriting, return it to stage 02. Quietly reworking the prose here bypasses the review the draft stage already cleared.
- **Treating the constraint pass as a creative read.** It is a line-by-line checklist against the constraints file — disclosures, footers, forward-looking language present and correct. Skimming for "feel" instead of checking each rule is how a missing disclosure ships.
- **Generating or adjusting per-reader figures.** Reader-specific numbers merge from the platform source, not the model. AI formats and assembles; if a per-reader figure looks wrong, fix it at the source, never in the draft.

## Layer Annotation
This is an L2 stage contract. The draft from 02_draft/output/ is L4 (working artifact, specific to this cycle). The constraints file is L3 (reference, stable across cycles). Distribution requirements are L4 (specific to this cycle and audience).
