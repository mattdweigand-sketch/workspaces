# PRD: Artifact Trust Layer Module

## Decision

Build an `artifact-trust-layer` module for Workspces.

Do not create a seventh architecture. Do not build runnable sales-harness software in this repo. The module should package reusable workflows, templates, prompts, review gates, and operating-model guidance for teams that turn messy source material into trustworthy artifacts.

The sales harness can enforce artifact trust behavior in code. Workspces should make the same discipline portable as files a human or agent can apply across workflows.

## Product Summary

The Artifact Trust Layer is a reusable Workspces module for producing and reviewing PowerPoint decks, Excel workbooks, Word documents, IC materials, LP narratives, board materials, diligence evidence maps, and one-off deliverables from messy source sets.

It gives teams a repeatable pattern:

1. Build a source packet.
2. Map claims to evidence.
3. Define the artifact spec.
4. Run hostile review.
5. Route unresolved issues to a human approver.

The module plugs into existing Workspces architectures:

| Architecture | Artifact Trust Layer Role |
|---|---|
| `messy-input-intake` | Capture scattered files, emails, exports, notes, and context before review. |
| `evidence-review` | Build source packets, authority maps, conflict logs, and claim evidence maps. |
| `decision-prep` | Prepare IC materials, approval packets, investment memos, and board decision materials. |
| `stakeholder-response-prep` | Prepare LP narratives, investor updates, board updates, and executive communications from verified facts. |
| `institutional-memory-loop` | Capture validated lessons from artifact review failures and recurring source issues. |

## Problem

Teams use AI to draft artifacts from messy inputs: PDFs, emails, spreadsheets, call notes, prior decks, screenshots, exported data, and ad hoc analyst workbooks.

The output often looks finished before it is trustworthy.

Common failures:

- A slide repeats a claim no source supports.
- A workbook blends a current export with an old analyst model.
- A deck cites a number without a freshness date.
- An LP narrative turns an inference into a fact.
- An IC memo relies on a superseded diligence document.
- A chart is recreated from an unknown table.
- A formula risk hides inside a workbook nobody checks.
- A review catches tone and formatting but misses source integrity.

These are not primarily drafting failures. They are source, evidence, and review failures.

## Why Workspces Should Own This

Workspces owns the judgment layer above platforms. It does not own the source of record, calculation engine, permissions, version history, delivery, or audit trail.

The Artifact Trust Layer belongs in Workspces because the hard work is not creating a file. The hard work is knowing what the source set supports, what the artifact claims, where the risks are, and what a human must approve before the artifact is trusted.

The module must preserve the platform boundary:

| Layer | Owner |
|---|---|
| Source files, permissions, version history, delivery, audit | Document platform, CRM, fund admin platform, data warehouse, SharePoint, Google Drive, Box, or other source system |
| Calculations, tie-outs, duplicate hashes, workbook inspection | Deterministic tools, Excel, scripts, data warehouse, source platform |
| Source interpretation, claim mapping, review framing, issue classification | Workspces |
| Approval, external use, final judgment | Human owner |

## Goals

- Provide a reusable source-to-artifact pattern for artifact work.
- Make source provenance visible before creation starts.
- Make every load-bearing claim traceable to evidence.
- Make unsupported claims, stale numbers, formula risks, and inferred facts visible.
- Give PowerPoint, Excel, and Word artifacts artifact-specific review controls.
- Keep the six Workspces architectures intact.
- Make the module easy to attach to existing and future Workspces workflows.
- Produce examples for LP narratives, IC materials, diligence evidence maps, and workbook review.

## Non-Goals

- Do not generate PowerPoint, Excel, or Word files directly.
- Do not create runnable artifact gates, tests, or blocking enforcement.
- Do not duplicate sales-harness behavior.
- Do not become a document management system.
- Do not become a calculation engine.
- Do not reconcile source-of-record conflicts automatically.
- Do not write to external systems.
- Do not approve stakeholder-facing or investment-facing material.

## Primary Users

### Operating Partner, Investor Relations, Finance, or Diligence Lead

