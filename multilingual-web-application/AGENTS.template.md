# Multilingual Web Application Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing. Preserve project-specific instructions below this template.

This repository adheres to:

- {{SPECIFICATION_URL}}

Read the specification and its complete transitive `spec.toml` inheritance
graph before changing locale handling, frontend messages, localized content,
API errors, generated documents, routing, or catalog delivery.

Treat `i18n/config.json` as the locale authority. Keep message identifiers
stable, use ICU-capable messages, and serve generated runtime catalogs through
the backend. Keep UI messages separate from localized domain content.

Run the catalog validation, application tests, and browser locale flows
documented by the repository before committing multilingual changes.
