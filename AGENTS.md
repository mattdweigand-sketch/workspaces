# Workspces

`AGENTS.md` is canonical. Claude Code reads it through the thin `CLAUDE.md` wrapper.

Workspces is a plain-file toolkit for building AI operating systems around the work platforms cannot own:
firm judgment, source interpretation, decision framing, exception handling, stakeholder response
prep, and institutional memory.

## Start Here

- For **Run setup**, **add a workflow**, or **build a <workflow>**, read `SETUP.md`.
- Setup state lives in `_shared-config/setup-session.json` while work is in progress. If setup is
  interrupted, resume from that file instead of restarting orientation.
- Setup is complete only when `_shared-config/setup-progress.md` exists and this file has been
  rewritten into the organization's operating map.

## Architecture Families

Workspces has six persistent architecture families:

- `messy-input-intake`
- `evidence-review`
- `decision-prep`
- `exception-handling`
- `stakeholder-response-prep`
- `institutional-memory-loop`

Do not recreate the old four-shape model. Route work by business job, then by platform boundary.

## Reusable Modules

Modules are optional patterns that attach to architecture families. They do not create new
architecture families.

- `modules/artifact-trust-layer/`: source packets, claim evidence maps, artifact specs, review
  reports, workbook controls, and human approval notes for decks, workbooks, memos, diligence
  artifacts, IC materials, LP narratives, board materials, and one-off deliverables.

## Guardrails

- Do not run finalize unless the user explicitly asks.
- Do not move toolkit folders into or out of `_kit/` without confirmation.
- Do not delete, overwrite, or reset live `workspaces/` or `_shared-config/` content.
- Do not write to external systems or send stakeholder-facing output without human review.
- If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do
  not make it a toolkit architecture.
