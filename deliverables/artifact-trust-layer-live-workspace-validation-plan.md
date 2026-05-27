# Artifact Trust Layer Live Workspace Validation Plan

Date: 2026-05-27

## Purpose

Validate that a real workspace can use the Artifact Trust Layer without changing the six-architecture Workspces model.

## Recommended Test

Build a workspace using:

- Architecture: `evidence-review`
- Module: `modules/artifact-trust-layer/`
- Example source set: `modules/artifact-trust-layer/examples/diligence-evidence-map/`

## Test Workspace

Suggested name:

`workspaces/atlas-diligence-evidence-review/`

## Setup Answers

Use these answers for a controlled test:

| Question | Answer |
|---|---|
| What source material needs review? | CIM, management call notes, customer export, prior model, and market summary. |
| Where is source storage, version history, and access controlled? | Data room and shared drive. |
| What source is authoritative for key facts? | Customer export for customer metrics, pending RevOps confirmation. |
| What conflicts or stale-version risks are common? | Retention conflict between CIM and customer export. Prior model is stale. |
| Who resolves conflicts and approves claims? | Deal lead resolves diligence conflicts. RevOps confirms customer export. |
| Attach Artifact Trust Layer? | Yes. |
| Artifact type in scope? | Diligence evidence map feeding IC materials. |

## Expected Workspace Changes

The workspace should keep the `evidence-review` architecture and add only module references or customized templates.

Expected references:

- `modules/artifact-trust-layer/README.md`
- `modules/artifact-trust-layer/_config/artifact-boundary.md`
- `modules/artifact-trust-layer/_config/review-severity.md`
- `modules/artifact-trust-layer/_prompts/build-source-packet.md`
- `modules/artifact-trust-layer/_prompts/create-claim-evidence-map.md`
- `modules/artifact-trust-layer/_prompts/hostile-review.md`

Expected copied templates if customization is needed:

- `_templates/artifact-trust/source-packet.md`
- `_templates/artifact-trust/claim-evidence-map.md`
- `_templates/artifact-trust/artifact-review-report.md`

## Expected Outputs

| Output | Expected Location |
|---|---|
| Source packet | `01_inventory/output/source-packet-atlas-diligence-[date].md` |
| Claim evidence map | `04_evidence_brief/output/claim-evidence-map-atlas-diligence-[date].md` |
| Artifact review report | `04_evidence_brief/output/artifact-review-report-atlas-diligence-[date].md` |

## Pass Criteria

The live workspace test passes when:

- The selected architecture remains `evidence-review`.
- The module is referenced in workspace or stage context.
- The source packet exists and names source IDs.
- The claim evidence map cites only known source IDs.
- Unsupported claims are blocked or assigned to a human owner.
- The artifact review report has an overall status.
- Open confirmations are captured in `_config/before-you-trust-this.md`.
- No platform-native action is delegated to Workspces.

## Fail Conditions

The test fails if:

- The workspace becomes a new architecture.
- The module copies every file by default.
- Source conflicts are silently resolved.
- Figures are recomputed by the model.
- Human approval is missing.
- Output locations are ambiguous.

## Follow-On Decision

If this test passes, the next question is whether Workspces needs programmatic workspace generation for module attachment. The current setup script only tracks setup state. Do not add copying behavior to `scripts/setup_state.py` unless the setup engine becomes responsible for workspace materialization.
