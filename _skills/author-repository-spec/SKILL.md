---
name: author-repository-spec
description: >-
  Use whenever an agent maintains this repository-specs catalog, adds or
  revises a foundation, capability, profile, inheritance declaration, agent
  template, or catalog validation rule.
---

# Author a repository specification

Maintain this catalog as a composable, release-pinned product. Changes must be
clear to consuming agents and must not duplicate inherited requirements.

## Workflow

1. Read the root README.md, AGENTS.md, and the relevant existing
   specifications before editing.
2. Decide whether the change belongs in a foundation, language base, capability,
   or profile. Prefer extending an existing specification over copying rules.
3. Update spec.toml first when changing inheritance. extends contains direct
   relative parents; the effective graph is transitive and must remain acyclic.
4. Keep SPEC.md focused on requirements introduced by that specification.
   Avoid redundant direct parents when an ancestor is already reached through
   another parent, while preserving explicit parents that communicate a
   meaningful independent capability.
5. Keep AGENTS.template.md as a visibly templated, manually rendered
   instruction file with {{SPECIFICATION_URL}}; do not add generators.
6. Add or update examples, enforcement guidance, and documentation links.
7. Run python _scripts/validate_catalog.py, inspect the staged diff, and
   update the changelog when the catalog's public behavior changes.
8. Commit one logical change and publish a new release tag when consumers need
   the updated specification.

## Quality checks

- Folder names and specification IDs use lowercase kebab-case.
- Every specification has spec.toml, SPEC.md, and AGENTS.template.md.
- Every extends path resolves to a specification folder.
- No inheritance cycle exists.
- Markdown has one H1, final newlines, and no private paths or secrets.
- Templates contain a placeholder and instruct agents to follow inherited
  specifications.
