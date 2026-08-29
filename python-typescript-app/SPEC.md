# Full-Stack Application Repository Specification

## 1. Purpose

This specification defines the standard structure and tooling for applications
with:

- a Python backend;
- a TypeScript and React frontend;
- a relational database accessed through async SQLAlchemy;
- Alembic database migrations; and
- all application code hosted in one Git repository.

The specification has two goals:

1. allow coding agents to create a new application with minimal ambiguity;
2. allow coding agents to onboard an existing application into the same
   conventions without unnecessary rewrites.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## 2. Design principles

The repository MUST optimize for:

- simple navigation;
- explicit conventions;
- reproducible development environments;
- database portability;
- strict static analysis;
- automated testing;
- agent usability;
- small, understandable files;
- minimal duplicated configuration; and
- identical local, pre-commit, and CI quality rules.

Avoid directory layers which provide no useful namespace.

In particular, Python MUST NOT use a layout such as:

```text
src/
    application_name/
```

when `src/` contains only that single package.

The backend and frontend MUST instead be visible directly from the repository
root.

## 3. Baseline technology

### 3.1 Python

The minimum supported Python version MUST be Python 3.13.

Python dependencies MUST be managed with `uv`.

The repository MUST contain:

```text
pyproject.toml
uv.lock
.python-version
```

`uv.lock` MUST be committed.

Normal development commands SHOULD execute Python tools using `uv run`.

The baseline backend stack is:

- FastAPI;
- Pydantic;
- pydantic-settings;
- SQLAlchemy 2.x;
- async SQLAlchemy sessions and engines;
- Alembic;
- pytest;
- pytest-asyncio;
- pytest-cov;
- Ruff; and
- Pyright in strict mode.

### 3.2 TypeScript and React

The frontend MUST use:

- Node.js 24 LTS or newer supported LTS;
- pnpm;
- TypeScript;
- React 19 or newer compatible major;
- Vite;
- ESLint;
- typescript-eslint;
- Prettier;
- Vitest; and
- React Testing Library.

The exact dependency versions MUST be recorded in `pnpm-lock.yaml`.

The repository MUST contain a Node version declaration such as
`.node-version`.

TypeScript MUST use strict type checking.

The frontend SHOULD use browser-native functionality and React functionality
before adding additional state-management dependencies.

TanStack Query SHOULD be used when the application has significant
server-state synchronization requirements.

### 3.3 Markdown

Markdown MUST be linted.

`markdownlint-cli2` SHOULD be used for Markdown linting.

Prettier SHOULD be used to normalize Markdown formatting where its output is
compatible with the Markdown linting rules.

## 4. Repository layout

The initial repository SHOULD resemble:

```text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── Makefile
├── .editorconfig
├── .env.example
├── .gitignore
├── .node-version
├── .pre-commit-config.yaml
├── .python-version
├── pyproject.toml
├── pyrightconfig.json
├── uv.lock
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json
├── eslint.config.mjs
├── alembic.ini
├── Dockerfile
├── compose.yaml
├── backend/
│   ├── AGENTS.md
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   └── features/
├── frontend/
│   ├── AGENTS.md
│   ├── main.tsx
│   ├── app.tsx
│   ├── api/
│   ├── components/
│   ├── features/
│   ├── routes/
│   └── styles/
├── migrations/
│   ├── AGENTS.md
│   ├── env.py
│   └── versions/
├── tests/
│   ├── AGENTS.md
│   ├── backend/
│   └── frontend/
├── scripts/
│   └── AGENTS.md
└── playground/             # Git ignored and created locally
    └── agentic-work/
```

Directories SHOULD be added only when they have a defined responsibility.

Empty architectural layers MUST NOT be created merely to match the example.

## 5. Directory documentation

Every project-owned directory MUST contain an `AGENTS.md` describing, briefly:

- the purpose of the directory;
- what belongs there;
- what does not belong there; and
- any directory-specific rules.

The root `AGENTS.md` defines repository-wide rules.

A nested `AGENTS.md` supplements the root instructions and MAY introduce more
specific rules. It MUST NOT silently contradict repository-wide requirements.

Generated, vendored, cache, virtual-environment, and package-manager
directories are exempt from the `AGENTS.md` requirement.

Examples include:

