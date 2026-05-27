# Architecture Library Migration Plan

## Decision

Replace the current architecture library with six persistent architectures:

- `messy-input-intake`
- `evidence-review`
- `decision-prep`
- `exception-handling`
- `stakeholder-response-prep`
- `institutional-memory-loop`

Delete or demote everything else. The repo should not keep generic shapes as public architectures once these six are built.

## Boundary Rule

If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do not make it a toolkit architecture.

If the work depends on firm judgment, source interpretation, decision framing, or institutional memory, it belongs here.

That means:

- Platforms own facts, state, permissions, calculations, delivery, and audit.
- Automation owns known rules, routing, checklists, templates, and repeatable handoffs.
- Workspces owns interpretation, judgment, exception reasoning, decision prep, communication framing, and memory.

The six architectures below are the recurring places where that third layer appears across almost every business.

## Target Architecture Library

| Architecture | Plain meaning | Why it persists |
|---|---|---|
| `messy-input-intake` | Turn unstructured inputs into a clean brief. | Most business work starts before the record is clean: email, calls, docs, Slack, forms, screenshots, notes. |
| `evidence-review` | Decide what the source set supports. | File systems store documents. AI helps interpret authority, conflicts, gaps, and support. |
| `decision-prep` | Prepare a human to make a better decision. | Platforms can record approvals. They do not frame tradeoffs, assumptions, risks, and precedent. |
| `exception-handling` | Handle cases that do not fit the normal workflow. | Automation handles standard cases. AI helps reason through edge cases and route them safely. |
| `stakeholder-response-prep` | Prepare high-context communication from verified facts. | Platforms own the data and delivery. AI helps explain, frame, and prepare. |
| `institutional-memory-loop` | Capture validated lessons and apply them later. | Databases can store memory artifacts. They cannot create, validate, interpret, or apply judgment. |

## What Gets Removed

Remove these public architecture folders:

- `architectures/gated-decision-pipeline/`
- `architectures/recurring-operations-queue/`
- `architectures/recurring-document-production/`
- `architectures/learning-loop/`

Remove these public builder files:

- `skill-starters/gated-decision-pipeline-builder.md`
- `skill-starters/recurring-operations-queue-builder.md`
- `skill-starters/recurring-document-production-builder.md`
- `skill-starters/learning-loop-builder.md`
- `skill-starters/build-from-scratch.md`

Remove or replace the old worked examples:

- `architectures/_examples/hiring-pipeline/`
- `architectures/_examples/support-escalation-queue/`
- `architectures/_examples/monthly-board-report/`
- `architectures/_examples/sales-win-loss/`

These can be mined for useful language, but they should not remain as shipped examples because they reinforce the old four-shape model.

## What Gets Built

### 1. `messy-input-intake`

Purpose: turn messy inputs into a clean brief that can be reviewed, routed, or entered into the right platform.

Platform boundary:

- Platform owns the final record and workflow state.
- Workspces owns interpretation of messy inputs before the record is clean.

Folder shape:

```text
architectures/messy-input-intake/
  CLAUDE.md
  CONTEXT.md
  01_capture/CONTEXT.md
  02_interpret/CONTEXT.md
  03_normalize/CONTEXT.md
  04_handoff/CONTEXT.md
  _config/input-types.md
  _config/normalization-schema.md
  _config/routing-rules.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
```

Stages:

1. Capture: gather the input set without judging it.
2. Interpret: identify intent, facts, missing context, and source confidence.
3. Normalize: create the clean brief in a stable schema.
4. Handoff: route to the platform, owner, or next architecture.

Builder:

- `skill-starters/messy-input-intake-builder.md`

Worked example:

- `architectures/_examples/vendor-request-intake/`

### 2. `evidence-review`

Purpose: inspect a source set before the business relies on it.

Platform boundary:

- Document systems own storage, permissions, version history, and audit.
- Workspces owns source interpretation: authority, support, conflicts, gaps, and questions.

Folder shape:

