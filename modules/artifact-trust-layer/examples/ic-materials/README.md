# Example: IC Materials

Architecture: `decision-prep`

A deal team prepares investment committee materials from diligence findings, a financial model, management notes, and market research. The Artifact Trust Layer makes the IC artifact reviewable before the approval packet is finalized.

## Boundary

- Approval workflow owns the decision record.
- Finance or data platform owns figures of record.
- Excel or deterministic tools own model checks.
- Kit owns claim mapping, assumption visibility, and hostile review.
- IC approver owns the decision.

## Outputs

- `sample-artifact-spec.md`
- `sample-hostile-review.md`
