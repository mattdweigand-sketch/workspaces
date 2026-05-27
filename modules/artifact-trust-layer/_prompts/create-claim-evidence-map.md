# Prompt: Create Claim Evidence Map

## Inputs

- Draft artifact or artifact outline.
- Source packet.
- Artifact spec, if available.
- `_templates/claim-evidence-map.md`

## Task

Map every load-bearing claim in the artifact to evidence.

## Process

1. Extract factual claims, numbers, dates, charts, assumptions, interpretations, recommendations, and commitments.
2. Create one row for each load-bearing claim.
3. Tie each claim to a source ID where possible.
4. Label the claim type.
5. Mark confidence.
6. Flag unsupported claims.
7. Flag claims based on stale, superseded, or background sources.

## Output

Use `_templates/claim-evidence-map.md`.

## Rules

- Do not rewrite the artifact.
- Do not invent sources.
- Do not treat interpretation as fact.
- Commitments require human owner approval.