```text
.venv/
node_modules/
dist/
coverage/
__pycache__/
```

Ignored agent workspaces SHOULD also contain a small `AGENTS.md` when an agent
creates additional directories inside them.

## 6. Claude instructions

The repository MUST contain a top-level `CLAUDE.md`.

`CLAUDE.md` MUST NOT duplicate the agent instructions.

Its purpose is to direct Claude-compatible tools to `AGENTS.md` for both
reading and durable instruction updates.

Its contents SHOULD be approximately:

```markdown
# Claude Instructions

Read `AGENTS.md` before making changes.

`AGENTS.md` is the authoritative source for agent instructions.

Write durable changes to agent instructions into `AGENTS.md`, not this file.
```

## 7. Agent workspace

`playground/` MUST be excluded by Git.

`.gitignore` MUST contain:

```gitignore
/playground/
```

Repository initialization MUST create:

```text
playground/agentic-work/
```

Before performing substantial work, an agent MUST create a work directory
using this format:

```text
playground/agentic-work/YYYY-MM-DD HH-MM-SS xxx/
```

The timestamp MUST use local time and 24-hour notation.

`xxx` SHOULD be a short three-character lowercase alphanumeric identifier.

For example:

```text
playground/agentic-work/2026-08-29 13-10-42 a7k/
```

Shell commands MUST quote this path because it contains spaces.

All non-deliverable files created by an agent MUST be stored inside its work
directory, including:

- temporary scripts;
- investigation notes;
- command output;
- logs;
- downloaded diagnostic data;
- generated intermediate files;
- database dumps;
- patches used during investigation;
- benchmark output; and
- temporary test data.

Deliverable source files belong in their proper repository locations and not
in `playground/`.

Agents MUST NOT delete files from `playground/agentic-work/`.

Agents MUST NOT run cleanup commands which can remove these workspaces.

In particular, agents MUST NOT use destructive `git clean` commands which can
remove ignored files.

## 8. Agent Git behavior

An agent MUST commit its completed work.

The agent MUST stage only files belonging to its work and MUST avoid including
unrelated pre-existing changes.

Commits MUST NOT be GPG, SSH, or otherwise cryptographically signed.

Agents SHOULD create commits using a command equivalent to:

```text
git -c commit.gpgsign=false commit ...
```

Agents MUST NOT bypass repository hooks using `--no-verify`.

Before committing, the agent MUST ensure:

```text
make lint
make test
```

both pass.

An agent MUST leave the repository with its completed work committed unless a
pre-existing repository condition makes committing impossible.

## 9. Python structure

`backend/` MUST itself be the Python package root.

A redundant `src/` directory MUST NOT be introduced.

Application imports SHOULD therefore resemble:

```python
from backend.core.config import settings
from backend.db.session import get_session
```

Feature-oriented organization is preferred for domain code:

```text
backend/
    features/
        users/
            AGENTS.md
            __init__.py
            model.py
            schemas.py
            service.py
            router.py
```

Shared infrastructure belongs outside individual features.

For example:

```text
backend/core/
backend/db/
backend/api/
```

Business logic MUST NOT be placed directly inside HTTP route handlers when it
can reasonably be represented as domain or service logic.

## 10. Python formatting and typing

Python MUST use four spaces for indentation.

Tabs MUST NOT be used for indentation.

The maximum line length for human-authored Python files is 80 characters.

Comments and docstrings SHOULD be wrapped at 72 characters.

Ruff MUST be configured with:

```text
line-length = 80
```

Ruff MUST be responsible for Python formatting and linting.

Pyright MUST type-check the Python application and tests.

Pyright MUST use:

```text
typeCheckingMode = "strict"
pythonVersion = "3.13"
```

Application code MUST NOT rely on widespread `Any` annotations to make the
type checker pass.

Any intentional type suppression MUST be narrow and include a short
explanation when the reason is not obvious.

## 11. TypeScript formatting and typing

TypeScript, TSX, JavaScript configuration, JSON, CSS, and related frontend
files MUST use two spaces for indentation.

The normal maximum line width is 80 characters.

Comments SHOULD be wrapped at 72 characters.

Prettier MUST use a print width of 80.

TypeScript MUST enable strict checking.