Needs to turn fragmented materials into a board deck, LP update, IC memo, diligence summary, or workbook. Cares about whether the artifact is supportable, not whether the first draft is fluent.

### Analyst or Associate

Needs a repeatable structure for source prep, evidence mapping, workbook controls, and review notes. Cares about reducing rework and avoiding unsupported claims.

### Human Approver

Needs a compact review packet showing what is supported, what is assumed, what is stale, and what needs approval. Cares about knowing where to focus review.

### AI Agent Running Workspces

Needs stage contracts, templates, prompts, and examples that make the expected process explicit. Cares about knowing what to read, what to produce, and what not to decide.

## Core Use Cases

### 1. Diligence Evidence Map

A team receives a source folder with CIMs, data room exports, management call notes, prior models, customer data, market research, and internal notes. The module helps produce a source packet, authority map, conflict log, and claim evidence map before the team drafts diligence findings.

Primary architecture: `evidence-review`

### 2. IC Materials

A team prepares an investment committee memo or deck. The module helps map claims, assumptions, numbers, and open risks to source evidence. It adds a hostile review prompt that asks what would make the recommendation wrong.

Primary architecture: `decision-prep`

### 3. LP Narrative

A team prepares an investor-facing update from performance data, portfolio notes, market commentary, and prior messaging. The module helps separate verified facts from narrative interpretation and flags unsupported or sensitive claims before drafting.

Primary architecture: `stakeholder-response-prep`

### 4. Workbook Review

A team uses an Excel workbook as a support artifact for a memo, deck, or operating decision. The module provides a control map for raw data, assumptions, checks, outputs, change log, formula risk, stale inputs, and hardcoded numbers.

Primary architecture: `evidence-review`

### 5. One-Off Deliverable Review

A team creates an ad hoc deck, memo, workbook, or briefing from scattered inputs. The module provides a short path: source packet, claim map, hostile review, approval checklist.

Primary architecture: `messy-input-intake` into `evidence-review`, then either `decision-prep` or `stakeholder-response-prep`.

## Product Shape

Add a module folder:

```text
modules/artifact-trust-layer/
  README.md
  _config/
    artifact-boundary.md
    artifact-types.md
    review-severity.md
  _templates/
    source-packet.md
    claim-evidence-map.md
    artifact-spec.md
    pptx-claim-map.md
    xlsx-control-map.md
    docx-claim-map.md
    artifact-review-report.md
    human-approval-note.md
  _prompts/
    build-source-packet.md
    create-claim-evidence-map.md
    hostile-review.md
    stale-number-review.md
    formula-risk-review.md
    two-model-review.md
  _operating-model/
    review-gates.md
    human-approval.md
    architecture-attachment-guide.md
    workspace-output-conventions.md
    setup-automation-boundary.md
  examples/
    diligence-evidence-map/
      README.md
      sample-source-packet.md
      sample-claim-evidence-map.md
      sample-review-report.md
    ic-materials/
      README.md
      sample-artifact-spec.md
      sample-hostile-review.md
    lp-narrative/
      README.md
      sample-verified-facts.md
      sample-claim-evidence-map.md
    workbook-review/
      README.md
      sample-xlsx-control-map.md
      sample-review-report.md
```

This folder is reference material. It is not a workspace. Setup can attach it to a workspace when the selected workflow produces or reviews artifacts.

## Functional Requirements

### FR1: Module Entry Point

`modules/artifact-trust-layer/README.md` must explain:

- What the module is.
- When to use it.
- Which architectures it attaches to.
- What it produces.
- What it does not own.
- The standard sequence: source packet, claim map, artifact spec, hostile review, human approval.

Acceptance criteria:

- A user can open the README and know whether the module applies in under two minutes.
- The README reinforces that platforms own records, calculations, permissions, delivery, and audit.
- The README does not describe runnable software.

### FR2: Source Packet Template

`_templates/source-packet.md` must define the standard upstream artifact.

Required sections:

- Purpose.
- Source register.
- Source authority ladder.
- Version families.
- Duplicate or near-duplicate notes.
- Missing metadata.
- Conflicts.
- Unsupported claims requested by the user.
- Source-of-record notes.
- Human confirmations.