```text
architectures/evidence-review/
  CLAUDE.md
  CONTEXT.md
  01_inventory/CONTEXT.md
  02_authority/CONTEXT.md
  03_conflicts_gaps/CONTEXT.md
  04_evidence_brief/CONTEXT.md
  _config/authority-ladder.md
  _config/source-register-schema.md
  _config/conflict-rules.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
```

Stages:

1. Inventory: list sources and metadata.
2. Authority: rank sources as authoritative, supporting, background, or superseded.
3. Conflicts and gaps: flag disagreement, missing proof, stale versions, and unsupported claims.
4. Evidence brief: explain what the source set supports and what still needs human resolution.

Builder:

- `skill-starters/evidence-review-builder.md`

Worked example:

- `architectures/_examples/contract-renewal-evidence-review/`

### 3. `decision-prep`

Purpose: prepare a human to make a better decision.

Platform boundary:

- Platform owns the record, approval state, and decision log.
- Workspces owns decision framing, tradeoffs, assumptions, risks, precedent, and conditions.

Folder shape:

```text
architectures/decision-prep/
  CLAUDE.md
  CONTEXT.md
  01_decision_frame/CONTEXT.md
  02_options_tradeoffs/CONTEXT.md
  03_challenge/CONTEXT.md
  04_approval_packet/CONTEXT.md
  _config/decision-criteria.md
  _config/risk-lenses.md
  _config/precedent-sources.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
```

Stages:

1. Decision frame: state the decision, owner, facts, constraints, and deadline.
2. Options and tradeoffs: compare viable paths.
3. Challenge: pressure-test assumptions, missing evidence, second-order effects, and precedent.
4. Approval packet: produce the human-ready recommendation and open conditions.

Builder:

- `skill-starters/decision-prep-builder.md`

Worked example:

- `architectures/_examples/pricing-exception-decision-prep/`

### 4. `exception-handling`

Purpose: handle cases that do not fit the normal workflow.

Platform boundary:

- Platform owns queues, statuses, ownership, entitlement, and escalation logs.
- Workspces owns interpreting the exception, applying judgment, drafting options, and preparing handoff.

Folder shape:

```text
architectures/exception-handling/
  CLAUDE.md
  CONTEXT.md
  01_exception_brief/CONTEXT.md
  02_rule_context/CONTEXT.md
  03_response_options/CONTEXT.md
  04_escalation_handoff/CONTEXT.md
  _config/exception-types.md
  _config/rule-sources.md
  _config/escalation-rules.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
```

Stages:

1. Exception brief: describe what makes the case non-standard.
2. Rule context: identify relevant policy, precedent, constraints, and unknowns.
3. Response options: propose safe paths with tradeoffs.
4. Escalation handoff: send the case to the right human or platform workflow.

Builder:

- `skill-starters/exception-handling-builder.md`

Worked example:

- `architectures/_examples/customer-escalation-exception/`

### 5. `stakeholder-response-prep`

Purpose: prepare high-context communication from verified facts.

Platform boundary:

- Platform owns stakeholder records, permissions, figures, delivery, and audit.
- Workspces owns narrative, tone, likely questions, response posture, and review packet.

Folder shape:

```text
architectures/stakeholder-response-prep/
  CLAUDE.md
  CONTEXT.md
  01_verified_facts/CONTEXT.md
  02_message_frame/CONTEXT.md
  03_question_prep/CONTEXT.md
  04_review_packet/CONTEXT.md
  _config/audience-map.md
  _config/voice-and-tone.md
  _config/claim-rules.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
```

Stages:

1. Verified facts: gather the facts the platform or owner has approved.
2. Message frame: explain what happened, why it matters, and what posture to take.
3. Question prep: prepare likely questions, objections, and approved responses.
4. Review packet: produce a human-reviewed draft or meeting brief.

Builder:

- `skill-starters/stakeholder-response-prep-builder.md`

Worked example:

- `architectures/_examples/service-issue-stakeholder-response/`

### 6. `institutional-memory-loop`

