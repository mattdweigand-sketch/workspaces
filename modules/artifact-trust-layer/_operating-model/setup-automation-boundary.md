# Setup Automation Boundary

The Artifact Trust Layer is currently attached through setup and builder instructions, not through a file-copying script.

## Current State

- `SETUP.md` tells the agent when to attach the module.
- Builders name architecture-specific copy/reference rules.
- `architecture-attachment-guide.md` gives exact files and output locations.
- `scripts/setup_state.py` tracks setup state only.

## Do Not Automate Yet

Do not add module copying to `scripts/setup_state.py`. That script is a state helper, not a workspace materializer.

## Automate Later If

Add programmatic attachment only if Workspaces gains a command that creates or updates workspace files from architecture and module selections.

That future command should:

- Copy the selected architecture.
- Reference module files in place by default.
- Copy selected templates into `_templates/artifact-trust/` only when customization is requested.
- Add output locations to relevant stage contracts.
- Add unresolved confirmations to `_config/before-you-trust-this.md`.
- Avoid changing the selected architecture family.
