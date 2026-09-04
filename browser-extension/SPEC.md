# Browser Extension

Use this profile for browser extensions built on the WebExtensions platform.

## Required

- Keep shared behavior in one source tree when targeting multiple browsers.
  Generate a distinct, unpacked artifact for every supported browser.
- Keep browser-specific manifests and compatibility settings explicit. Manifest
  versions MUST match the repository's release version.
- Request only the permissions and URL matches needed by the current features.
  A new permission MUST include a documented user-facing rationale.
- Do not load remote executable code. Commit source code and deterministic build
  inputs, and exclude generated extension artifacts from version control.
- Make page modifications idempotent and resilient to relevant DOM content that
  appears after the initial document load.
- Preserve the host page's content and core behavior. Prefer reversible UI
  changes and collision-resistant class, attribute, and event names.
- Treat accessibility, keyboard operation, focus management, narrow viewports,
  and touch targets as release requirements for injected user interfaces.
- Test shared behavior in a real browser DOM. Validate every target manifest and
  smoke-test every supported browser before release.
- Document unpacked installation, build and test commands, supported browser
  versions, URL scope, permissions, and browser-specific release steps.

## Recommended structure

Keep shared content scripts and styles under `src/`, browser-specific manifests
under `manifests/<browser>/`, and generated unpacked extensions under
`dist/<browser>/`. Projects with an established equivalent layout may retain it.

## Release guidance

Use one product version across browser artifacts. Package and publish from the
same tested source revision, while allowing browser stores to use their own
signing and review processes.
