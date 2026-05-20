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

This repo ships with a **GitHub Custom Agent** — a purpose-built Copilot agent that knows every audit control, evidence requirement, and common blocker for this specialization.

### Using the Engagement Agent on GitHub.com

1. Go to **github.com/copilot** (or open Copilot in your repo)
2. Click the agent selector dropdown
3. Choose **Engagement Agent**
4. Ask anything:

> *"What should we work on first?"*
> *"What evidence do we need for A.2.2?"*
> *"We only have 2 DPOR-linked customers — what are our options?"*
> *"Our DP-420 cert holder just left — what do we do?"*

The agent reads the repository documentation and open GitHub Issues to give you contextual, step-by-step guidance.

### Using the Engagement Agent in VS Code

The agent is also available in **VS Code Copilot Chat** once the repo is open — select it from the agent dropdown in the Copilot Chat panel.

### Assigning the agent to an issue

You can assign the Engagement Agent to a GitHub Issue directly — it will read the control checklist, search the docs, and prescribe the next action.

The agent profile is defined in [`.github/agents/engagement-agent.agent.md`](.github/agents/engagement-agent.agent.md).

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
│   ├── agents/
│   │   └── engagement-agent.agent.md  # GitHub Custom Agent definition
│   ├── copilot-instructions.md        # Copilot Chat base context
│   ├── scripts/create-issues.sh       # Issue creation script
│   └── workflows/
│       ├── deploy.yml                  # Build & deploy to GitHub Pages
│       ├── create-issues.yml           # Annual issue creation
│       └── copilot-setup-steps.yml     # Copilot coding agent environment
└── src/content/docs/
    ├── index.mdx / overview.mdx / requirements.mdx / ...
    ├── module-a/                    # Controls A.1.1 – A.3.3
    └── module-b/                    # Controls B.1.1 – B.4.2
```

---

## 📄 License

Content is provided for partner enablement purposes. Refer to your Microsoft Partner Agreement for usage terms.
