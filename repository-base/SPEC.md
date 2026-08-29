# Repository Base

This is the foundation imported by every repository profile.

## Required

- Keep a concise root `README.md` with setup, commands, architecture, and
  troubleshooting.
- Keep durable agent rules in `AGENTS.md`; nested directories may add scoped
  rules without contradicting the root.
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
directory under `playground/agentic-work/`. They do not delete prior work.
