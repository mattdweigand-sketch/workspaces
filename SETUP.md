# Workspaces Setup Engine

You are an AI agent. This file is the setup and workspace-build engine for Workspaces.

`AGENTS.md` is canonical. `CLAUDE.md` only imports `AGENTS.md` for Claude Code compatibility.

## Core Rule

If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do not make it a toolkit architecture.

If the work depends on firm judgment, source interpretation, decision framing, or institutional memory, it belongs here.

## Workflow Registry

Workspaces has six persistent architectures:

| Business job | Architecture | Builder |
|---|---|---|
| Turn messy inputs into a clean starting point | `messy-input-intake` | `skill-starters/messy-input-intake-builder.md` |
| Figure out what source material supports | `evidence-review` | `skill-starters/evidence-review-builder.md` |
| Prepare a human to make a decision | `decision-prep` | `skill-starters/decision-prep-builder.md` |
| Handle a case that does not fit the normal process | `exception-handling` | `skill-starters/exception-handling-builder.md` |
| Prepare a high-context stakeholder response | `stakeholder-response-prep` | `skill-starters/stakeholder-response-prep-builder.md` |
| Capture what the organization learned | `institutional-memory-loop` | `skill-starters/institutional-memory-loop-builder.md` |

Do not build a workspace for CRM, ticketing, project management, dashboarding, calculation, entitlement, audit, or platform-native execution. Build only the layer above those systems.

## Module Registry

Modules are optional reusable patterns that attach to the selected architecture. They do not create new architecture families.

| Pattern | Module | Attach When |
|---|---|---|
| Artifact trust | `modules/artifact-trust-layer/` | The workflow produces or reviews decks, workbooks, memos, reports, IC materials, LP narratives, board materials, diligence artifacts, or one-off deliverables. |

## Module Attachment Rule

Reference module files in place by default. Copy templates into the workspace only when they need local fields, naming, owners, or review rules.

Copied Artifact Trust Layer templates go under `_templates/artifact-trust/`.

When attaching `modules/artifact-trust-layer/`, name the output locations for:

- Source packet, if source review is in scope.
- Claim evidence map, if an artifact is in scope.
- Artifact review report, if a draft artifact exists.
- Human approval note, if the artifact supports a decision or stakeholder-facing use.

scripts/setup_state.py tracks setup state only. Do not add file-copying module attachment behavior there unless Workspaces gains a separate workspace materialization command.

## Context Matrix

Load only what the selected architecture needs.

| Architecture | `_shared-config/org-profile.md` | `_shared-config/voice-and-tone.md` | `_shared-config/learnings.md` | Constraints | Builder |
|---|---|---|---|---|---|
| `messy-input-intake` | full | summary | `## General`, `## messy-input-intake` | 03, 06, 08, 09, 10 | full |
| `evidence-review` | summary | none | `## General`, `## evidence-review` | 03, 06, 08, 09, 10 | full |
| `decision-prep` | full | summary | `## General`, `## decision-prep` | 02, 03, 06, 08, 09, 10 | full |
| `exception-handling` | full | summary | `## General`, `## exception-handling` | 02, 04, 06, 08, 09, 10 | full |
| `stakeholder-response-prep` | full | full | `## General`, `## stakeholder-response-prep` | 01, 02, 05, 06, 08, 09, 10 | full |
| `institutional-memory-loop` | full | summary | `## General`, `## institutional-memory-loop` | 03, 04, 06, 08, 09, 10 | full |

## Run Setup Starts Here

When the user says `Run setup`, `add a workflow`, or `build a <workflow>`, do this:

1. Run `python3 scripts/setup_state.py status`.
2. If needed, run `python3 scripts/setup_state.py doctor --json`.
3. Follow the status:
   - `not_started`: run `python3 scripts/setup_state.py init-session`, then run Organization Orientation, Value Triage, and Build Sequence.
   - `in_progress`: read `_shared-config/setup-session.json` and resume from the recorded phase, step, and question.
   - `ready_to_build`: read `_shared-config/setup-session.json`, open the selected builder, and continue.
   - `complete`: read `_shared-config/org-profile.md` and `_shared-config/setup-progress.md`, summarize what exists, and offer to add another workflow.

Ask one question at a time. Do not turn setup into a form.

## Organization Orientation

Run once, before the first workspace. Capture:

