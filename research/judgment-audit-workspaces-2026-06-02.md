# Judgment Audit: Workspaces Criteria

## Scope

- Repo: `/Users/matthewweigand/Code/folder structures/systems/workspaces`
- Criteria source: `AGENTS.md`, `SETUP.md`, `architectures/**/_config/*.md`, `modules/artifact-trust-layer/**`, and example stage outputs.
- Eval/log source: `deliverables/artifact-trust-layer-smoke-test-report.md`, `deliverables/artifact-trust-layer-live-workspace-test-report.md`, and `scripts/setup_state.py doctor --json`.
- Artifact sample: Artifact Trust Layer examples, archived Atlas diligence workspace, and architecture examples under `architectures/_examples/`.

## Criteria Catalog

| Criterion | Parent | Type | Rubric | Current status |
|---|---|---|---|---|
| architecture-fit | `AGENTS.md:17-28`, `SETUP.md:13-26`, `SETUP.md:103-114` | manual/judge | Route by business job and platform boundary. Do not invent a seventh architecture casually. | Documented, no judge runner |
| platform-boundary | `README.md:32-51`, `AGENTS.md:39-46`, `SETUP.md:7-11` | manual/judge | Platforms own records, state, permissions, calculations, delivery, and audit. Workspaces owns judgment layer. | Documented, partially checked by examples |
| builder-readiness | `SETUP.md:116-128`, `SETUP.md:141-167` | checklist | Workspace is ready only when architecture, platform boundary, approver, config, confirmations, stage customization, sample input, and no platform-native delegation are verified. | Manual checklist |
| artifact-attachment-readiness | `SETUP.md:28-49`, `modules/artifact-trust-layer/_operating-model/architecture-attachment-guide.md:137-172` | checklist | Attach module only for artifact-producing workflows; reference by default; copy templates only when local customization is needed; name output locations and approval owner. | Tested once in live workspace |
| source-packet-completeness | `architectures/evidence-review/_config/source-register-schema.md:3-13`, `modules/artifact-trust-layer/_operating-model/review-gates.md:5-13` | deterministic/manual | Every source has an ID, file/link, type, date, owner, system, version, related record, metadata gaps, authority, stale flags, and source-of-record questions. | Tested in Artifact Trust examples |
| authority-ranking | `architectures/evidence-review/_config/authority-ladder.md:1-8`, `architectures/evidence-review/CONTEXT.md:28-35` | judge/manual | Claims cite up the authority ladder; AI interprets authority, support, conflicts, gaps, and questions. | Documented, manually demonstrated |
| conflict-handling | `architectures/evidence-review/_config/conflict-rules.md:1-8` | judge/manual | Never silently resolve conflicts; show both sides; name likely source of record when clear; mark unresolved conflicts for human review; do not blend versions or recompute figures. | Demonstrated in examples |
| claim-map-integrity | `modules/artifact-trust-layer/_templates/claim-evidence-map.md:1-15`, `modules/artifact-trust-layer/_operating-model/review-gates.md:14-22` | deterministic/judge | Load-bearing claims get rows; numbers, dates, charts, and commitments require source IDs; assumptions need owner or approval path; superseded-source claims are blocked until reviewed. | Tested in smoke and live reports |
| artifact-review-severity | `modules/artifact-trust-layer/_config/review-severity.md:1-25`, `modules/artifact-trust-layer/_templates/artifact-review-report.md:13-80` | judge/manual | Assign severity and status; high severity blocks human resolution when artifact could mislead a stakeholder, committee, investor, customer, auditor, or approver. | Demonstrated in sample/live reports |
| hostile-review | `modules/artifact-trust-layer/_prompts/hostile-review.md:12-38` | judge | Skeptical review identifies unsupported claims, stale figures, blended versions, overconfidence, missing caveats, assumptions as facts, and hard-to-defend claims. | Prompt exists, no runner |
| stale-number-review | `modules/artifact-trust-layer/_prompts/stale-number-review.md:9-32` | deterministic/judge | Extract numbers/dates/charts/tables, map to source IDs, flag stale or unsupported figures, and do not compute corrections. | Prompt exists, no runner |
| formula-risk-review | `modules/artifact-trust-layer/_prompts/formula-risk-review.md:9-33`, `modules/artifact-trust-layer/_config/artifact-boundary.md:13-22` | deterministic/manual | Identify workbook risk and route exact checks to Excel, scripts, platform, or human owner. Workspaces does not become calculation owner. | Prompt exists, no workbook execution signal |
| human-approval | `modules/artifact-trust-layer/_operating-model/human-approval.md:1-26`, `modules/artifact-trust-layer/_operating-model/review-gates.md:32-39` | deterministic/manual | Approval ends with named human decision, explicit use, listed conditions, and open issues accepted, resolved, or blocked. | Documented, represented in examples |
| decision-prep-quality | `architectures/decision-prep/CONTEXT.md:1-35`, `architectures/decision-prep/_config/decision-criteria.md:1-10` | manual/judge | Decision prep frames options, tradeoffs, risks, assumptions, constraints, calculations, thresholds, disqualifiers, and reversibility. | Example exists, no eval signal |
| stakeholder-response-safety | `architectures/stakeholder-response-prep/CONTEXT.md:1-35` | manual/judge | Use verified facts; do not invent facts, bypass approval, send messages, or manage stakeholder records. | Example exists, no eval signal |
| memory-causal-validation | `architectures/institutional-memory-loop/CONTEXT.md:1-26`, `architectures/institutional-memory-loop/_config/validation-rules.md:1-7` | manual | Separate stated reason from assessed cause; human validation required before causal claims enter store; uncertainty recorded; provisional lessons labeled. | Example exists, should stay human-owned |
| legacy-naming-absence | `deliverables/artifact-trust-layer-smoke-test-report.md:13-24` | deterministic | Earlier naming is absent from checked files. | One-time migration check, not recurring judge criterion |

