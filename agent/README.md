# Engagement Agent

An interactive CLI assistant that guides consultants through the
**AI Applications on Microsoft Azure Advanced Specialization** audit engagement.

The agent reads the repository's documentation and your live GitHub issue status to
provide contextual, step-by-step guidance — no separate knowledge base required.

---

## Prerequisites

- Python 3.9+
- `gh` CLI authenticated (`gh auth login`) — needed for live issue status
- One of:
  - **GitHub token** with `models:read` permission *(recommended — free, works with your existing `GITHUB_TOKEN`)*
  - Azure OpenAI endpoint + key

---

## Quick start

```bash
# From the repo root
cd agent
pip install -r requirements.txt

# Option 1: GitHub Models (free — uses your GitHub token)
export GITHUB_TOKEN=ghp_...          # or: gh auth token
python engagement-agent.py

# Option 2: Azure OpenAI
export AZURE_OPENAI_ENDPOINT=https://YOUR_RESOURCE.openai.azure.com
export AZURE_OPENAI_KEY=...
export AZURE_OPENAI_DEPLOYMENT=gpt-4o   # optional, defaults to gpt-4o
python engagement-agent.py
```

---

## Usage

```
python engagement-agent.py           # interactive chat (default)
python engagement-agent.py --status  # show engagement dashboard and exit
```

### In-session shortcuts

| Command | Action |
|---|---|
| `status` | Show current engagement progress (open/closed issues) |
| `refresh` | Reload issue status from GitHub |
| `clear` | Start a fresh conversation (keeps repo context) |
| `quit` | Exit |

---

## Example questions

```
"What should we work on first?"
"What evidence do I need for control A.2.2?"
"We only have 2 customers in ACR — what can we do?"
"Which certifications are we missing?"
"How do I export the ACR data from Partner Center?"
"What's the fastest way to get a complaint handling case if we have no complaints?"
"We have ISO 27001 — does that satisfy A.3.3?"
"How long does the audit take?"
```

---

## How it works

1. **On startup**: reads all MDX documentation from `src/content/docs/` into the system prompt
2. **Live issue status**: queries your GitHub repo's issues via `gh issue list` to know which controls are open vs closed
3. **Chat**: streams responses from GitHub Models (GPT-4o) or Azure OpenAI

The agent's context is refreshed each session. Use `refresh` during a session to pull updated issue status.

---

## Using with GitHub Copilot Chat (zero setup)

The repository also includes `.github/copilot-instructions.md`, which automatically
makes **GitHub Copilot Chat** (on github.com, VS Code, or mobile) aware of the engagement
context. No setup needed — just open Copilot Chat in the repo and ask your question.
