# Python Library

Use this profile for a reusable, installable Python distribution whose public
API is the primary product.

## Required

- Keep importable package code separate from tests and development scripts.
- Declare the supported Python range, public exports, optional extras, and
  package data in `pyproject.toml`.
- Provide a minimal install-and-use example in the README.
- Test the public API and build the distribution in CI.
- Keep format-specific adapters independent from shared canonical models when
  the repository is part of an interoperability stack.