## Execution Signal

| Criterion | Observed skips/reviews/failures | Artifact evidence | Notes |
|---|---:|---|---|
| architecture-fit | 1 live Artifact Trust test passed | Live validation kept `evidence-review` selected and did not create a new architecture: `deliverables/artifact-trust-layer-live-workspace-test-report.md:44-57`. | Good signal for one evidence-review path only. |
| platform-boundary | 1 live test passed; doctor structural check passed registry references | Live test confirmed no platform-native action delegated: `deliverables/artifact-trust-layer-live-workspace-test-report.md:44-57`. Doctor logic checks setup state, workspace existence, bootstrap map, and registry references: `scripts/setup_state.py:184-204`. | Current doctor output showed `status: not_started`, placeholders, missing setup progress, six registry rows, six builder rows, ten constraints, and no missing registry references. |
| artifact-attachment-readiness | 1 smoke test passed; 1 live test passed | Smoke checks passed required module files, architecture hooks, builder hooks, source IDs, claim citations, unsupported-claim blocking, review status, and naming cleanup: `deliverables/artifact-trust-layer-smoke-test-report.md:13-24`. Live test passed copy/reference behavior and output placement: `deliverables/artifact-trust-layer-live-workspace-test-report.md:44-64`. | Strongest covered area. |
| source-packet-completeness | 2 review passes | Smoke/live reports confirm source packets exist and name source IDs: `deliverables/artifact-trust-layer-smoke-test-report.md:20-21`, `deliverables/artifact-trust-layer-live-workspace-test-report.md:51-52`. | Deterministic parser would cover most of this. |
| claim-map-integrity | 2 review passes, 1 real blocked claim | Sample claim map blocks unsupported category leadership: `modules/artifact-trust-layer/examples/diligence-evidence-map/sample-claim-evidence-map.md:5-8`. Archived report repeats the block and adds open confirmations: `Archive/atlas-diligence-evidence-review/04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md:14-39`. | Split into deterministic integrity checks plus judge for omitted load-bearing claims. |
| conflict-handling | 2 example conflicts caught | Contract renewal example requires human resolution for date conflict and missing approvals: `architectures/_examples/contract-renewal-evidence-review/evidence-brief-contract-renewal-2026-05-27.md:9-20`. Atlas report flags NRR conflict: `Archive/atlas-diligence-evidence-review/04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md:20-27`. | Good candidate for judge because source conflict interpretation is not just schema validation. |
| hostile-review | 1 live report acted like hostile review | Archived report blocked an unsupported claim, NRR conflict, source-of-record confirmation, and stale model status: `Archive/atlas-diligence-evidence-review/04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md:14-39`. | Most valuable judge candidate. |
| stale-number-review | 1 live number conflict and stale model issue | Atlas report flags conflicting NRR and current approved model missing: `Archive/atlas-diligence-evidence-review/04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md:20-27`. | Start with deterministic extraction and citation checks, then judge freshness only when dates/sources are present. |
| formula-risk-review | No workbook run observed | Formula-risk prompt exists but the live report only notes missing current model/workbook inspection status: `Archive/atlas-diligence-evidence-review/04_evidence_brief/output/artifact-review-report-atlas-diligence-2026-05-27.md:26-35`. | Do not build an LLM judge before a workbook parser/control-map check exists. |
| human-approval | 2 review passes, no approval-note sample in live path | Smoke/live reports require blocked pending human review and open confirmations: `deliverables/artifact-trust-layer-smoke-test-report.md:22-23`, `deliverables/artifact-trust-layer-live-workspace-test-report.md:53-56`. | Mostly deterministic presence/status checks. Human decision remains manual. |
| decision-prep-quality | 1 example, no eval log | Pricing example names options, tradeoffs, challenge, and conditions: `architectures/_examples/pricing-exception-decision-prep/approval-packet-pricing-exception-2026-05-27.md:1-23`. | Valuable but under-sampled. Keep manual until there are real packets. |
| stakeholder-response-safety | 1 example, no eval log | Service issue example keeps facts constrained and does not promise root cause prevention before approval: `architectures/_examples/service-issue-stakeholder-response/review-packet-service-issue-2026-05-27.md:3-22`. | High stakes but insufficient execution signal. |
| memory-causal-validation | 1 example, no eval log | Lost renewal example separates source facts, assessed cause, validation, lesson, and future use: `architectures/_examples/lost-renewal-memory-loop/memory-record-lost-renewal-2026-05-27.md:7-23`. | Human validation should not become an LLM judge. |
| legacy-naming-absence | 1 migration pass | Smoke test includes "Earlier naming is absent from checked files": `deliverables/artifact-trust-layer-smoke-test-report.md:23-24`. | Drop as a recurring judge. Use ad hoc `rg` when needed. |

