# Worked Example: A Running Sales Win/Loss Loop

This is a worked sample from a different, fictional organization. It is a **read-only
calibration reference, not your data.** The company, the opportunities, and the people do not
exist. Study the shape and the rigor, not the content.

This folder is a fully instantiated copy of the `learning-loop` shape, populated for a B2B SaaS
sales win/loss practice so you can see what the loop looks like once it has run a few times. The
reference shape one level up (`../../learning-loop/`) ships empty on purpose — you copy and fill
it. This example shows a store with more than one record, because the whole point of the loop is
what emerges *across* records.

## The fictional setup

**Tessera** sells a data-integration SaaS platform (pipelines and connectors that move data
between a customer's systems). The revenue team runs a win/loss review each time an opportunity
closes — won or lost. The store below holds three closed opportunities; one of them (Atlas
Freight) is shown running through all three stages so you can follow a single pass end to end.

## What to look at, in order

1. **`_config/`** — the filled reference files. Note that `review-questions.md` is a fixed set
   answered the same way every time; that fixed set is what makes the three records comparable.
   The load-bearing question is the **stated-vs-assessed reason** check — the rep's stated reason
   for the outcome versus the reason the analysis actually establishes.
2. **A single pass (Atlas Freight, $84K ARR, Closed-Lost):**
   - `01_signal/output/record-atlas-freight-2026-05-09.md` — the raw facts: opportunity history,
     pipeline path, and the rep's *stated* loss reason, logged but not yet assessed.
   - `02_analysis/output/analysis-atlas-freight-2026-05-09.md` — the root-cause analysis, with
     the stated reason held distinct from the assessed real reason and confidence marked.
   - `03_capture/output/captured-atlas-freight-2026-05-09.md` — the capture log: what a human
     validated and which patterns moved.
3. **The store (`_store/`)** — the deliverable:
   - `records/` holds three opportunity records (Atlas Freight, Bluepeak Retail, Cedar Health).
   - `patterns.md` is the payoff: the pattern visible *across* the three records that no single
     opportunity could show. Read it last — it is the thing the next rep reads first.

## The lesson this example is meant to teach

A single win/loss write-up is nearly worthless. Three already reveal a theme: **both losses
trace to single-threading and never reaching the economic buyer** — a class of failure, not two
unrelated misses. That is exactly what the loop exists to surface, and it is exactly what the
stated-vs-assessed-reason check protects: in Atlas Freight the rep's stated reason was "lost on
price," which would have led to discounting harder next time and missing the real fix (multi-
threading early so a champion's departure doesn't end the deal). The store is the product; the
per-opportunity records are its inputs.

Everything here is fictional and illustrative.
