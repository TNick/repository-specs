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

## Agent workspace

Agents store temporary notes, scripts, logs, and fixtures in a timestamped
`YYYY-MM-DD HH-MM-SS description` directory under
`playground/agentic-work/`, where description is no longer than 40
characters. They do not delete prior work. A brief README.md inside this
timestamped directory explains the goals, any hiccups, workarounds and
solutions.
