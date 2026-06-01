# Review Severity

| Severity | Meaning | Required Action |
|---|---|---|
| High | The artifact could mislead a stakeholder, committee, investor, customer, auditor, or approver. | Block pending human resolution. |
| Medium | The artifact may be supportable, but evidence, freshness, wording, or assumptions are incomplete. | Review before external or decision use. |
| Low | The artifact has clarity, formatting, or minor support issues that do not change the conclusion. | Fix when practical. |

## High Severity Examples

- Unsupported factual claim.
- Number with no source.
- Superseded source used as current.
- Formula output used without checks.
- Inference presented as verified fact.
- Conflicting sources with no resolution note.
- Sensitive commitment without owner approval.

## Overall Status

Use one of:

- `pass`
- `pass with warnings`
- `blocked pending human review`
