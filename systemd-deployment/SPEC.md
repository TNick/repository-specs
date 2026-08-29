# Systemd Deployment

Use this opt-in capability when a repository owns one or more systemd system
or user services and the automation that installs or updates them on Linux
hosts.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## Scope and boundaries

This capability governs committed unit files, service configuration
boundaries, rollout, rollback, health verification, and operator commands. It
does not imply that the application runs in a container.

A repository that also builds container images MAY independently adopt
`containerized-deployment`. Managing LXC or other hosts does not by itself
select that Docker-and-Compose-oriented capability.

## Service inventory

- The repository MUST document every owned unit, its purpose, service manager
  scope (`system` or `user`), runtime identity, host role, and dependencies.
- The repository MUST document whether each unit is enabled, static,
  socket-activated, timer-activated, or started by another unit.
- User services MUST document login-session and lingering requirements.
- Hostnames, addresses, usernames, and paths specific to a private environment
  MUST live in project configuration or private design records, not in a
  reusable public specification.

## Repository layout

- Authored units and related assets MUST live under a clearly named deployment
  directory such as `deploy/systemd/`.
- Example environment files MUST be safe to commit and MUST list every
  supported setting without real credentials.
- Generated units MUST identify their source and regeneration command.
- Installed units MUST NOT be edited in place as the source of truth. Local
  operator overrides SHOULD use systemd drop-ins.

## Unit design

- `ExecStart`, `ExecReload`, and lifecycle commands MUST use explicit absolute
  executable paths in installed units.
- Shell operators and pipelines MUST NOT be placed directly in `ExecStart`.
  Complex behavior belongs in a versioned, tested executable or script.
- `User`, `Group`, `WorkingDirectory`, restart policy, stop timeout, and signal
  behavior MUST be explicit when applicable.
- Ordering and requirement dependencies MUST describe actual dependencies.
  A network client SHOULD use `network-online.target` only when startup truly
  requires configured networking.
- Long-running services MUST define predictable restart behavior and MUST NOT
  use an unbounded rapid restart loop.
- Application state, cache, logs, and runtime files MUST have documented
  locations and ownership. Prefer systemd directory directives such as
  `StateDirectory`, `CacheDirectory`, `LogsDirectory`, and `RuntimeDirectory`
  where they fit the service.
- Services SHOULD log to stdout and stderr for journald unless the application
  has a documented file-retention requirement.

## Configuration and secrets

- Runtime configuration MUST be supplied through environment files,
  credentials, or mounted configuration outside the release artifact.
- Secrets MUST NOT appear in source control, command-line arguments, unit
  files, journal messages, or deployment output.
- Units MAY reference `EnvironmentFile`, but the repository MUST document who
  creates it, its required permissions, and behavior when it is missing.
- Non-secret defaults MAY be committed in an example environment file.
- A deployment MUST preserve existing operator-owned configuration unless an
  explicit migration says otherwise.

## Security posture

- Each service MUST run with the least privilege required for its purpose.
- Network listeners, writable paths, device access, capabilities, namespaces,
  and host-control permissions MUST be documented.
- Units SHOULD enable compatible hardening such as `NoNewPrivileges`,
  `PrivateTmp`, `ProtectSystem`, `ProtectHome`, capability restrictions, and
  system-call or namespace restrictions.
- Hardening MUST be selected from evidence. A directive MUST NOT be copied
  blindly when it breaks required access.
- Every omitted or weakened high-value control MUST have a concise rationale
  in a design record or adjacent unit documentation.
- Deployment automation MUST NOT disable host firewalls, mandatory access
  controls, or unrelated services as a workaround.

## Installation and updates

- Install and update commands MUST be idempotent and safe to rerun after an
  interrupted attempt.
- Deployment MUST use a committed lockfile or immutable artifact identity.
- The deployed revision MUST be observable through a release marker, version
  endpoint, package version, or equivalent mechanism.
- A release SHOULD be staged in a versioned location and activated atomically.
  In-place replacement is allowed only when documented and recoverable.
- Automation MUST run `systemctl daemon-reload` after unit changes and MUST
  use the correct manager scope for system or user units.
- Enabling a unit and starting or restarting it MUST be separate, intentional
  steps in the deployment model.
- A documentation-only or validation command MUST NOT restart a live service.
- Remote deployment MUST target an allowlisted host and service inventory. It
  MUST NOT infer destructive targets from broad globs or unvalidated input.

## Health checks and rollback

- Every deployable service MUST have a bounded smoke or health check that
  tests useful behavior, not only process existence.
- Deployment success MUST require the expected revision, active unit state,
  and passing health check.
- Failed activation or health verification MUST stop the rollout and preserve
  diagnostic output.
- The previous known-good artifact and unit configuration MUST remain
  available until the deployment is verified.
- The repository MUST provide and test a documented rollback path. Rollback
  MUST restore the previous release, reload units when necessary, restart the
  affected service, and repeat health verification.
- Persistent data MUST NOT be deleted by deploy, stop, uninstall, or rollback
  commands unless a separately named destructive operation is explicitly
  requested.

## Operator interface

The root Makefile or documented equivalent MUST expose safe commands for:

- validating deployment assets;
- installing or updating the service;
- starting, stopping, restarting, and reporting status;
- reading recent logs;
- running the health check; and
- rolling back to the previous known-good release.

Commands MUST make their target host, manager scope, and service name clear.
Stop and rollback commands MUST preserve persistent data by default.

## Validation and tests

- Authored unit files MUST pass `systemd-analyze verify` on a compatible Linux
  environment before deployment.
- Scripts MUST pass their language-specific lint and test tools. Shell scripts
  SHOULD pass ShellCheck.
- Tests MUST cover unit rendering or installation, configuration preservation,
  idempotent reruns, failed health checks, and rollback selection.
- CI SHOULD validate units in a Linux job matching the oldest supported
  systemd version.
- A live deployment check MUST NOT be part of an ordinary unit-test command.
  Live operations require an explicitly named deployment command and the
  repository's authorization policy.

## Documentation

The README or deployment guide MUST explain prerequisites, supported Linux and
systemd versions, install and upgrade procedures, configuration ownership,
normal operator commands, log locations, health verification, rollback, and
uninstallation behavior.

Design records MUST state why system or user scope was selected, describe the
security boundary, and identify any deliberate exception to this capability.

## Existing-service adoption

Agents onboarding an existing service MUST first perform read-only inspection
of committed assets and, when authorized, the live unit and its drop-ins. They
MUST record the current release, configuration ownership, runtime identity,
dependencies, writable paths, hardening, health behavior, and rollback method.

Adoption SHOULD proceed in this order:

1. document inventory and ownership;
2. establish offline unit validation;
3. separate secrets and operator configuration from artifacts;
4. make installation and update idempotent;
5. expose operator and health commands;
6. add observable release identity;
7. establish staged activation and rollback;
8. apply compatible hardening; and
9. test failure and recovery paths.

Existing behavior MUST be preserved unless an accepted design record
explicitly authorizes a change.
