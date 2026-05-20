#!/usr/bin/env python3
"""
Engagement Agent – AI Applications on Microsoft Azure Advanced Specialization

An interactive CLI assistant that guides consultants through the audit engagement.
Reads the repo's MDX content and live GitHub issue status to provide contextual,
step-by-step guidance.

Usage:
    python engagement-agent.py              # interactive chat
    python engagement-agent.py --status     # show engagement dashboard only

Authentication (in order of preference):
    1. GITHUB_TOKEN env var  → uses GitHub Models (free, no extra account needed)
    2. AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_KEY env vars → uses Azure OpenAI
"""

import os
import sys
import json
import glob
import argparse
import subprocess
import textwrap
from pathlib import Path

try:
    from openai import OpenAI, AzureOpenAI
except ImportError:
    print("❌ Missing dependency. Run: pip install openai")
    sys.exit(1)


# ──────────────────────────────────────────────────────────────────────────────
# Client setup
# ──────────────────────────────────────────────────────────────────────────────

def get_client():
    github_token = os.environ.get("GITHUB_TOKEN")
    azure_key = os.environ.get("AZURE_OPENAI_KEY")
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

    if github_token:
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=github_token,
        )
        return client, "gpt-4o"

    if azure_key and azure_endpoint:
        client = AzureOpenAI(
            api_key=azure_key,
            azure_endpoint=azure_endpoint,
            api_version="2024-02-01",
        )
        return client, azure_deployment

    print(
        "❌ No authentication configured.\n"
        "   Set GITHUB_TOKEN (recommended) or\n"
        "   AZURE_OPENAI_ENDPOINT + AZURE_OPENAI_KEY"
    )
    sys.exit(1)


# ──────────────────────────────────────────────────────────────────────────────
# Content loading
# ──────────────────────────────────────────────────────────────────────────────

def load_repo_content() -> str:
    """Load all MDX guide pages as system context."""
    repo_root = Path(__file__).parent.parent
    pattern = str(repo_root / "src" / "content" / "docs" / "**" / "*.mdx")
    files = sorted(glob.glob(pattern, recursive=True))

    if not files:
        return "(No MDX content found — run the agent from inside the repository.)"

    sections = []
    for path in files:
        rel = Path(path).relative_to(repo_root)
        text = Path(path).read_text(encoding="utf-8")
        sections.append(f"### {rel}\n\n{text}")

    return "\n\n---\n\n".join(sections)


