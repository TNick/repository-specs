# Python Base

Python repositories use a `pyproject.toml` as the build and tool source of
truth and target a supported, explicitly declared Python version.

## Required

- Use four-space indentation, type hints for new code, and Google-style
  docstrings.
- Configure one formatter and linter with an 80-column human-authored limit.
- Run type checking and pytest through the documented project command.
- Keep runtime configuration in environment variables or explicit config
  files; never commit secrets.
- Keep tests under `tests/`, mirroring the package layout.
- Use an editable, lockfile-backed development workflow (`uv` is preferred).
