# Stage 03: Capture

## Purpose
Validate the proposed "why," then commit the record to the store and update the rolled-up patterns. This is where the loop closes — the per-run analysis becomes part of the workspace's memory. It is also the control gate: nothing enters the store as institutional memory without the team lead signing off on the causal claims.

## Inputs
- **02_analysis/output/analysis-[case]-[date].md**: The structured analysis with its stated-vs-assessed reason, proposed why, and confidence flags.
- **_config/store-schema.md**: The structure a stored record must follow.
- **_config/taxonomy.md**: To confirm the tags used for aggregation, including the controlled counterparty list.
- **_store/**: The destination — records/ and patterns.md — and the current state of both.

## Process
1. Human validation first. The team lead reviews the proposed "why," focusing on the claims the analysis flagged as low-confidence or pattern-contradicting — and especially anywhere the analysis is leaning on the counterparty's stated reason. Confirm, correct, or downgrade each causal claim. This step is not optional — it is the reason the store stays trustworthy and spin stays out of it.
2. Normalize the validated analysis into the store schema: the standard fields, the taxonomy tags, our offer vs. the winning outcome and the gap, the decisive dimension, the validated why with its final confidence, the stated-vs-assessed reason, the transferable lessons.
3. Write the record to `_store/records/[case]-[date].md`. Do not overwrite prior records; the store is append-only history.
4. Update `_store/patterns.md`: does this record strengthen a pattern (add to its evidence), extend one (a new counterparty type or domain), or contradict one (revise or qualify it)? Make the pattern change explicit and dated. A contradiction revises the pattern; it is not discarded to protect the existing story.
5. Note anything that should flow to another workspace now — a process type worth chasing, a strategy adjustment, a prioritization signal.
6. Record the capture in output.

## Output
Write to: 03_capture/output/captured-[case]-[date].md

```
# Capture Log: [Case Name]
Analysis reference: [filename]   Validated by: [name], [date]

## Stored
Record written to: _store/records/[case]-[date].md
Validation: [causal claims confirmed / corrected — note any changes, especially
 where the counterparty's stated reason was downgraded in favor of an assessed one]

## Patterns Updated
[Which pattern in _store/patterns.md changed and how:
 strengthened / extended / contradicted-and-revised. Dated.]

## Flag to Other Workspaces
[Anything the decision / strategy workspaces should pick up now, or "none."]
```

## Done Looks Like
A validated record in the store, append-only, and a patterns file that reflects it — strengthened, extended, or honestly revised. The loop has closed: the next run will read this back. Any cross-workspace signal is flagged.

## Common Failure Modes
- **Skipping validation.** Capturing the model's unvalidated "why" — or the counterparty's polite stated reason — turns the store into a pile of confident guesses that then drive real attempts. The human sign-off is the control that makes the whole workspace worth trusting.
- **Overwriting instead of appending.** The store is history. Revising a pattern is fine and expected; deleting a prior record erases the evidence trail and the ability to see how understanding changed.
- **Protecting the pattern from the evidence.** When a record contradicts an existing pattern, the pattern changes — not the record. Smoothing the contradiction away to keep a tidy story defeats the purpose of learning.

## Layer Annotation
L2 stage contract. The analysis is L4 (this run). The schema and taxonomy from _config/ are L3. The store is written here — its L4-like role — completing the loop whose L3-like role is read by future runs. This dual read/write relationship to _store/ is the structural signature of the learning loop.