Required source fields:

- Source ID.
- File or link.
- Type.
- Date.
- Owner.
- Source system.
- Version.
- Related record.
- Authority level.
- Freshness status.
- Key contents.
- Metadata gaps.

Acceptance criteria:

- A downstream claim map can cite source IDs from the packet.
- The template makes stale and superseded sources visible.
- The template does not ask the model to reconcile facts or recompute figures.

### FR3: Claim Evidence Map Template

`_templates/claim-evidence-map.md` must define the core trust object for all artifacts.

Required fields:

- Claim ID.
- Artifact location.
- Claim text.
- Claim type: fact, number, date, interpretation, assumption, recommendation, commitment.
- Source ID.
- Evidence note.
- Source authority.
- Freshness date.
- Confidence.
- Open issue.
- Review status.
- Human owner.

Acceptance criteria:

- Every load-bearing claim in an artifact can be mapped to source evidence.
- Claims without evidence are visible.
- Inferences and assumptions cannot appear as verified facts.

### FR4: Artifact Spec Template

`_templates/artifact-spec.md` must define the target artifact before drafting.

Required sections:

- Artifact type.
- Audience.
- Decision or communication job.
- Source packet path.
- Required claims.
- Prohibited claims.
- Required sections.
- Numbers and charts expected.
- Review gates.
- Human approver.

Acceptance criteria:

- The artifact has a clear job before creation starts.
- Review can compare the draft against the spec.
- The spec separates artifact structure from evidence support.

### FR5: PowerPoint Claim Map

`_templates/pptx-claim-map.md` must support deck-specific review.

Required fields:

- Slide number.
- Slide title.
- Slide job.
- Load-bearing claim.
- Number, date, or chart.
- Source ID.
- Evidence note.
- Inference label.
- Speaker-note support.
- Unsupported or stale issue.
- Reviewer status.

Acceptance criteria:

- A reviewer can inspect claims slide by slide.
- Charts and tables must trace to a source or workbook.
- Speaker notes cannot introduce unsupported facts.

### FR6: Excel Control Map

`_templates/xlsx-control-map.md` must support workbook-specific review.

Required sections:

- Workbook purpose.
- Source data tabs.
- Raw data tabs.
- Assumptions tabs.
- Calculation tabs.
- Checks tabs.
- Output tabs.
- Change log.
- Named ranges or key cells.
- Hardcoded inputs.
- External links.
- Formula risk areas.
- Stale data warnings.
- Manual override notes.

Required control checks:

- Raw data exists and is not overwritten by formulas.
- Assumptions are labeled with owner and date.
- Output tabs trace back to calculation tabs or source tabs.
- Checks exist for key totals or tie-outs.
- Hardcoded numbers are either labeled assumptions or flagged.
- External links are listed.
- Hidden sheets or hidden rows are noted when known.

Acceptance criteria:

- The workbook can be reviewed as a controlled artifact.
- The template makes formula risk and stale data visible.
- The template does not turn Workspces into the calculation owner.

### FR7: Word Claim Map

`_templates/docx-claim-map.md` must support memos and narrative documents.

Required fields:

- Section.
- Paragraph or heading.
- Claim text.
- Claim type.
- Source ID.
- Evidence note.
- Confidence.
- Unsupported issue.
- Sensitive language issue.
- Reviewer status.

Acceptance criteria:

- LP narratives, IC memos, board memos, and one-off written deliverables can use the same source discipline as decks.
- The template keeps narrative interpretation separate from verified fact.

### FR8: Artifact Review Report

`_templates/artifact-review-report.md` must standardize review output.

Required sections:

- Artifact reviewed.
- Inputs reviewed.
- Overall status: pass, pass with warnings, blocked pending human review.
- High-severity issues.
- Medium-severity issues.
- Low-severity issues.
- Unsupported claims.
- Stale numbers.
- Formula or chart risks.
- Inferences presented as facts.
- Missing human confirmations.
- Recommended next action.

Acceptance criteria:

