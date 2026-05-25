# Stage 02: Evaluate

## Purpose
Measure the item against the team's decision criteria, run a rough sanity check, test for disqualifiers, and produce an advance / decline / need-more recommendation with a clear rationale. Fast and consistent — the same kind of item should get the same read every time.

## Inputs
- **01_intake/output/snapshot-[item-name]-[date].md**: The standardized item.
- **_config/decision-criteria.md**: What the team takes on. The fit standard.
- **_config/thresholds.md**: The go/no-go thresholds and automatic disqualifiers.
- **_config/evaluation-assumptions.md**: Standard rough-check assumptions for the quick evaluation.
- **_references/** (selectively): Prior evaluations of similar items, comparables.

## Process
1. Read the snapshot and the decision criteria. Assess fit on each dimension: type, scope, size, profile. Fit / partial / miss on each, with a one-line reason.
2. Run the disqualifier checks from thresholds.md. A disqualifier is automatic and ends the evaluation — an out-of-scope type, a condition the team will not take on, a size outside the range, a structure it will not do. If one trips, the recommendation is decline; say which disqualifier and stop.
3. If no disqualifier trips, run the rough check: a back-of-envelope assessment on the standard assumptions. This is a filter to catch items that cannot work even before the full analysis, not the analysis itself. Label every figure as a rough screen estimate.
4. Weigh fit and the rough check together against the thresholds. Form a recommendation: advance, decline, or need-more (a specific missing fact that would change the call).
5. Write the rationale so a reader who never saw the inbound materials understands why. The rationale is the product; the recommendation is one line of it.

## Output
Write to: 02_evaluate/output/evaluation-[item-name]-[date].md

Format:
```
# Evaluation: [Item Name]
Snapshot reference: [filename from intake]

## Recommendation
[Advance / Decline / Need-more] — one-line reason.

## Fit vs. the Bar
[Each criteria dimension: fit / partial / miss, with a reason.]

## Disqualifier Check
[Each threshold: clear / tripped. If tripped, which and why.]

## Rough Check (screen-level, not the full analysis)
[The back-of-envelope assessment on standard assumptions.
 Every figure labeled as a rough screen estimate. State the assumptions used.]

## Rationale
[Why this recommendation. Enough that a reader who never saw the inbound
 materials follows the logic. The strongest reasons for and against.]

## If Need-More
[The specific fact that would change the call, and where to get it.]
```

## Done Looks Like
A recommendation with a rationale that stands on its own, measured against the bar and the thresholds, with the rough check clearly marked as a filter. Fast enough that decisions keep pace with inbound flow.

## Common Failure Modes
- **Running the full analysis instead of evaluating.** The rough check is a filter. If you are building a real model here, you have left triage and entered the downstream work. Stop and pursue it properly downstream, or decline.
- **Letting a marginal rough check override a disqualifier.** A great-looking number on an item type the team does not take on is still a decline. Disqualifiers are automatic.
- **A recommendation with no rationale.** "Decline" with no reason teaches the team nothing and is not auditable. The rationale is the deliverable.

## Layer Annotation
L2 stage contract. The snapshot is L4 (this item). The decision criteria, thresholds, and evaluation assumptions from _config/ are L3. Prior evaluations and comparables from _references/ are L3.
