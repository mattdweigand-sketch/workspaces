# Contributing

Workspces is a plain-file toolkit. Contributions should make the operating model clearer, safer, or easier to adapt.

## Good Contributions

- Clearer architecture guidance.
- Better source-boundary or review patterns.
- Small examples that show how a workspace should behave.
- Improvements to setup instructions.
- Templates that reduce ambiguity without hiding judgment.

## What To Avoid

- Turning Workspces into a runnable SaaS product.
- Adding platform-specific integrations by default.
- Adding broad prompt libraries that are not tied to an architecture.
- Moving records, calculations, permissions, or audit trails into Workspces.
- Removing human approval from external or decision-facing work.

## Local Review

Before opening a pull request:

1. Read `AGENTS.md`.
2. Confirm the change preserves the six architecture families.
3. Run:

```bash
python3 scripts/setup_state.py doctor --json
```

Expected pre-setup warnings are acceptable, such as placeholder organization profile fields or missing live workspaces.

## Pull Requests

Keep pull requests focused. Explain:

- what changed
- which architecture or module it affects
- how the platform boundary is preserved
- how a user can verify the change
