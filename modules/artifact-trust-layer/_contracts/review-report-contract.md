# Review Report Contract

Use this contract for hostile review, second-pass review, stale-number review, workbook review, or deck review.

## Required Top-Level Fields

| Field | Required | Notes |
|---|---|---|
| `artifact_id` | yes | Stable artifact identifier. |
| `created_at` | yes | Date the review was created. |
| `issues` | yes | List of review issues. Empty means no issues found, not no review performed. |

## Issue Record

| Field | Required | Allowed Or Expected Values |
|---|---|---|
| `issue_id` | yes | Stable issue identifier. |
| `severity` | yes | `low`, `medium`, `high`. |
| `artifact_location` | yes | Where the issue appears. |
| `description` | yes | Concrete issue, not a generic warning. |
| `source_ids` | no | Source IDs involved. |
| `risk_type` | no | Use `_config/office-risk-taxonomy.md` where possible. |
| `requires_human` | yes | `true` or `false`. |
| `recommended_owner` | no | Person or role that should resolve it. |

## Validation Rules

- High severity issues require a human owner or explicit blocking status.
- Reviews enumerate issues. They do not rewrite the artifact.
- A review report must distinguish unresolved issues from accepted risks.
- `review_theater` applies when review status is claimed but evidence maps, checks, or issue logs are missing.
