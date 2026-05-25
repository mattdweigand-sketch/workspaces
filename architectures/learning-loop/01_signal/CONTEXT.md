# Stage 01: Signal

## Purpose
Assemble the factual record for a competitive process that has resolved. Pull the facts from the source record, the debrief, and the final outcome into a structured record the analysis stage can reason over — without yet explaining anything. Facts in; the why comes later.

## Inputs
- **The trigger**: a competitive process has resolved. Name the case, the outcome (Won / Lost, or Withdrew-late as a flagged sub-case), and the date.
- **Source record** (the CRM, ERP, or the upstream workspace): how the opportunity reached us, our evaluation, the terms and offer we made, our proposal, the timeline through the final round.
- **Debrief**: what the counterparty or intermediary told us about why we won or lost, recorded as *stated* — kept distinct from the *actual* reason, which analysis will probe.
- **Final outcome**: the winning offer and terms, from the counterparty or public record.
- **_store/** (for context): any prior record involving this counterparty or domain, and records for similar processes, so this record is assembled with awareness of what is already known.
- **_config/taxonomy.md**: to tag the process per the controlled vocabulary.

## Process
1. Confirm the trigger: which case, won or lost (or withdrew-late), and the date.
2. Pull how the opportunity reached us: the intermediary or direct path, and the process type (broadly marketed / limited / direct / bilateral).
3. Record our thesis and what we offered: terms, structure, certainty/timing — from the source record, not from memory.
4. Record the winning outcome and terms, and compute our **gap** to it — in the key figure *and* in terms. State the source (shared or public record).
5. Record the counterparty's stated reason for the outcome, verbatim or close, as a logged fact — distinct from the assessed reason analysis will probe.
6. Note where in the process we gained or lost ground if known (first round, final round, last look).
7. Tag the process per the taxonomy: case type, size band, process type, counterparty type, counterparty/intermediary, domain, outcome.
8. Note what the record does not capture — gaps the analysis stage should know about (off-record color, a term we offered blind on, a relationship factor not logged).
9. Produce the record. State facts and their source. Do not analyze.

## Output
Write to: 01_signal/output/record-[case]-[date].md

Format:
```
# Record: [Case Name]
Outcome: [Won / Lost / Withdrew-late]   Resolved: [Date]
Case type: [from taxonomy]   Size band: [from taxonomy]
Process type: [from taxonomy]   Counterparty type: [from taxonomy]
Counterparty/intermediary: [from taxonomy]   Domain: [from taxonomy]

## How It Reached Us
[Intermediary or direct path. Process type.]

## Our Offer
[Thesis, terms, structure, certainty/timing. From the source record.]

## Winning Outcome & Our Gap
[Winning offer and terms. Our gap in the key figure AND in terms. Source: shared / public record.]

## Counterparty's Stated Reason
[As told to us, verbatim or close. A logged fact, not yet assessed.]

## Process Path
[Where we gained/lost ground, if known: first round, final round, last look.]

## Gaps
[What is not in the record that analysis should know about: off-record color,
 a term offered blind, an unlogged relationship factor.]
```

## Done Looks Like
A factual, source-grounded record of the process — our offer, the winning outcome, and our gap, tagged by the taxonomy — that the analysis stage can work from without re-querying the source system. No explanation of why — just what happened.

## Common Failure Modes
- **Reconstructing from memory.** The source record and outcome data are the source. A history assembled from impression is exactly the unreliable input that would corrupt the analysis and then the store. Pull it; do not recall it.
- **Conflating stated and actual reasons.** "They said we were just outbid" is a logged fact. Whether the key figure was the real reason is an analysis question. Keep them separate at this stage.
- **Inventing an outcome figure.** If the winning offer is not knowable, say so in Gaps — do not estimate a number and let it harden into the record.
- **Analyzing early.** The job is assembly. An early "why" shapes the record and undermines the comparability the whole workspace depends on.

## Layer Annotation
L2 stage contract. The source record, debrief, and outcome are L4 (this run). The store is read here for context (its L3-like role). The taxonomy from _config/ is L3.
