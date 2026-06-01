# Example: Diligence Evidence Map

Architecture: `evidence-review`

A team receives a CIM, management call notes, a customer export, a prior model, and a market summary. The team needs to know which claims can support diligence findings before drafting IC materials.

## Boundary

- Document platform owns storage, permissions, version history, and audit.
- Data warehouse or fund platform owns figures of record.
- Deterministic tools own duplicate checks and workbook inspection.
- Workspaces owns source authority, claim support, conflict visibility, and review framing.
- Human owner resolves conflicts and approves claims.

## Outputs

- `sample-source-packet.md`
- `sample-claim-evidence-map.md`
- `sample-review-report.md`
