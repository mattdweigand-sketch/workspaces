# SKILL: Institutional Memory Loop Workspace Builder

## Description

Builds a workspace that captures validated lessons and applies them to future work.

## When To Use

Use for wins, losses, incidents, churn, escalations, decisions, post-mortems, and recurring outcomes where the organization should not relearn the same lesson.

Do not use as a source system for facts or as an unvalidated opinion store.

## Diagnosis

Read shared config as directed by `SETUP.md`. Ask one question at a time.

1. What recurring outcomes should the organization learn from?
2. Which source systems own the facts and outcome?
3. What lessons or causal claims matter most?
4. Who validates the lesson before it enters memory?
5. Where should future workflows read the memory back?

## Assembly

1. Copy `architectures/institutional-memory-loop/` into `workspaces/<name>/`.
2. Customize event capture, interpretation, validation, and pattern update stages.
3. Populate `_config/memory-schema.md`, `_config/taxonomy.md`, `_config/validation-rules.md`, and `_config/platform-boundary.md`.
4. Keep `_store/records/` append-only.
5. Record open confirmations in `_config/before-you-trust-this.md`.
6. Run one resolved event through event capture if available.

## Verification

The workspace is ready when it separates facts from causal interpretation and requires human validation before updating patterns.
