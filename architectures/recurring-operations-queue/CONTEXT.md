# Workflow: Recurring Operations Queue

## Overview
Three-stage queue: Intake → Resolve → Respond. Designed for the inbound stakeholder questions that arrive between formal events. The stages separate three distinct modes of work: deciding what a request actually is, finding and drafting the answer, and reviewing before it reaches the stakeholder. Each request passes through all three. A human reviews before anything is sent.

## Stage Map

| Stage | Purpose | Inputs | Output Location |
|---|---|---|---|
| 01_intake | Receive, classify, prioritize, route | Stakeholder email, portal message, call note, forward | 01_intake/output/ |
| 02_resolve | Gather governed data, draft the response, flag escalations | Classified ticket, FAQ bank, request context, platform data | 02_resolve/output/ |
| 03_respond | Review for accuracy and tone, send, log, capture patterns | Drafted response, response standards | 03_respond/output/ |

## How Stages Connect
- 01 → 02: Intake produces a classified ticket — what type of request, which stakeholder, which account, what it actually requires, and how urgent. Resolve picks that up and answers it. If resolve has to ask "what is this person actually asking and is it sensitive?", intake did not finish its job.
- 02 → 03: Resolve produces a drafted response plus any escalation flags. Respond reviews it against the standards, sends it, and logs it. If respond is rewriting the substance, resolve needs tighter standards or better source data.
- Escalation path: at any stage, a request that is not the team's to answer (departure signal, complaint, legal/compliance/contract question) is flagged and routed to the right owner. It does not get a casual answer. The workflow's job then is to acknowledge and hand off, not to resolve.

## Reference Material (in _config/)
- response-standards.md: Service-level expectations, the answer-vs-refer line, and the response register on top of the team's shared voice (`_shared-config/voice-and-tone.md`). Loaded in stages 02 and 03.
- request-context.md: The recurring stakeholder record — entities, contacts, sensitivities, history. Loaded in stages 01 and 02.
- faq-bank.md: Vetted answers to recurring questions. Loaded in stage 02 and added to in stage 03.

## Reference Material (in _templates/)
- Response structures for the most common request types: acknowledgment, resolution, holding statement, escalation.

## When to Add Stages
Common additions:
- **02a_review** between resolve and respond: if responses that touch figures require an independent second-set-of-eyes check before they go out, separate from the tone review in respond.
- **01a_authentication** within or before intake: if you must verify the requester's identity and authority before releasing any account information (a real control for figure and document requests).

Add a stage when you find yourself consistently doing that work informally. Do not add it preemptively.

## AI vs. Platform: Where Each Step Lives

The temptation here is to let the model answer a figure or status question from context. Do not. The rule: rely on your platform for the data and the record, use AI for the language and the judgment. See Constraint 09 (Platform Boundary).

| Step in this workflow | Layer | Who owns it |
|---|---|---|
| Balances, performance figures, history, the stakeholder record, the audit trail | Platform / data foundation | Your system of record — the platform that owns the data |
| Whether the requester is authorized to receive the information | Deterministic / control | Platform entitlements plus a human check |
| Classifying the request, retrieving and phrasing the answer, drafting the response, flagging escalations | AI | You, on top of governed data |
| Anything that commits the organization — a departure, a contract reading, a complaint resolution | Human in the loop | The team principal, compliance, or counsel |

The trap on this workflow: the model stating a figure it did not retrieve from the platform, or answering a sensitive request that should have been escalated. AI classifies, retrieves, and drafts. The number comes from the platform, and a human owns anything that binds the organization.