def get_issue_status() -> tuple[list, str]:
    """Fetch GitHub issues via gh CLI. Returns (issues_list, formatted_summary)."""
    try:
        result = subprocess.run(
            [
                "gh", "issue", "list",
                "--state", "all",
                "--json", "number,title,state,labels,body",
                "--limit", "100",
            ],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            return [], "(Issue status unavailable — gh CLI not authenticated or not in a GitHub repo.)"

        issues = json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return [], "(Issue status unavailable — gh CLI not found or timed out.)"

    if not issues:
        return [], "(No issues found — run the 'Create Audit Engagement Issues' workflow first.)"

    open_issues = [i for i in issues if i["state"] == "OPEN"]
    closed_issues = [i for i in issues if i["state"] == "CLOSED"]

    lines = [
        f"ENGAGEMENT PROGRESS: {len(closed_issues)}/{len(issues)} controls complete\n"
    ]

    if open_issues:
        lines.append("OPEN (evidence still needed):")
        for i in open_issues:
            labels = ", ".join(l["name"] for l in i.get("labels", []))
            lines.append(f"  ⬜ #{i['number']} {i['title']}  [{labels}]")

    if closed_issues:
        lines.append("\nCOMPLETED:")
        for i in closed_issues:
            lines.append(f"  ✅ #{i['number']} {i['title']}")

    return issues, "\n".join(lines)


def print_status_dashboard(issues: list, summary: str):
    width = 70
    print("\n" + "─" * width)
    print("  ENGAGEMENT DASHBOARD")
    print("─" * width)
    print(summary)
    print("─" * width + "\n")


# ──────────────────────────────────────────────────────────────────────────────
# System prompt
# ──────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are the Engagement Agent for the **AI Applications on Microsoft Azure \
Advanced Specialization** audit. You guide consultants step-by-step through the \
engagement, helping partners collect evidence, resolve gaps, and pass the \
third-party audit.

Your capabilities:
- Explain exactly what evidence is needed for any audit control (A.1.1–B.4.2)
- Recommend the next priority action based on the current engagement status
- Identify blockers (missing insurance, expired certs, below-threshold ACR)
- Provide practical, specific advice — never vague generalities
- Suggest the fastest path to obtain any missing document or data

Rules:
- Always reference control numbers (e.g. A.2.1, B.3.1) when discussing requirements
- Flag hard blockers (expired certs, no insurance, ACR below threshold) prominently
- Be encouraging — partners often feel overwhelmed; remind them it is manageable
- Keep responses concise and scannable — use bullet points and short paragraphs
- When the user asks "what next?", check open issues and recommend the earliest \
  unclosed control in Module A then Module B order

---

CURRENT ENGAGEMENT STATUS:
{issue_status}

---

ENGAGEMENT GUIDE (full documentation):
{repo_content}
"""


# ──────────────────────────────────────────────────────────────────────────────
# Chat loop
# ──────────────────────────────────────────────────────────────────────────────

WELCOME = """\
╔══════════════════════════════════════════════════════════════════════╗
║   AI Apps on Microsoft Azure – Advanced Specialization              ║
║   Engagement Agent                                                  ║
╚══════════════════════════════════════════════════════════════════════╝

Type a question to get guidance, or use these shortcuts:
  status   – show current engagement dashboard
  refresh  – reload issue status from GitHub
  clear    – start a new conversation
  quit     – exit

Examples:
  "What should we work on first?"
  "What evidence do I need for A.2.2?"
  "We only have 2 customers in ACR — what can we do?"
  "Which certifications are we missing?"
"""


def chat(client, model: str, system_prompt: str):
    messages = [{"role": "system", "content": system_prompt}]

    while True:
        try:
            raw = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            break

        if not raw:
            continue

        cmd = raw.lower()

        if cmd in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break

        if cmd == "clear":
            messages = [{"role": "system", "content": system_prompt}]
            print("✅ Conversation cleared.\n")
            continue

        if cmd in ("status", "refresh"):
            issues, summary = get_issue_status()
            print_status_dashboard(issues, summary)
            if cmd == "refresh":
                # Rebuild system prompt with fresh issue data
                _, fresh_summary = get_issue_status()
                messages[0]["content"] = system_prompt.replace(
                    messages[0]["content"].split("CURRENT ENGAGEMENT STATUS:\n")[1].split("\n\n---")[0],
                    fresh_summary,
                )
                print("✅ Issue status refreshed.\n")
            continue

        messages.append({"role": "user", "content": raw})

        print("\nAgent: ", end="", flush=True)
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                max_tokens=1500,
                temperature=0.3,
            )
            full_response = ""
            for chunk in response:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="", flush=True)
                    full_response += delta
        except Exception as exc:
            print(f"\n❌ Error: {exc}")
            messages.pop()
            continue

        print("\n")
        messages.append({"role": "assistant", "content": full_response})


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Engagement Agent – AI Apps on Microsoft Azure Advanced Specialization"
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Print the engagement dashboard and exit (no chat)"
    )
    args = parser.parse_args()

    # Always load content (needed for system prompt even in status mode)
    print("⏳ Loading repository content…", end="", flush=True)
    repo_content = load_repo_content()
    issues, issue_summary = get_issue_status()
    print(" done.\n")

    if args.status:
        print_status_dashboard(issues, issue_summary)
        return

    client, model = get_client()

    system_prompt = SYSTEM_PROMPT.format(
        issue_status=issue_summary,
        repo_content=repo_content,
    )

    print(WELCOME)
    print_status_dashboard(issues, issue_summary)

    chat(client, model, system_prompt)


if __name__ == "__main__":
    main()
