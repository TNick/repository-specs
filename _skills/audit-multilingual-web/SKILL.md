---
name: audit-multilingual-web
description: >-
  Use when reviewing a web application for multilingual readiness or
  compliance, including ICU messages, catalog delivery, locale negotiation,
  localized content identity, headers, SEO, accessibility, and test coverage.
---

# Audit multilingual web support

Audit the consuming repository against its tag-pinned
`multilingual-web-application` specification. Diagnose and document gaps; do
not modify application code unless the user requests remediation.

## Evidence to collect

Read the root instructions, design records, locale configuration, frontend and
backend manifests, catalog sources, generators, route definitions, content
schemas, error responses, document jobs, HTML metadata, and test commands.

Trace one message and one localized content page through their full paths:

```text
message source -> merged catalog -> backend response -> frontend render
content identity -> locale selection -> API response -> localized route
```

Inspect every published locale. Sampling only the default locale cannot prove
catalog completeness or fallback behavior.

## Audit areas

Classify each requirement as pass, partial, missing, or not applicable:

- one authoritative BCP 47 locale configuration;
- ICU-capable messages and translator context;
- duplicate, syntax, coverage, and parameter-parity checks;
- revisioned backend manifest and catalog files;
- allowlisted locale and namespace paths;
- cache, `Content-Language`, and `Vary` headers;
- explicit locale precedence and persistence;
- stable content identities independent of slugs;
- machine-readable API errors;
- explicit locale on generated artifacts and queued jobs;
- HTML `lang`, `dir`, canonical, and `hreflang` metadata;
- locale-aware formatting and collation; and
- unit, integration, pseudolocale, and per-locale browser coverage.

Search for hardcoded user-facing strings, concatenated sentences, manual date
or number formatting, language-specific database columns, translated protocol
values, unchecked catalog paths, and duplicate locale lists.

## Report

Write the findings in the repository's declared design location. Give each
non-pass finding a path or command as evidence, the user impact, and a testable
acceptance condition. Separate catalog migration from localized-content and
route migration so the owner can schedule bounded plans.

Do not claim support for a locale that appears in configuration but fails
catalog, backend delivery, or critical browser-flow checks.
