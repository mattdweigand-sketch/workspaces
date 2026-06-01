# Artifact Types

| Type | Examples | Primary Risk |
|---|---|---|
| Deck | Board deck, IC deck, investor deck, diligence deck | Claims and charts look final without evidence. |
| Workbook | Model, diligence workbook, analysis workbook, tracker | Formula risk, stale data, hardcoded assumptions. |
| Memo | IC memo, board memo, diligence memo, briefing note | Inference presented as verified fact. |
| Narrative | LP update, investor note, executive update | Unsupported claims or sensitive language. |
| Evidence map | Diligence map, source support matrix | Missing authority and unresolved conflicts. |
| One-off deliverable | Custom packet, ad hoc report, summary | Review process is skipped because the work feels non-recurring. |

## Default Routing

- Source uncertainty routes to `evidence-review`.
- Decision use routes to `decision-prep`.
- Stakeholder-facing use routes to `stakeholder-response-prep`.
- Scattered source intake routes first to `messy-input-intake`.
