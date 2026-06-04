# MDX content authoring rules

**Scope:** `src/content/docs/**/*.mdx`

This repository's documentation pages follow a **strict template** for control pages so that the Engagement Agent and the auto-generated GitHub Issues stay synchronised. Follow these rules whenever editing or creating MDX files.

## ⚠️ MDX syntax gotchas

MDX 3 (Astro 5 / Starlight) parses `<` followed by a letter, digit, or space as the start of a JSX tag. This breaks the build with `Unexpected character '...' before name`.

**Always escape these patterns:**

| ❌ Wrong | ✅ Right |
|---|---|
| `target <2 business days` | `target &lt; 2 business days` |
| `latency <100ms` | `latency &lt; 100ms` |
| `<6 months coverage` | `&lt; 6 months coverage` |
| `if x < 5 then` (in prose) | `if x &lt; 5 then` |
| `&` standalone in prose | `&amp;` |

Inside fenced code blocks (` ``` `) characters are NOT parsed as MDX — so you don't need to escape there.

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
- Cross-link controls with **relative** paths (Astro doesn't auto-prefix base on absolute markdown links): from a docs page at depth 1 like `src/content/docs/audit-process.mdx`, link to `../module-a/2-1-service-delivery-methodology/` (not `/module-a/...`).
- **Filenames must NOT contain dots** — Starlight strips them from URL slugs. Use `2-1-foo.mdx` (slug `/module-a/2-1-foo/`) not `2.1-foo.mdx` (which becomes `/module-a/21-foo/`).
- Never link to GitHub Issues by hard-coded number — they vary per fork.

## When evidence requirements change

If you add, remove, or reword an evidence item in a control page, you **must** make the matching edit to `.github/scripts/create-issues.sh` so the auto-created issue checkboxes stay aligned. The doc and the issue are a single source of truth in two forms.

## Starlight components allowed

Currently in use and safe to import:

```mdx
import { Aside, Steps, Card, CardGrid, Tabs, TabItem } from '@astrojs/starlight/components';
```

Do not introduce React components, MDX expressions that fetch data at build time, or third-party widgets without explicit need — partners may build this on locked-down CI runners.


## Engagement playbook page template

Every page in `src/content/docs/engagement/**` and `src/content/docs/innersource/**` follows this structure. It is intentionally different from the Module A / B control template because the audience and purpose are different — these pages instruct a consultant *how to run a step*, not *what evidence the auditor wants*.

```mdx
---
title: "<Section> – <Title>"
description: <One-sentence summary>
sidebar:
  label: "<Short label>"
  order: <integer>
---

import { Aside, Steps, Tabs, TabItem } from '@astrojs/starlight/components';

## When to use this

<Short paragraph — which engagement phase, which customer signal triggers this page>

## Inputs you need from the customer

| # | Input | Source | Format |
|---|---|---|---|
| 1 | <Input>  | <Where it comes from> | <Document / Spreadsheet / Diagram / Boolean / etc.> |

## Step-by-step

<Steps>

1. **<Step title>** — <action>.

</Steps>

## Output: customer-ready deliverable

<What the consultant hands to the customer at the end of this step. If there is a downloadable workfile, link it with an Aside:>

<Aside type="tip" title="Download the workfile">
[📄 <Workfile name> (.docx|.pptx|.xlsx)](pathname:///templates/<section>/<file>)
</Aside>

## Reuse & contribute back

<Aside type="tip">
  <Invitation to PR back changes, with the right label.>
</Aside>
```

### Rules specific to engagement / innersource pages

- **Tables need a blank line before AND after.** This page template is enforced — broken tables break the build under MDX 3.
- **Precede every Starlight component block with prose** so the page makes sense when rendered as plain Markdown on github.com.
- **Link downloadable workfiles via `pathname:///templates/...`** so Astro / Starlight base-prefix resolution works on GitHub Pages forks.
- **Cross-link with relative paths and trailing slash** — `../waf-assessment/` not `/engagement/waf-assessment`.
- **Anonymisation rules apply** — never include customer names, even in examples.

### Directories

| Directory | Audience | Purpose |
|---|---|---|
| `src/content/docs/module-a/` | Auditor + consultant | Module A audit evidence guidance (control template) |
| `src/content/docs/module-b/` | Auditor + consultant | Module B audit evidence guidance (control template) |
| `src/content/docs/engagement/` | Consultant | Engagement playbook steps (engagement template) |
| `src/content/docs/engagement/deliverables/` | Consultant | Templates for customer-facing deliverables (engagement template) |
| `src/content/docs/innersource/` | Consultant + practice lead | Contribution flow, governance, roadmap (engagement template) |

### Workfile sync

Any change to a `pathname:///templates/...` link or to the downloadable workfile itself **must** be paired with an update to the generator under `scripts/workfiles/` so the artefact stays in sync with the page that documents it. The CONTRIBUTING.md PR template enforces this with a checkbox.
