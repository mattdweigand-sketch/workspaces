# Stage 03: Decide

## Purpose
Record the go/no-go on the evaluated item. On an advance, produce the handoff brief that seeds a downstream workspace. On a decline, log the decision and its reason. This is the gate between the funnel and a committed effort.

## Inputs
- **02_evaluate/output/evaluation-[item-name]-[date].md**: The evaluation and recommendation.
- **_references/**: The decline log and prior decisions, for consistency and the audit trail.

## Process
1. Read the evaluation. The recommendation is an input to the decision, not the decision — the decision-makers make the call.
2. Record the decision: advance, decline, or hold (revisit on a trigger or date).
3. On **advance**: produce the handoff brief. This is the bridge downstream — it carries the snapshot, the evaluation rationale, the fit assessment, and the open questions forward so the downstream workspace starts from the evaluation's work, not a blank page.
4. On **decline**: log the decline with its reason, tied to the evaluation rationale. Add it to the decline record in _references so the same item type gets a consistent answer and the team can see its rejection patterns over time.
5. On **hold**: note the trigger or date that would bring it back, so it does not silently disappear.
6. Record the decision in output.

## Output
Write to: 03_decide/output/decision-[item-name]-[date].md

For an advance:
```
# Decision: ADVANCE — [Item Name]
Evaluation reference: [filename]
Decided by: [name], on [date]

## Why Advance
[The decision rationale, building on the evaluation.]

## Handoff Brief (seeds the downstream workspace)
[The snapshot summary, the fit assessment, the evaluation rationale, the open
 questions, and the rough check — packaged as the starting point for a new
 downstream workspace. Copy this into that workspace's _config to begin.]
```

For a decline / hold:
```
# Decision: DECLINE (or HOLD) — [Item Name]
Evaluation reference: [filename]
Decided by: [name], on [date]

## Reason
[Why, tied to the evaluation rationale. For a hold: the trigger or date to revisit.]

## Logged
[Confirm added to the decline record in _references.]
```

## Done Looks Like
A recorded decision. On an advance, a handoff brief that a downstream workspace can start from directly. On a decline, a logged reason that keeps decisions consistent and auditable.

## Common Failure Modes
- **Treating the recommendation as the decision.** The evaluation recommends; the team decides. Recording a decision means a person owns it.
- **An advance with no handoff.** If "advance" does not produce the brief that seeds the downstream workspace, the evaluation's work is lost and the downstream stage restarts from the inbound materials. The handoff is the point.
- **An unlogged decline.** A decline that is not recorded breaks consistency and the audit trail, and erases the pattern data that makes the team a sharper decider over time.

## Layer Annotation
L2 stage contract. The evaluation is L4 (this item). The decline log in _references/ is L3 reference this stage writes back to, so the team's decision record compounds.
