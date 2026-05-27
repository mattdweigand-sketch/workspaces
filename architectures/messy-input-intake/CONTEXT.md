# Architecture: Messy Input Intake

## Overview

Use this when work arrives as email, calls, notes, screenshots, forms, files, chat threads, or other messy input and the team needs a clean starting brief.

Do not use this as a CRM, ticketing queue, project tracker, or system of record. The output is a reviewed brief and handoff, not the final record.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_capture` | Gather the input set and source context. | Input packet |
| `02_interpret` | Identify intent, facts, gaps, confidence, and ambiguity. | Interpretation notes |
| `03_normalize` | Convert the interpreted input into the approved schema. | Clean intake brief |
| `04_handoff` | Route the brief to the platform, owner, or next architecture. | Handoff note |

## Optional Modules

Attach `modules/artifact-trust-layer/` when the messy input includes source files, prior artifacts, exports, screenshots, or notes that will feed a deck, workbook, memo, report, diligence artifact, IC material, LP narrative, board material, or one-off deliverable.

When attached, add these optional outputs:

- Draft source packet.
- Artifact trust handoff.
- Initial source-of-record questions.

## Platform Boundary

| Layer | Owner |
|---|---|
| Final record, status, permissions, audit | Platform |
| Known routing rules and assignment logic | Rules / automation |
| Intent recognition, ambiguity, gap finding, source confidence | AI |
| Record creation, escalation, stakeholder output | Human |

## Required Config

- `_config/input-types.md`
- `_config/normalization-schema.md`
- `_config/routing-rules.md`
- `_config/platform-boundary.md`
- `_config/before-you-trust-this.md`
