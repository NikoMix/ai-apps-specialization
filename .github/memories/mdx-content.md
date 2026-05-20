# MDX content authoring rules

**Scope:** `src/content/docs/**/*.mdx`

This repository's documentation pages follow a **strict template** for control pages so that the Engagement Agent and the auto-generated GitHub Issues stay synchronised. Follow these rules whenever editing or creating MDX files.

## Control page template (Module A / Module B)

Every file in `src/content/docs/module-a/` and `src/content/docs/module-b/` must follow this exact structure:

```mdx
---
title: "<MODULE>.<SECTION>.<ITEM> – <Short Title>"
description: <One-sentence summary used by Starlight + search engines>
sidebar:
  label: "<SECTION>.<ITEM> <Short Title>"
  order: <integer>
---

import { Aside } from '@astrojs/starlight/components';

## What the Auditor Checks

<Short prose paragraph>

**Typical questions:**
- <Q1>
- <Q2>
- <Q3>

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **<Item name>** | PDF, Word, Excel | ⬜ |
| ... |

<Aside type="tip">
  <Optional shortcut or pro tip>
</Aside>

---

## Evidence Guidance

### <Item 1 name>
<How to produce / collect it>

### <Item 2 name>
...

---

## Evidence Status

| Item | Owner | Status | Last Updated | Notes |
|---|---|---|---|---|
| <Item 1> | | ⬜ Not started | | |

---

## Common Gaps

- **<Gap>:** <Why it fails the audit and how to prevent it>
```

## Status icons (mandatory)

Use only these three icons in the `Status` column:

| Icon | Meaning |
|---|---|
| `⬜` | Not started |
| `🟡` | In progress |
| `✅` | Complete |

## Cross-references

- Control numbers in prose always use dots: `A.2.1`, `B.3.1`. Never `A2.1` or just `2.1`.
- Cross-link controls with relative paths: `[A.2.1](/module-a/2.1-service-delivery-methodology/)`
- Never link to GitHub Issues by hard-coded number — they vary per fork.

## When evidence requirements change

If you add, remove, or reword an evidence item in a control page, you **must** make the matching edit to `.github/scripts/create-issues.sh` so the auto-created issue checkboxes stay aligned. The doc and the issue are a single source of truth in two forms.

## Starlight components allowed

Currently in use and safe to import:

```mdx
import { Aside, Steps, Card, CardGrid, Tabs, TabItem } from '@astrojs/starlight/components';
```

Do not introduce React components, MDX expressions that fetch data at build time, or third-party widgets without explicit need — partners may build this on locked-down CI runners.
