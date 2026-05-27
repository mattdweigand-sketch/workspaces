# Evidence Map Contract

Use this contract when a workspace needs claim-level traceability for a deck, workbook, document, table, or metric.

## Required Top-Level Fields

| Field | Required | Notes |
|---|---|---|
| `artifact_id` | yes | Stable artifact identifier. |
| `created_at` | yes | Date the evidence map was created. |
| `items` | yes | Non-empty list of mapped artifact targets. |

## Evidence Item

| Field | Required | Allowed Or Expected Values |
|---|---|---|
| `target_id` | yes | Stable item identifier. |
| `artifact_location` | yes | Slide, sheet/cell, paragraph, table, or section. |
| `target_type` | no | `slide_claim`, `speaker_note`, `workbook_cell`, `workbook_chart`, `document_paragraph`, `table_row`, `metric`. |
| `claim_or_value` | yes | Claim, number, cell value, chart claim, or paragraph summary. |
| `source_ids` | yes | Non-empty list of source IDs. |
| `source_date` | yes | Date supporting the claim, or `unknown` with an issue. |
| `owner` | yes | Owner of the claim or source. |
| `transformation` | no | Calculation, rollup, filtering, or interpretation. |
| `assumption_flag` | no | `true` when the item depends on judgment. |
| `confidence` | yes | `high`, `medium`, `low`, `contested`. |
| `review_status` | yes | `unreviewed`, `reviewed`, `needs_human`, `blocked`. |

## Validation Rules

- Target IDs must be unique.
- Material numbers require a source date.
- Assumptions should be `needs_human` unless already approved.
- Charts and tables require either source IDs or a workbook/source-of-record reference.
- Consequential unsupported claims are `blocked`.
