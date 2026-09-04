# Playwright Browser E2E

Use this capability when the repository maintains Playwright end-to-end
browser tests as a first-class quality gate for user-visible UI.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## Scope and boundaries

This capability governs the dedicated browser E2E tree, runner, data
isolation, and when new or changed UI requires a regression spec. It does
not replace unit tests (Vitest, pytest, and similar).

## Repository layout

- Browser automation MUST live in a dedicated tree such as `e2e/`, separate
  from production frontend sources and from unit-test colocations.
- The tree MUST include a Playwright configuration file, a documented
  package manifest or workspace membership, and a `tests/` (or equivalent)
  directory for specs.
- Shared login and domain helpers SHOULD live under a helpers directory
  inside the E2E tree.

## Runner and contracts

- Playwright MUST be the named browser E2E runner for this capability.
- Specs MUST assert stable user-visible contracts: routes, roles, labels,
  documented automation ids, or successful API responses tied to UI.
- Specs MUST NOT depend on implementation-only internals that churn without
  changing user behavior.

## When a spec is required

- A change that implements or fixes user-visible frontend behavior MUST add
  or update a Playwright regression spec in the same change set.
- Vitest, Storybook, and HTTP smoke tests do not satisfy this requirement
  when the contract is navigation, map chrome, cross-route flows, or live
  API-and-UI integration.
- Pure refactors with no user-visible behavior change, read-only work,
  plan-only work, backend-only changes with no UI surface, and explicitly
  waived tasks MAY omit a Playwright update when the waiver is recorded.

## Data isolation

- Default Playwright runs MUST target a lab, fixture, or otherwise
  disposable database environment.
- Default Playwright runs MUST NOT target a live or external production-like
  database.
- Optional seed data MAY gate cases with `test.skip` and a clear message.
  Finished work MUST NOT leave `test.fixme` as a substitute for coverage
  unless a design record accepts an explicit follow-up.

## Operator interface

- The repository MUST document how to run a single spec and the full
  Playwright suite, including the base URL for local and lab stacks.
- Root Makefile or catalogued developer commands SHOULD expose Playwright
  entry points that install browsers when needed.

## Documentation

- Credentials used only for lab E2E MUST be documented as non-secret lab
  defaults or supplied through local env files that are gitignored.
- Hostnames and private inventory details MUST stay in project configuration
  or private design records, not in a reusable public specification.
