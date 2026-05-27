# SKILL: Exception Handling Workspace Builder

## Description

Builds a workspace for cases that do not fit the normal workflow.

## When To Use

Use when standard automation or platform workflows cannot safely handle a case and a human needs judgment support.

Do not use as a ticketing queue, case tracker, approval state, or entitlement system.

## Diagnosis

Read shared config as directed by `SETUP.md`. Ask one question at a time.

1. What exceptions recur?
2. What normal workflow do they break?
3. Which platform owns status, owner, and audit?
4. What rule sources or policies apply?
5. Who approves non-standard action or escalation?

## Assembly

1. Copy `architectures/exception-handling/` into `workspaces/<name>/`.
2. Customize the exception brief, rule context, response options, and escalation handoff stages.
3. Populate `_config/exception-types.md`, `_config/rule-sources.md`, `_config/escalation-rules.md`, and `_config/platform-boundary.md`.
4. Record open confirmations in `_config/before-you-trust-this.md`.
5. Run one known exception through the exception brief stage.

## Verification

The workspace is ready when it helps route edge cases safely while leaving state, permissions, and audit with the platform.