## Recommendations

| Criterion | Frequency | Stakes | Auto-convertibility | Evidence | Recommendation |
|---|---|---|---|---|---|
| architecture-fit | high | high | partial | mixed | PROMOTE |
| platform-boundary | high | high | partial | mixed | PROMOTE |
| builder-readiness | high | medium | yes | mixed | AUTO-CONVERT |
| artifact-attachment-readiness | medium | medium | yes | strong | AUTO-CONVERT |
| source-packet-completeness | high | high | yes | strong | AUTO-CONVERT |
| authority-ranking | medium | high | no | mixed | PROMOTE |
| conflict-handling | medium | high | partial | strong | PROMOTE |
| claim-map-integrity | high | high | partial | strong | AUTO-CONVERT |
| artifact-review-severity | medium | high | partial | strong | PROMOTE |
| hostile-review | medium | high | no | strong | PROMOTE |
| stale-number-review | medium | high | partial | mixed | AUTO-CONVERT |
| formula-risk-review | low | high | yes | weak | AUTO-CONVERT |
| human-approval | high | high | yes | mixed | AUTO-CONVERT |
| decision-prep-quality | medium | high | partial | weak | KEEP-MANUAL |
| stakeholder-response-safety | medium | high | partial | weak | KEEP-MANUAL |
| memory-causal-validation | medium | high | partial | weak | KEEP-MANUAL |
| legacy-naming-absence | low | low | yes | weak | DROP |

## V2 Judge Scope

### 1. Architecture Fit Judge

- Why deterministic checks are insufficient: a file can name one of six architectures while the actual business job is platform-native or belongs elsewhere.
- Judgment prompt sketch: Given setup answers, workspace `CONTEXT.md`, selected architecture, and platform boundary, decide whether the selected architecture fits the business job or whether the work should stay in a platform. Flag invented architecture families.
- Required evidence/context: `SETUP.md` registry, `AGENTS.md` architecture list, workspace `CONTEXT.md`, `_config/platform-boundary.md`, setup-session answers if present.
- Expected output shape: `{status: pass|warning|fail, selected_architecture, recommended_architecture, platform_native_risk, evidence, required_fix}`.

### 2. Platform Boundary Judge

- Why deterministic checks are insufficient: prohibited platform ownership can be implied by workflow language, not only explicit words like "send" or "approve."
- Judgment prompt sketch: Review a workspace for any delegation of record ownership, approval state, entitlement, calculation ownership, delivery, or audit trail to Workspaces or AI.
- Required evidence/context: root `AGENTS.md`, `README.md` boundary, selected architecture `CONTEXT.md`, stage `CONTEXT.md` files, outputs.
- Expected output shape: `{status, boundary_violations[], platform_owner_missing[], deterministic_owner_missing[], human_owner_missing[]}`.

### 3. Authority And Conflict Judge

- Why deterministic checks are insufficient: source authority and conflicts require interpretation across source types, dates, versions, and claim use.
- Judgment prompt sketch: Review source packet, authority map, conflict log, and evidence brief. Flag claims that cite down the authority ladder, silently resolve conflicts, blend versions, recompute figures, or miss human-resolution paths.
- Required evidence/context: source packet, authority ladder, conflict rules, claim/evidence outputs.
- Expected output shape: `{status, unsupported_claims[], authority_issues[], unresolved_conflicts[], recomputation_risks[], human_owner_gaps[]}`.

### 4. Hostile Artifact Review Judge

