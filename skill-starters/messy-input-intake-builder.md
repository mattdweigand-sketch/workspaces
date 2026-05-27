# SKILL: Messy Input Intake Workspace Builder

## Description

Builds a workspace that turns unstructured inputs into clean briefs for review, routing, or platform entry.

## When To Use

Use when work starts as email, calls, notes, chat threads, screenshots, forms, or file bundles and the team needs a structured starting point.

Do not use when the request is already a clean platform record or when the user wants to replace a CRM, ticketing system, project tracker, or approval queue.

## Diagnosis

Read `_shared-config/org-profile.md`, `_shared-config/learnings.md`, and `_shared-config/voice-and-tone.md` as directed by `SETUP.md`. Ask one question at a time.

1. What messy inputs arrive, and through which channels?
2. What clean brief does the team need before acting?
3. Which platform owns the final record?
4. What routing rules are already known?
5. Who approves record creation, escalation, or external output?

## Assembly

1. Copy `architectures/messy-input-intake/` into `workspaces/<name>/`.
2. Customize `CONTEXT.md` and stage contracts to the team's inputs and handoffs.
3. Populate `_config/input-types.md`, `_config/normalization-schema.md`, `_config/routing-rules.md`, and `_config/platform-boundary.md`.
4. If the messy inputs will feed a deck, workbook, memo, report, diligence artifact, IC material, LP narrative, board material, or one-off deliverable, attach `modules/artifact-trust-layer/` using its attachment guide.
   - Reference `modules/artifact-trust-layer/_prompts/build-source-packet.md` in place by default.
   - Copy `modules/artifact-trust-layer/_templates/source-packet.md` to `_templates/artifact-trust/source-packet.md` only when customized.
   - Name outputs for `01_capture/output/source-packet-draft-[name]-[date].md` and `04_handoff/output/artifact-trust-handoff-[name]-[date].md`.
5. Put unconfirmed owners, platforms, and thresholds in `_config/before-you-trust-this.md`.
6. Run one sample input through `01_capture` and `03_normalize` if a live input is available.

## Verification

The workspace is ready when the output brief separates facts, assumptions, gaps, confidence, platform owner, and human approver. If Artifact Trust Layer is attached, artifact source questions and handoff outputs are named before downstream review.
