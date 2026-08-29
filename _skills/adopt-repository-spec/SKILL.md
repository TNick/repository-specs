---
name: adopt-repository-spec
description: >-
  Use whenever an agent must choose, adopt, or apply repository-specs to a new
  or existing project, including requests to standardize a repository, add
  AGENTS.md, select a profile, or make a project comply.
---

# Adopt a repository specification

Use this skill to establish a consuming repository's specification baseline.
Adoption is configuration and documentation work; do not change application
code unless the user also requests implementation.

## Workflow

1. Read the consuming repository's root README.md and AGENTS.md, then inspect
   its top-level structure and package manifests.
2. If a tag-pinned specification URL already exists, use it. Otherwise select
   the narrowest profile that describes the repository. Use multiple profiles
   only when each describes a distinct concern.
3. Open the selected released SPEC.md and its spec.toml. Follow every
   relative extends entry recursively. Treat the union of that graph as the
   effective specification; do not infer inheritance from folder names or
   Markdown links.
4. Copy the selected AGENTS.template.md to the consuming repository's root
   AGENTS.md. Replace {{SPECIFICATION_URL}} with the exact tag-pinned URL.
   Preserve useful project-specific instructions and add them only after the
   shared instructions.
5. Decide where design records live. Declare exactly one of
   Design records: public or Design records: private in the root README or
   AGENTS file. Use design/ for public records and playground/design/ for
   private records.
6. Compare the effective requirements with the repository. Record missing or
   ambiguous requirements in a numbered gap document; do not silently weaken a
   specification to fit the current code.
7. Run the repository's documented validation commands and report the selected
   profiles, inherited specifications, files changed, and remaining gaps.

## Selection guidance

Prefer a profile over assembling low-level capabilities manually. Use a
foundation or language base only when no profile fits. When two profiles
overlap, keep the narrower profile's requirements and explain any conflict in
the gap document.

## Completion checklist

- The selected URL is tag-pinned and appears in root AGENTS.md.
- The complete transitive extends graph was read.
- Design-record visibility is explicitly declared.
- Existing project instructions were preserved unless they conflict.
- Validation commands and unresolved gaps are reported.

Do not create a second agent-instruction file at the root, commit secrets, or
replace project decisions without recording the reason.
