---
name: adopt-multilingual-web
description: >-
  Use when adding the repository-specs multilingual web capability to an
  existing frontend/backend application, including catalogs, locale routing,
  backend file delivery, localized content, API errors, and locale tests.
---

# Adopt multilingual web support

Apply the tag-pinned `multilingual-web-application` specification without
discarding sound locale work already present in the consuming repository.

## Before editing

1. Read the root `AGENTS.md`, design records, selected specification, and its
   complete `spec.toml` inheritance graph.
2. Inventory frontend message libraries, locale state, routes, catalogs,
   backend content models, generated artifacts, HTTP headers, SEO metadata,
   tests, and build commands.
3. Record the source, default, published, and draft locales. Identify every
   duplicated locale list.
4. Create or update an accepted gap review and derived implementation plan.
   Keep unrelated application changes out of the adoption work.

## Architecture decisions

Preserve an existing ICU-capable engine. For React without one, prefer
FormatJS and `react-intl`. Do not build a new interpolation engine.

Keep three boundaries explicit:

- UI messages use stable namespaced catalog identifiers.
- Domain content uses stable entity identities and localized variants.
- Protocol errors use machine codes and structured parameters.

Use one `i18n/config.json` locale authority. Package-owned bundles may remain
distributed in source, but one build must validate and merge the backend-served
runtime catalogs.

## Implementation order

1. Establish locale configuration and canonical BCP 47 identifiers.
2. Establish ICU-capable source catalogs and validation.
3. Merge package bundles and reject duplicate identifiers.
4. Add the revisioned backend manifest and catalog-file contract.
5. Implement locale precedence and persistence.
6. Separate localized content identity from translated routes and slugs.
7. Replace localized API prose contracts with codes and parameters.
8. Carry explicit locale values into generated documents and queued jobs.
9. Set HTML language, direction, canonical links, and alternate metadata.
10. Add unit, integration, and per-locale browser tests.

Each slice must preserve working behavior. Avoid a repository-wide string
rewrite in one commit when features can migrate by namespace.

## Verification

Run catalog generation twice and confirm the second run produces no diff.
Exercise the backend manifest and one catalog for every published locale.
Verify cache headers, invalid path rejection, locale fallback, language
switching, stable page identity, ICU plurals, and one critical browser flow per
locale.

Report migrated namespaces, retained legacy paths, commands run, design
records updated, and remaining gaps.
