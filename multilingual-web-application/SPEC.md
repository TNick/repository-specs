# Multilingual Web Application

Use this opt-in capability when a web application presents its interface or
content in more than one language and its backend serves runtime translation
catalogs.

This specification does not belong in a language base or application profile.
A consuming repository must reference it explicitly.

The words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are normative.

## Locale authority

The repository MUST keep one authoritative locale declaration at:

```text
i18n/config.json
```

It MUST declare:

- the source locale;
- the default locale;
- every published locale;
- each locale's native display name and text direction; and
- the runtime catalog namespaces.

For example:

```json
{
  "sourceLocale": "ro",
  "defaultLocale": "ro",
  "supportedLocales": [
    { "id": "ro", "name": "Română", "direction": "ltr" },
    { "id": "en", "name": "English", "direction": "ltr" }
  ],
  "namespaces": ["common", "application"]
}
```

Locale identifiers MUST use canonical BCP 47 language tags. Code and
configuration MUST NOT maintain separate, conflicting locale lists.

## Message catalogs

Application messages MUST use stable, namespaced identifiers such as:

```text
common.actions.save
auth.errors.invalidCredentials
survey.validation.missingCoordinates
```

The message system MUST support ICU MessageFormat semantics for:

- parameters;
- plural and ordinal selection;
- grammatical selection; and
- locale-aware numbers, dates, times, percentages, and currencies.

For React applications, FormatJS and `react-intl` SHOULD provide message
evaluation, extraction, and formatting. Another implementation MAY be used
when it supports the same message semantics and validation.

Code MUST NOT build sentences by concatenating translated fragments. A
message SHOULD contain the complete sentence so translators can change word
order and grammar.

Catalog entries SHOULD include translator context when the identifier and
source message do not make their use clear.

Catalog parameters MUST remain data. Implementations MUST escape untrusted
values and MUST NOT allow catalog content to inject arbitrary HTML. Rich text
MAY use an explicit, allowlisted component mapping.

## Catalog composition and generation

Applications and reusable packages MAY own partial translation bundles. The
application MUST merge them into complete runtime catalogs.

A typical source tree is:

```text
i18n/
├── config.json
├── source/
│   ├── common/
│   │   ├── ro.json
│   │   └── en.json
│   └── application/
│       ├── ro.json
│       └── en.json
└── generated/
```

The repository MAY use typed source modules instead of source JSON. It MUST
identify generated files and their regeneration command. Agents MUST edit the
source messages or generator rather than generated catalogs.

Catalog validation MUST fail for:

- duplicate message identifiers;
- invalid ICU syntax;
- missing messages in a published locale;
- different parameter names between locale variants;
- unsupported or malformed locale identifiers; and
- generated output that differs from committed output.

Draft locales MAY be incomplete, but the application MUST NOT publish them as
supported locales.

## Backend catalog delivery

The backend MUST serve the frontend's runtime catalogs. A reverse proxy or CDN
MAY cache those backend-owned resources.

The delivery contract SHOULD use:

```text
GET /i18n/manifest.json
GET /i18n/{revision}/{locale}/{namespace}.json
```

The manifest MUST declare the schema version, catalog revision, default
locale, supported locales, text directions, and namespaces.

For example:

```json
{
  "schemaVersion": 1,
  "revision": "sha256-7c91...",
  "defaultLocale": "ro",
  "locales": [
    { "id": "ro", "direction": "ltr" },
    { "id": "en", "direction": "ltr" }
  ],
  "namespaces": ["common", "application"]
}
```

The revision MUST change when any served catalog changes. Revisioned catalog
responses SHOULD use:

```http
Content-Type: application/json; charset=utf-8
Content-Language: ro
Cache-Control: public, max-age=31536000, immutable
```

The manifest SHOULD use an ETag and revalidation or a short cache lifetime.

The backend MUST validate locale and namespace values against the configured
allowlists. It MUST NOT map unchecked URL segments to filesystem paths.

An application MAY preload the default shell catalog to avoid an empty first
render. The backend-served files remain the runtime catalog authority.

## Locale selection

Applications MUST use this precedence order:

1. locale in an explicit URL or request parameter;
2. authenticated user preference;
3. a stored explicit browser choice;
4. `Accept-Language` during initial negotiation; and
5. the configured default locale.

An explicit user choice MUST NOT be replaced by browser negotiation.

Responses negotiated through `Accept-Language` MUST include:

```http
Vary: Accept-Language
Content-Language: ro
```

Explicit locale URLs SHOULD be preferred for catalogs and public content
because they produce stable links and simpler cache keys.

