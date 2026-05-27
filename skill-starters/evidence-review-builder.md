# SKILL: Evidence Review Workspace Builder

## Description

Builds a workspace that inspects a source set before the team drafts, decides, or responds.

## When To Use

Use when the team has files, notes, data exports, contracts, reports, or other sources and needs to know what they support.

Do not use as document storage, extraction, reconciliation, or audit logging.

## Diagnosis

Read shared config as directed by `SETUP.md`. Ask one question at a time.

1. What source material needs review?
2. Where is source storage, version history, and access controlled?
3. What source is authoritative for key facts?
4. What conflicts or stale-version risks are common?
5. Who resolves conflicts and approves claims?

## Assembly

1. Copy `architectures/evidence-review/` into `workspaces/<name>/`.
2. Customize the four stages around the team's source set.
3. Populate `_config/authority-ladder.md`, `_config/source-register-schema.md`, `_config/conflict-rules.md`, and `_config/platform-boundary.md`.
4. If the review supports a deck, workbook, memo, diligence map, IC material, LP narrative, board material, or one-off deliverable, attach `modules/artifact-trust-layer/` using its attachment guide.
   - Reference module prompts and config in place by default.
   - Copy customized templates to `_templates/artifact-trust/` only when needed.
   - Name outputs for `01_inventory/output/source-packet-[name]-[date].md` and `04_evidence_brief/output/claim-evidence-map-[name]-[date].md`.
   - If a draft artifact exists, name `04_evidence_brief/output/artifact-review-report-[name]-[date].md`.
5. Record open confirmations in `_config/before-you-trust-this.md`.
6. Run a sample source set through inventory and authority ranking.

## Verification

The workspace is ready when it can produce a source inventory, authority map, conflict/gap log, and evidence brief without resolving conflicts silently. If Artifact Trust Layer is attached, it can also produce a source packet and claim evidence map.
