# Catalog Agent Instructions

Read `README.md` and the applicable profile `SPEC.md` before changing this
catalog. Keep profile requirements composable and avoid copying rules from
`repository-base` or another imported specification.

Inheritance is authoritative in each specification's `spec.toml`: follow the
relative paths in `extends` to determine the complete transitive requirement
set. Do not infer inheritance from Markdown links or folder names.

Top-level directories beginning with an underscore are support directories,
not specifications. Keep catalog tooling in `_scripts/` and consumer-facing
agent skills in `_skills/`.

Run `python _scripts/validate_catalog.py` before committing. Do not place
local filesystem paths, credentials, generated build output, or
project-specific secrets in this public repository.

The canonical consumer reference is a tag-pinned GitHub folder URL under
`https://github.com/TNick/repository-specs/tree/<tag>/`.
