# Drafted Response: Acme Corporation — export truncation (ACME-4471)
Ticket reference: 01_intake/output/request-acme-2026-05-13.md
Type: Action request (bug resolution)

## Resolution Work-Up (internal; precedes the customer draft)

**Reproduction.** Re-ran Acme's export job def-9920 against a staging copy of their dataset.
Reproduced: job reports `completed`, file contains 38,114 rows, source query returns 52,090.
[per platform — Exports job run log, run IDs 11402–11404, 2026-05-11 to 05-13]

**Root cause.** The export pages the result set in 10,000-row batches behind a continuation
token (per FAQ bank, "How are scheduled exports paginated"). The documented contract is: a failed
page fetch retries the page and never emits a partial file. That contract did **not** hold. The
page-fetch retry path swallowed a timeout: on a slow page, the underlying request timed out, the
retry returned a 200 with an **empty body**, and the export treated the empty 200 as "this page
has no more rows" — terminating the job early and marking it `completed`. So the job stopped at
page 4 of 6. Rows on pages 5–6 were never written. [confirmed in the per-page log: page 5
returned 200, 0 bytes, after a retry following a timeout]

**Is data lost?** No. The **source data is intact** — the rows exist in the dataset; the export
failed to fetch them, it did not delete them. Verified by querying the source directly (52,090
rows present). [per platform — source dataset query, 2026-05-13]

**Permanent fix.** Engineering filed ENG-7781: the retry path must treat an empty-body 200
following a timeout as a *retryable failure*, not an end-of-stream signal, and the job must fail
loudly rather than mark `completed` on a short read. Committed for the 2026-05-20 release.

**Immediate workaround.** Re-running the export with a smaller page size (5,000 rows) avoids the
slow-page timeout that triggers the bug. Confirmed on staging: 5,000-row pages returned the full
52,090 rows. Customer can set this on job def-9920 tonight.

## Draft (customer-facing, support voice)

Hi Dana,

First and most important: **no data has been lost.** All 52,090 rows are present in the source
dataset. The export was failing to fetch some of them, not deleting them, so your underlying data
is intact.

Here's what was happening. Your export pages through the data in batches. On a slow batch, the
fetch was timing out, and the retry was coming back empty in a way the export misread as "no more
data," so the job stopped early and still marked itself completed. That's why you saw ~38k rows
with no error. The bug is on our side, and you were right to flag it.

What you can do tonight: on job def-9920, set the page size to 5,000 rows. That avoids the slow
batch that triggers the problem. We re-ran your export this way against a copy of your data and
got the full 52,090 rows.

The permanent fix is in progress and scheduled for our May 20 release, after which the export
will fail loudly instead of completing short, and the smaller page size won't be needed.

I'll keep this ticket open until the fix ships and confirm with you once it's live.

— Helio Support

## Source Trace
- 38,114 vs 52,090 row counts: platform — Exports job run log, def-9920, runs 11402–11404.
- Source intact (52,090 rows present): platform — source dataset direct query, 2026-05-13.
- Workaround verified (5,000-row pages → full count): staging reproduction, 2026-05-13.
- Fix date 2026-05-20: Engineering, ENG-7781 (committed, not yet shipped).

## For the Responder to Verify
- Confirm Dana Liu is the authorized requester before sending account-data detail (she is, per
  CRM — confirm it is still current).
- Confirm ENG-7781 is still committed to the 2026-05-20 release before stating that date.
- This is NOT a data-loss or exposure incident; do not let the reply imply one. Source verified
  intact.