- Review output is concise enough for a human approver.
- Issues are grouped by severity.
- The report does not rewrite the artifact unless the workflow explicitly asks for a revised draft.

### FR9: Hostile Review Prompt

`_prompts/hostile-review.md` must pressure-test the artifact.

Prompt behavior:

- Look for unsupported claims.
- Look for stale figures.
- Look for blended source versions.
- Look for overconfident wording.
- Look for missing caveats.
- Look for claims that would embarrass the team if challenged.
- Do not rewrite.
- Produce issues and severity.

Acceptance criteria:

- The prompt acts as a reviewer, not a copy editor.
- It asks what would make the artifact wrong.
- It names evidence gaps precisely.

### FR10: Stale Number Review Prompt

`_prompts/stale-number-review.md` must inspect figures, dates, and charts.

Prompt behavior:

- Extract every number, date, chart, and table reference.
- Map each to a source ID where possible.
- Identify freshness date.
- Flag figures from superseded, background, or unknown sources.
- Flag figures with no source.
- Flag mixed-period comparisons.

Acceptance criteria:

- A reviewer can tell which numbers are safe to use.
- The prompt does not compute corrected values.
- The prompt routes unresolved issues to the source owner.

### FR11: Formula Risk Review Prompt

`_prompts/formula-risk-review.md` must inspect workbook risk.

Prompt behavior:

- Identify hardcoded numbers.
- Identify formula-heavy sheets or ranges.
- Identify missing checks.
- Identify external links.
- Identify hidden sheets, hidden rows, or hidden columns when surfaced.
- Identify manual overrides.
- Identify assumptions without owner or date.

Acceptance criteria:

- The prompt produces workbook risk notes.
- The prompt does not certify the workbook.
- The prompt states where deterministic tools are needed.

### FR12: Two-Model Review Prompt

`_prompts/two-model-review.md` must define an independent second-pass review pattern.

Required instructions:

- Treat the draft as untrusted.
- Review against the source packet, claim evidence map, and artifact spec.
- Do not assume the first model read sources correctly.
- Produce a review report, not a rewrite.
- Name disagreements with the first pass.

Acceptance criteria:

- The pattern can be used by another model, another session, or a human reviewer.
- The second pass has a clear input contract.

### FR13: Architecture Attachment Guide

`_operating-model/architecture-attachment-guide.md` must explain how to attach the module to existing architectures.

Required guidance:

- For `messy-input-intake`, add source packet creation after capture.
- For `evidence-review`, use source packet and claim evidence map as standard outputs.
- For `decision-prep`, add artifact spec and hostile review before approval packet.
- For `stakeholder-response-prep`, require verified facts and claim evidence maps before drafting.
- For `institutional-memory-loop`, capture recurring source and artifact failures after human validation.

Acceptance criteria:

- The module does not fork the architecture library.
- A future setup flow can attach the module without changing the selected architecture.

### FR14: Examples

Each example must include a short README and sample outputs.

Required examples:

- Diligence evidence map.
- IC materials.
- LP narrative.
- Workbook review.

Acceptance criteria:

- Examples use realistic private markets language.
- Examples show the difference between supported fact, assumption, interpretation, and unresolved issue.
- Examples are short enough to be copied into a new workspace.

## Non-Functional Requirements

### NFR1: Plain Files

All module content must be markdown files. No scripts, packages, build steps, or runtime dependencies.

### NFR2: Small Context Footprint

Each file should be short enough to load intentionally. The README should point to the right template or prompt instead of requiring every file at once.

### NFR3: Artifact-Neutral Core

The source packet and claim evidence map must work across PowerPoint, Excel, Word, and markdown deliverables.

### NFR4: Artifact-Specific Controls

Artifact-specific templates must cover the failure modes unique to decks, workbooks, and narrative documents.

### NFR5: Human Approval

Every review flow must end with a human approval note. Workspces may classify issues. It must not approve external or decision-facing use.

### NFR6: Platform Boundary

Every file must preserve the boundary:

- Platforms own records and audit.
- Deterministic tools own exact calculations and checks.
- Workspces owns interpretation and review framing.
- Humans own approval.

