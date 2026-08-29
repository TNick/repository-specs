"""Validate the repository specification catalog."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_PATH_MARKERS = ("D:\\", "C:\\", "/Users/", "/home/")


def main() -> int:
    """Return a non-zero status when catalog invariants fail."""
    errors: list[str] = []
    specs = [
        path
        for path in ROOT.iterdir()
        if path.is_dir() and path.name != ".git" and (path / "spec.toml").exists()
    ]

    for spec in specs:
        if not SPEC_NAME.fullmatch(spec.name):
            errors.append(f"invalid spec folder: {spec.name}")
        if not (spec / "SPEC.md").exists():
            errors.append(f"missing SPEC.md: {spec.name}")
        if not (spec / "spec.toml").exists():
            errors.append(f"missing spec.toml: {spec.name}")
        else:
            metadata = tomllib.loads(
                (spec / "spec.toml").read_text(encoding="utf-8")
            )
            if metadata.get("id") != spec.name:
                errors.append(f"id does not match folder: {spec.name}")
            for imported in metadata.get("extends", []):
                imported_path = (spec / imported).resolve()
                if not (imported_path / "spec.toml").exists():
                    errors.append(f"missing import {imported}: {spec.name}")
        if (spec / "AGENTS.template.md").exists() is False:
            errors.append(f"missing AGENTS.template.md: {spec.name}")
        markdown = spec / "SPEC.md"
        if markdown.exists():
            headings: list[str] = []
            in_code_block = False
            for line in markdown.read_text(encoding="utf-8").splitlines():
                if line.startswith("```"):
                    in_code_block = not in_code_block
                elif not in_code_block and line.startswith("# "):
                    headings.append(line)
            if len(headings) != 1:
                errors.append(f"SPEC.md must have one H1: {spec.name}")
        for path in spec.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                if path.suffix.lower() in {".md", ".toml", ".yaml", ".yml", ".json"} and any(
                    marker in text for marker in LOCAL_PATH_MARKERS
                ):
                    errors.append(f"local path in {path.relative_to(ROOT)}")
                if not text.endswith("\n"):
                    errors.append(f"missing final newline: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {len(specs)} specifications")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
