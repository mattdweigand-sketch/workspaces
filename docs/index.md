# Workspaces Documentation

Workspaces is a file-based operating model for governed AI workflows.

It helps teams decide what belongs to AI, what belongs to a system of record, and where a human must approve the output.

## Start Here

- [README](https://github.com/mattdweigand-sketch/workspaces/blob/main/README.md)
- [Setup Engine](https://github.com/mattdweigand-sketch/workspaces/blob/main/SETUP.md)
- [Artifact Trust Layer](https://github.com/mattdweigand-sketch/workspaces/blob/main/modules/artifact-trust-layer/README.md)
- [Layer Triage](https://github.com/mattdweigand-sketch/workspaces/blob/main/constraints/06-layer-triage.md)
- [Platform Boundary](https://github.com/mattdweigand-sketch/workspaces/blob/main/constraints/09-platform-boundary.md)

## Core Concepts

| Concept | Meaning |
|---|---|
| Platform boundary | Systems of record own facts, status, calculations, permissions, delivery, and audit. |
| AI judgment layer | AI helps interpret sources, frame decisions, handle exceptions, draft responses, and capture memory. |
| Artifact trust | Serious outputs carry source packets, claim maps, review reports, and approval notes. |
| Human approval | Humans own external sends, irreversible actions, and accountable decisions. |

## Workflow Families

- `messy-input-intake`
- `evidence-review`
- `decision-prep`
- `exception-handling`
- `stakeholder-response-prep`
- `institutional-memory-loop`

## Running Setup

Open the repo in an AI coding agent and say:

```text
Read AGENTS.md, then run setup.
```

The agent will choose an architecture, ask diagnostic questions, and create a workspace under `workspaces/`.