Purpose: capture validated lessons and apply them to future work.

Platform boundary:

- Source systems own what happened.
- Workspces owns interpretation, causal analysis, validation, pattern capture, and reuse.
- A database can store the memory, but it cannot decide what the lesson means or when to apply it.

Folder shape:

```text
architectures/institutional-memory-loop/
  CLAUDE.md
  CONTEXT.md
  01_event_capture/CONTEXT.md
  02_interpretation/CONTEXT.md
  03_validation/CONTEXT.md
  04_pattern_update/CONTEXT.md
  _config/memory-schema.md
  _config/taxonomy.md
  _config/validation-rules.md
  _config/platform-boundary.md
  _config/before-you-trust-this.md
  _store/README.md
  _store/patterns.md
  _store/records/.gitkeep
```

Stages:

1. Event capture: collect the factual record and trigger.
2. Interpretation: separate facts, stated reasons, assessed causes, and open questions.
3. Validation: require a human to approve causal claims.
4. Pattern update: write the validated lesson and update reusable patterns.

Builder:

- `skill-starters/institutional-memory-loop-builder.md`

Worked example:

- `architectures/_examples/lost-renewal-memory-loop/`

## Repo-Wide File Updates

### `README.md`

Rewrite the architecture explanation around the six business jobs:

1. Messy input intake.
2. Evidence review.
3. Decision prep.
4. Exception handling.
5. Stakeholder response prep.
6. Institutional memory loop.

Update:

- Opening description.
- "What this is not."
- "Where AI helps most."
- "What is in here."
- Architecture section.
- Example section.

Remove:

- The old four-shape language as the public model.
- Any claim that architectures are only `gated-decision-pipeline`, `recurring-operations-queue`, `recurring-document-production`, and `learning-loop`.

### `SETUP.md`

Rewrite setup around the six architecture routes.

Update:

- Context Matrix: six rows, one per architecture.
- Workflow Registry: six rows, plus clear "do not build" guidance for platform-native work.
- Diagnose -> Route: plain-language questions, not abstract shape classification.
- Constraint Routing: constraints mapped to the six architectures.
- Onboarding Sequence: copy one of the six architecture folders into `workspaces/<name>/`.
- Shared Builder Kernel: keep one-question-at-a-time behavior and platform-boundary confirmation.

Remove:

- Old four-shape routing.
- Old generic workflow-shape language.
- Any public `build-from-scratch` fallback. If no architecture fits, setup should say the request is outside the current library or ask whether to create a new architecture intentionally.

### `scripts/setup_state.py`

Update the state helper so doctor checks the new registry.

Required changes:

- Rename `firm_orientation` to `organization_orientation` in `SESSION_TEMPLATE`.
- Preserve backward compatibility by accepting existing `firm_orientation` if present.
- Update `parse_registry_rows()` to find `## Workflow Registry`, not `## GP Workflow Registry`.
- Parse the new five-column registry table.
- Report six expected routes and six expected builders.
- Remove `firm-profile.md` from `profile_paths()` unless there is a compatibility reason to keep it.

Verification command:

```bash
python3 scripts/setup_state.py doctor --json
```

### `AGENTS.md`

Update the project-doc section so it says Workspces has six architecture families and keeps the platform boundary explicit.

Keep:

- Finalize guardrail.
- Do-not-delete live workspace guardrail.
- Human-review guardrail.

### `skill-starters/`

Replace the old builder set with:

```text
skill-starters/messy-input-intake-builder.md
skill-starters/evidence-review-builder.md
skill-starters/decision-prep-builder.md
skill-starters/exception-handling-builder.md
skill-starters/stakeholder-response-prep-builder.md
skill-starters/institutional-memory-loop-builder.md
```

Every builder must include:

- When to use.
- When not to use.
- Platform boundary questions.
- Diagnostic interview.
- Assembly instructions.
- Required `_config` files.
- First-run verification.

### `constraints/`

Keep the constraint library. Do not delete it.

Tune these files after the architecture migration:

