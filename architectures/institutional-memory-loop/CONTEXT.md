# Architecture: Institutional Memory Loop

## Overview

Use this when the organization should not have to relearn the same lesson: wins, losses, incidents, decisions, churn, escalations, post-mortems, and reviews.

Do not use this as the source system for facts or as an unreviewed opinion store.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_event_capture` | Capture the factual record and trigger. | Event record |
| `02_interpretation` | Separate facts, stated reasons, assessed causes, and questions. | Interpretation |
| `03_validation` | Human-validates causal claims. | Validation note |
| `04_pattern_update` | Update records and reusable patterns. | Memory record and pattern update |

## Platform Boundary

| Layer | Owner |
|---|---|
| Facts, timeline, outcome | Source platforms |
| Taxonomy and schema | Rules / team standards |
| Interpretation and pattern detection | AI |
| Causal validation | Human |
| Store maintenance | Workspace or approved database |
