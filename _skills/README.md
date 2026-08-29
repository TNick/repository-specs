# Consumer Agent Skills

This directory is reserved for reusable Agent Skills that help agents apply
the repository specifications in other projects. A skill belongs here only
when its workflow is specific to this catalog and useful across multiple
consuming repositories.

Each implemented skill should live in `_skills/<skill-name>/SKILL.md`. Skills
may include focused references, assets, deterministic scripts, and evaluation
cases when those resources materially improve reliability.

## Implemented skills

### [adopt-repository-spec](adopt-repository-spec/SKILL.md)

Select the appropriate profile or profiles for a new or existing repository,
resolve the complete transitive `extends` graph, create the root `AGENTS.md`
from the relevant template, and record whether design documents are public or
private.

### [audit-repository-spec](audit-repository-spec/SKILL.md)

Read a repository's tag-pinned specification references, resolve inherited
requirements, inspect the repository, and produce an evidence-backed compliance
and gap report. Auditing should not modify the consuming repository unless the
user separately requests remediation.

### [implement-spec-gaps](implement-spec-gaps/SKILL.md)

Turn an accepted compliance or gap report into bounded repository changes.
Preserve existing project decisions, apply requirements in dependency order,
run the project's documented checks, and record remaining gaps.

### [manage-design-records](manage-design-records/SKILL.md)

Create and maintain numbered design, gap-review, and derived-plan documents.
Apply the catalog's public/private location rules, parent relationships,
statuses, and precedence rules consistently.

### [upgrade-repository-spec](upgrade-repository-spec/SKILL.md)

Move a consuming repository from one released specification tag to another.
Compare the effective requirement graphs, explain the impact, update pinned
references, and create a migration plan before changing the project.

### [author-repository-spec](author-repository-spec/SKILL.md)

Maintain this catalog itself: choose between a foundation, capability, and
profile; minimize duplicated requirements; edit `spec.toml` inheritance; and
validate the catalog graph and documentation.

## Recommended use order

Start with `audit-repository-spec`, `adopt-repository-spec`, and
`manage-design-records`. They establish discovery, inheritance resolution, and
the documentation workflow used by the remaining skills. Add evaluation cases
before making further changes to these skills.
