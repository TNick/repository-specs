# Agent Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This repository adheres to:

- {{SPECIFICATION_URL}}

Read the specification and its complete transitive `spec.toml` inheritance
graph before changing persistence, ORM usage, or database bootstrap.

Do not duplicate canonical ORM models inside the application. Evolve schema
only through the external schema package and its migrations. Keep connection
settings in environment configuration and keep session lifetimes explicit.

Keep temporary work under `playground/agentic-work/`. Read public design
records from `design/` unless the repository declares
`Design records: private`.
