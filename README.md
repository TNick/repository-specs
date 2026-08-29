# Repository Specifications

Composable repository standards.

Each specification is a folder. Profiles import shared building blocks through
relative links, while consuming repositories reference a released GitHub tree:

`https://github.com/TNick/repository-specs/tree/v1.0.0/<spec-id>`

## Catalog

| Group | Specifications |
| --- | --- |
| Foundation | [repository-base](repository-base/SPEC.md), [workspace-base](workspace-base/SPEC.md) |
| Languages | [python-base](python-base/SPEC.md), [typescript-base](typescript-base/SPEC.md), [go-base](go-base/SPEC.md) |
| Capabilities | [react-vite-ui](react-vite-ui/SPEC.md), [http-service](http-service/SPEC.md) |
|  | [relational-persistence](relational-persistence/SPEC.md), [containerized-deployment](containerized-deployment/SPEC.md) |
| Profiles | [python-library](python-library/SPEC.md), [python-cli-application](python-cli-application/SPEC.md) |
|  | [python-service-application](python-service-application/SPEC.md), [python-workspace](python-workspace/SPEC.md) |
|  | [typescript-library-workspace](typescript-library-workspace/SPEC.md), [typescript-web-application](typescript-web-application/SPEC.md) |
|  | [python-typescript-app](python-typescript-app/SPEC.md), [schema-driven-polyglot-workspace](schema-driven-polyglot-workspace/SPEC.md) |
|  | [go-web-service](go-web-service/SPEC.md), [qgis-plugin](qgis-plugin/SPEC.md), [pi-package](pi-package/SPEC.md) |

Profiles are composable. A repository may use more than one profile when it
publishes a library and runs a service, or contains both a backend and UI.

## Contribution

Keep requirements normative and technology-specific only where the profile
requires them. Prefer importing a shared rule over copying it. Run
`python scripts/validate_catalog.py` before committing.
