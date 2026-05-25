# Worked Example: A Finished Gated-Decision (Hiring) Pipeline

This is a worked sample from a different, fictional organization. It is a **read-only
calibration reference, not your data.** The people, the company, and the decision do not exist.
Study the shape and the rigor, not the content.

This folder is a fully instantiated copy of the `gated-decision-pipeline` shape, populated for a
single hiring decision so you can see what "done" looks like. The reference shape one level up
(`../../gated-decision-pipeline/`) ships empty on purpose — you copy and fill it. This example
shows the filled result for one candidate moving through the gate.

**The company:** Northwind Analytics, a B2B SaaS company hiring a Senior Backend Engineer.
**The candidate:** Jordan Avery.
**The pipeline:** intake (application) → evaluate (screen + interview-loop synthesis) → decide
(the go/no-go offer call, with the hiring bar applied).

## What to look at

- **`_config/`** — the three reference files, populated: the role scorecard and what the team
  takes on (`decision-criteria.md`), the hiring bar and automatic disqualifiers
  (`thresholds.md`), the standard screen assumptions (`evaluation-assumptions.md`), plus
  `before-you-trust-this.md`. This is what a customer's `_config` should look like after
  onboarding.
- **`01_intake/output/`** — the candidate normalized into a standard snapshot, facts tagged to
  source (the ATS owns the record; we just snapshot it).
- **`02_evaluate/output/`** — the screen summary and the interview-loop debrief synthesis,
  measured against the scorecard, with an advance/decline recommendation.
- **`03_decide/output/`** — the go/no-go offer memo, the bar applied by a human, with the
  decision recorded.

## The gate logic this teaches

Each stage is a go/no-go, not a score-and-pass. Intake gates on "enough to evaluate." Evaluate
gates on fit against the bar plus the disqualifier check. Decide is the human gate: the
recommendation is an input, the hiring manager owns the call. A decline is logged with a reason,
not a non-event.

## AI vs. platform boundary

The **ATS owns the candidate record** (application, resume, scheduling, status) — that is the
platform of record. **AI synthesizes** the screen notes and the four interviewer debriefs into a
comparable read against the scorecard and drafts the rationale. **A human makes the offer
decision.** AI never decides; it never invents a candidate fact the ATS does not hold.

Everything here is fictional and illustrative.
