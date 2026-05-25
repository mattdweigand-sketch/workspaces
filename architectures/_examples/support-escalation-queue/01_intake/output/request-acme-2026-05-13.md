# Request Ticket: Scheduled export silently truncating rows

Customer / Entity: Acme Corporation (Enterprise)
Requester: Dana Liu (Data Engineering Lead) — authorized: yes (per CRM, _config/request-context.md)
Account: Acme Corporation
Ticket: ACME-4471 (ticketing system owns status; snapshotted here)
Date received: 2026-05-13
Type: Action request (a bug to resolve), bordering Sensitive (data completeness, reference account)
Priority: High → recommend Sev-2 (degraded function, data integrity, workaround likely)

## What Was Asked
Dana Liu, verbatim: "Our nightly export to the regulatory report has been short on rows for the
last three nights. The job says 'completed' every time but we're getting ~38k rows when the
source has ~52k. No error anywhere. This feeds a compliance report, so we need to know fast
whether data is being lost or just not exported."

## What It Actually Requires
The literal question is "why are rows missing." The real need is twofold: (1) confirm **no data
is lost** at the source — this is a compliance-fed pipeline, so the customer's true fear is data
loss, not export inconvenience; and (2) a fix plus an immediate workaround so tonight's run is
complete. Resolving it requires: the export job's per-run logs (from the platform), reproduction,
and a root-cause work-up. The FAQ bank has a near-match entry ("row count looks low") to start
from.

## Sensitivity / Escalation
- **Not yet a security/data-exposure matter** — this is missing rows in an export, not exposed
  data. Do not characterize it as an incident to the customer until root cause is known.
- **Relationship-sensitive:** Acme is a reference account up for Q3 renewal, and data
  completeness is their hot button. Per the routing map, T. Brooks (AM) is notified of this
  Sev-2 for visibility. Support still owns the technical resolution.
- **If the work-up finds actual source data loss,** that escalates immediately (AM + Support lead,
  and Security if exposure is implicated). The resolve stage must confirm the source is intact
  before reassuring the customer.

## Notes
- Standing sensitivity: regulatory-report dependency means "is data lost?" must be answered
  explicitly and first.
- Prior history: routine export-cadence question in Feb (FAQ-answered). No prior incidents.
- Deadline: tonight's run. Workaround needed same day.
