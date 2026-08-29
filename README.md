# Repository Specifications

Composable repository standards.

Each specification is a folder. Profiles import shared building blocks through
relative links, while consuming repositories reference a released GitHub tree:

`https://github.com/TNick/repository-specs/tree/v1.0.0/<spec-id>`

Top-level directories whose names start with an underscore contain catalog
support material and are not specifications. Catalog maintenance commands live
in `_scripts/`; reusable skills for agents working in consuming repositories
live in [`_skills/`](_skills/README.md).

## Composition and inheritance

The authoritative inheritance declaration is the `spec.toml` file inside each
specification folder. Its `extends` entries are relative paths to the direct
parent specifications; they are not inferred from Markdown links or folder
names. A specification inherits the requirements of every specification in
its transitive `extends` graph.

For example, the effective requirements for `python-library` are composed as:

```text
python-library → python-base → repository-base
```

A consuming repository normally references the released URL of its selected
profile. Agents must read that profile's `spec.toml`, follow its `extends`
entries, and read the inherited `SPEC.md` files as well. The catalog is
composable metadata and documentation; the GitHub folder URL does not itself
perform inheritance or merge documents.

## Catalog

### Foundation

- [repository-base](repository-base/SPEC.md)
- [workspace-base](workspace-base/SPEC.md)

### Languages

- [python-base](python-base/SPEC.md)
- [typescript-base](typescript-base/SPEC.md)
- [go-base](go-base/SPEC.md)

### Capabilities

- [react-vite-ui](react-vite-ui/SPEC.md)
- [http-service](http-service/SPEC.md)
- [relational-persistence](relational-persistence/SPEC.md)
- [containerized-deployment](containerized-deployment/SPEC.md)
- [multilingual-web-application](multilingual-web-application/SPEC.md)

### Profiles

- [python-library](python-library/SPEC.md)
- [python-cli-application](python-cli-application/SPEC.md)
- [python-service-application](python-service-application/SPEC.md)
- [python-workspace](python-workspace/SPEC.md)
- [typescript-library-workspace](typescript-library-workspace/SPEC.md)
- [typescript-web-application](typescript-web-application/SPEC.md)
- [python-typescript-app](python-typescript-app/SPEC.md)
- [schema-driven-polyglot-workspace](schema-driven-polyglot-workspace/SPEC.md)
- [go-web-service](go-web-service/SPEC.md)
- [qgis-plugin](qgis-plugin/SPEC.md)
- [pi-package](pi-package/SPEC.md)

Profiles are composable. A repository may use more than one profile when it
publishes a library and runs a service, or contains both a backend and UI.

## Contribution

Keep requirements normative and technology-specific only where the profile
requires them. Prefer importing a shared rule over copying it. Copy an
`AGENTS.template.md` file into a consuming repository as `AGENTS.md`, replace
its `{{SPECIFICATION_URL}}` placeholder with the tag-pinned URL, and then
customize only the project-specific instructions. Run
`python _scripts/validate_catalog.py` before committing.