## Review Severity Model

Create `_config/review-severity.md` with this model:

| Severity | Meaning | Required Action |
|---|---|---|
| High | The artifact could mislead a stakeholder, committee, investor, customer, auditor, or approver. | Block pending human resolution. |
| Medium | The artifact may be supportable, but the evidence, freshness, wording, or assumption basis is incomplete. | Mark for review before external or decision use. |
| Low | The artifact has clarity, formatting, or minor support issues that do not change the conclusion. | Fix when practical. |

High-severity examples:

- Unsupported factual claim.
- Number with no source.
- Superseded source used as current.
- Formula output used without checks.
- Inference presented as verified fact.
- Conflicting sources with no resolution note.
- Sensitive commitment without owner approval.

## Setup Integration

Update `SETUP.md` with a module attachment rule:

If a workflow produces or reviews decks, workbooks, memos, reports, IC materials, LP narratives, board materials, diligence artifacts, or one-off deliverables, ask whether to attach `modules/artifact-trust-layer/`.

If attached, setup should:

1. Keep the selected architecture unchanged.
2. Reference module files in place by default.
3. Copy templates only when they need workspace-specific fields, owners, naming, or review rules.
4. Add open confirmations to `_config/before-you-trust-this.md`.
5. Add source packet, claim evidence map, artifact spec, review report, and human approval outputs to the relevant stage contracts.

## Documentation Updates

Update `README.md` to introduce modules:

- Architectures define the business job.
- Modules provide reusable patterns for recurring artifact, review, or operating-model needs.
- The Artifact Trust Layer is the first module.

Update `architectures/evidence-review/CONTEXT.md`:

- Add optional Artifact Trust Layer outputs: source packet and claim evidence map.

Update `architectures/messy-input-intake/CONTEXT.md`:

- Add optional Artifact Trust Layer outputs: draft source packet and artifact trust handoff.

Update `architectures/decision-prep/CONTEXT.md`:

- Add optional Artifact Trust Layer outputs: artifact spec and hostile review for IC, board, or approval materials.

Update `architectures/stakeholder-response-prep/CONTEXT.md`:

- Add optional Artifact Trust Layer outputs: claim evidence map and artifact review for LP, investor, executive, and board narratives.

## Shipped Scope

The module has been deployed as a plain-file Workspces module.

Shipped files include:

- Module README.
- Boundary config.
- Artifact types config.
- Review severity config.
- Source packet template.
- Claim evidence map template.
- Artifact spec template.
- PPTX claim map template.
- XLSX control map template.
- DOCX claim map template.
- Artifact review report template.
- Human approval note template.
- Source packet prompt.
- Claim evidence map prompt.
- Hostile review prompt.
- Stale number review prompt.
- Formula risk review prompt.
- Two-model review prompt.
- Architecture attachment guide.
- Review gates guidance.
- Human approval guidance.
- Workspace output conventions.
- Setup automation boundary.
- Examples for diligence evidence map, IC materials, LP narrative, and workbook review.
- README and SETUP integration notes.
- Optional hooks in `messy-input-intake`, `evidence-review`, `decision-prep`, and `stakeholder-response-prep`.
- Builder attachment guidance for the same four architectures.

## Verification Completed

Completed checks:

- Required module files exist.
- Architecture hooks exist.
- Builder hooks exist.
- Diligence sample source IDs are defined.
- Claim map citations use known source IDs.
- Unsupported claims without sources are blocked.
- Review report blocks the artifact pending human review.
- Earlier naming is absent from checked files.
- Attachment contract checks pass.

## Future Scope

Future work may include:

- A live workspace build using `evidence-review` plus Artifact Trust Layer.
- Programmatic setup support if Workspces gains a workspace generation script beyond state tracking.
- A companion sales-harness implementation that enforces source packets, evidence maps, artifact gates, tests, and workbook checks in code.
- A deterministic workbook inspection script in another repo.
- A deck generation system in another repo.
- A source packet JSON schema for systems that want to enforce the pattern.

These are explicitly outside this Workspces module unless the repo scope changes.

## Implemented Plan

