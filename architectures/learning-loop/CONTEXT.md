# Workflow: Learning Loop

## Overview
A three-stage loop: Signal → Analysis → Capture, closing back into a store the next run reads from. Triggered each time a competitive process resolves — we won, or we lost. (Withdrawing late is allowed as a sub-case, flagged as a different lesson.) The stages are linear within a run, but the workflow is a loop across runs: each capture feeds the store, and the store feeds every future run and every workspace that sets strategy or chases a process.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_signal | Assemble the factual record | The trigger (process resolved), source record + debrief + outcome, store (for context) | 01_signal/output/ |
| 02_analysis | Forensic on why, against the canonical questions | Record, win/loss questions, store patterns | 02_analysis/output/ |
| 03_capture | Validate the why, write to the store, update patterns | Analysis, store schema, taxonomy | 03_capture/output/ + _store/ |

## How the Loop Closes
- 01 → 02: Signal produces the factual record — how the case reached us, what we offered, the winning outcome, and our gap, ending in the won/lost result. Analysis works from facts, never from impression. If analysis is reconstructing what happened rather than explaining why, signal did not finish.
- 02 → 03: Analysis produces the proposed "why," structured against the canonical questions, with the counterparty's *stated* reason held distinct from our *assessed* real reason. Capture is where a human validates that explanation and then commits it to the store. Unvalidated causal claims do not enter the store.
- 03 → _store → 01 (the loop): Capture writes the record into `_store/records/` and updates `_store/patterns.md`. The next run's signal and analysis stages read those back for context, so the team analyzes each new outcome against everything it has already learned. This back-edge is what makes it a loop rather than a queue.
- _store → other workspaces: `_store/patterns.md` is read by the decision and strategy workspaces. The loop pays off outside itself.

## Reference Material (in _config/)
- review-questions.md: The canonical question set every analysis answers, in the same order. This is what makes records comparable. Loaded in stage 02.
- taxonomy.md: The controlled tags (case type, size band, process type, counterparty type, counterparty, domain, outcome, decisive dimension) used to tag each record so patterns can aggregate. Loaded in stages 01 and 03.
- store-schema.md: The structure of a stored record and how patterns roll up. Loaded in stage 03.

## The Store (in _store/)
- records/: one structured record per resolved competitive process.
- patterns.md: the rolled-up, team-level intelligence — which processes we win, where our offers fall short, which dimension decides outcomes, whose feedback proves reliable — updated on each capture. This is the payoff-grain output.
- The store is read in stages 01 and 02 for context and written in stage 03. It is the workspace's memory.

## When to Add Stages
- **00_trigger** before signal: if you want an explicit step that detects resolved competitive processes from the source system and queues them, rather than running the loop manually per process.
- **04_review** after capture, periodically (not per-run): a standing pattern review that reads the whole store and writes a synthesis for the team ahead of a major push. This is the loop's intelligence consumed deliberately rather than incidentally.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model recall a process or assert a "why" without grounding — or to take the counterparty's polite stated reason at face value. The rule: rely on the record and source data for what happened, use AI to propose the why, keep a human on the causal claim. See Constraint 09 (Platform Boundary).

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| What happened: our offer, the timeline, the outcome, the counterparty of record | Platform / data foundation | Your CRM, ERP, or data warehouse + outcome data (shared or public record) |
| Assembling the record, structuring the analysis, proposing the why, detecting patterns across the store | AI | You, on top of governed data |
| Validating the causal explanation before it is captured | Human in the loop | The team lead |
| The accumulated store and its patterns | Team intelligence | This workspace (handle as confidential intelligence) |

The trap on this workflow: capturing the counterparty's polite stated reason ("they had a higher bid") as the real reason, when the assessed driver was something else ("they didn't trust our certainty"). AI proposes the explanation and keeps stated and assessed reasons distinct; the record and source data ground what happened; a human signs off on the why before it becomes memory.
