# Example: Vendor Request Intake

Architecture: `messy-input-intake`

An operations lead receives a forwarded email thread, a pricing screenshot, and two Slack notes about a requested vendor. The workspace turns those messy inputs into a clean brief for human review.

## Boundary

- Platform owns the vendor record, approval state, and audit trail.
- Rules own routing to procurement when the spend threshold is met.
- Kit owns interpretation of the messy input set.
- Human approver decides whether to create the vendor request.

## Finished Output

See `intake-brief-vendor-request-2026-05-27.md`.
