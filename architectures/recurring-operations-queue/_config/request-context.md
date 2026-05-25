# Request Context

> **CONFIRM BEFORE LIVE USE.** This roster gates authentication and routing: who is authorized on
> each account and what each stakeholder is sensitive to. An invented or stale entry means answering
> the wrong person or missing a sensitivity. The onboarding agent must not fabricate contacts or
> entitlements. Until the team populates it from the system of record, every entry stays flagged
> `[NEEDS CONFIRMATION — team lead]`. See Constraint 08; logged in `_config/before-you-trust-this.md`.

<!--
ANNOTATION: The recurring stakeholder record this workspace needs to identify a
requester, route correctly, and answer with the right history and sensitivities
in mind. This is L3 reference, updated as stakeholders and entities evolve.

This is NOT the system of record. The platform that owns the data holds the
authoritative stakeholder data, figures, and entitlements. This file holds the
working context the model needs to handle a request well: who is who, what they
care about, what has come up before. Keep figures OUT of this file — those come
from the platform at resolve time.
-->

## Stakeholder Entities and Contacts
[Per stakeholder: legal entity name(s), the authorized contacts and their roles,
preferred channel, and which account(s) they hold. Used at intake to identify
the requester and confirm authority.]

## Standing Sensitivities
[Anything that should shape how a request from this stakeholder is handled. Examples:
a stakeholder in a dispute, one who escalates quickly, one with special terms that
affect what they can be told, a relationship a principal manages personally.]

## Request History
[Recurring or notable prior requests per stakeholder, so a follow-up is handled
with context rather than from scratch. Grows over time.]

## Routing Map
[Who owns what when a request must be referred: the team principal, compliance
contact, counsel, the business-development lead. Used by intake and resolve to route
escalations to a named person, not a vague "someone."]
