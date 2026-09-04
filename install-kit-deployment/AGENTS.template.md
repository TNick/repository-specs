# Agent Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This repository adheres to:

- {{SPECIFICATION_URL}}

Read the specification and its complete transitive `spec.toml` inheritance
graph before changing install kits, systemd units, forge pipelines, release
artifacts, or host bootstrap scripts.

Never commit secrets. Keep forge variable versus secret classification
accurate. Treat Compose lab workflows and production install-kit rollouts as
separate operator paths.

Before touching a live host, inspect the current unit, release identity, and
rollback path without changing them. Validate units offline when possible.

Keep temporary work under `playground/agentic-work/`. Read public design
records from `design/` unless the repository declares
`Design records: private`.
