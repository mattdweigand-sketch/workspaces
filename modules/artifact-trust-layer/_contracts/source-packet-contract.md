# Source Packet Contract

Use this contract when a workspace needs a stricter source packet than the markdown template alone provides.

## Required Top-Level Fields

| Field | Required | Notes |
|---|---|---|
| `packet_id` | yes | Stable packet identifier. |
| `created_at` | yes | Date the packet was created. |
| `artifact_goal` | yes | What the source packet supports. |
| `sources` | yes | Non-empty list of source records. |
| `assumptions` | yes | Can be empty, but must be explicit. |
| `conflicts` | yes | Can be empty, but must be explicit. |
| `open_questions` | yes | Can be empty, but must be explicit. |

## Source Record

| Field | Required | Allowed Or Expected Values |
|---|---|---|
| `source_id` | yes | `S01`, `S02`, `S03`. |
| `title` | yes | Human-readable source name. |
| `date` | yes | Source date or `unknown`. |
| `owner` | yes | Source owner or review owner. |
| `type` | yes | File, export, transcript, deck, workbook, memo, note, system record. |
| `status` | yes | `current`, `superseded`, `background`, `raw_data`, `estimate`, `transcript`, `draft`, `unknown`. |
| `authority` | yes | `primary`, `secondary`, `background`, `unknown`. |
| `currentness` | yes | `current`, `stale`, `unknown`. |
| `notes` | no | Metadata gaps, scope, or caveats. |

## Assumption Record

| Field | Required | Allowed Or Expected Values |
|---|---|---|
| `assumption_id` | yes | Stable assumption identifier. |
| `statement` | yes | The assumption text. |
| `owner` | yes | Human owner. |
| `status` | yes | `open`, `approved`, `rejected`, `placeholder`. |
| `confidence` | yes | `high`, `medium`, `low`, `contested`. |
| `source_ids` | no | Source IDs if the assumption is source-linked. |

## Conflict Record

| Field | Required | Allowed Or Expected Values |
|---|---|---|
| `conflict_id` | yes | Stable conflict identifier. |
| `description` | yes | What conflicts and why it matters. |
| `source_ids` | yes | Source IDs involved. |
| `status` | yes | `open`, `resolved`, `accepted_unresolved`. |
| `decision_required` | yes | `true` or `false`. |
| `resolution` | no | Required when status is `resolved`. |

## Open Question Record

| Field | Required | Notes |
|---|---|---|
| `question` | yes | The missing context. |
| `owner` | yes | Person or role that can answer. |
| `needed_for_artifact` | yes | Whether the artifact is blocked. |

## Validation Rules

- Source IDs must be unique.
- Decision-critical conflicts stop artifact creation until resolved or accepted unresolved.
- High-confidence assumptions require approval.
- Source IDs referenced by assumptions or conflicts must exist in the source list.
