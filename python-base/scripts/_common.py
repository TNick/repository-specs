"""Shared helpers for repository source checks."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Directories whose contents are generated, vendored, or transient.
EXCLUDED_DIRS = {
    ".git",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    ".venv-lnx",
    ".venv-win",
    ".worktrees",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "htmlcov",
    "node_modules",
    "playground",
}

# Individual files exempt from source checks.
EXCLUDED_FILES = {"uv.lock"}


def iter_source_files(suffixes: set[str]) -> Iterator[Path]:
    """Yield repository files with one of ``suffixes``."""
    for path in REPO_ROOT.rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        try:
            is_file = path.is_file()
        except OSError:
            continue
        if not is_file or path.suffix not in suffixes:
            continue
        if path.name in EXCLUDED_FILES:
            continue
        yield path
