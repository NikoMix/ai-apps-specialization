# AI Applications on Microsoft Azure — Advanced Specialization

> Partner enablement guide for the **AI Applications on Microsoft Azure** Advanced Specialization audit.  
> This repo contains **only MDX content** — theming is handled by a separate private Astro/Starlight theme repo.

---

## 🎯 Purpose

This repository gives Microsoft partners a structured, step-by-step engagement guide to achieve the **AI Applications on Microsoft Azure Advanced Specialization**. It contains:

- Pre-qualification requirements checklist
- Audit process overview
- Per-control evidence templates (Module A & Module B)
- An evidence tracker to manage progress across your engagement

---

## 🚀 Getting Started (Forking this repo)

### 1. Fork this repository

Click **Fork** in the top-right corner of this page and create it in your GitHub organisation.

### 2. Enable GitHub Pages

Go to your fork → **Settings → Pages → Source** → select **GitHub Actions**.

### 3. Create a PAT for the theme repo

The site is built using a private Astro/Starlight theme repo. You need read access to it:

1. Ask your theme repo owner to invite you as a collaborator (or provide a PAT).
2. Create a **fine-grained Personal Access Token** with **Contents: Read** scoped to the theme repo.
3. In your fork → **Settings → Secrets and variables → Actions**, create a secret named:

```
THEME_REPO_TOKEN
```

and paste the PAT as its value.

### 4. Update placeholders

In `.github/workflows/deploy.yml`, replace:

| Placeholder | Replace with |
|---|---|
| `YOUR_ORG/YOUR_THEME_REPO` | The org/repo of the Astro theme (e.g. `contoso/astro-ms-partner-theme`) |

In `astro.config.mjs`, replace:

| Placeholder | Replace with |
|---|---|
| `YOUR_ORG/YOUR_CONTENT_REPO` | Your fork's full repo name |

### 5. Push to `main` — the site deploys automatically

The GitHub Actions workflow clones the theme, copies your MDX content into it, builds the Astro site, and deploys to GitHub Pages.

---

## 🖥️ Local Development

For a local preview (uses the stub `astro.config.mjs` in this repo):

```bash
npm install
npm run dev
```

> **Note:** The local preview uses Starlight directly from `node_modules`. The deployed site uses the private theme repo, which may have a custom look and feel.

---

## 📁 Content Structure

```
src/content/docs/
├── index.mdx                # Landing page
├── overview.mdx             # Specialization overview
├── requirements.mdx         # Pre-qualification requirements
├── audit-process.mdx        # End-to-end audit walkthrough
├── module-a/                # General requirements (7 controls)
│   ├── 1.1-organizational-data.mdx
│   ├── 1.2-financial-documentation.mdx
│   ├── 2.1-service-delivery-methodology.mdx
│   ├── 2.2-quality-management.mdx
│   ├── 3.1-customer-satisfaction.mdx
│   ├── 3.2-complaint-handling.mdx
│   └── 3.3-security-privacy.mdx
├── module-b/                # AI Apps specific (6 controls)
│   ├── 1.1-azure-ai-implementation.mdx
│   ├── 2.1-acr-performance.mdx
│   ├── 2.2-customer-diversity.mdx
│   ├── 3.1-certifications.mdx
│   ├── 4.1-audit-readiness.mdx
│   └── 4.2-partner-onboarding.mdx
├── evidence-tracker.mdx     # Master checklist across all controls
└── faq.mdx                  # Frequently asked questions
```

---

## 🤝 Contributing

To update content, edit the relevant MDX file and open a pull request. The site automatically rebuilds on merge to `main`.

---

## 📄 License

Content is provided for partner enablement purposes. Refer to your Microsoft Partner Agreement for usage terms.
