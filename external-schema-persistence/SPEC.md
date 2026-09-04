# External Schema Persistence

Use this capability when the canonical relational schema and its migrations
live in an external package or sibling repository, while the application
consumes that schema without duplicating ORM models.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

This capability extends `relational-persistence`. SQLAlchemy 2.x (or the
documented equivalent), environment-based connection settings, explicit
session lifetimes, and fresh-database verification remain required.

## Scope and boundaries

- The application repository MAY own zero in-repo Alembic trees when the
  schema package is the single source of truth.
- Private checkout paths and internal package names MUST NOT appear in a
  reusable public specification. Consumers document those bindings in
  project configuration and design records.

## Schema ownership

- The canonical tables, ORM models, and migration revisions MUST live in the
  schema package (or designated schema repository).
- The application MUST NOT duplicate those ORM models inside its own source
  tree.
- Schema changes MUST be reviewed and landed in the schema package with
  migrations. The application MUST NOT invent parallel DDL paths for the
  same tables.

## Application consumption

- The application MUST depend on the schema package through a published
  distribution, an editable mount in lab containers, or another documented
  install path that preserves version identity.
- Connection settings MUST still come from environment configuration.
- Transaction and session lifetimes MUST remain explicit. Mutable sessions
  MUST NOT be shared across concurrent tasks.

## Verification

- A fresh database MUST be creatable by applying the schema package
  migrations (or an equivalent documented bootstrap).
- The application MUST provide or participate in tests that exercise
  migration application and database-sensitive behavior.
- Lab bootstrap and seed tooling MUST document which schema package revision
  they expect.
