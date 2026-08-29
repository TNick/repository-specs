---
name: adopt-systemd-deployment
description: >-
  Use when bringing an existing Linux system or user service under the
  repository-specs systemd deployment capability, including units,
  environment files, rollout, health checks, hardening, and rollback.
---

# Adopt a systemd deployment

Apply the tag-pinned `systemd-deployment` capability without interrupting a
working service or replacing operator-owned configuration.

## Before editing

1. Read root instructions, design records, the selected specification, and its
   complete `spec.toml` inheritance graph.
2. Inventory committed units, installers, service scope, runtime identity,
   dependencies, environment files, writable paths, listeners, logs, health
   checks, release markers, and rollback behavior.
3. If live inspection is authorized, collect read-only evidence with the
   correct system or user manager. Do not restart, reload, enable, or modify a
   service during discovery.
4. Create or update an accepted gap review and a derived rollout plan. Record
   the current known-good revision and exact rollback path.

## Implementation order

1. Establish a documented service and host-role inventory.
2. Put authored units and safe examples under `deploy/systemd/` or the
   repository's established deployment directory.
3. Separate secrets and operator-owned configuration from release artifacts.
4. Add offline unit validation and tests for rendering or installation.
5. Make install and update operations idempotent.
6. Expose explicit status, logs, health, deploy, and rollback commands.
7. Add observable release identity and a bounded behavioral health check.
8. Stage releases and retain the previous known-good version.
9. Add compatible hardening based on required access, documenting exceptions.
10. Exercise failed activation and rollback in a non-production environment.

Do not copy hardening directives without checking filesystem, device,
namespace, capability, and network requirements. Do not convert a user service
to a system service, or the reverse, without an accepted design decision.

## Live rollout

Operate on a live host only when the user has authorized deployment. Confirm
the target host, manager scope, service, and current revision. Validate and
stage before activation, reload only after unit changes, then verify expected
revision, active state, and useful behavior. Stop on failure and preserve logs.

## Report

Report service scope, assets added or changed, configuration ownership,
hardening decisions, commands run, deployed revision, health result, rollback
result or readiness, design records updated, and remaining gaps.
