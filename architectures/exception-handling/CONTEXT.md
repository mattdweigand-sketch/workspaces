# Architecture: Exception Handling

## Overview

Use this when a case falls outside the standard process and needs judgment.

Do not use this as the queue, ticketing system, status tracker, entitlement system, or escalation log.

## Stage Map

| Stage | Purpose | Output |
|---|---|---|
| `01_exception_brief` | Describe what makes the case non-standard. | Exception brief |
| `02_rule_context` | Identify policy, precedent, and constraints. | Rule context |
| `03_response_options` | Propose safe paths with tradeoffs. | Options brief |
| `04_escalation_handoff` | Route to owner or platform workflow. | Escalation handoff |

## Platform Boundary

| Layer | Owner |
|---|---|
| Queue, state, owner, permissions, audit | Platform |
| Standard routing and policy checks | Rules / automation |
| Exception reasoning and option framing | AI |
| Non-standard action | Human |
