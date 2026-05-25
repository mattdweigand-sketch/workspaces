# Stage 02: Resolve

## Purpose
Answer the classified request. Retrieve the governed data or the vetted answer, draft a response in the team's voice, and flag anything that must be escalated rather than answered. The output is a response ready for review, with every figure tied to its platform source.

## Inputs
- **01_intake/output/request-[stakeholder]-[date].md**: The classified ticket. It defines the type, the real need, and any escalation flag.
- **_config/faq-bank.md**: Vetted answers to recurring questions. Check here first.
- **_config/request-context.md**: Entity details and history relevant to the answer.
- **_config/response-standards.md**: The answer-vs-refer line and the response register; its Voice section points to the team's shared voice in `_shared-config/voice-and-tone.md` — read that for the team voice.
- **Platform data**: The balance, performance figure, history, or document — retrieved from your system of record, the platform that owns the data. This is the source of any number. Load only what this request needs.

## Process
1. Read the ticket. If it is flagged sensitive, do not draft an answer. Draft an acknowledgment and route it to the named owner (see Output, escalation form). Stop there.
2. For non-sensitive requests, check the FAQ bank. If a vetted answer exists and fits, use it as the basis — do not reinvent an answer the team has already settled.
3. Retrieve any figure or document from the platform of record. Never state a balance, performance number, or financial figure of record from memory or inference. If the platform value is not available, say so in the draft and flag it for the responder, rather than estimating.
4. Draft the response in the team's voice (the shared `_shared-config/voice-and-tone.md`, reached via response-standards.md) at the response register. Answer the real need from the ticket, not just the literal question. Keep it accurate, complete, and on-tone.
5. Mark the source of every figure inline for the reviewer (e.g., "[figure per platform as of DATE]"). The responder confirms these; they are not sent to the stakeholder as-is unless the standards say so.
6. Note anything the responder must verify before sending.

## Output
Write to: 02_resolve/output/response-[stakeholder]-[date].md

For a standard request:
```
# Drafted Response: [Stakeholder] — [Request]
Ticket reference: [filename from intake]
Type: [Informational / Document request / Action request]

## Draft
[The response, in the team's voice, ready for review.]

## Source Trace
[Each figure or document referenced, and where it came from
 in the platform, with the as-of date. The reviewer confirms these.]

## For the Responder to Verify
[Anything to confirm before sending: requester authorization,
 a figure as-of date, an attached document.]
```

For a sensitive request (escalation):
```
# Escalation: [Stakeholder] — [Request]
Ticket reference: [filename from intake]
Routed to: [team principal / compliance / counsel]

## Why This Escalates
[What makes it sensitive and why it is not the team's to answer.]

## Drafted Acknowledgment to the Stakeholder
[A brief, non-committal acknowledgment confirming receipt and
 that the right person will follow up. Commits the organization to nothing.]
```

## Done Looks Like
A response the reviewer can check and send without re-researching it. Every figure traces to the platform. Sensitive requests carry an acknowledgment and a routing, not an answer.

## Common Failure Modes
- **Stating a number from memory.** The model will happily produce a plausible figure. A plausible figure is a wrong figure. Retrieve it or flag that you could not.
- **Answering a sensitive request anyway.** If intake flagged it, respect the flag. An off-hand answer to a departure or complaint can commit the organization to a position it did not intend.
- **Ignoring the FAQ bank.** Re-deriving an answer the team has already vetted is how two stakeholders get two different answers to the same question. Check the bank first.

## Layer Annotation
L2 stage contract. The ticket and the retrieved platform data are L4 (this run). FAQ bank, request context, and response standards from _config/ are L3 (stable reference).
