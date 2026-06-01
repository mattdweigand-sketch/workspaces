# Messy Input Intake

This workspace turns unstructured inputs into a clean brief that a human can review or enter into the right platform.

Start with `CONTEXT.md`, then load only the stage file for the step you are running.

## Boundary

- Platforms own the final record, workflow state, permissions, and audit trail.
- Rules own routing where the routing criteria are known.
- This workspace owns interpretation before the record is clean: intent, facts, gaps, confidence, and handoff notes.
- A human approves any record creation or stakeholder-facing output.

## Structure

- `01_capture/`: gather the input set without judging it.
- `02_interpret/`: identify intent, facts, missing context, and source confidence.
- `03_normalize/`: produce the clean brief in a stable schema.
- `04_handoff/`: route to the platform, owner, or next architecture.
- `_config/`: input types, schema, routing rules, platform boundary, and open confirmations.
