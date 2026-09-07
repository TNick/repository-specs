"""Fail when a checked source-code file exceeds 400 lines."""

from __future__ import annotations

import sys
from pathlib import Path

from _common import REPO_ROOT, iter_source_files

MAX_LINES = 400

# Documentation, configuration, and text files are not source-code targets.
SUFFIXES = {".css", ".html", ".js", ".ps1", ".py", ".sh", ".ts"}


def _is_test_file(path: Path) -> bool:
    """Return whether a source path belongs to a test file or directory."""
    relative = path.relative_to(REPO_ROOT)
    if any(part in {"test", "tests", "__tests__"} for part in relative.parts):
        return True
    return path.stem.startswith("test_") or path.stem.endswith("_test")


def main() -> int:
    """Return non-zero when a checked source file is too long."""
    offenders: list[tuple[str, int]] = []
    for path in iter_source_files(SUFFIXES):
        if _is_test_file(path):
            continue
        count = sum(1 for _ in path.open("rb"))
        if count > MAX_LINES:
            rel = path.relative_to(REPO_ROOT).as_posix()
            offenders.append((rel, count))

    for name, count in sorted(offenders):
        sys.stderr.write(f"{name}: {count} lines (limit {MAX_LINES})\n")
    if offenders:
        sys.stderr.write(
            "Split oversized modules into a package re-exporting the API.\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
