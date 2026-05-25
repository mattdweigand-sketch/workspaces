# Response Standards — Helio Support

How Helio support responds, how fast, in what voice, and where the line sits between what support
answers directly and what gets referred. The resolve stage drafts against this; the respond stage
reviews against it. L3 reference, stable across tickets.

## Service Levels

- Acknowledge every escalated ticket within **1 business hour**.
- Sev-2 (degraded function, workaround exists) — substantive response within **1 business day**;
  resolution target **3 business days**.
- Sev-1 (data loss, outage, security) — acknowledged immediately, paged to on-call, status
  updates every **2 hours** until mitigated.
- A ticket's official severity and SLA clock live in the ticketing system, not here. This file
  defines the policy; the platform tracks the state.

## Voice (support register)

Helio's core written voice is defined once in the shared team voice file
(`_shared-config/voice-and-tone.md`). Read it for the base voice; do not redefine it here. The
support register layered on top:

- Plain, direct, and human. Name the problem in the customer's words before explaining.
- Own the issue without grovelling. "You're right, the export was truncating" — not five
  sentences of apology.
- Lead with what the customer can do *now* (the workaround), then what we're doing to fix it
  permanently, then when.
- No internal jargon, no ticket numbers in the body unless the customer used them, no
  speculation about cause we haven't confirmed.

## What Support Answers Directly

- Reproduction status, confirmed root cause, the fix and its timeline.
- A documented workaround.
- Product behavior and configuration questions answerable from the docs or the FAQ bank.
- Data facts retrieved from the platform (a customer's plan, a job's run history, a log line).

## What Gets Referred (and to whom)

- **Service credits, refunds, or SLA-breach compensation** → Account manager + Support lead.
  Support never commits a credit.
- **Contract or SLA interpretation** → Account manager + Legal.
- **Anything implying a security or data-exposure incident** → Security on-call immediately; do
  not characterize scope to the customer until Security confirms.
- **A churn-risk or relationship escalation** → Account manager.

## Never-Do List

- Never state a system fact (job status, row counts, plan) not retrieved from the platform.
- Never promise a fix date Engineering has not committed to.
- Never confirm or deny data exposure before Security has assessed it.
- Never offer a credit or commit the company financially in a support reply.
