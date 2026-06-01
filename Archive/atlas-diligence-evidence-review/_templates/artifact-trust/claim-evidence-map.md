# Claim Evidence Map

Use this after the source packet exists and before trusting the artifact.

| Claim ID | Artifact Location | Claim Text | Claim Type | Source ID | Evidence Note | Source Authority | Freshness Date | Confidence | Open Issue | Review Status | Human Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 |  |  | fact/number/date/interpretation/assumption/recommendation/commitment |  |  | authoritative/supporting/background/superseded |  | high/medium/low/unverified |  | pass/warning/blocked |  |

## Rules

- Every load-bearing claim gets a row.
- Numbers, dates, charts, and commitments require a source ID.
- Inferences must be labeled as interpretations.
- Assumptions must name an owner or approval path.
- Claims resting on superseded sources are blocked until reviewed.
