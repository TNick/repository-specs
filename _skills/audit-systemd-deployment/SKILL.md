---
name: audit-systemd-deployment
description: >-
  Use when reviewing committed or live systemd service deployment practices,
  including unit design, secrets, privileges, hardening, rollout, health
  checks, release identity, rollback, and operator documentation.
---

# Audit a systemd deployment

Audit the repository against its tag-pinned `systemd-deployment` capability.
Diagnose and document gaps; do not change units or operate on live services
unless the user separately requests and authorizes remediation.

## Evidence to collect

Read root instructions, design records, unit files, drop-ins, environment-file
examples, installers, deployment scripts, Makefile commands, health checks,
rollback code, tests, and operator documentation.

When live inspection is authorized, use read-only commands with the correct
manager scope. Record unit content and drop-ins, enabled and active state,
runtime identity, dependencies, recent failure logs, current release identity,
and relevant security analysis. Do not run daemon-reload, enable, disable,
start, stop, restart, or deploy during an audit.

## Audit areas

Classify each requirement as pass, partial, missing, not applicable, or not
verified:

- complete unit and host-role inventory;
- explicit system or user manager scope;
- reproducible authored units and safe environment examples;
- secrets and operator configuration outside release artifacts;
- correct dependencies, lifecycle behavior, and restart limits;
- least-privilege runtime identity and justified hardening;
- documented writable paths, listeners, logs, and capabilities;
- idempotent installation and update;
- immutable or locked release input and observable deployed revision;
- staged or otherwise recoverable activation;
- bounded behavioral health verification;
- retained previous release and tested rollback;
- safe operator commands that preserve persistent data;
- offline `systemd-analyze verify` and script checks; and
- failure-path tests and operator documentation.

Distinguish absent evidence from a confirmed failure. A process being active
does not prove that the expected revision is healthy. A hardened-looking unit
does not prove least privilege if required access was never inventoried.

## Report

Write findings in the repository's declared design location. Give every
non-pass finding its file or command evidence, operational impact, and a
testable acceptance condition. Separate repository gaps from live-host drift,
and clearly label any live property that was not authorized or possible to
verify.
