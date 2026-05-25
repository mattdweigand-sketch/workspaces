# Constraint 01: AI Keeps Writing Like AI

## The Problem

You asked for a paragraph in a monthly board report and got a press release. The output uses words you would never say to a reader, structures you would never choose, and a tone that sounds like it was optimized for the widest possible audience. Because it was. Language models generate text by sampling likely next words, and their post-training tunes them toward a safe, broadly acceptable register. Unless you give the model a specific standard to hit, it defaults to that register. The result is competent, safe, and generic. It reads like a committee wrote it.

This is not a prompting problem. It is a probability problem. And it has solutions at every level.

---

## Layer 1: Principles That Predate AI

Most of what makes AI writing sound artificial is not new. It is the same set of bad habits that George Orwell identified in 1946 in "Politics and the English Language." His six rules remain the most efficient diagnostic for weak prose, whether a human or a model wrote it:

1. Never use a metaphor, simile, or figure of speech you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Rule 6 is the one people forget. The point is not mechanical obedience. It is deliberate choice. AI writing fails Orwell's test because the model is not choosing. It is predicting. Every rule violation in AI output exists because that pattern was statistically common in training data.

Strunk and White's "The Elements of Style" compresses the same insight into three words: omit needless words. If you applied nothing else, your output would improve.

**Traditional tools that handle this:**
- **Hemingway Editor** (hemingwayapp.com, free online version): Highlights passive voice, adverb overuse, and sentence complexity. Color-coded. Takes 30 seconds. If your AI output lights up like a Christmas tree in Hemingway, fix it there before you touch your prompt. This is a deterministic check. Do not waste tokens on it.
- **Grammarly** (free tier handles grammar and spelling; paid tier adds style, tone, and clarity): Catches mechanical errors and some pattern issues. Good for a first pass. The paid version's tone detection is useful if you are writing for a specific audience.
- **ProWritingAid** (paid, one-time purchase option): Goes deeper than Grammarly on style analysis. Better for long-form work. Highlights echoes, sentence length variation, and overused words.

Run your AI output through one of these before you decide the model is the problem. Often, the model gave you a decent draft that needs editing, not a different prompt.

---

## Layer 2: Existing Skills and Tools

The AI community has already built targeted solutions for common writing patterns. These work inside Claude Code, Cursor, or any environment that supports skills.

**blader/humanizer** (github.com/blader/humanizer, 3,000+ stars)
The most established writing cleanup skill. Based on Wikipedia's "Signs of AI writing" guide maintained by WikiProject AI Cleanup. Identifies and rewrites patterns like significance inflation ("marking a pivotal moment in the evolution of..."), AI vocabulary ("delve," "landscape," "leverage," "tapestry"), and hedging language ("It's worth noting that..."). Includes an audit pass after the first rewrite to catch patterns that survived.

Forks exist that run a more aggressive multi-pass edit (covering structure, rhythm, and grammar-level patterns) if a draft needs heavier cleanup than the original handles. The core skill is enough for most stakeholder communications.

**Build a cleanup or review pass into your own workflow**
The pattern these skills use transfers directly to a team. Wrap your own "de-slop" or review step that runs after a draft is generated and checks it against your constraints file (Constraint 05) and, for anything customer-facing or externally published, your compliance checklist. It is the same idea as a marketing team's content-review skill, pointed at board reports and customer release notes instead of campaign copy. The toolkit's recurring-report architecture already places this as the distribution-stage compliance pass.

**Important caveat about all of these:** Skills that clean up AI writing are treating symptoms. They catch patterns after the model produces them. This works, and you should use them. But the architectural fix is deeper.

---

## Layer 3: The Architectural Fix

The reason AI writing sounds like AI writing is that the model is working from an undifferentiated context. It has no specific standard to hit, so it hits the average. The fix is not better prompting. It is better context architecture.

In the Interpreted Context Methodology (ICM) framework, writing quality is a function of what sits at Layer 3 (reference material) and Layer 2 (stage contract). If your L3 reference describes a detailed, specific standard, the model hits that standard. If your L2 contract says "write the monthly report," you get a generic monthly report. If it says "open with the single headline metric in the first sentence, one paragraph per workstream with the key operating number, address the largest miss head-on, close with the next 30 days, no summary," you get something specific.

This maps to a principle David Parnas formalized in 1972: information hiding. Each module (or in this case, each stage of your workflow) should only see the information it needs to do its job. When a writing stage sees everything, the token soup that is your entire brand, every past draft, all your notes, and a voice file, the model has to sort through all of it to figure out what matters. It trends toward the generic center because that is the safest path through ambiguous context.

The three-file voice architecture solves this:

**File 1: Voice and Tone** (directional, not rigid)
How the organization sounds to its readers, how it delivers good news and bad. This file gives alignment without a straightjacket. It describes the conditions under which your voice emerges rather than prescribing what your voice is. A model that knows "state the result plainly, explain the drivers, then address what the reader is most worried about before they have to ask" will produce different output than one that knows "be transparent and confident."

**File 2: Format Patterns** (structural guidance per format)
How a monthly board report differs from a customer release note differs from an internal decision memo. Short paragraph per format. This scopes the model's structural decisions without locking every communication into the same skeleton.

**File 3: Constraints** (the never-do list)
Read every time. These are the hard boundaries. No em dashes. No bullet-heavy structure when a paragraph would work. No significance inflation. No "it's worth noting." This file is the cheapest in tokens and the highest in impact because it eliminates the most common failure modes in a few lines.

The key insight: do not describe your voice TO the model. Describe the conditions, standards, and constraints that produce your voice. The model figures out behavior from the environment you give it. You do not need to write "be thorough" if you have described a thorough standard.

---

## Tuning Questions

Answer these before you use this constraint. Your answers shape how you implement it.

**1. What does your organization's voice actually sound like?**
Not what you wish it sounded like. What your lead sounds like explaining a month's results to the leadership team on a call, or what your last well-received report sounded like. That is your baseline. If you cannot describe it in two sentences, pull your three best prior reports and read how they open, how they handle a miss, and how they close. That is closer to your voice than anything a model will infer.

**2. What patterns does your organization use that generic AI avoids?**
Do you name the project and the issue directly rather than abstracting it? Do you state the headline number in the first sentence? Do you pair every problem with the action being taken? These are the textures that make a report sound like your team and not a template. Most teams have 3-5 of these. Write them down. Put them in your constraints file as things the model SHOULD do, not just things it should avoid.

**3. At what point in your workflow does "sounding like us" actually matter?**
If you are generating a first draft that finance and legal will heavily edit, spending tokens on voice alignment at the draft stage is waste. Save the voice files for the editing or polishing stage. If you are generating a notice that goes out with minimal editing, voice alignment matters from the start. Know which situation you are in. This determines when you load the voice constraints, not whether you load them.

---

## Quick Reference

| If this is your situation | Start here |
|---|---|
| Output has obvious AI patterns (em dashes, "delve," bullet addiction) | Run through Hemingway Editor first, then apply blader/humanizer skill |
| Output is clean but sounds generic | Build the three-file voice architecture (voice/tone, format patterns, constraints) |
| Output matches your voice sometimes but drifts | Your L2 stage contract is too vague. Tighten the structural specification. |
| You are not sure what your voice sounds like | Record yourself explaining your work. Transcribe it. Read it. That is your starting point. |
