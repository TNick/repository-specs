# Python Base

Python repositories use a `pyproject.toml` as the build and tool source of
truth and target a supported, explicitly declared Python version.

## Required

- Use four-space indentation, type hints for new code, and Google-style
  docstrings.
- Configure one formatter and linter with an 80-column source-code limit.
- Run type checking and pytest through the documented project command.
- Keep runtime configuration in environment variables or explicit config
  files; never commit secrets.
- Keep tests under `tests/`, mirroring the package layout.
- Use an editable, lockfile-backed development workflow (`uv` is preferred).
- Use platform-specific UV environments: `.venv-win` on Windows and
  `.venv-lnx` on Linux/WSL/macOS. Never create or use a shared `.venv`.

## Code style

- Every module, class, function, and method MUST have a Google-style
  docstring, including private and nested functions.
- A docstring's first summary line MUST be on the same line as its opening
  triple quotes. Arguments MUST have type annotations; docstrings document
  meaning and behavior rather than repeating type syntax.
- Class docstrings MUST document every attribute, including private
  attributes, under an `Attributes` section. Attributes MUST have explicit
  types, with public attributes before private attributes.
- Properties MUST be documented in the class docstring. Functions MUST
  document each argument and the return value when it is meaningful.
- Type-only imports MUST be guarded by `if TYPE_CHECKING:`. Use `cast()` for
  narrowing instead of `getattr()` escape hatches.
- Prefer `attrs` `@define` and `field(...)` for data objects over the standard
  library `dataclass`.
- Source-code files MUST be no longer than 400 lines. Test
  files, documentation, configuration, generated files, lockfiles, and
  vendored files are exempt. Split an oversized source module into a package
  while re-exporting its public API.
- Code MUST be divided into short logical blocks. A block should start after
  a blank line, then a one- or two-line comment that briefly explains its
  purpose, followed by one to five lines of code. Avoid trailing inline
  comments.

## Preferred example

```python
"""Validate a project name against repository naming rules."""

from __future__ import annotations

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from .models import Project


MAX_NAME_LENGTH: Final = 80


class NameValidator:
    """Validate names used by a project.

    Attributes:
        max_length: Maximum permitted name length.
        _allow_unicode: Whether non-ASCII letters are accepted.
    """

    max_length: int
    _allow_unicode: bool

    def validate(self, name: str) -> bool:
        """Return whether ``name`` satisfies the validator's rules.

        Args:
            name: Candidate project name.

        Returns:
            True when the name is valid.
        """

        # Reject empty names before applying the length rule.
        if not name:
            return False

        # Enforce the configured maximum length.
        return len(name) <= self.max_length

    def project_name(self, project: Project) -> str:
        """Return the display name from a typed project model.

        Args:
            project: Project model imported only during type checking.

        Returns:
            The project's display name.
        """

        # Read the value through the typed model interface.
        return project.name
```

Avoid undocumented private helpers, docstrings whose summary starts below
the opening quotes, untyped arguments, and a monolithic module that exceeds
400 lines. Split such a module into focused files and re-export its API.

The block rule applies to cohesive operations, not every individual line.
Imports, decorators, adjacent declarations, continuation clauses such as
`else` and `finally`, closing delimiters, and generated code are exempt when a
comment would add no meaning. A block longer than five lines should be split
into smaller operations or have a documented reason to remain together.

## Enforcement

- Ruff MUST enable its `D` docstring rules with the Google convention,
  annotation rules, and an 80-character limit. `ruff format --check` MUST run
  in the normal lint command.
- The repository MUST provide a `delint` command that runs `ruff check --fix
  --unsafe-fixes`, `ruff format`, and the Python block-comment fixer.
- A repository MUST run a checked-in script that enforces the 400-line limit
  for source-code files, excluding test files, and the
  blank-line/comment/block-size convention. Formatter output alone is not
  sufficient to enforce this semantic layout rule.
- Pre-commit MUST run project tools through the selected platform environment;
  hooks MUST NOT depend on an activated shell environment or bare system
  `python`. The block-comment hook MUST use its `--fix` mode.
- CI and pre-commit MUST invoke the same checks as the developer lint command.

## Copyable tooling

The canonical, dependency-free script templates are included in this
specification under `scripts/`:

- `scripts/_common.py` — source-tree walking and generated-tree exclusions.
- `scripts/check_file_lengths.py` — source-only 400-line enforcement.
- `scripts/check_python_blocks.py` — block-comment validation and `--fix`.
- `scripts/run_in_project_env.py` — platform-specific `uv run` wrapper.
- `templates/pre-commit-config.yaml` — pre-commit hook wiring.
- `templates/Makefile` — platform environment, lint, delint, test, and check
  targets.

Consuming repositories SHOULD copy these files into their own `scripts/` and
customize exclusions, source suffixes, and package paths as needed. They MUST
not add the specification repository as a runtime or development dependency.
The copied scripts are repository-owned and may evolve independently while
retaining the requirements above.
