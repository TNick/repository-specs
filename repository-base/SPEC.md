# Repository Base

This is the foundation imported by every repository profile.

## Required

- Keep a concise root `README.md` with setup, commands, architecture, and
  troubleshooting.
- Keep durable agent rules in `AGENTS.md`; nested directories may add scoped
  rules without contradicting the root.
- Root `AGENTS.md` MUST contain a tag-pinned GitHub URL for every repository
  specification the project adopts.
- Provide one authoritative set of `init`, `test`, `lint`, and formatting
  commands through a root `Makefile` or documented equivalent.
- Keep tests separate from production code and keep experiments under an
  ignored `playground/` directory.
- Commit lockfiles, exclude secrets and generated build output, and run CI
  through the same commands developers use locally.
- Use UTF-8, final newlines, stable line endings, and a human-readable
  `CHANGELOG.md`.

## Design records

- Projects MUST keep durable design records and the plans derived from them.
  These records cover the initial design, implementation decisions, reviews,
  gaps discovered after changes, and follow-up feature plans.
- Public design records live in `design/`. A project using public records MUST
  keep that directory in the repository.
- A project MAY keep design records private in `playground/design/`. When it
  does, the root `README.md` or `AGENTS.md` MUST explicitly declare
  `Design records: private`; the absence of `design/` then indicates this
  private location. Public records MUST be declared with
  `Design records: public`.
- Design records MUST use a zero-padded numeric prefix and a lowercase
  kebab-case name, for example `01. initial-design.md` or
  `0101. implementation-plan.md`.
- Two-digit prefixes identify top-level records. Four-digit prefixes identify
  plans derived from a top-level record: `0101` and `0102` derive from `01`.
  Each derived record MUST state its `Parent` explicitly.
- Every record MUST state its `ID`, `Status`, and `Parent` when applicable.
  A record that replaces another MUST also state `Supersedes`.
- Agents MUST read the applicable design records before changing code and
  MUST create or update a gap review when implementation differs from the
  accepted design. New work MUST have a numbered plan linked to its parent.
- A later top-level record takes precedence over earlier top-level records.
  Derived plans apply only within their parent's scope. Explicit
  `Supersedes` metadata takes precedence over inferred ordering. Superseded
  records MUST be retained as historical context.

## Agent workspace

Agents store temporary notes, scripts, logs, and fixtures in a timestamped
`YYYY-MM-DD HH-MM-SS description` directory under
`playground/agentic-work/`, where description is no longer than 40
characters. They do not delete prior work. A brief README.md inside this
timestamped directory explains the goals, any hiccups, workarounds and
solutions.
