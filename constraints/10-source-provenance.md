# Constraint 10: I Don't Know What's In These Files

## The Problem

You point the model at a shared drive, a folder someone dumped on you, or a stack of uploaded documents and ask it to draft a memo, a report, or a summary. What comes back is fluent and confident, and it is wrong in a way that is hard to see. It weighted last quarter's model the same as the final one. It blended a number from `forecast_v2` with a number from `forecast_final`. It repeated a claim that no document in the set actually supports. It hit two files that disagreed on a figure and quietly picked one, without telling you there was a disagreement at all.

None of this is a drafting failure. The model wrote well. The failure happened at intake, before a single sentence was written, because the source set was never inspected. The model treated a pile of files of unknown age, authority, and provenance as if it were a single trustworthy corpus. Garbage in, garbage out is older than computing, but a language model makes the "garbage in" part frictionless: it will read anything you give it and never tell you it does not trust the inputs.

Every other constraint in this library governs what happens once the inputs are known and reliable. This one governs the step before that. The fix is not a better prompt. It is an inspection pass on the source set before any workflow stage runs.

---

## Layer 1: Principles That Predate AI

This is records management and chain of custody, and it predates AI by centuries. The discipline of knowing where a document came from, which version is authoritative, when it was superseded, and whether it can be trusted is the foundation of every audit, every legal proceeding, and every review ever run. ISO 15489 formalized records management as a discipline; the legal concept of chain of custody formalized provenance for evidence. Both exist because a decision is only as good as the records it rests on, and records that are unlabeled, duplicated, or stale corrupt the decision silently.

Teams already practice this when the stakes are visible. A review team maintains a document index. An accounting team keeps a single book of record. An auditor will not accept a number that does not tie to a source. The mistake is assuming the model inherits that discipline. It does not. It inherits whatever is in the folder, with no sense of which file is the book of record and which is a draft someone forgot to delete.

**Traditional tools that handle this:**
- **A document index or register.** The oldest version of a source inventory: a list of every document, what it is, and its status. Teams build these by hand. The model can build a first draft of one in minutes.
- **Version control (`git`, SharePoint version history, document management systems).** These exist precisely because "which version is current" is a question humans get wrong constantly. Where the system already tracks it, trust the system, not the model's guess.
- **File hashing and checksums.** Exact-duplicate detection is a deterministic operation. A checksum finds identical files faster and more reliably than any reasoning model.

---

## Layer 2: Existing Skills and Tools

**The document register, where your platform already keeps one**
If your CRM, ERP, or document management system maintains a register with upload dates, owners, and version status, that register is your authoritative inventory. Do not have the model rebuild it from scratch. Have the model read it and flag what looks stale or contradictory, layering judgment on top of the system of record rather than replacing it.

**Deterministic dedup before AI dedup**
Exact duplicates are a hashing problem, not a reasoning problem. Run a checksum or a file-comparison tool first. Reserve the model for the harder, genuinely probabilistic case: near-duplicates and version families where the content overlaps but the files are not identical (`model_v1`, `model_v2`, `model_final`). That is the 10% where reasoning earns its place.

**Project knowledge and file inspection**
In an environment with file-system access, the model can walk a folder tree, read metadata, and inspect contents to build an inventory directly. In an upload-based environment with project knowledge, it can do the same against the documents in the workspace. Either way, the inspection produces artifacts you read, not a silent judgment it acts on.

**The AGENTS.md and stage-contract pattern (Constraint 08)**
The inventory and its logs are reference material once built. They live alongside `_config`, get cited by every drafting stage, and survive the handoff. A claim cannot carry a `[S01]` citation unless an inventory assigned `S01` in the first place.

---

## Layer 3: The Architectural Fix