At minimum, the TypeScript configuration SHOULD enable the equivalent of:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true
  }
}
```

`tsc --noEmit` MUST be part of `make lint`.

ESLint MUST report warnings as failures in CI and `make lint`.

## 12. File size

Human-authored source, configuration, test, and documentation files MUST NOT
exceed 400 lines.

When a source file grows beyond 400 lines, the preferred refactoring is to
replace the file with a directory having the same logical name.

For Python:

```text
users.py
```

becomes:

```text
users/
    AGENTS.md
    __init__.py
    models.py
    service.py
    validation.py
```

The public API previously exposed by `users.py` MUST be exported through:

```text
users/__init__.py
```

For TypeScript:

```text
table.tsx
```

becomes:

```text
table/
    AGENTS.md
    index.ts
    table.tsx
    columns.ts
    types.ts
```

The public API MUST be exported through:

```text
table/index.ts
```

Import paths SHOULD remain stable during such a conversion.

Machine-owned files are exempt from the 400-line requirement.

Examples include:

- `uv.lock`;
- `pnpm-lock.yaml`;
- generated OpenAPI clients;
- generated type definitions; and
- other files explicitly marked as generated.

Generated files MUST NOT be manually split merely to satisfy this rule.

## 13. General text formatting

Human-authored text files MUST use UTF-8.

Files MUST end with exactly one newline.

Trailing whitespace MUST NOT be present.

Human-authored text SHOULD remain within 80 columns.

Source-code comments SHOULD remain within 72 columns.

Machine-generated and machine-owned files are exempt where their generator
does not preserve these rules.

A repository script MAY enforce rules not supported consistently by the
language-specific formatters.

Such scripts MUST live under:

```text
scripts/
```

For example:

```text
scripts/check_file_lengths.py
scripts/check_text_width.py
```

## 14. Database access

All application database access MUST use SQLAlchemy 2.x APIs.

Runtime application database access MUST use SQLAlchemy's asyncio API.

The application SHOULD use:

```python
create_async_engine(...)
async_sessionmaker(...)
AsyncSession
```

The database connection MUST be configured using an environment variable,
normally:

```text
DATABASE_URL
```

The default development value SHOULD use SQLite with `aiosqlite`, for example:

```text
sqlite+aiosqlite:///./playground/development.db
```

A production PostgreSQL installation could instead provide:

```text
postgresql+asyncpg://...
```

Changing database systems MUST NOT require changes to business logic.

## 15. Database portability

SQLite is a development and testing convenience, not an application
dependency.

Application code MUST NOT contain SQLite-specific behavior.

This includes avoiding:

- SQLite-specific SQL syntax;
- SQLite-specific functions;
- SQLite-specific PRAGMA statements in application logic;
- assumptions about SQLite type coercion;
- assumptions about SQLite locking;
- SQLite-specific connection behavior in domain code; and
- direct imports from a SQLite SQLAlchemy dialect.

Queries SHOULD be expressed through SQLAlchemy ORM or SQLAlchemy Core.

Raw SQL SHOULD be avoided.

When raw SQL is necessary, it MUST either be portable across supported
databases or be isolated behind a clearly documented database abstraction.

SQLAlchemy generic types SHOULD be preferred over dialect-specific types.

Database enums SHOULD normally be represented portably unless a project has
explicitly narrowed its supported database list.

Primary keys, timestamps, unique constraints, foreign keys, indexes, and
defaults MUST be defined using portable SQLAlchemy constructs.

SQLite tests MUST NOT be treated as sufficient proof of database portability
for database-sensitive functionality.

Projects targeting PostgreSQL in production SHOULD run database integration
tests against PostgreSQL in CI in addition to the normal SQLite suite.

## 16. SQLAlchemy sessions

An `AsyncSession` MUST have a clearly bounded lifetime.

HTTP requests SHOULD normally receive one session through FastAPI dependency
injection.

Sessions MUST NOT be stored in global mutable state.

Transaction boundaries MUST be explicit.

Business functions SHOULD receive an `AsyncSession` or a narrower repository
interface rather than opening unrelated sessions internally.

Concurrent tasks MUST NOT share the same `AsyncSession`.

## 17. Alembic

Alembic MUST be the only mechanism used to evolve persistent database schema.

Application startup MUST NOT call `metadata.create_all()` as a substitute for
migrations.

The repository MUST contain:

```text
alembic.ini
migrations/
    env.py
    versions/
