# Stage 01: Inventory

## Purpose

List the source set before interpretation.

## Inputs

- Source files or links.
- Platform document register, if available.
- `_config/source-register-schema.md`
- `../../modules/artifact-trust-layer/_prompts/build-source-packet.md`
- `_templates/artifact-trust/source-packet.md`

## Process

1. List every source.
2. Capture title, type, date, owner, source system, and version.
3. Note exact duplicates if a deterministic check is available.
4. Identify missing metadata.
5. Do not decide authority yet.

## Output

Write to `01_inventory/output/source-inventory-[name]-[date].md`.

When Artifact Trust Layer is attached, also write to `01_inventory/output/source-packet-[name]-[date].md`.

## Done Looks Like

Every source is visible with enough metadata for authority review, and the source packet assigns source IDs for downstream claim mapping.
