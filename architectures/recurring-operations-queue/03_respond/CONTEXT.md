# Stage 03: Respond

## Purpose
Review the drafted response for accuracy and tone, confirm the figures trace to source and the requester is authorized, send it, log it, and capture any reusable answer back into the FAQ bank. This stage is the control gate before anything reaches a stakeholder.

## Inputs
- **02_resolve/output/response-[stakeholder]-[date].md**: The drafted response or escalation, with its source trace.
- **01_intake/output/request-[stakeholder]-[date].md**: The original ticket, to confirm the response addresses what was actually asked.
- **_config/response-standards.md**: The accuracy and voice bar to check against (team voice from the shared `_shared-config/voice-and-tone.md`, plus the response register).
- **_config/faq-bank.md**: Updated here when a new reusable answer emerges.

## Process
1. Read the drafted response and the original ticket together. Does the response address the real need, not just the literal question?
2. Confirm the figures. Each number must trace to its platform source at the stated as-of date. A figure with no trace does not go out.
3. Confirm the requester is authorized to receive what is being sent. If intake left this unconfirmed, resolve it now.
4. Check tone against response-standards.md. The voice should be the team's (the shared `_shared-config/voice-and-tone.md`), at the response register, consistent with what other stakeholders receive.
5. For escalations: confirm the acknowledgment commits the organization to nothing and that the routing reached the named owner. Do not answer the substance here.
6. Send through the appropriate channel (portal message, email reply).
7. Log the request and its resolution. If the answer is one that will recur, add it to the FAQ bank so the next person does not re-derive it.

## Output
Write to: 03_respond/output/responded-[stakeholder]-[date].md

```
# Response Record

Stakeholder / Entity: [Name]
Request: [Short description]
Ticket reference: [filename from intake]
Type: [Informational / Document request / Action request / Sensitive-escalated]
Figures confirmed to source: [Yes / N/A]
Requester authorization: [Confirmed / N/A]
Sent via: [Portal / email]
Sent on: [Date]

## What Was Sent
[The final response text, or for an escalation, the acknowledgment
 sent and the owner the substance was routed to.]

## FAQ Bank
[Captured: [yes — added as "QUESTION"] / no — one-off]

## Follow-up Required
[None, or: what is outstanding (a referred item awaiting the owner's
 answer, a promised document) with a date.]
```

## Done Looks Like
The stakeholder has an accurate, on-voice response, or — for a sensitive request — a clean acknowledgment while the right owner handles the substance. A record exists of what was sent, when, and that the figures tied to source. Reusable answers are in the FAQ bank.

## Common Failure Modes
- **Rubber-stamping the figures.** This is the second set of eyes. If you send a number without confirming its trace, the control did nothing. Confirm before send.
- **Sending to an unauthorized requester.** Authorization is part of the control, not a formality. Confirm it before account information leaves.
- **Never feeding the FAQ bank.** If recurring answers are not captured, every person re-researches the same questions and the answers drift apart over time. Capture is what makes the workspace get faster and stay consistent.

## Layer Annotation
L2 stage contract. The drafted response and ticket are L4 (this run). Response standards are L3. The FAQ bank is L3 reference that this stage writes back to — the one place a stage output updates a config file, on purpose, so the bank compounds.
