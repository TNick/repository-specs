"""Run repository tools through the selected UV-managed environment."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def project_environment(root: Path) -> Path:
    """Return the platform-specific environment path for the repository."""
    suffix = ".venv-win" if os.name == "nt" else ".venv-lnx"
    return root / suffix


def main() -> int:
    """Run the requested command through ``uv run``."""
    if len(sys.argv) < 2:
        sys.stderr.write("a command is required\n")
        return 2
    root = Path(__file__).resolve().parent.parent
    uv = shutil.which("uv")
    if uv is None:
        sys.stderr.write("uv is required to run repository checks\n")
        return 2
    environment = os.environ.copy()
    environment["UV_PROJECT_ENVIRONMENT"] = str(project_environment(root))
    result = subprocess.run(
        [uv, "run", "--project", str(root), *sys.argv[1:]],
        cwd=root,
        env=environment,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
