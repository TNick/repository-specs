"""Validate the repository specification catalog."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCAL_PATH_MARKERS = ("D:\\", "C:\\", "/Users/", "/home/")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def main() -> int:
    """Return a non-zero status when catalog invariants fail."""
    errors: list[str] = []
    specs = [
        path
        for path in ROOT.iterdir()
        if (
            path.is_dir()
            and path.name != ".git"
            and not path.name.startswith("_")
            and (path / "spec.toml").exists()
        )
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
        else:
            template = (spec / "AGENTS.template.md").read_text(
                encoding="utf-8"
            )
            if "{{SPECIFICATION_URL}}" not in template:
                errors.append(f"missing specification placeholder: {spec.name}")
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
                text_suffix = path.suffix.lower()
                if text_suffix in {".md", ".toml", ".yaml", ".yml", ".json"}:
                    has_local_path = any(
                        marker in text for marker in LOCAL_PATH_MARKERS
                    )
                    if has_local_path:
                        errors.append(f"local path in {path.relative_to(ROOT)}")
                if not text.endswith("\n"):
                    relative = path.relative_to(ROOT)
                    errors.append(f"missing final newline: {relative}")

    skills_root = ROOT / "_skills"
    if skills_root.exists():
        for skill in skills_root.iterdir():
            if not skill.is_dir():
                continue
            if not SKILL_NAME.fullmatch(skill.name):
                errors.append(f"invalid skill folder: {skill.name}")
                continue
            skill_file = skill / "SKILL.md"
            evals_file = skill / "evals" / "evals.json"
            if not skill_file.exists():
                errors.append(f"missing SKILL.md: {skill.name}")
                continue
            if not evals_file.exists():
                errors.append(f"missing skill evals: {skill.name}")
            else:
                try:
                    evals = json.loads(
                        evals_file.read_text(encoding="utf-8")
                    )
                    if not isinstance(evals, dict):
                        errors.append(f"invalid skill evals: {skill.name}")
                    elif evals.get("skill_name") != skill.name:
                        errors.append(f"skill eval name mismatch: {skill.name}")
                    elif not evals.get("evals"):
                        errors.append(f"skill evals are empty: {skill.name}")
                except json.JSONDecodeError:
                    errors.append(f"invalid skill evals: {skill.name}")
            skill_text = skill_file.read_text(encoding="utf-8")
            if not skill_text.startswith("---\n"):
                errors.append(f"missing skill frontmatter: {skill.name}")
            if f"name: {skill.name}\n" not in skill_text:
                errors.append(f"skill name mismatch: {skill.name}")
            headings: list[str] = []
            in_code_block = False
            for line in skill_text.splitlines():
                if line.startswith("~~~") or line.startswith("```"):
                    in_code_block = not in_code_block
                elif not in_code_block and line.startswith("# "):
                    headings.append(line)
            if len(headings) != 1:
                errors.append(f"SKILL.md must have one H1: {skill.name}")
            if not skill_text.endswith("\n"):
                errors.append(f"missing final newline: {skill_file}")

    if errors:
        for error in errors:
            print(error)
        return 1
    skill_count = len(
        [path for path in (ROOT / "_skills").iterdir() if path.is_dir()]
    )
    print(f"validated {len(specs)} specifications and {skill_count} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
