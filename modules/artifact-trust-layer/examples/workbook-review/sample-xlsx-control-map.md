# XLSX Control Map: Atlas Revenue Bridge

## Workbook Purpose

- Workbook: Atlas-revenue-bridge.xlsx
- Owner: Finance owner
- Review date: 2026-05-27
- Source packet: Atlas diligence source packet
- Source of record for figures: CRM export and approved finance model

## Sheet Map

| Sheet | Role | Owner | Source ID | Notes |
|---|---|---|---|---|
| Raw_CRM_Export | raw data | RevOps owner | S03 | Export date needs confirmation. |
| Assumptions | assumptions | Finance owner |  | Contains hardcoded retention assumptions. |
| Bridge_Calc | calculation | Finance owner | S03 | Formula-heavy. |
| Checks | checks | Finance owner | S03 | ARR total check exists. |
| Output | output | Finance owner |  | Feeds IC deck. |

## Required Controls

| Control | Status | Notes |
|---|---|---|
| Raw data tabs exist and are not overwritten by formulas. | pass | Raw_CRM_Export appears separate. |
| Assumptions are labeled with owner and date. | warning | Owner listed, date missing. |
| Output tabs trace to calculation tabs or source tabs. | pass | Output traces to Bridge_Calc. |
| Checks exist for key totals or tie-outs. | warning | ARR check exists, customer count check missing. |
| Hardcoded numbers are labeled assumptions or flagged. | warning | Retention assumptions are hardcoded. |
| External links are listed. | blocked | External links not reviewed. |

## Warnings

| Warning | Severity | Owner | Resolution |
|---|---|---|---|
| External links not reviewed. | high | Finance owner | Run workbook link inspection. |
| Missing date on assumptions. | medium | Finance owner | Add date and source basis. |
