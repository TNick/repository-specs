# Workspace Base

Use this profile when one repository contains multiple independently
buildable packages or applications.

## Required

- Declare workspace membership once at the root.
- Give each package a focused responsibility and explicit public API.
- Keep package-level tests close to the package in the mirrored test tree.
- Define dependency direction and reject accidental imports across layers.
- Provide root commands that exercise all packages consistently.
- Publish or release packages from reproducible lockfiles and tags.
