# Agent Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This file is the repository's root `AGENTS.md`.

Before making changes:

1. Read this file completely.
2. Read the linked repository specification and its complete transitive
   `spec.toml` inheritance graph.
3. Locate and read the project's design records.
4. Keep temporary work under `playground/agentic-work/`.

Design records: public

Public design records are in `design/`. If the root `README.md` or
`AGENTS.md` declares `Design records: private`, read them from
`playground/design/` instead. Read the applicable numbered design and plan
records before changing code. Update the gap review and derived plan when an
implementation changes or extends the design.

## Repository specification

This repository adheres to:

- {{SPECIFICATION_URL}}

This profile is an alternative to `python-typescript-app` for QWC/webpack
map products. Do not also pin `python-typescript-app` as a primary profile.

The consuming repository owns implementation details. The referenced
specification supplies structure and quality requirements. Project-specific
rules below may be stricter; they must not silently weaken the
specification without a design-record deviation.
