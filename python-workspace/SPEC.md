# Python Workspace

Use this profile for a repository containing multiple Python distributions.

## Required

- Put each installable package in a named workspace member with its own
  metadata and tests.
- Keep shared packages lower in the dependency graph than applications.
- Define root commands for install, lint, typecheck, test, build, and release.
- Make generated packages and generated APIs reproducible and identifiable.
- Exercise package boundaries in CI rather than relying only on aggregate
  tests.
