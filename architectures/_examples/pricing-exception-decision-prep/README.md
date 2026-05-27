# Example: Pricing Exception Decision Prep

Architecture: `decision-prep`

A sales lead requests a non-standard discount. The workspace prepares the decision owner with options, tradeoffs, risks, and approval conditions.

## Boundary

- CRM owns the opportunity record and approval state.
- Pricing model owns margin math.
- Kit owns decision framing and challenge.
- Revenue leader approves or rejects.

## Finished Output

See `approval-packet-pricing-exception-2026-05-27.md`.