```

Alembic MUST use the application's SQLAlchemy metadata as its
`target_metadata`.

The migration environment MUST obtain its database URL from the same
configuration mechanism as the application.

Alembic MAY use its async environment pattern to work with async SQLAlchemy
drivers.

Every schema change MUST include an Alembic migration.

Autogenerated migrations MUST be reviewed before commit.

Migration scripts SHOULD remain database-neutral.

Both upgrade and downgrade behavior SHOULD be implemented when a safe downgrade
is practical.

Tests SHOULD verify that a fresh empty database can migrate to the current
head.

## 18. Configuration

Runtime configuration MUST come from environment variables.

Pydantic Settings SHOULD provide backend configuration parsing and validation.

Secrets MUST NOT be committed.

The repository MUST contain `.env.example`.

`.env.example` MUST contain all supported environment variable names with
safe example values or explanatory placeholders.

Local `.env` files MUST be ignored.

Configuration MUST fail clearly when a required production value is missing.

## 19. API contract

Backend HTTP APIs SHOULD be rooted beneath:

```text
/api/
```

Versioned public APIs SHOULD use a version prefix such as:

```text
/api/v1/
```

FastAPI's OpenAPI document SHOULD be treated as the canonical HTTP contract.

The frontend SHOULD NOT manually duplicate complex backend response types.

For non-trivial applications, TypeScript API types SHOULD be generated from
the OpenAPI schema using a maintained OpenAPI-to-TypeScript generator.

Generated API code MUST be clearly marked and MUST NOT be manually edited.

## 20. Frontend structure

The frontend MUST NOT contain an otherwise redundant `src/` directory.

The Vite application root is:

```text
frontend/
```

A typical feature SHOULD resemble:

```text
frontend/features/users/
    AGENTS.md
    index.ts
    api.ts
    components.tsx
    hooks.ts
    types.ts
