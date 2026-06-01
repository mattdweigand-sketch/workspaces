# Example: Customer Escalation Exception

Architecture: `exception-handling`

A customer asks for a support commitment outside the normal SLA. The workspace frames the exception, relevant rules, response options, and escalation handoff.

## Boundary

- Support platform owns the ticket, SLA clock, owner, and audit trail.
- SLA policy owns standard routing.
- Workspaces owns exception reasoning.
- Support leader approves any non-standard commitment.

## Finished Output

See `escalation-handoff-customer-sla-2026-05-27.md`.
