# AI Applications on Microsoft Azure — Advanced Specialization

> Engagement toolkit for Microsoft partners pursuing the **AI Applications on Microsoft Azure Advanced Specialization** audit.

---

## 🎯 Purpose

This repository gives consultants a structured, step-by-step engagement framework to guide partner organisations through the Advanced Specialization audit. It includes:

- **GitHub Issues** as the primary engagement task board — one issue per control with evidence checklists
- **Documentation site** (Astro/Starlight) with detailed evidence guidance for each control
- **Engagement Agent** — an AI assistant that guides consultants through the process
- **Automated issue creation** — recreates audit issues each year, 9 months before the next audit

---

## 🚀 Getting Started

This repo is a **GitHub Template**. Click **"Use this template"** (not Fork) to create your own copy.

### 1. Use this template

Click **Use this template → Create a new repository** and choose your GitHub organisation.

### 2. Set your site URL

In `astro.config.mjs`, the site URL is read from the `ASTRO_SITE` environment variable.
Add it as a **repository variable** (not a secret):

- Go to your repo → **Settings → Secrets and variables → Actions → Variables**
- Add variable `ASTRO_SITE` = `https://YOUR_ORG.github.io/YOUR_REPO_NAME`

Optionally also add `ASTRO_GITHUB_URL` = `https://github.com/YOUR_ORG/YOUR_REPO_NAME`.

### 3. Enable GitHub Pages

Go to your repo → **Settings → Pages → Source** → select **GitHub Actions**.

### 4. Create the engagement issues

Go to **Actions → Create Audit Engagement Issues → Run workflow**.

Enter the year of the next audit (e.g. `2027`). This creates 13 labelled issues and a milestone.

### 5. Done

- Issues appear as your engagement task board 📋
- The documentation site deploys automatically on push to `main` 🌐
- Use the Engagement Agent for guided assistance 🤖

---

## 🤖 Engagement Agent

The Engagement Agent guides consultants interactively — answering questions about requirements,
recommending next steps, and identifying blockers, based on the repository content and live issue status.

### Option A: GitHub Copilot Chat (zero setup)

The repo includes `.github/copilot-instructions.md` which makes **GitHub Copilot Chat**
aware of the engagement context automatically. Open Copilot Chat on github.com, in VS Code,
or on mobile and ask:

> "What should we work on next for the AI Apps specialization audit?"

### Option B: Standalone CLI Agent

```bash
cd agent
pip install -r requirements.txt

# Uses GitHub Models — free with your GitHub token
export GITHUB_TOKEN=$(gh auth token)
python engagement-agent.py
```

See [`agent/README.md`](agent/README.md) for full documentation and Azure OpenAI configuration.

---

## 📅 Annual Audit Cycle

The `Create Audit Engagement Issues` workflow runs automatically on a **schedule** (default: March 1st each year) to create a fresh set of issues for the next audit cycle, 9 months after the previous audit — giving your team 3 months to re-collect evidence.

To adjust the schedule to match your audit timing:
- Open `.github/workflows/create-issues.yml`
- Change the cron month: `0 9 1 **3** *` → your audit month + 9

---

## 🖥️ Local Development

```bash
npm install
npm run dev
```

---

## 📁 Structure

```
├── .github/
│   ├── copilot-instructions.md      # Copilot Chat engagement context
│   ├── scripts/create-issues.sh    # Issue creation script
│   └── workflows/
│       ├── deploy.yml               # Build & deploy to GitHub Pages
│       └── create-issues.yml        # Annual issue creation
├── agent/
│   ├── engagement-agent.py          # Interactive CLI agent
│   ├── requirements.txt
│   └── README.md
└── src/content/docs/
    ├── index.mdx / overview.mdx / requirements.mdx / ...
    ├── module-a/                    # Controls A.1.1 – A.3.3
    └── module-b/                    # Controls B.1.1 – B.4.2
```

---

## 📄 License

Content is provided for partner enablement purposes. Refer to your Microsoft Partner Agreement for usage terms.
