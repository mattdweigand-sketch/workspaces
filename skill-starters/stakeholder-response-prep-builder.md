# SKILL: Stakeholder Response Prep Workspace Builder

## Description

Builds a workspace that prepares high-context communication from verified facts.

## When To Use

Use when the team needs to explain facts to customers, executives, employees, partners, board members, investors, or other stakeholders.

Do not use to invent facts, bypass approval, send messages, manage stakeholder records, or own audit.

## Diagnosis

Read shared config as directed by `SETUP.md`. Ask one question at a time.

1. Which stakeholder conversations or responses need preparation?
2. Which platform or owner verifies the facts?
3. What audience context and sensitivities matter?
4. What claims, commitments, or wording require approval?
5. Who reviews and sends the final response?

## Assembly

1. Copy `architectures/stakeholder-response-prep/` into `workspaces/<name>/`.
2. Customize verified facts, message frame, question prep, and review packet stages.
3. Populate `_config/audience-map.md`, `_config/voice-and-tone.md`, `_config/claim-rules.md`, and `_config/platform-boundary.md`.
4. If the response produces LP narratives, investor updates, executive updates, board updates, decks, memos, or other stakeholder-facing artifacts, attach `modules/artifact-trust-layer/` using its attachment guide.
   - Reference module prompts, config, and human approval guidance in place by default.
   - Copy customized templates to `_templates/artifact-trust/` only when needed.
   - Name outputs for `01_verified_facts/output/claim-evidence-map-[name]-[date].md`, `04_review_packet/output/artifact-review-report-[name]-[date].md`, and `04_review_packet/output/human-approval-note-[name]-[date].md`.
5. Record open confirmations in `_config/before-you-trust-this.md`.
6. Run one sample response through verified facts and message frame.

## Verification

The workspace is ready when every claim traces to verified facts and every stakeholder-facing output requires human review. If Artifact Trust Layer is attached, artifact claims and review issues are mapped before approval.
