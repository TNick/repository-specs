# Relational Persistence

Use this building block when application state is stored in a relational
database.

## Required

- Use SQLAlchemy 2.x or the repository's documented equivalent behind a
  persistence boundary.
- Evolve schema only through reviewed migrations.
- Read connection settings from environment configuration.
- Keep transaction and session lifetimes explicit; never share mutable
  sessions across concurrent tasks.
- Test a fresh database migration and database-sensitive behavior.
