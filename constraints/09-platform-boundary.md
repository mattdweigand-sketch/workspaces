# Constraint 09: I Do Not Know What to Build and What to Rely on My Platform For

## The Problem

You are sold on applying AI to your organization. You have read Constraint 06 and you accept that only a slice of your work is genuinely an AI task. But a harder question sits underneath it: of the work that is not AI, what should you build yourself, and what should you rely on an enterprise platform to provide? You see vendors demoing impressive AI, and you also have a capable team that could wire something together. So you are tempted to build your own data layer, your own reconciliation, your own agent that reads everything and answers anything.

This is the most expensive mistake a team can make with AI. The reason is simple and it is not about model quality. AI does not fail at the model. It fails at the data and at the deployment layer underneath the model. The parts that determine whether an AI agent produces real work or just produces output are almost entirely non-model components, and most of them are enterprise infrastructure that takes years and domain expertise to build correctly. Building them yourself, or worse, asking a language model to be them, produces a confident system that is wrong in ways you cannot see until a customer or an auditor finds them.

The fix is to know exactly where the boundary sits: what AI does, what a deterministic tool does, and what your platform must own.

---

## Layer 1: Principles That Predate AI

This is the build-versus-buy decision, and it is older than software. Every organization faces it for every capability: is this core to what we do and a source of edge, or is it infrastructure that is necessary but not differentiating? Theodore Levitt and later Geoffrey Moore framed the same idea as core versus context. You invest your own effort in core. You source context from someone whose core it is.

For most organizations, serving customers and building the product is core. Maintaining a normalized, reconciled, audit-ready record of your business data across multiple systems is context. It is essential, and getting it wrong is catastrophic, but it does not win you a single customer or a single sale. It is the plumbing. You do not win by having better plumbing than the company down the street. You win by spending your scarce attention on the things that compound, and sourcing the plumbing from someone whose whole business is getting it right.

The same separation-of-concerns principle that governs your workspace (Constraint 03) governs your technology stack. A module should own the thing it is best at and expose a clean interface to everything else. Your organization's edge is a module. Your data foundation is a different module. Do not collapse them.

**The traditional version of this decision:**
- You do not run your own electrical grid. You buy power and put your effort into what you make with it.
- You do not build your own accounting standards. You apply GAAP and put your effort into the judgment that GAAP cannot make for you.
- You do not write your own accounting engine from scratch in Excel and trust it with the company's books. You use a system built and audited for that purpose.

AI does not change this calculus. It sharpens it, because AI raises the cost of a bad foundation. A spreadsheet error stays in the spreadsheet. A bad foundation that an AI agent reads from and acts on propagates the error at machine speed into customer communications, financial reports, and decisions.

---

## Layer 2: Existing Skills and Tools

The question is not which model to use. It is whether the six things that make an AI agent actually work are being built, and by whom. None of these are model work. All of them land on the enterprise platform by default. When you evaluate any vendor, including the one you might build yourself into, these are the components to account for.

**1. Workflow design.** Which decisions does the model make, which stay human, where are the handoffs, what counts as done? This is a defined process with owners, inputs, and outputs, not a prompt. The toolkit's stage contracts are how you build this part yourself, and you can. This one is yours.

**2. Data access.** Which sources of truth does the agent read? Which permissions apply at the row and field level? Which records are authoritative and which are stale? A model gives an equally confident answer from a six-month-old PDF and a live record. Deciding which it reads, and enforcing record-level entitlement while it does, is platform infrastructure. **This one is not yours to build.**

**3. Authority.** What is the agent allowed to do, against which systems, with what limits? Reading is one risk profile. Writing to a system of record is another. Committing money or changing a customer's status is something you cannot easily undo. Authority has to be enforced at the action level by the systems being acted on. **Platform infrastructure.**

**4. Evals.** How do you measure whether output is correct, complete, and safe before it goes anywhere? Evals score adherence to your specific business rules, not generic benchmarks. You can and should own the business rules. The platform should be able to tell you what its own AI is evaluated against.

