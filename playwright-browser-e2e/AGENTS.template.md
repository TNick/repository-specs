# Agent Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This repository adheres to:

- {{SPECIFICATION_URL}}

Read the specification and its complete transitive `spec.toml` inheritance
graph before changing Playwright specs, E2E helpers, or lab stack wiring.

When implementing or fixing user-visible frontend behavior, add or update a
Playwright regression spec in the same change set. Run tests against the lab
or fixture database only; never point default E2E at a live external
database.

Keep temporary work under `playground/agentic-work/`. Read public design
records from `design/` unless the repository declares
`Design records: private`.
