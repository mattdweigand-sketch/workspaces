# Stage 02: Draft

## Purpose
Write the reader communication from the verified data pack. The output is a recurring report, scheduled notice, or statement cover ready for the constraint and formatting pass.

## Inputs
- **01_data/output/data-pack.md**: The verified numbers. This is your only source for figures. Do not pull a number from anywhere else. Every figure in the report traces to the pack.
- **_config/voice-and-tone.md**: The report's voice. It points to the team's core voice in `_shared-config/voice-and-tone.md` (the shared team voice — read that first to calibrate tone) and layers the report-specific register on top. Structural patterns are in format-patterns.md.
- **_config/format-patterns.md**: Structure for the report type. Read the section that matches what you are producing.
- **_config/constraints.md**: The never-do list, including compliance and disclosure rules. Read this every time. It must contain, at minimum: required disclosures and footers that appear on every communication; forward-looking-statement language the team uses; results-reporting rules; and any phrasing a reviewer has flagged. If this file is thin, stop and have the user confirm its contents with the reviewer before drafting.

## AI vs. Platform
Every figure in the draft traces to `01_data/output/data-pack.md`, which traces to the platform source of record. AI writes the language and the judgment around the numbers. It does not produce, reconcile, or recompute a figure. If a number is missing, return to stage 01; do not estimate it here. See Constraint 09 (Platform Boundary).

## Process
1. Read the data pack. Identify the narrative: what is the story of the period, supported by the numbers?
2. Read the team voice (`_shared-config/voice-and-tone.md`, reached via `_config/voice-and-tone.md`) and the format patterns for the report type.
3. Read constraints.
4. Write the draft. Follow the structure for the report type. Lead with what matters to the reader. State the numbers plainly and let the data carry the message.
5. Verify every figure against the data pack. A figure that is not in the pack does not belong in the report.
6. Self-check against constraints, especially disclosure and forward-looking language.
7. Write to output.

## Output
Write to: 02_draft/output/draft-[report-type]-[account]-[period].md

Format varies by report type:
- **Recurring report**: Opening summary, results, activity, outlook, what's next. Length matches the team's norm.
- **Scheduled notice**: Purpose, amount or detail, per-reader reference, due date, instructions reference. Tight and unambiguous.
- **Statement cover**: Source, detail reference, payment or action date, character note.

Include a header:
```
# [Title]
Report type: [recurring report / scheduled notice / statement cover]
Account: [name]   Period: [period/date]
Figures source: 01_data/output/data-pack.md
```

## Done Looks Like
A draft that can move to the constraint and formatting pass with only that work remaining. Every number ties to the data pack. If the distribution stage has to restructure the narrative, fix tone, or chase a figure, this stage needs tighter execution.

## Common Failure Modes
- **Opening with throat-clearing.** Cut the windup. Lead with the period result or the action being requested. The reader wants the headline first.
- **Putting a figure in the report that is not in the data pack.** Every number traces to the pack. If a figure is missing, go back to stage 01, do not estimate it in the draft.
- **Over-promising on forward-looking statements.** Results language is a compliance surface. If the constraints file flags forward-looking caution, keep projections qualified and grounded. Confidence is fine, guarantees are not.

## Layer Annotation
This is an L2 stage contract. It loads only when working in this stage. The data pack (from 01_data/output/) is L4, specific to this cycle. The voice, format, and constraint files (from _config/) are L3, stable across cycles.