**5. Audit trails.** What gets logged, what must be logged, what can an auditor reconstruct after a failure? In any regulated or customer-facing workflow this is a compliance requirement, not optional infrastructure. Reconstructing every agent action, its inputs, its decision, and its output, is something the system of record has to provide. **Not yours to build.**

**6. Recovery and ongoing ownership.** What happens when the agent gets something wrong, how is an action reversed, who keeps the system tuned a year from now? Reversibility lives in the systems that hold state. **Platform infrastructure.**

The tools and skills that supply these components already exist. The question is which ones you assemble yourself and which come from one foundation. Workflow design you build with the stage contracts in this toolkit. Evals you can run with lightweight frameworks (Promptfoo, or your own rule checks against your business logic). The other four are properties of the systems that hold your data: your CRM, ERP, accounting platform, or data warehouse supplies data access and authority, an identity provider (SSO) decides who the agent acts for, and audit-grade logging and reversibility come from the system of record. A model vendor supplies none of them.

Four of these six (data access, authority, audit trails, recovery) are properties of the systems that hold your data. You do not build them in a folder structure and you do not get them from a model. The two you genuinely own, workflow design and your business rules for evals, are exactly what the rest of this toolkit helps you build. That division is the boundary.

---

## Layer 3: The Architectural Fix

Sequence the decision. Do not start with the model. Start with the foundation, then automate the repeatable, then apply judgment, then keep a human on the decisions that matter.

**Step 1: Get the data foundation right before you add intelligence to it.** Identify where your sources of truth live. If they are fragmented across systems, stale by weeks, or reconciled by hand, the answer is not a better AI tool. It is a data foundation that is normalized, reconciled, current, and access-controlled. This is the long-lead-time item and the prerequisite for everything else.

**What "AI-ready data" actually requires, as a checklist:**
1. Clear sources of truth by data type, normalized and reconciled.
2. Workflows with approval authority, exception thresholds, and audit history encoded.
3. Access controls that reflect your actual organization and who is entitled to what.
4. Data that updates in near real-time, not weekly.
5. Every AI action traceable, reversible, and documented.

If you cannot check those five, your AI work is premature. Fix the foundation.

**Step 2: Automate the repeatable before you augment the strategic.** The highest-value AI work is high-volume, rules-based, error-prone work: reconciliation, document ingestion, record population, the figures of record your platform computes. Much of that is platform automation, not a model you build. Start by removing work that never needed judgment.

**Step 3: Apply AI where judgment lives, on top of governed data.** Drafting a customer update, synthesizing research findings, explaining a variance, triaging an inbound request. This is the slice from Constraint 06. It works only when the data underneath it is trustworthy, which is why it comes after Step 1.

**Step 4: Keep humans on the decisions that matter.** In any high-stakes workflow, AI suggests and a human approves. This is the governance posture that lets you tell a customer their data is protected and your process is auditable.

