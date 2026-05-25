# Organization Profile (shared)

<!--
THE ORGANIZATION, CAPTURED ONCE. Run Setup's orientation fills this in before any workspace is
built, and every builder reads it instead of re-asking the same questions. It is the org-level
context that is true regardless of which workflow you are running. Refine it any time the
organization changes.

This file is L3 reference. (Run Setup tells a first-time setup from a returning one by whether
`_shared-config/setup-progress.md` exists — that file is written at the end of the first setup.)
-->

## Organization
- **Name:** [Organization name]
- **What we do:** [What the organization does, who it serves, the kind of work it runs — e.g.,
  a 30-person B2B SaaS company; a regional accounting practice; an in-house marketing team]
- **The recurring work this toolkit will help with:** [The cyclical, repeatable knowledge work
  you want to put AI behind — high level]

## Systems of Record (the platform boundary)
[The authoritative systems AI must NARRATE but never compute or override. Name each and what it
owns. This is the single most important section for keeping AI in its lane (Constraint 09).
Examples — keep the ones that apply, add your own:]
- **CRM / pipeline:** [platform] — accounts, contacts, deal and relationship tracking.
- **Accounting / ERP / finance:** [platform] — the books, invoices, payroll, financial actuals.
- **Ticketing / project tracking:** [platform] — issues, tasks, support tickets, status of record.
- **Data warehouse / analytics:** [platform] — the metrics and numbers of record.
- **HRIS / ATS:** [platform] — people, candidates, the employee record.

## Team and Roles
[Who owns what, so workspaces route handoffs and sign-offs correctly. Examples:]
- [Name] — [Owns the work this workspace produces / final sign-off]
- [Name] — [Owns the data or the system of record this workflow reads from]
- [Name] — [Reviews / approves before anything goes to a customer, partner, or the public]

## Voice
The organization's written voice lives in `_shared-config/voice-and-tone.md` (this folder). Run
Setup seeds it here; it is fully populated the first time a writing workspace is built.
