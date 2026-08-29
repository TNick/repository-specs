---
name: manage-design-records
description: >-
  Use whenever an agent must create, update, number, organize, or reconcile
  project design documents, gap reviews, implementation plans, or private
  design records.
---

# Manage design records

Keep a project's design history navigable for both humans and agents. Design
records explain decisions and plans; they are not disposable scratch notes.

## Location and visibility

Read the root README.md or AGENTS.md for the explicit declaration
Design records: public or Design records: private.

- Public records belong in design/.
- Private records belong in playground/design/.
- If the directory is absent and the project declares private records, use
  playground/design/; do not create a public design/ directory merely as a
  pointer.
- If visibility is not declared, stop and request that the repository owner
  choose before adding records.

## Numbering

- Use NN. title.md for a top-level design, decision, or gap review.
- Use NNNN. title.md for a plan derived from a top-level record. For example,
  0101. implementation-plan.md and 0102. migration-plan.md derive from 01.
- Use lowercase kebab-case after the numeric prefix.
- Choose the next unused number; never renumber or delete historical records.
- Every document starts with one H1 and includes metadata like:

~~~text
ID: 0101
Parent: 01
Status: Proposed
Supersedes: —
~~~

## Precedence

A later top-level record supersedes an earlier top-level record when both apply.
A child plan applies within its parent's scope. Explicit Supersedes metadata
takes precedence over inferred ordering. Retain superseded records.

When documents disagree, state the conflict and cite both IDs. Do not treat a
child plan as a global replacement for its parent.

## Document workflow

- Initial design records establish goals, constraints, alternatives, and
  acceptance criteria.
- Gap reviews record deviations discovered after implementation.
- Derived plans turn accepted gaps into bounded work.
- Completed plans link to the implementation commit or pull request.
- Keep documents concise, factual, and specific about unresolved questions.

## Safe template

Use this outline for a new record:

~~~markdown
# NN. Short title

ID: NN
Parent: —
Status: Proposed
Supersedes: —

## Context

## Decision or findings

## Acceptance criteria

## Alternatives and consequences

## Open questions

## Related records
~~~
