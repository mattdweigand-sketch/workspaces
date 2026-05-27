# Security Policy

Workspces is a plain-file toolkit. It has no hosted service, database, authentication layer, or telemetry.

## Supported Version

Security updates apply to the current `main` branch.

## Data Handling

Workspces does not upload data by itself. The AI agent or model provider you use may receive any files the agent reads.

Before using Workspces with sensitive data:

- follow your organization's data policy
- use approved AI tooling
- prefer enterprise or zero-retention model settings when required
- keep systems of record in their source platforms
- require human review before external use

## Reporting A Vulnerability

Open a private security advisory on GitHub if available, or contact the maintainer directly.

Do not open a public issue with secrets, customer data, credentials, proprietary source files, or exploit details.

## Scope

Security reports are most useful when they involve:

- accidental secret exposure in templates or examples
- unsafe default instructions
- guidance that could cause external writes without approval
- guidance that could make AI replace a system of record, calculation owner, or human approver