**How to evaluate the foundation (yours or a vendor's):**
- Does the AI run on your data in a governed environment, or does it ship your data somewhere?
- Is your data contractually prevented from training third-party models?
- Does it expose a headless or agent-accessible interface (an MCP server, APIs) so your own AI tools can read from it directly, with the domain meaning intact, not just screen-scraped?
- Are its AI controls independently audited (SOC 2 Type 2 or equivalent)?

A vendor that gives a model access to your screens is not the same as one that gives a model your domain logic: the business rules, record entitlement, approval authority, exception flags, and audit history. Access without meaning produces fluent guesses. Insist on meaning.

**How this changes your workspace design:** when you build a workspace with this toolkit, every stage should declare which layer owns it. Some stages read from the platform (the data foundation). Some run deterministic tools. Some apply AI. A well-designed workspace keeps its figures of record on the platform, runs AI on the language and the judgment, and never asks a model to be the source of truth for a number a customer will see.

---

## If You Build It Yourself: Three Domains You Must Own

Some organizations will decide to build anyway, often because they have a strong engineering team and treat technology as core. That can be the right call. If you make it, go in clear-eyed about what you are taking on. There are three domains you now own end to end, and they are the same three where the value of enterprise software actually lives. This is why most organizations rely on a trusted software partner for the foundation and spend their own effort on top of it.

### Build

Shipping an agent that actually closes work is mostly not model work. It is the six components from Layer 2: workflow design, data access, authority, evals, audit trails, recovery. The model is the easy 10%. The rest is the real project, and it lands on you, not on the model vendor.

The reason this is hard: those six components need a structured, permissioned, auditable data substrate to act against. Years of clean business data is exactly that substrate. Build on a fragmented stack and you are rebuilding data access and audit on every single deployment. On a real foundation, that part already exists and you build once.

### Govern

The question to sit with is not how capable the agent is. It is whether you can govern it. The risky agent is the one with fuzzy authority, not the smartest one.

Governability breaks into seven questions:
1. Where does it run?
2. Who does it act for?
3. What data can it read?
4. What can it do?
5. What can it spend or commit? (An emerging frontier. Most organizations will not grant write-and-commit authority for irreversible actions like payments, refunds, or status changes any time soon.)
6. What is logged?
7. How do you stop it?

In a compliance-sensitive business, that governability is the product. It is what your security review is actually testing. Two of the seven matter most: data and identity. Agents should inherit your existing permissions and write to an audit-grade ledger. Identity plus audit is what clears the review, and it is exactly where these projects otherwise fail. A system of record gives you both by default. A stack you assemble yourself makes you build them, prove them, and defend them.

### Maintain

The cost you feel after launch is decay. Data goes stale. Rules drift. Write actions need a way to be undone. A kill switch has to actually stop the agent, not politely ask it to. And someone has to own tuning it.

The structural advantage of building on the system of record is that the agent reads the live record, not a stale copy, and reversal and audit come for the price of the platform. Reversal design and post-launch ownership for write-access agents are the least mature part of the field today, and they are where doing it yourself gets most expensive over time. With regulators set to tighten scrutiny on AI use across industries over the next few years, that maintenance burden becomes a compliance obligation, not just an operational one.

### The Through-Line

None of this is model work, and all of it sits on the data environment. The question is not whether your AI is smart enough. It is what environment it runs in, who it answers to, and who keeps it honest. Answer those three and you have answered build versus rely.

---

## Tuning Questions

**1. For your most important AI use case, where does every number it touches come from?**
Trace each figure to its source. If any of them come from a manual export, a spreadsheet, or a system that is not the authoritative record, that is your weakest link. The model is not the risk. The data path is.

**2. Of the six implementation-layer components, which are you currently building yourself?**
Workflow design and your eval business rules are yours to own. If you find yourself building data access controls, authority enforcement, audit logging, or reversibility, stop and ask whether that should come from your platform instead. Those four take years to build correctly and failing at them is a compliance event.

**3. If you had to prove to an auditor exactly what an AI agent did six months ago, could you?**
If the answer is no, you do not have the audit and recovery layer, and no model will give it to you. That capability is a property of the system holding your data. This question alone often settles the build-versus-rely decision.

---

## Quick Reference

| If this is your situation | Start here |
|---|---|
| You are about to build your own data layer or reconciliation engine | This is context, not core. Source it from an enterprise platform. Put your effort into customers and product. |
| Your AI reads from manual exports or spreadsheets | The data path is your risk. Get an authoritative, current source of truth before scaling the AI on top. |
| You are building data access, authority, audit, or recovery yourself | These four implementation-layer components are platform infrastructure. Rely on a partner that has them. |
| You cannot reconstruct what an AI agent did months ago | You are missing the audit and recovery layer. No model provides it. Your platform must. |
| You are evaluating an agent on how capable it is | Wrong test. Evaluate whether you can govern it: where it runs, who it acts for, what it reads, what it can do, what it can spend, what is logged, how you stop it. |
| You are worried about cost after launch, not before | That is decay: stale data, drifting rules, write actions with no undo, no real kill switch, no owner. Reversal and audit come free on a system of record; on a DIY stack they are your most expensive line item. |
| You are choosing a platform | Evaluate AI-readiness, not AI marketing: governed environment, no training on your data, agent-accessible interface, independent audit. |
| You want AI value fast | Apply AI to the language and the judgment on top of governed data. Rely on the platform for the numbers and the record. |
