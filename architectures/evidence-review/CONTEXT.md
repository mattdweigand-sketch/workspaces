# Architecture: Evidence Review

## Overview

Use this when a team has a source set and needs to know what it supports before drafting, deciding, or responding.

Do not use this as document management, document extraction, reconciliation, or audit logging.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_inventory` | List sources and metadata. | Source inventory |
| `02_authority` | Rank source authority. | Authority map |
| `03_conflicts_gaps` | Flag conflicts, stale versions, and unsupported claims. | Conflict and gap log |
| `04_evidence_brief` | Explain what the source set supports. | Evidence brief |

## Optional Modules

Attach `modules/artifact-trust-layer/` when the source review supports a deck, workbook, memo, diligence map, IC material, LP narrative, board material, or one-off deliverable.

When attached, add these optional outputs:

- Source packet.
- Claim evidence map.
- Artifact review report when a draft artifact exists.

## Platform Boundary

| Layer | Owner |
|---|---|
| Storage, permissions, version history, audit | Platform |
| Exact duplicate checks and metadata extraction | Deterministic tools |
| Authority judgment, conflict interpretation, support mapping | AI |
| Conflict resolution and claim approval | Human |
