# Worked Example: A Finished Support-Escalation Queue Run

This is a worked sample from a different, fictional organization. It is a **read-only
calibration reference, not your data.** The customer, the ticket, and the bug do not exist.
Study the shape and the rigor, not the content.

This folder is a fully instantiated copy of the `recurring-operations-queue` shape, populated for
a single escalated support ticket so you can see what "done" looks like. The reference shape one
level up (`../../recurring-operations-queue/`) ships empty on purpose — you copy and fill it.

**The company:** Helio, a B2B SaaS analytics product.
**The ticket:** ACME-4471 — a customer reports that their scheduled data export is silently
truncating rows.
**The queue:** intake (triage the ticket) → resolve (root cause + fix/workaround, drawing on the
FAQ bank) → respond (a customer-facing reply, on-voice).

## What to look at

- **`_config/`** — the four reference files, populated: `response-standards.md` (service levels,
  the answer-vs-refer line, the support voice register), `request-context.md` (the customer
  record and standing sensitivities), `faq-bank.md` (vetted answers, including the one this run
  draws on and the new one it adds back), and `before-you-trust-this.md`.
- **`01_intake/output/`** — the triaged ticket: type, severity, customer, what it actually
  requires.
- **`02_resolve/output/`** — the resolution work-up: reproduction, root cause, the permanent fix
  and the immediate workaround, every status fact tied to its source system.
- **`03_respond/output/`** — the customer-facing reply, drafted on-voice and reviewed, plus the
  log and the FAQ-bank capture.

## AI vs. platform boundary

The **ticketing system owns ticket status** (severity, SLA clock, assignment, the audit trail) —
that is the platform of record. **AI owns the judgment and the language**: classifying the
ticket, working up the root cause from logs and the FAQ bank, and drafting the on-voice reply. A
**human reviews before the reply is sent**, and anything that commits the company (a credit, a
contractual promise) is escalated, not answered.

Everything here is fictional and illustrative.
