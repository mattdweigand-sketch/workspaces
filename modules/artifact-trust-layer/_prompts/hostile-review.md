# Prompt: Hostile Review

## Inputs

- Artifact.
- Source packet.
- Claim evidence map.
- Artifact spec.
- Review severity config.
- Office risk taxonomy.

## Task

Review the artifact as if a skeptical approver, investor, auditor, committee member, or customer will challenge it.

## Process

1. Identify unsupported claims.
2. Identify stale figures.
3. Identify blended source versions.
4. Identify overconfident wording.
5. Identify missing caveats.
6. Identify assumptions presented as facts.
7. Identify claims that would be difficult to defend if challenged.
8. Label the risk type using `_config/office-risk-taxonomy.md` where possible.
9. Assign severity.

## Output

Use `_templates/artifact-review-report.md`.

## Rules

- Do not rewrite.
- Do not soften issues.
- Do not certify the artifact.
- Name the evidence gap and the owner needed to resolve it.
- Use `review_theater` when the artifact claims review but has no claim map, checks tab, or issue log.
