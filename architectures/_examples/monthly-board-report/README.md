# Worked Example: A Finished Monthly-Board-Report Cycle

This is a worked sample from a different, fictional organization. It is a **read-only
calibration reference, not your data.** The company, the numbers, and the board do not exist.
Study the shape and the rigor, not the content.

This folder is a fully instantiated copy of the `recurring-document-production` shape, populated
for one reporting cycle so you can see what "done" looks like. The reference shape one level up
(`../../recurring-document-production/`) ships empty on purpose — you copy and fill it.

**The company:** Northwind Analytics, a B2B SaaS company.
**The cycle:** monthly board report for May 2026.
**The pipeline:** data (verified metrics pack) → draft (the board report) → distribution (the
final, after a review pass).

## What to look at

- **`_config/`** — the four reference files, populated: `voice-and-tone.md`,
  `format-patterns.md`, `constraints.md`, and `before-you-trust-this.md`.
- **`01_data/output/metrics-pack.md`** — the verified numbers, every figure sourced to the
  system of record. The draft is written only from this.
- **`02_draft/output/draft-board-report-northwind-may-2026.md`** — the report written from the
  pack, before the review and constraint pass.
- **`03_distribution/output/final-board-report-northwind-may-2026.md`** — the same report after
  the review pass, ready to send.

## The two things this example is built to teach

1. **Every figure traces to the metrics pack.** Open the draft, pick any number, and you will
   find it in `01_data/output/metrics-pack.md` with a source. Nothing is generated in the draft.
2. **The draft → final diff shows a real review pass.** Compare the draft and the final: the
   review (a) added the required confidentiality and forward-looking note that the draft was
   missing, and (b) **corrected one figure** — the draft rounded runway to "14 months" but the
   metrics pack says **13 months**; the final matches the source. That is the control working.

## AI vs. platform boundary

The **system of record owns the metrics** (ARR, retention, burn, cash, headcount) — that is the
platform. **AI writes the narrative** around verified figures and explains the variances. It does
not produce or recompute a number. A **human reviews and signs off** before the report reaches
the board.

Everything here is fictional and illustrative.