### Phase 1: Module Skeleton

Create:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/artifact-types.md`
- `modules/artifact-trust-layer/_config/review-severity.md`

Status: shipped.

### Phase 2: Core Templates

Create:

- `_templates/source-packet.md`
- `_templates/claim-evidence-map.md`
- `_templates/artifact-spec.md`
- `_templates/artifact-review-report.md`

Status: shipped.

### Phase 3: Artifact-Specific Templates

Create:

- `_templates/pptx-claim-map.md`
- `_templates/xlsx-control-map.md`
- `_templates/docx-claim-map.md`

Status: shipped.

### Phase 4: Review Prompts

Create:

- `_prompts/build-source-packet.md`
- `_prompts/create-claim-evidence-map.md`
- `_prompts/hostile-review.md`
- `_prompts/stale-number-review.md`
- `_prompts/formula-risk-review.md`
- `_prompts/two-model-review.md`

Status: shipped.

### Phase 5: Operating Model

Create:

- `_operating-model/review-gates.md`
- `_operating-model/human-approval.md`
- `_operating-model/architecture-attachment-guide.md`

Status: shipped.

### Phase 6: Examples

Create:

- `examples/diligence-evidence-map/`
- `examples/ic-materials/`
- `examples/lp-narrative/`
- `examples/workbook-review/`

Status: shipped.

### Phase 7: Repo Integration

Update:

- `README.md`
- `SETUP.md`
- `architectures/evidence-review/CONTEXT.md`
- `architectures/decision-prep/CONTEXT.md`
- `architectures/stakeholder-response-prep/CONTEXT.md`

Status: shipped.

### Phase 8: Attachment Contract

Created:

- `deliverables/artifact-trust-layer-attachment-plan.md`
- `modules/artifact-trust-layer/_operating-model/workspace-output-conventions.md`
- `modules/artifact-trust-layer/_operating-model/setup-automation-boundary.md`
- `deliverables/artifact-trust-layer-live-workspace-validation-plan.md`

Updated:

- `SETUP.md`
- `messy-input-intake`, `evidence-review`, `decision-prep`, and `stakeholder-response-prep`
- All four matching architecture builders.

Status: shipped.

## Acceptance Criteria

The Artifact Trust Layer module is complete when:

- It exists as `modules/artifact-trust-layer/`.
- It does not create a seventh architecture.
- It does not introduce scripts or runnable software.
- It includes source packet, claim evidence map, artifact spec, and review report templates.
- It includes PowerPoint, Excel, and Word artifact controls.
- It includes hostile review, stale number review, formula risk review, and two-model review prompts.
- It includes attachment guidance for existing architectures.
- It includes examples for diligence evidence maps, IC materials, LP narratives, and workbook review.
- It preserves the platform boundary in every file.
- A user can attach the module to a `messy-input-intake`, `evidence-review`, `decision-prep`, or `stakeholder-response-prep` workspace without changing the architecture itself.

## Risks

### Risk: The module becomes too broad.

Mitigation: Keep the core sequence fixed. Source packet, claim map, artifact spec, hostile review, human approval.

### Risk: Users treat review prompts as certification.

Mitigation: Every review file must state that Workspces flags issues but does not approve the artifact.

### Risk: Workbook controls imply Workspces owns calculations.

Mitigation: The workbook template must route calculations, tie-outs, and exact checks to deterministic tools or Excel owners.

### Risk: The module duplicates sales-harness implementation work.

Mitigation: Keep Workspces as markdown operating discipline. Leave enforcement, logs, tests, and gates to runnable repos.

### Risk: Setup becomes confusing.

Mitigation: Explain that architectures answer "what business job is this?" Modules answer "what reusable pattern should this workflow include?"

## Resolved Decisions

1. Use generic private markets examples. Keep JSQ-specific language out of the public Workspces module unless this repo becomes JSQ-specific.
2. Include Word controls in the shipped module.
3. Reference module files by default. Copy only when a workspace needs customization.
4. Use both: issue severity as `low`, `medium`, `high`; overall artifact status as `pass`, `pass with warnings`, `blocked pending human review`.
