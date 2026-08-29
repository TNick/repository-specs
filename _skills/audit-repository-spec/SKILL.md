---
name: audit-repository-spec
description: >-
  Use whenever an agent must audit a repository against repository-specs, find
  compliance gaps, review adherence, assess inherited requirements, or produce
  a design gap report before implementation.
---

# Audit a repository specification

Produce an evidence-backed compliance report for a consuming repository. An
audit diagnoses; it does not remediate code unless the user explicitly asks for
implementation.

## Workflow

1. Read the root AGENTS.md, README.md, and any declared design records.
2. Extract every tag-pinned repository specification URL from AGENTS.md. If
   none exists, report adoption as the first gap and ask which profile applies.
3. For each selected specification, read spec.toml, resolve its relative
   extends entries recursively, and deduplicate shared ancestors. Read every
   effective SPEC.md; inheritance is defined by TOML, not by Markdown links.
4. Inspect the repository structure, manifests, configuration, tests, CI, and
   documented commands. Use the specification's own required terms as the
   audit checklist.
5. Classify each requirement as pass, partial, missing, or not-applicable.
   Cite a repository path and line or command as evidence.
6. Write a numbered gap-review document in the declared design location. Use
   design/ for public records or playground/design/ for private records.
   If the project has no numbering convention yet, create the next top-level
   NN. gap-review.md record.
7. End with a prioritized remediation list and explicit questions. Do not edit
   source files while producing the audit.

## Gap-review structure

Use these sections:

- Scope and effective specification graph
- Evidence and requirement matrix
- Gaps, risks, and ambiguities
- Recommended priority
- Proposed follow-up plans
- Open questions

Every gap must describe the desired requirement, current evidence, impact, and
a testable acceptance condition. Separate factual findings from suggestions.

## Completion checklist

- All transitive specifications were read.
- Findings distinguish inherited requirements from profile-specific ones.
- Every non-pass finding has evidence and an acceptance condition.
- The report location and public/private status are clear.
- No source or configuration files were changed as a side effect.
