# Workflow: Gated Decision Pipeline

## Overview
Three-stage gated pipeline: Intake → Evaluate → Decide. Each item advances toward a single go/no-go: advance (hand off downstream) or decline (logged with a reason). The stages are lean by design — the point is a fast, consistent, defensible triage, not a full analysis.

## Stage Map

| Stage | Purpose | Key Inputs | Output Location | Decision Checkpoint |
|---|---|---|---|---|
| 01_intake | Normalize the inbound item into a standard snapshot | Brief, request, inbound note, source data | 01_intake/output/ | Enough captured to evaluate? |
| 02_evaluate | Fit against the bar, rough check, disqualifiers | Snapshot, decision criteria, thresholds, assumptions | 02_evaluate/output/ | Advance / decline / need-more |
| 03_decide | The go/no-go gate; handoff or decline log | Evaluation | 03_decide/output/ | Advance → downstream; Decline → logged |

## How Stages Connect
- 01 → 02: Intake produces a normalized snapshot of the item — the facts pulled out of the inbound materials into a standard shape. Evaluate works from the snapshot, so every item is judged on comparable terms regardless of how it was presented.
- 02 → 03: Evaluate produces a recommendation with rationale. Decide records the go/no-go. A "need-more" loops back to intake for the specific missing fact, not a vague "look closer."
- 03 → downstream (on advance): The decide stage produces a handoff brief that becomes the input to a new downstream workspace. The evaluation's work carries forward; the downstream stage does not restart it.
- 03 → _references (on decline): The decline and its reason are logged, building the decline record that keeps decisions consistent and creates the audit trail.

## Reference Material (in _config/)
- decision-criteria.md: What the team takes on — scope, type, size, profile. The standard the evaluation measures against. Loaded in stage 02.
- thresholds.md: The go/no-go thresholds and the automatic disqualifiers. Testable rules. Loaded in stage 02.
- evaluation-assumptions.md: Standard rough-check assumptions so every quick evaluation uses the same basis. Loaded in stage 02.

## Reference Material (in _references/)
- Prior evaluations and the decline log (consistency and audit trail), comparables, and the team's standards as they apply at the evaluation level.

## When to Add Stages
- **01a_authorization** for items that need a decision-maker's sign-off to even spend evaluation time.
- Keep the pipeline lean otherwise. The most common mistake here is over-building a process whose entire value is speed.

## AI vs. Platform: Where Each Step Lives

The temptation here is to treat the rough check as the full analysis, or to let the model "decide." The rule: rely on your data sources for the facts, use AI for the fit judgment and the rough filter, keep the decision human. See Constraint 09 (Platform Boundary).

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Item facts, source data, ownership, comparables | Platform / data foundation | Your CRM, ERP, accounting platform, or data warehouse |
| The real analysis — the numbers, the valuation | Deterministic / modeled | The model or spreadsheet that computes the numbers, downstream (not here) |
| Normalizing the item, assessing fit against the bar, the rough filter, surfacing disqualifiers, drafting the rationale | AI | You, on top of governed data |
| The advance / decline decision | Human in the loop | The decision-makers |

The trap on this workflow: presenting a rough screen-stage figure as if it were the full analysis, or letting the rough check override an obvious disqualifier. AI normalizes, filters, and surfaces; the facts come from your data sources; the real analysis is downstream; the advance/decline call is the team's.