1. What is the organization, and what does it do?
2. What systems of record does it use?
3. Who owns data, decisions, and approval?
4. How should the organization sound in writing?

Write answers into `_shared-config/org-profile.md` and `_shared-config/voice-and-tone.md`. Do not re-ask these facts in builders.

## Value Triage

Before selecting a workspace, score candidate work from 1 to 5:

| Dimension | What to score |
|---|---|
| Frequency | How often the work recurs. |
| Risk | Cost of inconsistency, delay, or unsupported judgment. |
| Data readiness | Whether inputs exist in reliable systems or files. |
| Decision leverage | Whether better judgment changes money, time, trust, or compliance outcomes. |
| Adoption ease | Whether the team can run it next week. |

Recommend the highest-scoring architecture. If the work is platform-native, say so and do not build.

## Diagnose To Route

| If the work sounds like... | Route to |
|---|---|
| "We get messy emails, calls, files, screenshots, or notes and need a clean brief." | `messy-input-intake` |
| "We need to know what these documents support before relying on them." | `evidence-review` |
| "A human needs to make a better decision with options, risks, and tradeoffs." | `decision-prep` |
| "This case does not fit the normal process." | `exception-handling` |
| "We need to explain verified facts to a stakeholder." | `stakeholder-response-prep` |
| "We need to capture lessons so future work improves." | `institutional-memory-loop` |

If none fit, do not invent a seventh architecture casually. Explain the gap and ask whether the user wants to create a new architecture intentionally.

## Build Sequence

1. Confirm the architecture and workspace name.
2. Open the matching builder from `skill-starters/`.
3. Ask the builder's diagnostic questions one at a time.
4. Load only the constraints named in the Context Matrix.
5. Copy `architectures/<architecture>/` into `workspaces/<name>/`.
6. If the workflow produces or reviews artifacts, ask whether to attach `modules/artifact-trust-layer/`.
7. Customize `CLAUDE.md`, `CONTEXT.md`, stage contracts, and `_config/` from the answers.
8. If a module is attached, follow its attachment guide. Reference module files in place by default, copy only templates that need customization, and name module output locations in the relevant stage contracts.
9. Populate `_config/before-you-trust-this.md` with every unresolved confirmation.
10. Run one stage against live or sample input when available.
11. Report the checklist below.

## Constraint Routing

| Architecture | Load these constraints | Why |
|---|---|---|
| `messy-input-intake` | 03, 06, 08, 09, 10 | Keep inputs scoped, route only what belongs to AI, and hand off cleanly. |
| `evidence-review` | 03, 06, 08, 09, 10 | Inspect sources without replacing storage, reconciliation, or audit. |
| `decision-prep` | 02, 03, 06, 08, 09, 10 | Keep decisions comparable, source-backed, and human-owned. |
| `exception-handling` | 02, 04, 06, 08, 09, 10 | Keep edge cases consistent and safely escalated. |
| `stakeholder-response-prep` | 01, 02, 05, 06, 08, 09, 10 | Keep communication accurate, on voice, source-backed, and reviewed. |
| `institutional-memory-loop` | 03, 04, 06, 08, 09, 10 | Keep memory structured, comparable, source-aware, and validated. |

## Shared Builder Kernel

Every builder must:

- Reuse organization facts from `_shared-config/`.
- Ask one question at a time.
- Name the platform that owns the record.
- Name the deterministic rule or calculation owner.
- Name the AI judgment being added.
- Name the human approver.
- Write open confirmations to `_config/before-you-trust-this.md`.
- Verify against the checklist before calling the workspace ready.

## Onboarding Complete

Report each item as pass or open:

- [ ] Architecture identified.
- [ ] Platform boundary documented.
- [ ] Human approver named.
- [ ] Required `_config` files populated.
- [ ] Open confirmations listed.
- [ ] At least one stage contract customized.
- [ ] A sample or live input can run through the first stage.
- [ ] No platform-native action is delegated to AI.

Use **MVP ready** when the workspace is configured and only visible confirmations remain. Use **Operating ready** when a live run has completed.

## Keeping The OS Map Current

After a build, update `AGENTS.md` so it describes the organization's live workspaces and the six architecture families. Do not run finalize unless the user explicitly asks.

## Finalize

Finalize only on explicit user request. Move toolkit methodology into `_kit/`, leave live workspaces and organization config visible at the root, and write restore instructions.
