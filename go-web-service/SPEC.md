# Go Web Service

Use this profile for a Go HTTP service, including a repository with an
embedded browser UI.

## Required

- Keep the Go binary, configuration, handlers, and domain logic separately
  testable.
- Document API compatibility, listen configuration, and model or process
  lifecycle behavior.
- Run Go quality gates and UI quality gates independently.
- Keep the UI build reproducible and make its handoff to the Go service
  explicit.