```

Large features SHOULD be further divided before individual files exceed
400 lines.

Shared components belong in:

```text
frontend/components/
```

Application routing belongs in:

```text
frontend/routes/
```

Shared HTTP client infrastructure belongs in:

```text
frontend/api/
```

## 21. Development networking

During normal development:

- the backend SHOULD listen on port 8000;
- Vite SHOULD listen on port 5173; and
- Vite SHOULD proxy `/api` requests to the backend.

Frontend application code SHOULD use relative API URLs by default.

The frontend MUST NOT hardcode `localhost:8000` throughout application code.

This allows development and production to use the same API call structure.

## 22. Tests

Tests MUST NOT be colocated with production source files.

All tests MUST live beneath:

```text
tests/
```

The test directory MUST mirror the source directory structure.

For example:

```text
backend/features/users/service.py
tests/backend/features/users/test_service.py
```

and:

```text
frontend/features/users/hooks.ts
tests/frontend/features/users/hooks.test.ts
```

Each test directory MUST contain its own `AGENTS.md`.

Backend tests MUST use pytest.

Frontend tests MUST use Vitest.

React component tests SHOULD use React Testing Library.

Tests MUST favor externally visible behavior over internal implementation
details.

## 23. Coverage

The minimum automated test coverage is 80%.

Backend coverage MUST fail the test command below 80%.

Backend coverage SHOULD include branch coverage.

Frontend coverage MUST enforce at least 80% for:

- statements;
- branches;
- functions; and
- lines.

Generated files, migration files, and deliberate framework bootstrap files MAY
be excluded from coverage when the exclusion is documented in configuration.

Coverage exclusions MUST NOT be used to hide ordinary untested application
logic.

## 24. Makefile

A top-level `Makefile` is mandatory.

Running:

```text
make
```

with no arguments MUST print available targets and a short description of
each target.

The first/default target SHOULD therefore be `help`.

At minimum, the Makefile MUST expose the following targets:

```text
init
init-def
web-dev
frontend
backed
test
lint
delint
docker-run
docker-stop
docker-shell
docker-rebuild
```

A correctly spelled `backend` target MAY additionally be provided as an alias
for `backed`.

### `make init`

`init` MUST bootstrap the repository without destroying existing local
configuration.

It SHOULD:

1. verify required tools;
2. install locked Python dependencies;
3. install locked Node dependencies;
4. install pre-commit hooks;
5. create required ignored directories; and
6. print any remaining setup steps.

The command MUST be idempotent.

### `make init-def`

`init-def` MUST initialize a usable default development environment.

It SHOULD call or depend on `init`.

It SHOULD additionally:

1. create `.env` from `.env.example` when `.env` does not exist;
2. create `playground/agentic-work/`;
3. configure the default SQLite development database; and
4. apply Alembic migrations.

It MUST NOT overwrite an existing `.env`.

### `make frontend`

Starts the Vite frontend development server.

### `make backed`

Starts the Python backend development server with reload enabled.

A `backend` alias MAY point to this target.

### `make web-dev`

Starts both frontend and backend development servers.

If process orchestration requires a script, the script MUST live beneath
`scripts/`.

The orchestration MUST correctly terminate both child processes when the
parent command exits.

### `make test`

Runs the complete normal automated test suite.

At minimum this includes:

```text
pytest
vitest
```

Coverage requirements MUST be enforced by this command.

### `make lint`

`lint` MUST be read-only.

It MUST NOT modify repository files.

It MUST run all required static validation, including:

```text
ruff check
ruff format --check
pyright
tsc --noEmit
eslint
prettier --check
markdownlint-cli2
```

It MUST also enforce repository-specific checks for:

- maximum human-authored file size;
- text line lengths where necessary; and
- other structural invariants not covered by standard tools.

### `make delint`

`delint` applies safe automatic formatting and lint fixes.

It SHOULD run the equivalents of:

```text
ruff check --fix
ruff format
eslint --fix
prettier --write
```

After automatic changes, it SHOULD run `make lint`.

Structural problems such as a file exceeding 400 lines MUST NOT be hidden by
`delint`; they require refactoring.

### Docker targets

`docker-run` starts the normal Docker Compose environment.

`docker-stop` stops it without deleting persistent data by default.

`docker-shell` opens an interactive shell in the primary application
container.

`docker-rebuild` rebuilds the application image and restarts the normal
environment.

## 25. Tooling scripts

Repository-specific automation scripts MUST live beneath:

```text
scripts/
```

Tooling scripts MUST NOT be scattered through application packages.

Scripts used by the Makefile SHOULD be independently executable where
practical.

Python tooling scripts MUST themselves be formatted, linted, and type-checked.

Shell scripts MUST fail on errors and SHOULD use strict shell settings where
portable.

Complex shell logic SHOULD be replaced with a small typed Python script when
that produces clearer behavior.

## 26. Pre-commit

`pre-commit` MUST be installed as a development dependency.

`make init` MUST install its Git hooks.

The repository MUST contain:

```text
.pre-commit-config.yaml
```

Pre-commit MUST use the same authoritative commands as normal development.

It MUST NOT maintain a second, subtly different lint configuration.

The preferred approach is local hooks which invoke:

```text
make lint
make test
```

with `pass_filenames: false`.

This intentionally makes the Makefile the source of truth.

Agents MUST NOT bypass these hooks.

If test runtime later becomes genuinely excessive, a project MAY move the
complete test suite to a pre-push hook, but the distinction MUST be documented
in `AGENTS.md` and CI MUST still execute `make test`.

## 27. Docker

The repository MUST contain a Dockerfile and Compose configuration.

The Dockerfile SHOULD use a multi-stage build.

The frontend build stage SHOULD use the repository's pinned Node environment.

The backend runtime stage MUST use Python 3.13 or newer.

Production images MUST install dependencies from lockfiles.

Development-only tools SHOULD NOT be copied into the final production image
unless required at runtime.

The application container MUST receive `DATABASE_URL` through configuration
rather than baking a database location into the image.

Docker development with SQLite SHOULD store its database under the mounted
`playground/` directory.

`docker-stop` MUST NOT delete database volumes unless explicitly requested by
a separate destructive command.

## 28. README

The root `README.md` MUST explain:

- the application's purpose;
- prerequisites;
- `make init-def`;
- `make web-dev`;
- all principal Makefile targets;
- configuration and `.env`;
- database migrations;
- running tests;
- linting and formatting;
- Docker usage;
- the backend/frontend structure; and
- where agent instructions live.

The README SHOULD optimize for a developer reaching a working application
quickly.

Repository policy belongs primarily in `AGENTS.md`, not duplicated verbatim
throughout the README.

## 29. CI

CI MUST execute authoritative repository commands rather than rebuilding their
logic manually.

At minimum CI MUST execute:

```text
make lint
make test
```

CI MUST install dependencies using committed lockfiles.

The Python environment MUST use Python 3.13 or newer.

The Node environment SHOULD use the repository's selected Node 24 LTS version
until the template is deliberately upgraded.

If PostgreSQL is the expected production database, CI SHOULD additionally run
database-sensitive tests and Alembic migrations against PostgreSQL.

A CI failure MUST be reproducible locally through a documented Makefile
command.

## 30. Existing-application onboarding

Agents onboarding an existing application MUST preserve working behavior while
moving the repository toward this specification.

The migration SHOULD be performed incrementally.

First, the agent MUST create its timestamped agent workspace and record its
inventory or investigation files there.

The agent SHOULD then establish, in this order:

1. root `AGENTS.md` and `CLAUDE.md`;
2. `playground/` exclusion and workspace policy;
3. the root Makefile contract;
4. dependency lockfiles;
5. linting and formatting;
6. strict type checking;
7. separated and mirrored tests;
8. coverage enforcement;
9. async SQLAlchemy database boundaries;
10. Alembic migrations;
11. Docker entry points; and
12. CI parity.

Large directory moves SHOULD be separated from behavioral refactors when
possible so changes remain reviewable.

An existing synchronous SQLAlchemy application SHOULD be migrated behind a
clear database/session boundary rather than converted through scattered
one-line changes across unrelated business code.

SQLite-specific application logic discovered during onboarding MUST be
removed, generalized, or isolated behind an explicitly supported database
abstraction.

Existing migrations SHOULD normally be preserved rather than rewritten solely
for aesthetics.

## 31. Adding dependencies

Agents MUST prefer existing dependencies and standard-library functionality
before introducing a new package.

A new dependency MUST have a clear purpose.

Python dependencies MUST be added through `uv`, so `pyproject.toml` and
`uv.lock` remain synchronized.

Node dependencies MUST be added through `pnpm`, so `package.json` and
`pnpm-lock.yaml` remain synchronized.

Agents MUST NOT hand-edit lockfiles.

A dependency used only during development MUST be declared as a development
dependency.

## 32. Generated content

Generated files MUST have a clearly identifiable source and regeneration
command.

Generated files SHOULD contain a generated-file warning when the generator
supports one.

Agents MUST modify the source or generator rather than manually editing
generated output.

Intermediate generated files MUST be written beneath the agent's
`playground/agentic-work/...` directory.

Only final generated artifacts required by the repository MAY be copied into
tracked locations.

## 33. Definition of done

Agent work is complete only when all applicable conditions are true:

- the requested behavior works;
- new code follows the repository structure;
- each new project-owned directory has an `AGENTS.md`;
- no human-authored file exceeds 400 lines;
- Python uses four-space indentation;
- TypeScript uses two-space indentation;
- human-authored lines satisfy width rules;
- Python passes strict type checking;
- TypeScript passes strict type checking;
- Markdown passes linting;
- database code remains portable;
- schema changes have reviewed Alembic migrations;
- tests mirror source structure;
- backend coverage is at least 80%;
- frontend coverage is at least 80%;
- `make lint` passes;
- `make test` passes;
- temporary artifacts remain in the agent workspace;
- no temporary artifact has been deleted merely for cleanup;
- no unrelated user changes were committed; and
- the completed work has been committed with commit signing disabled.

## 34. Source of truth

The order of authority for repository behavior is:

```text
this specification
AGENTS.md
nested AGENTS.md
Makefile
tool-specific configuration
README.md
```

The implemented repository MUST avoid duplicating configuration where one tool
can call another authoritative command.

In particular:

```text
pre-commit -> Makefile -> underlying tools
CI         -> Makefile -> underlying tools
developer  -> Makefile -> underlying tools
agent      -> Makefile -> underlying tools
```

This relationship is intentional.

A command that succeeds locally through `make lint` or `make test` SHOULD
behave identically when invoked by an agent, pre-commit, or CI.
