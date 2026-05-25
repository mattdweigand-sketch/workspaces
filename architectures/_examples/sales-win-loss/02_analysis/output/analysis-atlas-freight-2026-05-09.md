# Win/Loss Analysis: Atlas Freight — Data-integration platform
Record reference: 01_signal/output/record-atlas-freight-2026-05-09.md   Outcome: Lost ($84K ARR)

## Canonical Questions
1. **Source / ARR / segment:** Outbound, $84K ARR (Large band), Logistics. SDR-sourced into the
   VP of Operations.
2. **Pipeline path:** Discovery 2026-02-03; technical eval 2026-02-19; POC confirmed 2026-03-11;
   champion departed 2026-03-30; re-engaged analysts 2026-04-08; security questionnaire stalled
   from 2026-04-15; Closed-Lost 2026-05-09. ~95-day cycle. Stalled at the champion's departure.
3. **Threading:** Single-threaded. The only real relationship was the VP of Operations (champion);
   below her, two analysts with no budget authority. **No economic buyer was ever reached**
   (confirmed: no EB contact in the CRM). When the VP left, the opportunity had no one with
   authority left in it.
4. **Buyer's goal / alternative:** Eliminate ~10 hrs/week of manual CSV handoffs between warehouse
   and billing systems. The alternative was the **status quo** (keep doing it by hand) — not a
   named competitor. No competitive tool was in the evaluation.
5. **Stated vs. assessed reason:** *Stated* (rep, close note) — "lost on price, $84K was too much."
   *Assessed* — a **champion loss compounded by single-threading and a stalled security review**.
   The champion departed mid-cycle (2026-03-30); because the rep had never multi-threaded to an
   economic buyer, there was no one with authority to carry the purchase, so it defaulted to the
   status quo. Price was *named* in the close note but **no discount was ever requested and no one
   with budget authority ever said the price was too high** — there was no budget holder in the
   deal at all. Asking "why" past "price": who said it cost too much? No economic buyer was ever
   in the room to say it. Price is the comfortable post-hoc label, not the driver. [assessed
   confidence: HIGH — the absence of any EB contact and the timing of the stall both point here]
6. **Reason class:** `champion-loss` (primary), with `procurement-security` (secondary — the
   stalled security questionnaire removed the last path to recovery). Not `price`.
7. **Where momentum broke:** It held through technical evaluation and POC, then broke at the
   champion's departure and never recovered through procurement/security.
8. **What made it worse:** Single-threading — the entire opportunity rode on one person, so her
   departure ended it. And leaving the security review to the end with no internal owner to push
   it meant there was no momentum to overcome the leadership gap.
9. **What would have changed it:** Multi-threading to the VP's manager or a head of IT *before*
   the champion left would have preserved an authority path. It stopped being winnable around
   2026-04-08, once the re-engaged analysts confirmed no one could authorize spend and no
   replacement sponsor was pursued.
10. **If won:** n/a (lost).
11. **Transferable play:** On any opportunity above the Mid ARR band, reach the economic buyer by
    the technical-evaluation stage, not after. Treat a single-threaded large opportunity as
    at-risk by default. Front-load the security review while a champion is still engaged.

## Stated vs. Assessed Reason
The rep stated "lost on price." The assessed real reason is a **champion loss that single-
threading turned terminal**, with a stalled security review closing off recovery. These are not
the same, and the difference is decisive: if we accept "price," the next move is to discount
harder, which would not have saved a deal that had no budget authority left in it. I do not
collapse them. The evidence is strong — there is no economic-buyer contact anywhere in the CRM, no
discount was ever requested, and the opportunity stalled the day the champion left, not over a
number. [HIGH]

## Why (proposed)
Root reason: the opportunity was single-threaded on one champion and never reached an economic
buyer; when the champion departed, no one with authority remained to carry the purchase, and a
late, unowned security review removed the last path back. Causal: the single-threading / no-EB
access and the champion's departure. Incidental: price (named in the close note but never a live
objection — no discount requested, no budget holder to object) and the security questionnaire's
SOC 2 detail (real friction, but it only mattered because there was no sponsor left to push past
it). [HIGH]

## Against the Store
**Extends the emerging single-threading pattern.** Bluepeak Retail (lost) was also single-threaded
with no executive sponsor; the rep there stated "went with a competitor," but the assessed driver
was the same no-EB-access gap. Atlas Freight is the **second loss** in this class. Cedar Health
(won) is the contrast: multi-threaded, economic buyer reached by stage 2, security cleared early.
This should **promote the single-threading pattern toward STATED** and **strengthen the
counter-pattern that "price" / "competitor" is the stated reason but rarely the decisive one**.
Does not contradict any pattern.

## What We'd Do Differently
- Make economic-buyer access a stage-gate on any opportunity above Mid ARR: do not advance a
  Large opportunity past technical evaluation while it is single-threaded.
- Front-load the security questionnaire while the champion is still engaged, so it cannot become
  the thing that quietly kills a leaderless deal.

## For the Validator
- Confirm the assessed reason (champion-loss + single-threading, not price), HIGH, based on the
  absence of any EB contact and the fact that no discount was ever requested.
- Confirm the close note's "price" should be downgraded to incidental — capturing it as the cause
  would point the team at discounting, the wrong fix.
- Confirm this extends the single-threading pattern (this is the second loss in the class).
