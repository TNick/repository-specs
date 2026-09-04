# Python TypeScript Map Application

Use this profile for a monorepo that combines a Python HTTP service with a
QWC-based (or equivalent) TypeScript map SPA, Compose lab containers,
external schema ownership, Playwright browser E2E, and systemd install-kit
production rollout.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## Relationship to `python-typescript-app`

This profile is an **alternative** to `python-typescript-app` for map and
QWC products. It reuses the Python service and repository foundations
without inheriting `react-vite-ui`.

A repository MUST NOT adopt both profiles as primary pins. Choose
`python-typescript-app` for Vite-first SPAs, or this profile for QWC/webpack
map shells.

Inherited capabilities already cover: HTTP service health, TypeScript base
style, QWC vendor/overrides, Compose containers, external schema
persistence, Playwright E2E, and install-kit/systemd deployment. This SPEC
adds only monorepo glue that those parents do not define.

## Repository layout

The backend and frontend MUST be visible directly from the repository root
as `backend/` and `frontend/` (names MAY vary only when documented).

A typical shape:

```text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── Makefile
├── backend/
├── frontend/
├── docker/
├── deploy/
├── e2e/
├── scripts/
├── design/
└── playground/             # Git ignored
```

- The Python package MAY live at `backend/<package_name>/` rather than
  importing modules directly from `backend/`.
- The frontend MAY use a `frontend/src/` tree when the custom viewer and SPA
  routes need that namespace. The redundant-`src/` prohibition from
  `python-typescript-app` does **not** apply here.
- Empty architectural layers MUST NOT be created merely to match the
  example.

## Directory documentation

Every project-owned directory MUST contain an `AGENTS.md` describing the
purpose of the directory, what belongs there, what does not, and any
directory-specific rules. Nested files supplement the root and MUST NOT
silently contradict repository-wide requirements.

Generated, vendored, cache, virtual-environment, and package-manager
directories are exempt.

## Claude instructions

The repository MUST contain a top-level `CLAUDE.md` that directs
Claude-compatible tools to `AGENTS.md` without duplicating agent rules.

## Design records

Design records follow `repository-base`. The project MUST declare
`Design records: public` or `Design records: private` exactly.

## Agent Git behavior

Agents MUST create unsigned commits when the project policy requires agent
auto-commits (`--no-gpg-sign` or equivalent). Agents MUST NOT prompt for a
GPG passphrase. Agents MUST NOT push unless explicitly asked.

## Baseline technology (profile-level)

### Python service

- The backend SHOULD use FastAPI, Pydantic settings, async SQLAlchemy 2.x,
  pytest, Ruff, and a documented type checker.
- Python 3.13 SHOULD be the target. Python 3.12 MAY remain when a design
  record records the intentional deviation and images/docs agree.
- Dependency management SHOULD use `uv` with a committed lockfile. A
  documented `backend/venv` + pip editable install MAY remain when a design
  record records the intentional deviation.

### TypeScript map SPA

- The frontend MUST use TypeScript, React 19 or a newer compatible major,
  pnpm, ESLint, Prettier, and Vitest (or a documented equivalent).
- The production bundler follows `qwc-map-spa` (webpack allowed).
- Node and pnpm versions used by CI MUST be pinned and MUST match the
  package manager field in the frontend manifest unless a design record
  documents a temporary mismatch.

## API contract

Backend HTTP APIs SHOULD be rooted beneath `/api/`. Versioned public APIs
SHOULD use a prefix such as `/api/v1/`. FastAPI's OpenAPI document SHOULD be
treated as the canonical HTTP contract. Generated TypeScript clients MUST be
clearly marked and MUST NOT be manually edited.

## Development networking

- The backend SHOULD listen on port 8000 (or a documented lab port).
- The frontend dev server SHOULD listen on port 5173 (or a documented port)
  and SHOULD proxy `/api` to the backend.
- Application code SHOULD use relative API URLs by default and MUST NOT
  hardcode backend hostnames throughout the tree.

## Tests and coverage

- Backend unit/integration tests SHOULD live under `backend/tests/` or a
  documented mirrored tree.
- Frontend unit tests MAY be colocated with components when the project
  documents that convention; Playwright remains under `e2e/` per
  `playwright-browser-e2e`.
- Coverage gates SHOULD be documented. New projects SHOULD target at least
  80% for owned application code. Existing projects MAY record a lower
  enforced floor as an intentional deviation with a plan to raise it.

## Makefile and CI

The root Makefile or documented equivalent MUST expose install, lint, test,
format, frontend/backend development, Docker lab, and E2E entry points.
Exact target names MAY differ from `python-typescript-app` when documented
in `make help` or the README.

CI MUST execute authoritative repository commands (at minimum lint and test
entry points) and MUST install from committed lockfiles.

## Docker lab and production kits

- Compose lab assets follow `containerized-deployment` and SHOULD live under
  `docker/` when the lab is multi-service.
- Production install kits follow `install-kit-deployment` under `deploy/`.
- Agents MUST treat lab Compose workflows and production install-kit
  rollouts as distinct paths.

## Configuration

Runtime configuration and secrets MUST come from environment files or
mounted configuration. Secrets MUST NOT be committed. A safe `.env.example`
(or per-kit examples) MUST list supported settings.

## Onboarding existing applications

Agents onboarding an existing map application MUST preserve working
behavior while closing gaps incrementally. Record intentional deviations in
a numbered design gap review. Do not silently weaken this specification.

## Source of truth

When project instructions conflict with this specification, the
specification wins unless a design record explicitly accepts a deviation.
Project-specific boundaries that are stricter than this specification
(vendor read-only trees, hard private-package rules, mandatory Playwright
for UI changes) remain in force.
