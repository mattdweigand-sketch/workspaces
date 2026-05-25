# Request Context — Helio Support

The recurring customer record support needs to identify a requester, route correctly, and answer
with the right history and sensitivities in mind. L3 reference. This is NOT the system of record;
the CRM and ticketing platform hold authoritative customer data and entitlements. This file holds
the working context.

## Customer Entities and Contacts

- **Acme Corporation** — Enterprise plan, annual contract. Primary technical contact: Dana Liu
  (Data Engineering Lead), authorized on the account. Billing/commercial contact: Raj Mehta
  (routes through their Account Manager, not support). Account Manager (Helio side): T. Brooks.
- Authorized support requesters for Acme: Dana Liu and two named engineers on her team (per CRM
  entitlements). Anyone else asking for account data is unconfirmed until checked against the
  CRM.

## Standing Sensitivities

- Acme is a **reference customer** and is up for renewal in Q3 2026. Relationship-sensitive;
  T. Brooks (AM) wants visibility on any Sev-1/Sev-2 escalation.
- Acme runs Helio exports into a downstream regulatory report, so **data completeness is a hot
  button** for them — a truncation bug is exactly the kind of issue that escalates fast on their
  side.

## Request History

- 2026-02 — asked about export scheduling cadence (answered from FAQ, no issue).
- 2026-03 — feature request for column-level export filtering (logged to product, not a support
  matter).

## Routing Map

- Service credits / SLA compensation → T. Brooks (AM) + Support lead.
- Contract/SLA interpretation → T. Brooks (AM) + Legal.
- Security / data-exposure → Security on-call (pager).
- Renewal / relationship escalation → T. Brooks (AM).