- `06-layer-triage.md`: align examples to the six architecture jobs.
- `09-platform-boundary.md`: make the boundary rule the central test.
- `10-source-provenance.md`: connect directly to `evidence-review`.
- `04-session-consistency.md`: connect directly to `institutional-memory-loop`.
- `08-handoff-readiness.md`: connect directly to platform handoffs.

### `_shared-config/`

Update only section names and examples:

- Rename any architecture-specific learning headers to the six new architecture names.
- Keep organization profile and voice files.

Do not delete live setup/session/progress files without explicit confirmation.

## Migration Order

### Phase 1: Freeze the target model

1. Confirm the six architecture names.
2. Replace the implementation plan with this plan.
3. Update README language so readers understand the six jobs.

Done when: README makes sense to a business reader before they see folder names.

### Phase 2: Build architecture skeletons

1. Create the six architecture folders.
2. Add `CLAUDE.md`, `CONTEXT.md`, stage contracts, and required `_config` files.
3. Add empty output folders or `.gitkeep` where needed.
4. Add `_store/` only to `institutional-memory-loop`.

Done when: `find architectures -maxdepth 1 -type d` shows only `_examples` plus the six target architectures.

### Phase 3: Build builders

1. Create six matching builder files.
2. Remove old builder files.
3. Ensure each builder asks workflow-specific questions and does not re-ask organization facts.
4. Ensure each builder names the platform boundary and human approval gate.

Done when: `find skill-starters -maxdepth 1 -type f` shows only the six target builders.

### Phase 4: Replace setup routing

1. Rewrite Context Matrix.
2. Rewrite Workflow Registry.
3. Rewrite Diagnose -> Route.
4. Rewrite Constraint Routing.
5. Update `scripts/setup_state.py` registry parsing.

Done when: `python3 scripts/setup_state.py doctor --json` reports no registry mismatch.

### Phase 5: Replace examples

1. Delete old examples.
2. Add one worked example per architecture.
3. Keep each example small but complete enough to show finished output.
4. Make every example state:
   - What the platform owns.
   - What rules own.
   - What AI adds.
   - What human approves.

Done when: every architecture has one example and no old four-shape examples remain.

### Phase 6: Tune constraints and shared config

1. Update constraint examples.
2. Update `_shared-config/learnings.md` headings.
3. Run `rg` for old architecture names.

Searches that should return no public architecture references:

```bash
rg "gated-decision-pipeline|recurring-operations-queue|recurring-document-production|learning-loop"
rg "decision-pressure-test|evidence-map|variance-intervention|stakeholder-narrative-prep|organization-memory-loop"
```

The first search should be empty except possibly migration notes. The second search should be empty because those labels are replaced by the six final names.

### Phase 7: Verify

Run:

```bash
python3 scripts/setup_state.py doctor --json
find architectures -maxdepth 1 -type d | sort
find skill-starters -maxdepth 1 -type f | sort
rg "GP Workflow|firm_orientation|gated-decision-pipeline|recurring-operations-queue|recurring-document-production|learning-loop" README.md SETUP.md AGENTS.md scripts skill-starters architectures constraints _shared-config
```

Expected result:

- Six architecture folders.
- Six builder files.
- No public old-shape language.
- Setup doctor passes.
- README explains the business jobs in plain language.

## Definition Of Done

The migration is complete when:

- The only public architecture folders are the six target folders.
- The only builder files are the six matching builders.
- README explains where AI belongs without relying on abstract architecture labels.
- SETUP routes by business job, not old generic shapes.
- Every architecture has a platform-boundary file and a human-approval rule.
- Every architecture has one worked example.
- `scripts/setup_state.py doctor --json` reports no registry mismatch.
- `rg` does not find the old four-shape model in reader-facing docs.

## Non-Goals

Do not build:

- CRM.
- Ticketing.
- Project management.
- Dashboarding.
- Calculation engines.
- Entitlement systems.
- Audit systems.
- Standard document extraction as a standalone architecture.

Those belong to platforms. Workspces exists above them.
