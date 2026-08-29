# HTTP Service

Use this building block for a deployable HTTP API or daemon.

## Required

- Document the service entry point, listen address, health check, and
  configuration variables.
- Keep transport handlers thin; validation and business rules belong in
  testable service or domain modules.
- Provide deterministic unit tests and an integration smoke test.
- Define an explicit error response contract and structured logging policy.
- Make startup fail clearly when required production configuration is absent.
