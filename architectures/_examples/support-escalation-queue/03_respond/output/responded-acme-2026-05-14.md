# Response Record

Customer / Entity: Acme Corporation
Request: Scheduled export silently truncating rows (ACME-4471)
Ticket reference: 01_intake/output/request-acme-2026-05-13.md
Type: Action request (bug resolution)
Figures confirmed to source: Yes
Requester authorization: Confirmed (Dana Liu, per CRM, re-checked 2026-05-14)
Sent via: Ticketing system reply (email-backed)
Sent on: 2026-05-14

## Review Notes (the control gate)
- **Addresses the real need?** Yes — leads with "no data lost," which was the customer's true
  fear given the compliance dependency, then the workaround, then the fix and timeline.
- **Figures confirmed to source?** Yes. Row counts trace to the platform run log; source-intact
  to a direct dataset query; workaround to the staging reproduction. The fix date was re-checked
  against ENG-7781 before send.
- **Authorization?** Confirmed Dana Liu is current authorized contact in the CRM.
- **Anything that commits the company?** No credit or SLA-compensation language in the reply —
  that is correctly absent (it would route to the AM, not support). T. Brooks (AM) was notified
  separately of the Sev-2 for renewal-relationship visibility; the customer reply itself commits
  nothing financial.
- **Incident framing?** Reply does not characterize this as data loss or exposure. Correct.

## What Was Sent
The customer-facing draft from 02_resolve/output, sent verbatim after the checks above. Ticket
left open pending the 2026-05-20 fix, with a commitment to confirm once it ships.

## FAQ Bank
Captured: yes — added "Export job shows 'completed' but downstream is missing rows — what now?"
to `_config/faq-bank.md` (dated 2026-05-14), with the empty-200-after-timeout signature, the
5,000-row workaround, and the escalate-to-Engineering instruction. This was the third
export-completeness question this quarter, so it earned a bank entry.

## Follow-up Required
- Confirm with Dana once ENG-7781 ships in the 2026-05-20 release, then close the ticket. (Owner:
  support, due on release.)
- AM (T. Brooks) to fold into the Q3 renewal touchpoint that the issue was resolved with no data
  loss. (Owner: AM.)
