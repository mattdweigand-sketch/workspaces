# Workflow: Recurring Document Production

## Overview
Three-stage pipeline: Data → Draft → Distribution. Each stage has a defined contract, explicit inputs, and a clear output location. Human reviews between stages. The data stage gates the others: nothing gets written until the numbers are verified.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_data | Gather and verify the numbers | Platform export, source reports, prior report | 01_data/output/ |
| 02_draft | Write the report or notice | Verified data pack, team voice (shared, via _config/voice-and-tone.md), format patterns, constraints | 02_draft/output/ |
| 03_distribution | Finalize and distribute | Approved draft, format spec, distribution list | 03_distribution/output/ |

## How Stages Connect
- 01 → 02: The verified data pack becomes the source for drafting. The draft stage reads the data pack and the variance notes, NOT the raw platform export. If the data stage did its job, the draft stage should never have to reconcile a number itself.
- 02 → 03: The approved draft becomes the distribution input. The distribution stage formats, applies the constraint pass, and prepares the report for each reader. It does not rewrite the narrative. If distribution is doing heavy rewriting, the draft stage needs tighter constraints.

## Reference Material (in _config/)
- voice-and-tone.md: Points to the team's shared voice (`_shared-config/voice-and-tone.md`) and adds the report register. Loaded in stage 02.
- format-patterns.md: Structure per report type (recurring report, scheduled notice, statement cover). Loaded in stage 02.
- constraints.md: The never-do list, including compliance and disclosure rules. Loaded in stages 02 and 03.

## When to Add Stages
Add a stage when you consistently find yourself doing a distinct type of work between two existing stages. If a reviewer always reads before distribution, add 02a_review or renumber. Do not add stages preemptively. Add them when the process demands it.

## AI vs. Platform: Where Each Step Lives

This is the workflow where the boundary is least negotiable. The numbers come from a governed source. AI writes the narrative around them. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09 (Platform Boundary).

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Verified figures of record, the books, the single source of truth, the audit trail | Platform / data foundation | Your system of record — the platform that owns the data |
| The allocation and roll-up math of record | Deterministic | The platform's calculation engine |
| Drafting the report narrative, explaining variances, summarizing activity, tailoring tone | AI | You, on top of governed data |
| Sign-off and approval before anything reaches a reader | Human in the loop | The team and its reviewer |

The trap on this workflow: asking AI to produce or "reconcile" a figure rather than to write about a figure the platform already verified. The data stage (01_data) exists to enforce exactly this. Every number in the report traces to the platform source, never to the model.
