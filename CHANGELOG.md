# Changelog

## [Unreleased]

## [1.2.0] - 2026-09-04

### Added

- `qwc-map-spa` capability for QWC2 (or equivalent) custom map viewers with
  read-only vendor trees and application-owned overrides (webpack allowed).
- `playwright-browser-e2e` capability for dedicated Playwright regression
  trees and lab-database isolation.
- `install-kit-deployment` capability extending `systemd-deployment` for
  versioned install kits, artifact split, and forge variable/secret docs.
- `external-schema-persistence` capability extending
  `relational-persistence` when schema and migrations live outside the app
  repository.
- `python-typescript-map-app` profile composing the map SPA, Compose lab,
  external schema, Playwright, and install-kit capabilities as an
  alternative to `python-typescript-app` for QWC/webpack products.

### Changed

- `systemd-deployment` layout examples now include install-kit trees under
  `deploy/` in addition to `deploy/systemd/`.

## [1.1.0] - 2026-08-30

### Added

- Browser-extension profile for shared, least-privilege WebExtension
  projects.
- Opt-in `systemd-deployment` capability with adoption and audit skills.
- Opt-in `multilingual-web-application` capability.

## [1.0.0] - 2026-08-29

### Added

- Initial composable repository specification catalog.
