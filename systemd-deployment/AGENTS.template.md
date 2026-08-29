# Systemd Deployment Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This repository adheres to:

- {{SPECIFICATION_URL}}

Read the specification and its complete transitive `spec.toml` inheritance
graph before changing units, installers, deployment scripts, service
configuration, health checks, or rollback behavior.

Before operating on a live host, read the applicable design records and host
inventory. Inspect the current unit, drop-ins, service state, and release
identity without changing them. Record the planned rollout and rollback.

Never commit secrets or embed them in a unit. Validate units offline, run the
repository checks, deploy a staged release, verify service health, and retain
the previous known-good release until rollback is no longer needed.
