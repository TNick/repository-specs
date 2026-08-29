# TypeScript Base

TypeScript repositories use strict types and a lockfile-backed Node package
manager.

## Required

- Enable strict TypeScript checking and keep generated files clearly marked.
- Use two-space indentation and Prettier as the formatting source of truth.
- Run lint, typecheck, and tests through the root documented command.
- Keep tests separate from production code and use Vitest or the repository's
  explicitly documented equivalent.
- Pin the Node and package-manager versions used by CI.
