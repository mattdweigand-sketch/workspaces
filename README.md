# Workspces

Workspces is a plain-file toolkit for building AI operating systems around the work platforms cannot own:

- messy input intake
- source interpretation
- decision prep
- exception handling
- stakeholder response prep
- institutional memory

Your CRM, ticketing system, project tracker, finance platform, document system, dashboard, and audit trail stay the source of truth. Workspces builds the judgment layer above them.

## Who This Is For

Workspces is for teams that want AI to help with recurring knowledge work without turning the model into a system of record.

Use it when the work depends on judgment, context, source interpretation, or human approval.

Do not use it to replace platforms that already own records, workflow state, permissions, calculations, delivery, or audit.

## Quick Start

1. Open this folder in an AI coding agent that can read files and make edits.
2. Tell the agent: `Read AGENTS.md, then run setup.`
3. Setup captures the organization profile, picks the right architecture, asks diagnostic questions, and creates a workspace under `workspaces/`.

If your agent automatically reads repo instructions, `Run setup` is enough.

A plain browser chat can still use the reference files, but it cannot run setup or create workspaces.

## The Boundary

Use this rule before building anything:

> If a platform can own the record, workflow state, entitlement, calculation, or audit trail, do not make it a toolkit architecture. If the work depends on firm judgment, source interpretation, decision framing, exception handling, stakeholder response prep, or institutional memory, it belongs here.

| Layer | Owns |
|---|---|
| Platforms | Facts, records, status, permissions, calculations, delivery, audit |
| Automation | Known rules, routing, checklists, templates, repeatable handoffs |
| Workspces | Interpretation, judgment, exceptions, decision prep, response framing, memory |
| Humans | Approval, accountability, external sends, irreversible actions |

Every workspace should answer:

1. What platform owns the record?
2. What deterministic tool owns the math or rule?
3. What routing or template can be automated?
4. What judgment does AI add?
5. What human approves the output?

## The Six Architectures

| If the team needs to... | Use |
|---|---|
| Turn messy emails, calls, notes, screenshots, forms, or files into a clean brief | `messy-input-intake` |
| Figure out what a source set supports, conflicts with, or leaves unanswered | `evidence-review` |
| Prepare options, tradeoffs, risks, assumptions, and conditions for a human decision | `decision-prep` |
| Handle a case that does not fit the normal process | `exception-handling` |
| Prepare high-context communication from verified facts | `stakeholder-response-prep` |
| Capture validated lessons so future work improves | `institutional-memory-loop` |

## Reusable Modules

Modules are optional patterns that attach to an architecture. They do not create new architecture families.

| If the workflow needs to... | Attach |
|---|---|
| Turn messy sources into trustworthy decks, workbooks, memos, diligence maps, IC materials, LP narratives, or one-off deliverables | `modules/artifact-trust-layer/` |

## Artifact Trust Layer

The Artifact Trust Layer is the Workspces reusable pattern for making polished artifacts inspectable.

It gives a workspace:

- setup checks
- source packets
- artifact specs
- claim evidence maps
- deck, workbook, and document control maps
- hostile review prompts
- Office risk taxonomy
- human approval notes
- final audit README templates

The rule is simple:

```text
Truth layer first. Artifact second.
```

Workspces can make evidence, assumptions, freshness, formula risk, and unresolved issues visible. It does not certify an artifact or replace human approval.

## Repository Map

```text
AGENTS.md        canonical project instructions for AI agents
CLAUDE.md        Claude Code compatibility wrapper
SETUP.md         setup and workspace-build engine
_shared-config/  organization profile, voice, setup progress, learnings
constraints/     principles for reliable AI work
architectures/   six architecture families and examples
modules/         reusable patterns that attach to architectures
skill-starters/  six builders, one per architecture
workspaces/      live workflows created during setup, ignored by default in public use
```

## Examples

Each architecture has a small worked example under `architectures/_examples/`:

- `vendor-request-intake`
- `contract-renewal-evidence-review`
- `pricing-exception-decision-prep`
- `customer-escalation-exception`
- `service-issue-stakeholder-response`
- `lost-renewal-memory-loop`

The Artifact Trust Layer also includes examples for diligence maps, IC materials, LP narratives, and workbook review.

## Setup Model

Setup is intentionally file-based.

It does not require a server, database, SaaS account, or package install. The only requirement is an AI coding agent that can read and write files in this repository.

Setup asks one question at a time, writes the answers into plain markdown files, and builds a workspace from the selected architecture.

## Data And Security

Workspces does not upload data on its own. It is a folder of plain files.

Your AI tool may send the files it reads to its model provider. Follow your organization's data policy, and use an enterprise or zero-retention plan when your data requires it.

Workspces should not write to external systems or send stakeholder-facing output without human review.

## Useful References

Start with:

- `constraints/06-layer-triage.md`
- `constraints/09-platform-boundary.md`
- `constraints/10-source-provenance.md`
- `modules/artifact-trust-layer/README.md`

Those explain what belongs to AI, what belongs to platforms or deterministic automation, and how to keep source-backed artifacts inspectable.

## License

Workspces is released under the [MIT License](LICENSE).

Built by Matt Weigand.
