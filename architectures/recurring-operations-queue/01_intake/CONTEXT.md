# Stage 01: Intake

## Purpose
Receive an inbound request, determine what it actually is, classify it by type and sensitivity, confirm which stakeholder and account it concerns, assign priority, and produce a classified ticket the resolve stage can act on without re-reading the original.

## Inputs
- **The request**: stakeholder email, portal message, call note, or a forward from a colleague. Paste or reference it here.
- **_config/request-context.md**: To identify the stakeholder, the entities involved, and any standing sensitivities or preferences.
- **_config/response-standards.md**: To apply the right priority and to recognize what is the team's to answer versus what must be referred.

## Process
1. Read the request in full. Identify the actual question, which is not always the stated one. "Can you confirm my figure?" may really be "I am reconciling for my own review and need it by Friday."
2. Identify the stakeholder, the entity, the account, and the requester. Confirm against request-context.md. If you cannot identify the requester or their authority to receive the information, flag it — do not assume.
3. Classify the request by type:
   - **Informational** — a question answerable from governed data or the FAQ bank (a figure, a status, history, facts).
   - **Document request** — a re-send or copy of a statement, notice, or agreement.
   - **Action request** — the stakeholder wants something done (update contact details, explore an expansion, change instructions).
   - **Sensitive** — anything touching departure, a complaint, a contract interpretation, legal/compliance, or a figure dispute. These are flagged for escalation now, not answered later.
4. Assign priority based on the requester, the stated deadline, and the sensitivity.
5. Note what resolving it will require: which platform data, which team if escalation is needed, any authentication step.
6. Produce the classified ticket.

## Output
Write to: 01_intake/output/request-[stakeholder]-[date].md

Format:
```
# Request Ticket: [Short Description]

Stakeholder / Entity: [Name]
Requester: [Name, role, authorized: yes / no / unconfirmed]
Account: [Name]
Date received: [Date]
Type: [Informational / Document request / Action request / Sensitive]
Priority: [High / Medium / Low]

## What Was Asked
[The request in their words. Direct quote or close paraphrase.]

## What It Actually Requires
[Your read of the real need, and what answering it takes:
 which platform data, which document, which team.]

## Sensitivity / Escalation
[None, or: what makes this sensitive and who it must route to
 (team principal, compliance, counsel). If sensitive, the resolve
 stage acknowledges and hands off — it does not answer.]

## Notes
[Standing stakeholder sensitivities, prior related requests, deadline.]
```

## Done Looks Like
A ticket the resolve stage can act on without re-reading the original message or asking "is this one I can answer?" The type and sensitivity are decided here, on purpose, before any drafting.

## Common Failure Modes
- **Answering in the inbox.** The fastest way to mishandle a sensitive request is to dash off a reply before classifying it. Classify first. The departure signal that reads like a routine question is exactly the one this stage exists to catch.
- **Skipping requester verification.** Releasing account information to someone whose authority is unconfirmed is a control failure. If you cannot confirm the requester, say so in the ticket.
- **Taking the stated question literally.** Read for the real need. The misread question produces a technically-correct, actually-useless answer.

## Layer Annotation
L2 stage contract. The request is L4 (this run). Request context and response standards from _config/ are L3 (stable reference).
