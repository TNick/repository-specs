# QGIS Plugin

Use this profile for code loaded by QGIS or PyQt and tested against supported
QGIS/Qt versions.

## Required

- Keep plugin metadata, registration, GUI, layer logic, and domain adapters
  in explicit directories.
- State supported QGIS, Qt, Python, and provider versions.
- Avoid importing QGIS-specific APIs into reusable domain libraries.
- Run tests in the supported QGIS containers or environments.
- Document installation, reload behavior, and deployment packaging.
