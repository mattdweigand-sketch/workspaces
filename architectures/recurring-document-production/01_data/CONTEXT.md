# Stage 01: Data

## Purpose
Gather, organize, and verify the numbers for a reporting cycle. The output of this stage is a verified data pack that the draft stage can write from directly, without re-deriving any numbers.

## Inputs
- **Reporting brief**: What this cycle covers. Period, account, report type. Provide this when you enter the stage.
- **Platform export** (from your system of record): the figures of record, balances, activity, costs.
- **Source-level reports** (optional): segment performance, operational metrics, activity detail.
- **Prior report** (from _config/ or pasted): Last cycle's reported figures, for continuity and variance.

## Process
1. Pull all source data for the period. If more than one version of an export or report is present, confirm which is authoritative before pulling — never blend figures across versions (Constraint 10, Source Provenance).
2. Identify the headline figures the report has to carry. The top-line numbers a reader expects every period.
3. Reconcile each headline figure to its source. A number that cannot be tied to the platform export does not go in the pack.
4. Compute the variances against the prior period and note anything a reader will ask about. A drop, a change in direction, an anomaly.
5. Flag any figure that is preliminary, estimated, or subject to review. Those carry a label all the way to the report.
6. Produce the verified data pack in the output format below.

## Output
Write to: 01_data/output/data-pack.md

Format:
```
# Data Pack: [Account] [Period]

## Headline Figures
[The top-line numbers a reader expects. Each with its source and a tie-out note.]

## Segment-Level Detail
[Per segment or per area: value, key metric, key activity.]

## Variances vs. Prior Period
[What changed and why. The items a reader will notice and ask about.]

## Flags
[Preliminary, estimated, or unreviewed figures. Anything that needs a
 disclosure label in the report.]

## Reconciliation Status
[Tied to source: yes / no for each headline figure. Nothing reaches
 the draft stage marked "no."]
```

## Done Looks Like
A data pack where every headline figure is tied to source and every notable variance is explained. If the writer in stage 02 has to open the platform export to check a number, this stage did not finish its job.

## Common Failure Modes
- **Blending figures across export versions.** When two versions of an export exist, pick the authoritative one and pull every figure from it. Mixing one figure from one version with another from a second produces a pack that ties to nothing.
- **Letting a figure through without a tie-out.** A headline number with no source note is a number nobody can defend when a reader asks. Reconciliation status "no" never reaches the draft stage.
- **Dropping the flags.** Preliminary, estimated, and unreviewed labels have to travel with the figure all the way to the report. Stripping them here is how an unreviewed number reaches a reader with no caveat.

## Layer Annotation
This is an L2 stage contract. It loads only when working in this stage. The platform export and source reports loaded here are L4 (working artifacts specific to this cycle). The prior report from _config/ is L3 (reference, stable across cycles).
