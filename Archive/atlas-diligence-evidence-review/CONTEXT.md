# Workspace: Atlas Diligence Evidence Review

## Overview

Use this workspace to review the Atlas Growth diligence source set before drafting IC materials.

Do not use this as document management, document extraction, reconciliation, or audit logging.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_inventory` | List sources and metadata. | Source inventory |
| `02_authority` | Rank source authority. | Authority map |
| `03_conflicts_gaps` | Flag conflicts, stale versions, and unsupported claims. | Conflict and gap log |
| `04_evidence_brief` | Explain what the source set supports. | Evidence brief |

## Attached Module

Artifact Trust Layer is attached because the evidence review feeds IC materials.

Reference these files in place:

- `../../modules/artifact-trust-layer/README.md`
- `../../modules/artifact-trust-layer/_config/artifact-boundary.md`
- `../../modules/artifact-trust-layer/_config/review-severity.md`
- `../../modules/artifact-trust-layer/_prompts/build-source-packet.md`
- `../../modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `../../modules/artifact-trust-layer/_prompts/hostile-review.md`

Customized templates live in `_templates/artifact-trust/`.

## Artifact Trust Outputs

| Output | Location |
|---|---|
| Source packet | `01_inventory/output/source-packet-atlas-diligence-2026-05-27.md` |
| Claim evidence map | `04_evidence_brief/output/claim-evidence-map-atlas-diligence-2026-05-27.md` |
| Artifact review report | `04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md` |

## Platform Boundary

| Layer | Owner |
|---|---|
| Storage, permissions, version history, audit | Platform |
| Exact duplicate checks and metadata extraction | Deterministic tools |
| Authority judgment, conflict interpretation, support mapping | AI |
| Conflict resolution and claim approval | Human |

## Test Inputs

- CIM.
- Management call notes.
- Customer export.
- Prior model.
- Market summary.

## Human Owners

- Deal lead resolves diligence conflicts.
- RevOps confirms whether the customer export is the source of record for customer metrics.
