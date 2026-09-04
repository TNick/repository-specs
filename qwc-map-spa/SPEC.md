# QWC Map SPA

Use this capability when the browser application is a QWC2 (or equivalent)
custom map viewer with a read-only vendor tree and application-owned
overrides, rather than a Vite-first SPA under `react-vite-ui`.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## Scope and boundaries

This capability governs the map SPA layout, vendor boundary, bundler choice,
override style, and automation hooks. It does **not** require Vite.

Repositories that need a conventional React+Vite application MUST adopt
`react-vite-ui` / `typescript-web-application` / `python-typescript-app`
instead of this capability.

## Vendor tree

- The QWC2 (or equivalent) vendor sources MUST live in a clearly named
  directory such as `frontend/qwc2/`.
- The vendor tree MUST be treated as read-only for day-to-day development.
  Prefer a git submodule or another pinned vendor checkout.
- Application customizations MUST NOT be edited inside the vendor tree.
- Customizations MUST live under an application-owned overrides directory
  that mirrors the upstream relative paths (for example
  `frontend/qwc-overrides/components/…`).

## Bundler and entry

- The application MUST document its production bundler. Webpack is allowed.
- Vite MAY be used for unit tests or secondary tooling without becoming the
  production bundler.
- The custom viewer entry, webpack (or equivalent) config, static assets,
  icons, and theme/config JSON MUST live under the frontend application
  tree and MUST be documented in the frontend `README` or `AGENTS.md`.
- Development API calls SHOULD use relative `/api` paths with a documented
  reverse-proxy or webpack-dev-server proxy rather than hardcoded backend
  hostnames.

## Map shell

- The authenticated map route SHOULD present the QWC (or equivalent) chrome
  as the primary top-level UI for that surface.
- A separate host-application top bar above the map SHOULD NOT be retained
  unless a design record documents why it is required.
- Customer actions that belong on the map SHOULD integrate through
  application-owned menu, toolbar, or panel overrides.

## Overrides and TypeScript style

- Override modules MUST follow the same TypeScript documentation and style
  rules as application TypeScript (`typescript-base`), including JSDoc on
  types, functions, and components.
- New or heavily edited overrides SHOULD use TypeScript (`.tsx` / `.ts`).
- Upstream license headers MUST be preserved when present. Application fork
  headers SHOULD state the upstream path and why the override exists.

## Automation hooks

- Interactive map controls that agents or browser tests must target SHOULD
  expose stable selectors (for example `#qwc-*` ids or documented
  `data-*` attributes).
- Selector conventions MUST be documented in a playbook or design record so
  end-to-end tests do not depend on brittle CSS class churn.

## Tests

- Component and hook unit tests MAY use Vitest and Testing Library.
- Browser automation for the map shell MUST live in a separate end-to-end
  tree. Prefer adopting `playwright-browser-e2e` when Playwright is the
  chosen runner.
