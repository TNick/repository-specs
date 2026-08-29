# Schema-Driven Polyglot Workspace

Use this profile when multiple language implementations must obey one shared
data format, protocol, or execution contract.

## Required

- Keep schemas or protocol definitions in a language-neutral source directory.
- Generate or derive language types from that source where practical.
- Maintain golden fixtures and conformance tests for every runtime.
- Document compatibility and versioning rules for schema changes.
- Keep language-specific adapters behind the same semantic contract.

This is distinct from a Python backend plus TypeScript frontend: the runtimes
here implement overlapping contract semantics rather than separate tiers.
