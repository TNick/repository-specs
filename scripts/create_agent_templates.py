"""Create the small agent template shipped with every catalog profile."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = """# Agent Instructions

Read the repository root `AGENTS.md` and the linked repository specification
before making changes. Keep temporary work under `playground/agentic-work/`.

The consuming repository owns implementation details. This document supplies
durable workflow guidance; the referenced specification supplies structure and
quality requirements.
"""


def main() -> None:
    """Write templates for every specification folder."""
    for path in ROOT.iterdir():
        if path.is_dir() and path.name != ".git":
            (path / "AGENTS.template.md").write_text(TEMPLATE, encoding="utf-8")


if __name__ == "__main__":
    main()
