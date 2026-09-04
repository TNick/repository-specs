# Install Kit Deployment

Use this capability when production rollout is delivered through versioned
install kits, host bootstrap scripts, and CI/CD forge automation onto Linux
hosts that run systemd units — including LXC or similar application hosts
behind an external reverse proxy and database.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

This capability extends `systemd-deployment`. Inherited unit inventory,
hardening, health, rollback, and operator-command requirements remain in
force. Docker Compose lab concerns belong in `containerized-deployment` and
MUST NOT be restated here.

## Scope and boundaries

- This capability covers install kits, release artifacts, forge pipeline
  documentation, and host-role separation.
- Managing application LXC (or similar) hosts does **not** by itself select
  `containerized-deployment`.
- Private hostnames, addresses, and operator inventory MUST live in project
  configuration or private design records.

## Install kits

- Production install assets MUST live under a clearly named deployment
  directory such as `deploy/`.
- Each owned service SHOULD ship as a versioned install kit containing:
  - bootstrap and upgrade scripts;
  - committed systemd unit templates;
  - a safe-to-commit environment example listing every supported setting;
  - an operator `ReadMe.md` with prerequisites and procedures; and
  - optional interactive helper menus for diagnostics and service control.
- When backend, frontend SPA, worker, or cache components roll out
  separately, the repository SHOULD provide separate kits or clearly named
  kit sections for each.
- Generated scripts MUST begin with usage text and SHOULD use short commented
  blocks that explain each logical step.

## Artifacts and host roles

- A release SHOULD publish the backend package and the frontend static web
  app as separate artifacts when those surfaces update independently.
- Application hosts SHOULD NOT run the shared reverse proxy or the shared
  database locally when those services are external shared infrastructure.
- Host roles (application, reverse proxy, database, worker, cache) MUST be
  documented so operators know which kit applies where.
- Heavy-traffic scale-out that adds application hosts MUST document how
  shared secrets and writable runtime storage stay aligned across instances.

## CI/CD forge documentation

- Forge configuration (Forgejo, Gitea, GitHub Actions, or equivalent) MUST be
  documented with explicit variable and secret names.
- Each value MUST be classified as a non-secret variable or a secret.
- Non-secret package indexes and public URLs MUST NOT be stored as secrets
  when a variable slot exists.
- Pipeline documentation MUST describe full, backend-only, and frontend-only
  rollout modes when the project supports them.
- Live deployment MUST remain an explicitly named command or workflow. It
  MUST NOT run as part of ordinary unit tests.

## Relationship to lab containers

- A repository MAY also adopt `containerized-deployment` for local Compose
  labs and image builds.
- Install-kit production rollout and Compose lab simulation MUST be
  documented as distinct operator paths so agents do not confuse them.