Run a provenance pass before any stage contract fires. Its job is to make the source set inspectable, and its single most important rule is the boundary it shares with Constraint 09: **the model classifies and flags; it never reconciles or computes.** It surfaces that two figures disagree. It does not decide which is correct. That decision belongs to a human or to the platform's book of record. A provenance pass that resolves conflicts on its own has reintroduced the exact failure it exists to prevent.

The pass produces four artifacts:

```
source_inventory   One row per file: name, type, date, owner,
                   relevance (high/med/low), authority
                   (authoritative/supporting/background/superseded),
                   current-or-stale, and a note for human review.

duplicate_log      Exact duplicates (from hashing), near-duplicates,
                   and version families. Which version appears current,
                   and why. Nothing deleted — flagged only.

conflict_log       Where two sources disagree on a number, date, or
                   decision. Both sides quoted. Which looks more
                   authoritative, and whether resolution needs a human.

missing_context    Claims with no supporting source. References to
                   documents not present. Numbers with no stated basis.
                   "As discussed" with no matching record.
```

**The authority ladder.** Not all sources are equal, and the model's default is to treat them as if they were. Force a ranking:
- **Authoritative** — the book of record. The system-of-record export, the executed agreement, the audited statement.
- **Supporting** — adds context but is not the source of truth. An analyst's summary, a working model.
- **Background** — relevant but not load-bearing. A market study, prior correspondence.
- **Superseded** — kept for history, never cited as current. The draft that a final replaced.

Once the ladder is set, drafting stages cite up the ladder, never down. A claim resting on a superseded file is a flag, not a sentence.

**Practical rules:**

1. **Inspect before you draft.** The provenance pass is a gate, not a suggestion. If a workflow drafts before the source set is inventoried, it is drafting on faith.
2. **Copy, never move; flag, never delete.** Originals stay untouched. Superseded and duplicate files are labeled, not removed. History is part of provenance.
3. **Never blend across versions.** A figure from `v2` and a figure from `final` do not belong in the same sentence. If the model cannot tell which version a number came from, that is a flag.
4. **Never silently resolve a conflict.** Two sources disagreeing is information. Surface it. The cheapest error to catch is the one the model was about to hide.
5. **Send numbers to the book of record.** The inventory establishes *which* source is authoritative for a figure. It does not recompute the figure. Tie-out is deterministic work (Constraint 09).

This is the upstream half of inspectable output. The inventory is what makes inline source citations, inference labels, and unsupported-claim flags possible in the drafting stages. Without it, "tie every figure to source" is an instruction with no sources to tie to.

---

## Tuning Questions

**1. Where do your inputs come from, and is provenance already tracked there?**
If they arrive through a platform with a document register and version history, that system is your inventory — have the model read it, not rebuild it. If they arrive as a pile of files in a shared drive or an email thread, there is no register, and the provenance pass is doing real work. Know which situation you are in before you run it.

**2. What is your authoritative source of record for numbers?**
Name it explicitly: the system-of-record export, the general ledger, the executed contract. This is the source the model is never allowed to adjudicate against. Everything else is supporting or background. If you cannot name a single book of record for a given figure, that ambiguity is itself the first thing to resolve.

**3. How often does stale or duplicate material reach you?**
If your inputs are clean and well-controlled, a light inventory is enough. If you routinely receive three versions of the same model and a folder no one has pruned in a year, the duplicate and version analysis is the highest-value part of the pass. Tune the depth to the mess.

---

## Quick Reference

| If this is your situation | Start here |
|---|---|
| Model blended numbers from two versions of a file | Run the provenance pass. Build the version families. Never cite across versions. |
| Output rests on a claim no document supports | The missing-context list catches this. Inspect inputs before drafting. |
| Two sources disagree and the model picked one silently | Conflict log. Both sides surfaced, resolution escalated to a human. |
| You don't know which file is the current one | Authority ladder. Rank every source before drafting; cite up, never down. |
| The model recomputed a number it should have looked up | Boundary violation (Constraint 09). The pass flags provenance; the platform owns the figure. |
