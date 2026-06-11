# Hermes Agent — Deep Dive & Build-Your-Own Guide

> **Source:** https://dev.to/truongpx396/hermes-agent-deep-dive-build-your-own-guide-1pcc
> **Retrieved:** 2026-06-01T00:00:00

---

## What Is Hermes?

**Hermes** is a model-agnostic, self-improving conversational agent that runs:
- Locally as CLI/TUI
- On a server as messaging gateway (Telegram/Discord/Slack/WhatsApp/Signal)
- As a scheduled cron worker

**Key differentiator:** A closed learning loop — writes reusable skills and curates persistent memory.

## Core Principles

1. **Platform-Agnostic Core**: All platform specifics live in adapters
2. **Prompt Stability**: System prompt assembled once at session start (cache-friendly)
3. **Progressive Disclosure**: Level 0 (descriptions) → Level 1 (full skill) → Level 2 (referenced files)
4. **Self-Registration**: Tools register themselves at import time
5. **Profile Isolation**: Each agent owns a HERMES_HOME directory
6. **Agent Owns Learning**: Skills written via skill_manage, memory curated via MEMORY.md/USER.md

## Architecture

```
Entry Points (CLI/TUI/Gateway/Cron)
        ↓
    AIAgent (core loop)
   ↙     ↘        ↘        ↘
Tools   Skills   Memory   Providers
Registry Loader   Manager  (model API)
        ↓
Execution Environments (local/Docker/SSH/Modal)
```

## Agent Loop

1. Receive input
2. Build system prompt (ONCE per session)
3. Resolve provider
4. Call model (chat_completions | codex_responses | anthropic_messages | bedrock_converse)
5. Parse response → dispatch tool calls → repeat
6. Persist to SQLite SessionDB

## System Prompt Assembly Order

1. SOUL.md
2. DEFAULT_AGENT_IDENTITY
3. PLATFORM_HINTS
4. MEMORY_GUIDANCE
5. MEMORY.md
6. USER.md
7. § (delimiter)
8. SESSION_SEARCH_GUIDANCE
9. SKILLS_GUIDANCE
10. AGENTS.md
11. .hermes.md
12. TOOL_USE_ENFORCEMENT_GUIDANCE

---

*Extracted by web-research-pipeline v1.0.0*