# SKILL: Decision Prep Workspace Builder

## Description

Builds a workspace that prepares humans to make better decisions.

## When To Use

Use when the value is framing options, tradeoffs, risks, assumptions, precedent, and approval conditions.

Do not use to replace an approver, approval workflow, calculation model, or decision log.

## Diagnosis

Read shared config as directed by `SETUP.md`. Ask one question at a time.

1. What decision needs better preparation?
2. Who owns the decision, and where is approval recorded?
3. What facts and calculations come from platform or deterministic tools?
4. What criteria, risks, or precedents should shape the decision?
5. What would change the recommendation?

## Assembly

1. Copy `architectures/decision-prep/` into `workspaces/<name>/`.
2. Customize the decision frame, options, challenge, and approval packet stages.
3. Populate `_config/decision-criteria.md`, `_config/risk-lenses.md`, `_config/precedent-sources.md`, and `_config/platform-boundary.md`.
4. If the decision packet includes IC materials, board materials, approval decks, workbooks, memos, or other decision-facing artifacts, attach `modules/artifact-trust-layer/` using its attachment guide.
   - Reference module prompts, config, and human approval guidance in place by default.
   - Copy customized templates to `_templates/artifact-trust/` only when needed.
   - Name outputs for `01_decision_frame/output/artifact-spec-[name]-[date].md`, `03_challenge/output/artifact-review-report-[name]-[date].md`, and `04_approval_packet/output/human-approval-note-[name]-[date].md`.
5. Record open confirmations in `_config/before-you-trust-this.md`.
6. Run one sample decision through the decision frame stage.

## Verification

The workspace is ready when it produces a human-ready packet that makes the decision sharper without making the decision. If Artifact Trust Layer is attached, artifact claims and open issues are mapped before approval.
