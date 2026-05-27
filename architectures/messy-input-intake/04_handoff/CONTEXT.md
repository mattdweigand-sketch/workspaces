# Stage 04: Handoff

## Purpose

Route the clean brief to the right owner, platform, or next architecture.

## Inputs

- `03_normalize/output/intake-brief-[name]-[date].md`
- `_config/routing-rules.md`
- `_config/platform-boundary.md`

## Process

1. Apply known routing rules.
2. Identify the platform that should own the final record.
3. Identify the human owner who approves record creation or next action.
4. If the case needs judgment, route to `decision-prep`, `exception-handling`, or `stakeholder-response-prep`.
5. Produce a handoff note. Do not write to external systems.

## Output

Write to `04_handoff/output/handoff-[name]-[date].md`.

## Done Looks Like

The next owner knows what to do, where the record belongs, and what remains unconfirmed.
