# Prompt: Build Source Packet

## Inputs

- Source files, links, exports, notes, or prior artifacts.
- Platform document register if available.
- `_config/artifact-boundary.md`
- `_templates/source-packet.md`

## Task

Build a source packet before any artifact work starts.

## Process

1. List every source with the required metadata.
2. Assign a source ID.
3. Classify authority as authoritative, supporting, background, or superseded.
4. Flag stale files, version families, duplicates, and missing metadata.
5. Identify conflicts without resolving them.
6. Identify requested claims that lack support.
7. Name the source of record for each major fact type when known.

## Output

Use `_templates/source-packet.md`.

## Rules

- Do not draft the artifact.
- Do not delete, move, or rename source files.
- Do not blend facts across versions.
- Do not recompute figures.
- Mark unresolved items as `[NEEDS CONFIRMATION - owner]`.
