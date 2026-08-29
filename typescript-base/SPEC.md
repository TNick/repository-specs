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
  that briefly explains their purpose, followed by one to five lines of code.
  Standalone comments and JSDoc lines MUST wrap at 80 columns; avoid trailing
  inline comments.
- Keep generated declarations and API clients clearly marked and do not edit
  them manually.

## Preferred example

```typescript
/** A stable identifier for a project. */
type ProjectId = string;

/** A project returned by the service. */
interface Project {
  /** Stable project identifier. */
  id: ProjectId;

  /** Human-readable project name. */
  name: string;
}

/**
 * Options used when loading a project.
 *
 * @property projectId - Stable project identifier.
 * @property includeDrafts - Whether draft documents are included.
 */
interface LoadOptions {
  /** Stable project identifier. */
  projectId: string;

  /** Whether draft documents are included. */
  includeDrafts: boolean;
}

/** Client for the project service.
 *
 * This class centralizes request construction and response validation.
 */
class ProjectClient {
  /** API base URL. */
  private readonly baseUrl: string;

  /** Create a project client.
   *
   * @param baseUrl - API base URL.
   */
  constructor(baseUrl: string) {

    // Store the normalized URL for subsequent requests.
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  /** Load a project by identifier.
   *
   * @param projectId - Project to load.
   * @returns The loaded project.
   * @throws {Error} If the API rejects the request.
   */
  async load(projectId: ProjectId): Promise<Project> {

    // Build the request URL from the validated identifier.
    const url = `${this.baseUrl}/api/projects/${projectId}`;

    // Send the request and inspect the HTTP result.
    const response = await fetch(url);

    // Convert an unsuccessful response into a useful exception.
    if (!response.ok) {
      throw new Error(`Project request failed: ${response.status}`);
    }

    // Decode the validated project response.
    return response.json() as Promise<Project>;
  }
}
```

Avoid undocumented private members, props, type aliases, nested functions, or
arrow functions. Avoid one-line comments after code and files that grow past
400 lines; split them into focused modules while preserving exports.

The block rule applies to cohesive operations, not every individual line.
Imports, decorators, adjacent declarations, continuation clauses such as
`else`, `catch`, and `finally`, closing delimiters, generated code, and
formatter-required constructs are exempt when a comment would add no meaning.
A block longer than five lines should be split into smaller operations or
have a documented reason to remain together.

## Enforcement

- ESLint MUST use `jsdoc/require-jsdoc`, `jsdoc/require-param`,
  `jsdoc/require-returns`, and the TypeScript-aware equivalents for the
  repository's supported syntax.
- ESLint MUST enforce `max-lines` for the 400-line limit and `max-len` where
  Prettier does not provide the check. Prettier MUST run in check mode in CI.
- A repository MUST provide a checked-in custom ESLint rule or equivalent
  script for the blank-line/comment/block-size convention; ESLint's generic
  comment rules cannot infer logical intent reliably.
- CI and pre-commit MUST invoke the same checks as the developer lint command.
