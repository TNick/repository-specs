---
name: upgrade-repository-spec
description: >-
  Use whenever an agent must upgrade a consuming repository to a newer
  repository-specs release, compare specification tags, migrate AGENTS.md, or
  assess breaking documentation and tooling requirements.
---

# Upgrade a repository specification

Treat a specification upgrade as a migration, not as a URL replacement. Preserve
the old context while making the new requirements explicit.

## Workflow

1. Read the consuming repository's AGENTS.md, README.md, declared design
   records, and current tag-pinned specification URL.
2. Resolve the current and target spec.toml graphs. Compare every direct and
   transitive SPEC.md, including additions, removals, changed requirements, and
   inheritance changes.
3. Write a numbered migration or gap-review document before changing project
   files. Link it to the design record that established the current adoption.
4. Create a derived implementation plan with explicit acceptance conditions.
5. Implement the plan in small slices. Update the root AGENTS.md to the new
   tag only when the project is ready to follow the new requirements.
6. Run the project's documented checks and verify that the final URL is
   tag-pinned and points to the intended profile.
7. Mark the migration plan complete, record deferred gaps, and retain the old
   design history.

## Decision rules

- Do not assume a patch release is behavior-free; compare the effective graphs.
- Do not remove project-specific instructions unless they conflict with the
  target specification and the reason is recorded.
- When the target profile changes, explicitly state why the old profile no
  longer fits.
- Treat inherited requirements as part of the upgrade even when the selected
  profile's Markdown does not repeat them.
