# Artifact Trust Layer Smoke Test Report

Date: 2026-05-27

## Result

Pass.

## Test Scope

The smoke test checked whether the Artifact Trust Layer can attach to an `evidence-review` workflow and produce a usable diligence evidence map pattern.

## Checks Run

| Check | Result |
|---|---|
| Required module files exist. | Pass |
| Architecture hooks exist in `evidence-review`, `decision-prep`, and `stakeholder-response-prep`. | Pass |
| Builder hooks exist in the matching skill starters. | Pass |
| Diligence source packet defines source IDs. | Pass |
| Diligence claim map cites only known source IDs. | Pass |
| Unsupported claims without a source are blocked. | Pass |
| Review report marks the artifact as blocked pending human review. | Pass |
| Earlier naming is absent from checked files. | Pass |

## Test Data

Source packet: `modules/artifact-trust-layer/examples/diligence-evidence-map/sample-source-packet.md`

Claim evidence map: `modules/artifact-trust-layer/examples/diligence-evidence-map/sample-claim-evidence-map.md`

Review report: `modules/artifact-trust-layer/examples/diligence-evidence-map/sample-review-report.md`

## Findings

The module is usable as an attachable pattern. The diligence example creates the right chain:

1. Source IDs exist.
2. Claims cite those source IDs.
3. Unsupported claims are visible.
4. The review report blocks the artifact pending human review.

## Gaps To Tighten Next

The attachment guidance still leaves workspace customization to the builder. A future pass should make the copy/reference behavior more concrete:

- Which module files are copied into a workspace.
- Which files are referenced in place.
- Which stage outputs are added for each architecture.
- Where generated source packets and claim maps should land inside a live workspace.
