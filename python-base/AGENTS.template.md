# Agent Instructions

> Template: copy this file to the consuming repository's root `AGENTS.md`.
> Replace `{{SPECIFICATION_URL}}` with the tag-pinned specification URL before
> committing.

This file is the repository's root `AGENTS.md`.

Before making changes:

1. Read this file completely.
2. Read the linked repository specification.
3. Locate and read the project's design records.
4. Keep temporary work under `playground/agentic-work/`.

## Project environments and tooling

Never create or use a shared `.venv`. Use `.venv-win` on Windows and
`.venv-lnx` on Linux/WSL/macOS. The project's UV or Make commands MUST create
the selected environment when it is missing; agents MUST not require manual
activation before running checks.

Copy the Python tooling templates from the selected specification into the
repository's own `scripts/` directory. Use
`scripts/run_in_project_env.py` for pre-commit and direct tool invocations so
Ruff, Ty, and repository check scripts run from the selected environment.
Keep the copied scripts local to the consuming repository; do not add the
specification repository as a dependency.

## Test scope

Agents are prohibited from running the full test suite while developing or
fixing a bug. Determine which test files cover the changed behavior and run
only those files, for example:

```text
uv run pytest tests/unit/package/test_feature.py
```

The Forgejo Actions workflow runs the full suite after changes are pushed;
that CI run is the full-suite verification boundary.

Whenever you create a source module containing executable behavior, create a
corresponding test file in the mirrored test tree. Empty modules,
import-only modules, and modules containing only constants do not require a
test file.

Public design records are in `design/`. If the root `README.md` or
`AGENTS.md` declares `Design records: private`, read them from
`playground/design/` instead. Read the applicable numbered design and plan
records before changing code. Update the gap review and derived plan when an
implementation changes or extends the design.

## Repository specification

This repository adheres to:

- {{SPECIFICATION_URL}}

The consuming repository owns implementation details. The referenced
specification supplies structure and quality requirements.
