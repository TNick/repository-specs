# TypeScript Library Workspace

Use this profile for a pnpm or npm workspace that publishes reusable
TypeScript packages.

## Required

- Keep packages framework-agnostic unless a package explicitly owns a UI
  framework integration.
- Define package exports, build outputs, and declaration generation explicitly.
- Test each package and run a workspace-wide boundary check.
- Version and publish packages from lockfile-backed release commands.
- Keep examples and playground consumers outside production packages.
