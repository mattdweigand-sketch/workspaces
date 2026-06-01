# Atlas Diligence Evidence Review

This workspace inspects Atlas Growth diligence source material before the team relies on it for IC materials.

Start with `CONTEXT.md`, then load only the stage file for the current step.

## Boundary

- Document systems own storage, permissions, version history, and audit.
- Deterministic tools own exact duplicate checks and file metadata extraction.
- This workspace owns source interpretation: authority, support, conflicts, gaps, and questions.
- A human resolves conflicts and approves claims.

## Attached Module

Artifact Trust Layer is attached by reference for source packets, claim evidence maps, and artifact review.

Reference these module files in place:

- `../../modules/artifact-trust-layer/README.md`
- `../../modules/artifact-trust-layer/_config/artifact-boundary.md`
- `../../modules/artifact-trust-layer/_config/review-severity.md`
- `../../modules/artifact-trust-layer/_prompts/build-source-packet.md`
- `../../modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `../../modules/artifact-trust-layer/_prompts/hostile-review.md`

Customized templates live in `_templates/artifact-trust/`.
