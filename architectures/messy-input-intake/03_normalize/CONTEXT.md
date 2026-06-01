# Stage 03: Normalize

## Purpose

Create a clean intake brief in the approved schema.

## Inputs

- `02_interpret/output/interpretation-[name]-[date].md`
- `_config/normalization-schema.md`
- `_config/before-you-trust-this.md`

## Process

1. Fill the schema exactly.
2. Include only facts supported by the input packet or confirmed context.
3. Label assumptions, open questions, and low-confidence facts.
4. Do not create a platform record or decide final ownership.
5. Prepare the brief for human review.

## Output

Write to `03_normalize/output/intake-brief-[name]-[date].md`.

## Done Looks Like

The brief is structured, source-aware, and ready for review or routing.