- Why deterministic checks are insufficient: the important failures are often omitted claims, overconfident wording, missing caveats, and hard-to-defend assertions.
- Judgment prompt sketch: Review artifact, source packet, claim evidence map, artifact spec, severity config, and risk taxonomy as a skeptical approver. Do not rewrite. Name evidence gaps and required owners.
- Required evidence/context: artifact, source packet, claim evidence map, artifact spec, `_config/review-severity.md`, `_config/office-risk-taxonomy.md`.
- Expected output shape: artifact review report with overall status, high/medium/low severity issues, unsupported claims, stale numbers, formula/chart risks, inferences as facts, missing human confirmations, and recommended next action.

### 5. Artifact Severity Judge

- Why deterministic checks are insufficient: severity depends on use, audience, decision impact, and whether the artifact could mislead a stakeholder or approver.
- Judgment prompt sketch: Given identified issues and intended use, classify severity using the repo severity rules. Block high-severity issues that affect stakeholder, committee, investor, customer, auditor, or approver reliance.
- Required evidence/context: issue list, intended audience/use, severity config, artifact boundary, human approval rules.
- Expected output shape: `{overall_status, severity_by_issue[], blocking_issues[], warnings[], owner_required[]}`.

## Auto-Conversion Candidates

1. Builder readiness.
   - Check selected architecture exists.
   - Check required `_config` files exist.
   - Check `_config/before-you-trust-this.md` exists and has unresolved confirmations when placeholders or open questions appear.
   - Check stage `CONTEXT.md` files are customized from template defaults.
   - Check no seventh architecture directory was added without explicit approval.

2. Artifact attachment readiness.
   - Check module references are present when attached.
   - Check copied templates live under `_templates/artifact-trust/`.
   - Check source packet, claim evidence map, artifact review report, and human approval output paths are named when applicable.
   - Check module did not copy all files by default.

3. Source packet completeness.
   - Parse markdown table/sections for required fields from `source-register-schema.md`.
   - Require source IDs and uniqueness.
   - Flag blank owner, date, version, source system, and metadata gaps.

4. Claim evidence map integrity.
   - Parse claim table.
   - Require `Source ID` for numbers, dates, charts, and commitments.
   - Require owner or approval path for assumptions.
   - Require `blocked` status for superseded sources or missing source IDs.
   - Validate `Source ID` values against the source packet.

5. Stale number precheck.
   - Extract numbers, dates, charts, and table references.
   - Check whether they appear in claim map rows.
   - Check freshness date is present.
   - Flag rows with unknown, superseded, background, or blank source authority.

6. Formula risk precheck.
   - Use workbook extraction before any LLM review.
   - Detect formulas, hardcodes, external links, hidden sheets/ranges, missing check tabs, and output tabs without visible source/calculation lineage.
   - Let an LLM summarize risks only after deterministic workbook inspection.

7. Human approval gate.
   - Require named approver.
   - Require approved use.
   - Require status from `approved`, `approved with conditions`, or `not approved`.
   - Block external/stakeholder-facing use when approval note is missing.

8. Legacy naming absence.
   - Use `rg` when migration hygiene matters.
   - Do not keep as a recurring LLM judge.

## Drop / Keep Manual

Drop `legacy-naming-absence` as a standing judge criterion. It was useful for a one-time rename/refactor verification, but it is not a recurring quality judgment.

Keep `decision-prep-quality` manual for now. The repo has a clean example, but not enough real decisions or failure logs to justify a judge. Start with deterministic packet completeness: decision, owner, options, tradeoffs, risks, calculations, thresholds, recommendation, approval owner, and open confirmations.

Keep `stakeholder-response-safety` manual for now. It is high stakes, but the only observed example is short and controlled. A future judge may be justified after real response packets exist.

Keep `memory-causal-validation` manual. The repo explicitly makes causal validation human-owned. Automation should verify that validation status, dissent, uncertainty, and provisional labels are present. It should not decide the causal truth.

## Implementation Effort

| Work | Effort | Notes |
|---|---:|---|
| Deterministic markdown checks for source packets, claim maps, approval notes, status fields, and output paths | 1-2 days | Highest ROI. Uses local markdown parsing and `rg`. |
| Doctor extension for builder readiness and module attachment readiness | 1 day | Extends existing `scripts/setup_state.py doctor --json` pattern. |
| Workbook precheck for formula risk | 1-2 days | Needs XLSX parser and fixture work before any judge. |
| V2 LLM judges for architecture fit, platform boundary, authority/conflict, hostile review, and severity | 2-4 days | Build only after deterministic checks define the evidence bundle. |

## Summary

Top promotions: architecture fit, platform boundary, authority/conflict handling, hostile artifact review, and artifact severity.

Top auto-conversions: source packet completeness, claim map integrity, artifact attachment readiness, human approval gates, stale-number prechecks, formula-risk prechecks, and builder readiness.

Drops: legacy naming absence as a recurring judge.

Keep manual: decision-prep quality, stakeholder-response safety, and memory causal validation until real outputs create enough failure signal.
