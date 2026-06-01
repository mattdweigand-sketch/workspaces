## Summary

What changed?

## Why

What problem does this solve?

## Area

- [ ] Architecture
- [ ] Module
- [ ] Setup
- [ ] Constraint
- [ ] Example
- [ ] Documentation

## Boundary Check

- [ ] The change keeps platforms as the source of truth.
- [ ] The change does not move calculations, permissions, delivery, or audit into Workspaces.
- [ ] Human approval remains explicit for decision-facing or external-facing work.
- [ ] Public examples are fictional or safe to publish.
- [ ] No secrets, customer data, or private workspace output is committed.

## Verification

- [ ] `python3 scripts/setup_state.py doctor --json` runs.
- [ ] Relevant docs, examples, or builder references were checked.
