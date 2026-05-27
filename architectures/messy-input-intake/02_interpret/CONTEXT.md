# Stage 02: Interpret

## Purpose

Turn the captured input into an interpretation: intent, facts, uncertainty, gaps, and source confidence.

## Inputs

- `01_capture/output/input-packet-[name]-[date].md`
- `_config/input-types.md`
- `_config/platform-boundary.md`

## Process

1. Identify the likely intent or request.
2. Separate stated facts from assumptions and interpretations.
3. Note missing context that would change routing or response.
4. Assign confidence to each key fact: high, medium, low, or unverified.
5. Mark anything that requires human confirmation.

## Output

Write to `02_interpret/output/interpretation-[name]-[date].md`.

## Done Looks Like

The team can see what the input probably means, what is known, what is uncertain, and what must be confirmed.
