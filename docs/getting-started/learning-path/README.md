# Hermes Agent Learning Path - Comprehensive Summary

## Quick Start Command

```bash
hermes setup --portal
```
> **First-time users almost always want `hermes setup --portal`** — one OAuth covers a model plus the four Tool Gateway tools (search/image/TTS/browser). See [Nous Portal](/docs/integrations/nous-portal).

---

## Learning Paths by Experience Level

| Level | Goal | Reading Order | Time |
|-------|------|---------------|------|
| **Beginner** | Get running, basic conversations, built-in tools | [Installation](/docs/getting-started/installation) → [Quickstart](/docs/getting-started/quickstart) → [CLI Usage](/docs/user-guide/cli) → [Configuration](/docs/user-guide/configuration) | ~1 hour |
| **Intermediate** | Messaging bots, memory, cron jobs, skills | [Sessions](/docs/user-guide/sessions) → [Messaging](/docs/user-guide/messaging) → [Tools](/docs/user-guide/features/tools) → [Skills](/docs/user-guide/features/skills) → [Memory](/docs/user-guide/features/memory) → [Cron](/docs/user-guide/features/cron) | ~2–3 hours |
| **Advanced** | Custom tools, skills, RL training, contribute | [Architecture](/docs/developer-guide/architecture) → [Adding Tools](/docs/developer-guide/adding-tools) → [Creating Skills](/docs/developer-guide/creating-skills) → [Contributing](/docs/developer-guide/contributing) | ~4–6 hours |

---

## Learning Paths by Use Case

### 🖥️ CLI Coding Assistant

- Use Hermes as interactive terminal assistant for writing, reviewing, running code
- Pass files directly via **context files** — agent can read, edit, and run code in your projects

### 🤖 Telegram/Discord Bot

- Deploy Hermes as a bot on messaging platforms
- Full project examples available in docs

### ⚙️ Task Automation

- Schedule recurring tasks, run batch jobs, chain agent actions
- **Cron jobs** enable daily summaries, periodic checks, automated reports — runs without you present

### 🔧 Build Custom Tools/Skills

- Extend Hermes with your own tools and reusable skill packages
- **Important**: For most custom tool creation, start with **plugins**. The [Adding Tools](/docs/developer-guide/adding-tools) page is for *built-in Hermes core development*, not the usual user/custom-tool path

### 🧠 Train Models (RL)

- Fine-tune model behavior via reinforcement learning using Hermes' RL pipeline (powered by [Atropos](https://github.com/NousResearch/atropos))
- **Prerequisite**: Understand basics of Hermes conversations and tool calls — run Beginner path first if new

### 🐍 Python Library Integration

- Integrate Hermes Agent programmatically into your own Python applications

---

## Key Features Directory

| Feature | Description | Documentation |
|---------|-------------|---------------|
| **Tools** | Built-in tools agent can call (file I/O, search, shell, etc.) | [Tools](/docs/user-guide/features/tools) |
| **Skills** | Installable plugin packages adding new capabilities | [Skills](/docs/user-guide/features/skills) |
| **Memory** | Persistent memory across sessions | [Memory](/docs/user-guide/features/memory) |
| **Context Files** | Feed files/directories into conversations | [Context Files](/docs/user-guide/features/context-files) |
| **MCP** | Connect to external tool servers via Model Context Protocol | [MCP](/docs/user-guide/features/mcp) |
| **Cron** | Schedule recurring agent tasks | [Cron](/docs/user-guide/features/cron) |
| **Delegation** | Spawn sub-agents for parallel work | [Delegation](/docs/user-guide/features/delegation) |
| **Code Execution** | Run Python scripts calling Hermes tools programmatically | [Code Execution](/docs/user-guide/features/code-execution) |
| **Browser** | Web browsing and scraping | [Browser](/docs/user-guide/features/browser) |
| **Hooks** | Event-driven callbacks and middleware | [Hooks](/docs/user-guide/features/hooks) |
| **Batch Processing** | Process multiple inputs in bulk | [Batch Processing](/docs/user-guide/features/batch-processing) |
| **Provider Routing** | Route requests across multiple LLM providers | [Provider Routing](/docs/user-guide/features/provider-routing) |

---

## Navigation Guidance

> **You don't need to read everything.** Pick the path that matches your goal, follow the links in order, and you'll be productive quickly. You can always come back to this page to find your next step.

---

## Prerequisites

- **Installation guide** → **Quickstart** required before any path below
- Assumes working Hermes Agent installation

## Key Insights

1. **Single OAuth via `--portal`** unlocks model + 4 Tool Gateway tools (search, image, TTS, browser)
2. **Plugins ≠ Core Tools**: Custom tools typically use plugin system, not core development APIs
3. **RL Training** requires foundational knowledge — not a starting point
4. **Modular documentation**: Each feature has dedicated page; follow ordered paths for efficiency

---

**Source:** [Hermes Agent Docs - Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)  
**Extracted:** 2026-06-08