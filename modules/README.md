# Modules

Modules are reusable patterns that attach to architecture families.

Use constraints for principles. Use modules for repeatable artifact checks. Use architectures for complete workflows.

## Available Modules

| Module | Use when |
|---|---|
| `artifact-trust-layer` | A workflow produces or reviews decks, workbooks, memos, reports, IC materials, LP narratives, board materials, diligence artifacts, or one-off deliverables. |

## How To Use

Builders should load only the module needed by the selected architecture. Reference module files in place by default. Copy templates into a workspace only when they need local fields, naming, owners, or review rules.

When the repo is finalized, these paths move with the toolkit to `_kit/modules/`.
