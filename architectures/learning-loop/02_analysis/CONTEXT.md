# Stage 02: Analysis

## Purpose
Explain why the process resolved as it did, answering the canonical win/loss questions in the standard structure so this record is comparable to every other in the store. Propose the "why" — grounded in the record, tested against existing patterns, with the counterparty's *stated* reason held distinct from the *assessed* real reason — for a human to validate at capture.

## Inputs
- **01_signal/output/record-[case]-[date].md**: The factual record.
- **_config/review-questions.md**: The canonical question set. Answer all of them, in order. This is what makes the record comparable.
- **_store/patterns.md**: The current team-level patterns, so this outcome can be read as confirming, extending, or contradicting what is already known.

## Process
1. Read the record and the canonical questions.
2. Answer each canonical question from the record. Where the record does not support an answer, say so — do not fill the gap with a guess. A consistent "unknown" is more useful to the store than a fabricated cause.
3. **Separate the counterparty's stated reason from your assessed real reason (question 5), and say which you believe and why.** "Why you lost" feedback is often a polite fiction — "they had a higher bid" can mask "they didn't trust our certainty." This distinction is the central defense against poisoning the store with spin.
4. Identify the decisive dimension: price, certainty/speed, structure, terms, reputation/relationship, or timing. Separate causal from incidental — we may have had a wrinkle AND lost, but was that wrinkle the reason, or incidental to a decision driven by something else? Make the distinction explicit and flag your confidence.
5. Test against the store. Does this outcome fit an existing pattern in patterns.md, extend it, or contradict it? A contradiction is valuable — surface it loudly, because it is how patterns get corrected.
6. Identify what the team would do differently. Concrete and transferable: a relationship to build, a term to pre-clear, a faster path to certainty — not "do better." If lost, state what realistically would have changed it, and the point at which it would have stopped being a case we wanted. If won, state the decisive edge and what nearly lost it.
7. Mark every causal claim with a confidence level, so the human validator knows where to focus.
8. Produce the structured analysis.

## Output
Write to: 02_analysis/output/analysis-[case]-[date].md

Format:
```
# Win/Loss Analysis: [Case Name]
Record reference: [filename from signal]   Outcome: [Won / Lost / Withdrew-late]

## Canonical Questions
[Each question from review-questions.md, answered from the record.
 "Unknown" where unsupported. Same order every time.]

## Stated vs. Assessed Reason
[The counterparty's stated reason, then your assessed real reason, and why you
 believe the one you do. This is the spin-defense — do not collapse the two.]

## Why (proposed)
[The proposed explanation, with the decisive dimension named. Causal vs.
 incidental made explicit. Each causal claim marked with a confidence level.]

## Against the Store
[Does this confirm / extend / contradict an existing pattern? If it
 contradicts, say so plainly.]

## What We'd Do Differently
[Concrete, transferable lessons. If lost: what would have changed it and the
 walk-away point. If won: the decisive edge and what nearly lost it.]

## For the Validator
[The causal claims that most need a human check before capture, and why —
 especially anywhere you are taking the counterparty's word.]
```

## Done Looks Like
A structured analysis answering every canonical question, with the counterparty's stated reason held distinct from the assessed reason, a proposed "why" whose causal claims are explicit and confidence-marked, tested against the store, ready for a human to validate at capture.

## Common Failure Modes
- **Taking spin as the real reason.** The counterparty's stated "why you lost" is frequently a polite fiction. Recording it as the assessed cause is the single most damaging output here — it enters the store and skews every future attempt. Hold stated and assessed apart, and flag the claim for the validator.
- **Confident causation from thin evidence.** A plausible "why" stated with false certainty will enter the store and shape future attempts. Mark confidence honestly; prefer "unknown" to invention.
- **Answering the questions inconsistently.** If the canonical questions are answered loosely or in a different shape each time, the records stop being comparable and the store stops revealing patterns. Hold the structure.
- **Burying a contradiction.** When an outcome breaks an existing pattern, that is the most valuable thing in the analysis. Do not smooth it over to fit the story the store already tells.

## Layer Annotation
L2 stage contract. The record is L4 (this run). The canonical questions from _config/ are L3. The store patterns are read here for context (the store's L3-like role).
