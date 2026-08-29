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

## Code style

- TypeScript compiler settings MUST enable strict checking. New projects
  SHOULD also enable `noUncheckedIndexedAccess` and `noImplicitOverride`.
- Prettier MUST use an 80-column print width. Human-authored TypeScript,
  TSX, JavaScript, tests, configuration, and documentation files MUST be no
  longer than 400 lines. Generated files, lockfiles, and vendored files are
  exempt; split oversized modules while preserving public exports.
- Every class, interface, type alias, and type-literal member MUST have a
  JSDoc comment, including private members. The first line is a short summary,
  followed by a blank JSDoc line before detail.
- Every function and method MUST have JSDoc, including private functions,
  nested functions, and block-bodied arrow functions. Document every
  parameter with `@param`, the return value with `@returns`, and relevant
  exceptions with `@throws` or equivalent prose.
- React components MUST be documented. Components with props SHOULD declare a
  documented interface for those props above the component.
- Logical blocks SHOULD begin after a blank line and a short `//` comment
  when their purpose is not obvious. Standalone comments and JSDoc lines MUST
  wrap at 80 columns; avoid trailing inline comments.
- Keep generated declarations and API clients clearly marked and do not edit
  them manually.
