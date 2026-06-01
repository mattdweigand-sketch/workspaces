# Artifact Trust Layer

Use this module when a workflow turns messy sources into a business artifact that someone may trust: a deck, workbook, memo, LP update, IC packet, diligence summary, board material, or one-off deliverable.

This is a module, not a seventh architecture. Architectures answer the business job. The Artifact Trust Layer adds source and review discipline to artifacts produced inside those architectures.

## Standard Pattern

1. Run a setup check.
2. Build a source packet.
3. Define the artifact spec.
4. Draft only from approved source structure.
5. Map claims to evidence.
6. Run artifact review.
7. Route unresolved issues to a human approver and record final audit notes.

## Where It Attaches

| Architecture | Use This Module For |
|---|---|
| `messy-input-intake` | Capturing scattered files, emails, exports, and notes before artifact work starts. |
| `evidence-review` | Source packets, authority maps, claim evidence maps, and review reports. |
| `decision-prep` | IC materials, board materials, approval packets, and hostile review. |
| `stakeholder-response-prep` | LP narratives, investor updates, executive updates, and reviewed communications. |
| `institutional-memory-loop` | Capturing repeated source failures or artifact review lessons after validation. |

## Boundary

Platforms own records, permissions, version history, delivery, audit, and figures of record.

Deterministic tools own calculations, tie-outs, workbook inspection, duplicate hashes, and exact checks.

Workspaces owns source interpretation, claim mapping, review framing, and issue visibility.

Humans own approval.

## What This Produces

- Setup check.
- Source packet.
- Claim evidence map.
- Artifact spec.
- Deck claim map.
- Workbook control map.
- Artifact review report.
- Final artifact README.

Default output paths live in `_operating-model/workspace-output-conventions.md`.

## Optional Contracts

Use `_contracts/` when a workspace needs stricter field expectations without adding runnable validation software:

- `source-packet-contract.md`
- `evidence-map-contract.md`
- `review-report-contract.md`

Use `_config/office-risk-taxonomy.md` to label review issues consistently across decks, workbooks, documents, tables, and charts.

## What This Does Not Do

- Generate PowerPoint, Excel, Word, or other artifact files.
- Certify an artifact.
- Reconcile conflicts.
- Recompute figures.
- Write to external systems.
- Replace human approval.
