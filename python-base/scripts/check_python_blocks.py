"""Enforce and repair blank-line spacing for Python block comments."""

from __future__ import annotations

import ast
import sys
from collections.abc import Iterator
from pathlib import Path

from _common import REPO_ROOT, iter_source_files

_FunctionNode = ast.FunctionDef | ast.AsyncFunctionDef
MAX_SHORT_FN = 5


def _iter_functions(tree: ast.Module) -> Iterator[_FunctionNode]:
    """Yield every function and method definition in the module."""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            yield node


def _is_first_body_comment(line: int, lines: list[str]) -> bool:
    """Return whether a comment directly follows a docstring or definition."""
    if line < 2:
        return True
    previous = lines[line - 2].strip()
    return previous.endswith(('"""', "'''")) or previous.startswith(
        ("def ", "async def ")
    )


def _violation_lines(path: Path) -> list[int]:
    """Return 1-based comment lines requiring a preceding blank line."""
    try:
        source = path.read_text(encoding="utf-8")
    except OSError:
        return []
    lines = source.splitlines()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    violations: list[int] = []
    for function in _iter_functions(tree):
        if not function.body or function.end_lineno is None:
            continue
        if function.end_lineno - function.lineno + 1 <= MAX_SHORT_FN:
            continue
        start = function.body[0].lineno
        end = max(
            statement.end_lineno or statement.lineno for statement in function.body
        )
        for line in range(start, end + 1):
            if not lines[line - 1].lstrip().startswith("#"):
                continue
            if _is_first_body_comment(line, lines):
                continue
            previous = lines[line - 2].strip() if line >= 2 else ""
            if previous == "" or previous.startswith("#"):
                continue
            if previous.endswith((":", ",", "(", "[", "{", "\\")):
                continue
            violations.append(line)
    return violations


def check_file(path: Path) -> list[str]:
    """Return comment-spacing violations for one Python file."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    relative = path.relative_to(REPO_ROOT).as_posix()
    return [
        f"{relative}:{line}: comment not preceded by a blank line: "
        f"{lines[line - 1].strip()!r}"
        for line in _violation_lines(path)
    ]


def fix_file(path: Path) -> int:
    """Insert blank lines before fixable comments in one Python file."""
    try:
        source = path.read_text(encoding="utf-8")
    except OSError:
        return 0
    violations = _violation_lines(path)
    if not violations:
        return 0
    newline = "\r\n" if "\r\n" in source else "\n"
    lines = source.splitlines(keepends=True)
    for line in reversed(violations):
        lines.insert(line - 1, newline)
    path.write_text("".join(lines), encoding="utf-8", newline="")
    return len(violations)


def main() -> int:
    """Check comment spacing, optionally inserting missing blank lines."""
    fix = "--fix" in sys.argv[1:]
    issues: list[str] = []
    fixed = 0
    for path in iter_source_files({".py"}):
        if fix:
            fixed += fix_file(path)
        issues.extend(check_file(path))
    if fixed:
        sys.stderr.write(f"fixed {fixed} python block-comment violation(s)\n")
    for issue in issues:
        sys.stderr.write(f"{issue}\n")
    if issues:
        sys.stderr.write(f"{len(issues)} python block-comment spacing violation(s)\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
