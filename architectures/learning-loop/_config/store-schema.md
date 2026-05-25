# Store Schema

<!--
ANNOTATION: The structure of a stored record and how patterns roll up. The
capture stage normalizes each validated analysis into this shape before writing
it to _store/records/. A consistent schema is what lets the store be queried and
aggregated rather than just read one file at a time.

This is L3 reference, loaded in stage 03.
-->

## Record Schema (one per resolved process)
[The fields every stored record carries. Keep them stable. Example:
- Case name and taxonomy tags (case type, size band, process type, counterparty
  type, counterparty/intermediary, domain)
- Outcome (won / lost / withdrew-late) and date
- Our offer vs. the winning outcome, and the gap — in the key figure and in terms
- Decisive dimension
- Canonical-question answers (the comparable core)
- Validated why, with final confidence level
- Stated vs. assessed reason (kept distinct — the spin-defense)
- Transferable lessons
- Validator and validation date
- Links to the source record and analysis files]

## Patterns File (_store/patterns.md)
[How team-level patterns are structured and maintained. Each pattern entry should
carry:
- The pattern statement (e.g., "We lose limited processes on certainty, not price")
- The segment(s) it applies to (case type, process type, counterparty, decisive
  dimension)
- The supporting records (count and references)
- Confidence, and the date last updated
- Any contradicting records and how the pattern was qualified

Rules:
- Append-only for records; patterns are revised in place but every revision is
  dated and notes what evidence drove it.
- A pattern needs a stated minimum of supporting records before it is treated as
  more than a hypothesis — set that threshold here.
- A contradicting record revises the pattern; it does not get discarded to
  preserve the pattern.]

## Privacy / Handling
[Reminder: records contain sensitive intelligence — our behavior, our gap to the
winning outcome, and our candid read on specific counterparty relationships.
State here who may access the store and any redaction rules for anything that
leaves this workspace (e.g., what may flow to the strategy workspaces vs. what
stays internal to the team — in particular, our assessed-vs-stated read on a
named counterparty should not circulate outside the team).]
