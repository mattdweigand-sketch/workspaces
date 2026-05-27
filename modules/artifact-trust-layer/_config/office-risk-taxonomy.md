# Office Risk Taxonomy

Use these risk types when reviewing decks, workbooks, documents, tables, charts, and one-off deliverables.

| Risk Type | Meaning | Typical Review Action |
|---|---|---|
| `polished_but_unsupported` | The artifact looks complete, but claims do not map to sources. | Block or require source IDs. |
| `stale_number` | A current artifact includes an old number, old chart, old plan, or superseded draft. | Require current source or explicit stale-source label. |
| `formula_drift` | Parallel formulas point to different rows, columns, periods, or assumptions without explanation. | Route to deterministic workbook check. |
| `static_model` | A workbook looks like a model but contains hardcoded outputs where formulas should exist. | Flag hardcodes and require calculation owner review. |
| `mixed_actuals_plan` | Actuals, budgets, forecasts, and estimates are blended without labels. | Require labels, periods, and source dates. |
| `untraceable_chart` | A chart is presentation-ready, but source data, transformation, or date range is unclear. | Require chart source, source range, or workbook reference. |
| `assumption_as_fact` | An estimate, inference, placeholder, or judgment call is presented as confirmed. | Relabel or route to human approval. |
| `review_theater` | The artifact claims review, but no claim map, checks tab, or issue log exists. | Require review artifacts before final use. |

## Severity Guidance

- High: could mislead a stakeholder, approver, investor, auditor, customer, or committee.
- Medium: may be supportable, but evidence, freshness, labels, or ownership are incomplete.
- Low: clarity or formatting issue that does not change the conclusion.

## Boundary

Kit names the risk and routes ownership. Platforms, deterministic tools, and humans resolve the underlying source, calculation, or approval question.
