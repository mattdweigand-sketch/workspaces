# Example: Workbook Review

Architecture: `evidence-review`

A team reviews an analysis workbook before its outputs are used in a deck or memo. The Artifact Trust Layer does not certify formulas. It makes workbook risks visible and routes exact checks to the deterministic owner.

## Boundary

- Excel or deterministic tools own formula checks.
- Source systems own raw data and figures of record.
- Workspces owns workbook risk framing and review notes.
- Human owner approves use of the workbook output.

## Outputs

- `sample-xlsx-control-map.md`
- `sample-review-report.md`
