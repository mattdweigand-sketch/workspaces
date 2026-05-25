# FAQ Bank — Helio Support

Vetted answers to recurring questions. The resolve stage checks here first; the respond stage
adds to it when a new reusable answer emerges. This is the asset that keeps support fast and
consistent. L3 reference; the one config file a stage (03_respond) writes back to.

Keep figures and live status as pointers to the platform — never hard-code a number here.

## How to Use This File

Each entry is a settled answer pattern and, where data is involved, where the live value is
retrieved. When you answer a new question that will recur, add it.

## Entries

### Q: My scheduled export ran but the row count looks low. How do I check it?
Direct the customer to the export job's run detail in the Helio console (Exports → job → Run
history), which shows rows written and the status code per run. If the row count is below the
source query count, capture the job ID and run timestamp and escalate to support — do not assume
the data is lost; it is usually a pagination or timeout issue on the export side. (Pattern only;
the live counts come from the platform.)

### Q: How are scheduled exports paginated?
Helio exports page through the result set in batches of 10,000 rows. Each page is fetched with a
continuation token. If a page fetch fails, the documented behavior is to retry the page, not to
emit a partial file. (This is the documented contract; see the resolution log for ACME-4471 for a
case where it did not hold.)

### Q: Can you re-send a past export file?
Yes, for any run inside the retention window (30 days on Enterprise). Confirm the requester is
authorized on the account in the CRM first, then re-trigger the run from the console. (Pattern;
authorization check required before sending data.)

### Q: Export job shows "completed" but downstream is missing rows — what now? [ADDED 2026-05-14, from ACME-4471]
A "completed" status only means the job finished, not that every page was written. If rows are
missing, check the job's per-page log for a page that returned a 200 with an empty body after a
retry. The immediate workaround is to re-run the export with the smaller page size (5,000) until
the permanent fix ships. Root cause and fix are documented in the ACME-4471 resolution log.
Escalate any new instance to Engineering with the job ID.
