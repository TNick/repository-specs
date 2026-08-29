# Go Base

Go repositories use a module at the root and the standard Go toolchain.

## Required

- Commit `go.mod` and `go.sum` where dependencies exist.
- Run `gofmt`, `go vet`, and the complete Go test suite in CI.
- Keep command entry points under `cmd/` when more than one binary exists.
- Separate configuration, transport, and domain logic so the service can be
  tested without external processes.
