---
name: implement-spec-gaps
description: >-
  Use whenever an agent is asked to remediate repository-spec gaps, bring a
  project into compliance, implement an accepted design plan, or make changes
  derived from an audit report.
---

# Implement specification gaps

Implement an accepted, bounded plan derived from a repository-spec audit. Keep
the design record and the code synchronized so future agents can understand
why each change exists.

## Before editing

1. Read root AGENTS.md, the pinned specification URL, and the complete
   transitive extends graph from spec.toml.
2. Read the relevant accepted gap review and derived plan. A plan must have an
   explicit ID, Parent, and Status; if none exists, use
   manage-design-records to create one before coding.
3. Identify the acceptance conditions, affected packages, required commands,
   and files that are intentionally out of scope.
4. Check the working tree and preserve unrelated changes.

## Implementation loop

For each bounded slice:

1. Make the smallest coherent change that satisfies one or more acceptance
   conditions.
2. Update or add tests at the same time. Follow the consuming repository's
   documented test command.
3. Run focused checks, then the full lint, typecheck, build, and test commands
   required by the effective specifications.
4. Record discoveries or deviations in the gap review. If the design changes,
   create a new numbered plan or revise the current plan with an explicit
   status rather than silently overriding it.
5. Keep commits atomic and describe the reason for the change.

Do not rewrite unrelated code, suppress a check without documenting why, or
declare a requirement complete without evidence.

## Completion report

Report:

- The plan and acceptance conditions addressed
- Files changed and tests/checks run
- Remaining gaps or intentionally deferred work
- Design documents updated, including their IDs and statuses
- Any new project-specific instruction added to AGENTS.md