Locale does not determine timezone, currency, measurement system, or every
regional preference. Applications MUST model those settings separately when
they affect behavior.

## Localized application content

UI messages and localized domain content MUST use separate models.

Content entities MUST have stable identifiers that do not depend on a locale,
translated title, or translated slug. A content response SHOULD expose the
stable identifier, actual locale, localized route, and alternate routes.

For example:

```json
{
  "pageKey": "contact",
  "locale": "en",
  "slug": "contact",
  "title": "Contact",
  "alternateRoutes": {
    "ro": "/ro/contact",
    "en": "/en/contact"
  }
}
```

Public, indexable content MUST have locale-specific URLs. Switching locale
SHOULD preserve the current content identity when an alternate exists.

Localized backend responses MUST send `Content-Language` for the locale that
the backend served. If the backend falls back, it MUST report the fallback
locale rather than the requested locale.

Authoring or administration APIs MAY return language maps. Read APIs SHOULD
return one negotiated or requested locale unless the consumer needs all
translations.

## API errors and backend artifacts

Normal API errors MUST expose a stable code and structured parameters:

```json
{
  "code": "survey.points.tooFew",
  "params": {
    "minimum": 3,
    "actual": 2
  }
}
```

Frontend applications MUST translate the code. Localized prose MUST NOT be the
only error contract.

Backend-generated human artifacts, including emails, reports, spreadsheets,
PDF files, and job results, MUST accept an explicit locale. Asynchronous jobs
MUST store that locale in their durable job input so workers use the requested
language.

Logs, identifiers, metrics, and protocol fields MUST remain stable and MUST
NOT depend on translated text.

## HTML, accessibility, and direction

The application MUST set the document `lang` attribute to the active locale
and the document `dir` attribute from the locale configuration.

Content fragments in another language MUST declare their own `lang` value.

Language selectors MUST:

- use each language's native name;
- expose an accessible name and selected state;
- remain usable with a keyboard; and
- avoid flags as the sole language indicator.

Layouts SHOULD tolerate longer translations. Components MUST NOT depend on
fixed text widths that work only for the source language.

## Public metadata

Each indexable localized page MUST provide:

- a localized title and description;
- its canonical URL;
- a self-referencing `hreflang` entry;
- reciprocal `hreflang` entries for available translations; and
- `hreflang="x-default"` when a language-neutral entry page exists.

The sitemap or response metadata MUST keep alternate-language relationships
consistent with the page markup.

## Formatting and collation

Frontend code SHOULD use the platform `Intl` APIs or an ICU-based wrapper for
numbers, dates, times, currencies, lists, display names, relative times,
plural rules, and collation.

Code MUST NOT implement locale formatting with manual separators, translated
format strings, or language-specific conditionals scattered through features.

Backend formatting for generated artifacts MUST use an equivalent
locale-aware library.

## Testing and enforcement

The repository's read-only lint command MUST validate source catalogs, ICU
syntax, locale coverage, parameter parity, duplicate identifiers, and
generated catalog freshness.

The normal test command MUST cover:

- locale selection and fallback;
- catalog manifest and file loading;
- plural, selection, and locale formatting behavior;
- language switching that preserves content identity;
- document `lang` and `dir` updates;
- backend `Content-Language`, cache, and `Vary` headers;
- invalid locale and namespace rejection;
- machine-readable API error translation; and
- at least one critical browser flow in each published locale.

Projects SHOULD provide a development pseudolocale that expands text and
marks translated boundaries. It MUST NOT appear in the production locale
manifest.

## Documentation

The root README or design records MUST document:

- source, default, published, and draft locales;
- how to add a locale or namespace;
- how to extract, merge, validate, and regenerate catalogs;
- the backend catalog URLs and cache policy;
- locale selection and fallback behavior;
- localized content storage and route identity; and
- how translators obtain context and verify changes.

## Definition of done

Multilingual work is complete only when:

- every published locale passes catalog validation;
- runtime catalogs load from the backend;
- explicit locale choices persist and take precedence;
- content and API contracts retain stable machine identifiers;
- locale-aware formatting replaces manual formatting;
- HTML language, direction, and public metadata are correct;
- backend-generated artifacts honor their requested locale; and
- unit, integration, and browser locale tests pass.

## References

- [W3C language declarations](https://www.w3.org/International/docs/bp-html-lang/)
- [W3C language tags](https://www.w3.org/International/articles/language-tags/)
- [Unicode ICU message formatting](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
- [Google localized page metadata](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [MDN `Accept-Language`](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/Accept-Language)
- [MDN `Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl)
