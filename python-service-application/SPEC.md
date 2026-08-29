# Python Service Application

Use this profile for a deployable Python API, worker, or long-running daemon.

## Required

- Keep the process entry point small and document how it is run locally and
  in production.
- Validate external input at the boundary and keep domain operations
  framework-independent.
- Document health, readiness, configuration, logs, and graceful shutdown.
- Provide a service-level smoke test and isolated tests for domain behavior.
- Add `relational-persistence` and `containerized-deployment` only when the
  service owns those concerns.
