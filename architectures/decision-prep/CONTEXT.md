# Architecture: Decision Prep

## Overview

Use this when a person or committee needs to decide and the value is in framing the judgment.

Do not use this to replace an approver, approval workflow, model, or decision log.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_decision_frame` | State the decision, owner, deadline, facts, and constraints. | Decision frame |
| `02_options_tradeoffs` | Compare viable options. | Options brief |
| `03_challenge` | Pressure-test assumptions, risks, and missing evidence. | Challenge memo |
| `04_approval_packet` | Produce the human-ready packet. | Approval packet |

## Optional Modules

Attach `modules/artifact-trust-layer/` when the decision packet includes IC materials, board materials, approval decks, workbooks, memos, or other decision-facing artifacts.

When attached, add these optional outputs before `04_approval_packet`:

- Artifact spec.
- Claim evidence map.
- Hostile review.
- Open confirmations list.

## Platform Boundary

| Layer | Owner |
|---|---|
| Record, approval state, audit | Platform |
| Calculations and threshold checks | Deterministic tools |
| Judgment framing and challenge | AI |
| Final decision | Human |
