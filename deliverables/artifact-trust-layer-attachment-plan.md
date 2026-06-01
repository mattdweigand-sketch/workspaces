# Artifact Trust Layer Attachment Plan

Date: 2026-05-27

## Decision

Attach the Artifact Trust Layer by reference by default. Copy only the small templates a workspace needs to customize.

This keeps the module reusable and prevents each workspace from carrying stale copies of every prompt and template.

## Attachment Contract

Every attached workspace should answer four questions:

1. Which artifact is being produced or reviewed?
2. Which source packet supports it?
3. Which claim evidence map reviews it?
4. Which human approves unresolved issues?

## Shared Output Convention

When the module is attached, generated outputs should live under the stage that produces them:

| Output | Default Location |
|---|---|
| Source packet | `01_inventory/output/source-packet-[name]-[date].md` |
| Claim evidence map | `04_evidence_brief/output/claim-evidence-map-[name]-[date].md` |
| Artifact spec | Stage that defines the artifact, usually `01_decision_frame/output/` or `02_message_frame/output/` |
| Artifact review report | Final review stage output, usually `03_challenge/output/` or `04_review_packet/output/` |
| Human approval note | Final review or approval stage output |
| Workbook control map | Evidence review or challenge stage output |

If the workspace already has a better stage-specific folder, use it, but keep the filename explicit.

## Reference By Default

Reference these files in place:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/review-severity.md`
- `modules/artifact-trust-layer/_operating-model/architecture-attachment-guide.md`
- Prompt files in `modules/artifact-trust-layer/_prompts/`

Copy only when the workspace needs a customized standard.

## Copy When Needed

Copy templates into the workspace when they need local fields, naming, owners, or review rules:

- `_templates/source-packet.md`
- `_templates/claim-evidence-map.md`
- `_templates/artifact-spec.md`
- `_templates/artifact-review-report.md`
- `_templates/pptx-claim-map.md`
- `_templates/xlsx-control-map.md`
- `_templates/docx-claim-map.md`
- `_templates/human-approval-note.md`

Place copied templates in the workspace under `_templates/artifact-trust/`.

## Architecture Attachments

### `evidence-review`

Use when the team must know what a source set supports before drafting, deciding, or responding.

Reference:

- `README.md`
- `_config/artifact-boundary.md`
- `_config/review-severity.md`
- `_prompts/build-source-packet.md`
- `_prompts/create-claim-evidence-map.md`
- `_prompts/hostile-review.md`

Copy when needed:

- `_templates/source-packet.md`
- `_templates/claim-evidence-map.md`
- `_templates/artifact-review-report.md`
- `_templates/xlsx-control-map.md` if a workbook is in scope.

Add outputs:

- `01_inventory/output/source-packet-[name]-[date].md`
- `04_evidence_brief/output/claim-evidence-map-[name]-[date].md`
- `04_evidence_brief/output/artifact-review-report-[name]-[date].md` when a draft artifact exists.

### `decision-prep`

Use when the artifact supports a human or committee decision.

Reference:

- `README.md`
- `_config/artifact-boundary.md`
- `_config/review-severity.md`
- `_prompts/hostile-review.md`
- `_prompts/stale-number-review.md`
- `_prompts/formula-risk-review.md` if a workbook is in scope.
- `_operating-model/human-approval.md`

Copy when needed:

- `_templates/artifact-spec.md`
- `_templates/claim-evidence-map.md`
- `_templates/artifact-review-report.md`
- `_templates/human-approval-note.md`
- `_templates/pptx-claim-map.md` for decks.
- `_templates/xlsx-control-map.md` for workbooks.
- `_templates/docx-claim-map.md` for memos.

Add outputs:

- `01_decision_frame/output/artifact-spec-[name]-[date].md`
- `03_challenge/output/artifact-review-report-[name]-[date].md`
- `04_approval_packet/output/human-approval-note-[name]-[date].md`

### `stakeholder-response-prep`

Use when the artifact will explain verified facts to an investor, LP, board, executive, customer, partner, or employee.

Reference:

- `README.md`
- `_config/artifact-boundary.md`
- `_config/review-severity.md`
- `_prompts/create-claim-evidence-map.md`
- `_prompts/hostile-review.md`
- `_prompts/stale-number-review.md`
- `_operating-model/human-approval.md`

Copy when needed:

- `_templates/claim-evidence-map.md`
- `_templates/artifact-review-report.md`
- `_templates/human-approval-note.md`
- `_templates/docx-claim-map.md` for narratives or memos.
- `_templates/pptx-claim-map.md` for decks.

Add outputs:

- `01_verified_facts/output/claim-evidence-map-[name]-[date].md`
- `04_review_packet/output/artifact-review-report-[name]-[date].md`
- `04_review_packet/output/human-approval-note-[name]-[date].md`

### `messy-input-intake`

Use when source material arrives before the source set is clean.

Reference:

- `README.md`
- `_prompts/build-source-packet.md`

Copy when needed:

- `_templates/source-packet.md`

Add outputs:

- `01_capture/output/source-packet-draft-[name]-[date].md`
- `04_handoff/output/artifact-trust-handoff-[name]-[date].md`

## Setup Flow

During setup, ask:

Does this workflow produce or review a deck, workbook, memo, report, IC material, LP narrative, board material, diligence artifact, or one-off deliverable?

If yes, attach the module and ask:

1. What artifact type is in scope?
2. Which architecture stage should create the source packet?
3. Which stage should create the claim evidence map?
4. Which stage should run artifact review?
5. Who approves unresolved issues?

Do not ask these as a form unless the user asks for a checklist. Ask one at a time.

## Verification

An attached workspace is ready when:

- The selected architecture is unchanged.
- The module is referenced in the workspace `CONTEXT.md` or relevant stage contracts.
- Source packet output location is named.
- Claim evidence map output location is named.
- Artifact review report output location is named when an artifact exists.
- Human approval owner is named.
- Open confirmations are captured in `_config/before-you-trust-this.md`.
