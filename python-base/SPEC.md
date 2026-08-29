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
- Human-authored Python source, tests, configuration, and documentation MUST
  be no longer than 400 lines. Generated files, lockfiles, and vendored files
  are exempt. Split an oversized module into a package while re-exporting its
  public API.
- Code MUST be divided into short logical blocks. A block should start after
  a blank line and have a preceding comment when its purpose is not obvious;
  avoid trailing inline comments.

## Preferred example

```python
"""Validate a project name against repository naming rules."""

from typing import Final


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
        return bool(name) and len(name) <= self.max_length
```

Avoid undocumented private helpers, docstrings whose summary starts below
the opening quotes, untyped arguments, and a monolithic module that exceeds
400 lines. Split such a module into focused files and re-export its API.
