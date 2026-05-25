# Taxonomy — Tessera sales win/loss review

The fixed vocabulary for tagging each opportunity record, so the store can aggregate. Patterns
emerge by tag — "we lose competitive evaluations when we're single-threaded" is only visible if
the reason and the threading depth are tagged consistently. L3 reference, loaded in stages 01 and
03. Keep it stable; add categories deliberately.

## Outcome (tag exactly one)
- Won
- Lost
- No-decision (evaluation stalled / closed without a purchase by anyone)

## ARR Band
- Small — under $25K ARR
- Mid — $25K–$75K ARR
- Large — $75K–$150K ARR
- Strategic — over $150K ARR

## Loss / Win Reason (controlled list — the high-value tag)
The reason class, so causes aggregate rather than scattering across free text:
`price` (cost / discount / budget), `product-gap` (missing capability or integration),
`competitor` (chose a named rival), `timing-no-decision` (no urgency / deferred / status quo
won), `champion-loss` (the internal advocate left or went quiet), `procurement-security`
(security review, legal, or procurement stalled the deal). Tag the primary reason; note a
secondary in the record if needed.

## Threading (controlled list — the other high-value tag)
How many stakeholders the rep was engaged with, so "single-threaded deals lose" becomes queryable:
- Single-threaded — one contact only
- Lightly multi-threaded — two to three contacts, one function
- Multi-threaded — several contacts across functions, economic buyer reached

## Competitor (controlled list)
The rival the opportunity was evaluated against, when known. Keep it a fixed list so "who we lose
to" aggregates. Current list: `Conduit`, `Meshgrid`, `in-house build`, `status-quo / no tool`,
`unknown`. Add a competitor only when it appears in an opportunity.

## Source / Segment
- Inbound, Outbound, Partner-referral, Expansion (existing customer).
- Segment by industry vertical at the grain you actually sell into (e.g. Logistics, Retail,
  Healthcare). Add a vertical only when you will query by it.
