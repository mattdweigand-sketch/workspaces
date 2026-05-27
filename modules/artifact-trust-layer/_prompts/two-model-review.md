# Prompt: Two-Model Review

## Inputs

- Draft artifact.
- Source packet.
- Claim evidence map.
- Artifact spec.
- Prior review report, if one exists.

## Task

Run an independent second-pass review. Treat the draft and first review as untrusted until checked against the source packet and artifact spec.

## Process

1. Check whether the artifact follows the artifact spec.
2. Check whether load-bearing claims appear in the claim evidence map.
3. Check whether each mapped claim is supported by the cited source.
4. Check whether the first review missed unsupported claims, stale numbers, formula risks, or sensitive commitments.
5. Name disagreements with the first pass.
6. Assign severity to any new issues.

## Output

Use `_templates/artifact-review-report.md`.

## Rules

- Do not rewrite the artifact.
- Do not assume the first model read sources correctly.
- Do not decide unresolved conflicts.
- Route conflicts and high-severity issues to the human owner.
