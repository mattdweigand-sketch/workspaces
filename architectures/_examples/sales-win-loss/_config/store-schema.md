# Store Schema — Tessera sales win/loss review

The structure of a stored opportunity record and how patterns roll up. The capture stage
normalizes each validated analysis into this shape before writing it to `_store/records/`. A
consistent schema is what lets the store be queried rather than read one file at a time. L3
reference, loaded in stage 03.

## Record Schema (one per closed opportunity)

Every stored record carries:
- Opportunity name and taxonomy tags (outcome, ARR band, reason class, threading, competitor,
  source / segment)
- ARR value and close date (and sales-cycle length)
- Pipeline path — the stage the opportunity reached, and where it stalled or advanced
- Canonical-question answers (the comparable core)
- Stated reason (the rep's) vs. assessed real reason (kept distinct — the spin-defense)
- Validated reason, with final confidence level, and causal-vs-incidental factors marked
- The transferable play (what to do differently / what the win repeated) and any action owner
- Validator (revenue / sales lead) and validation date
- Links to the raw record and analysis files

## Patterns File (`_store/patterns.md`)

Each pattern entry carries:
- The pattern statement (e.g., "Single-threaded opportunities lose; we never reach the economic
  buyer")
- The segment(s) it applies to (reason class, threading, ARR band, competitor)
- The supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Rules:
- Records are append-only. Patterns are revised in place; every revision is dated and notes the
  evidence that drove it.
- A pattern is "stated" at **3+ supporting records**; below that it is "emerging."
- A contradicting record revises the pattern — it is not discarded to preserve it.

## Privacy / Handling

Win/loss records contain candid internal assessments (where our process broke down, our read on
specific accounts and the people in them). Access is limited to the revenue team and sales
leadership. What may be shared more widely is the pattern-level lesson and the transferable play,
not the raw account narrative or any named individual's behavior — in particular, a candid read
on a named prospect contact should not circulate outside the team.
