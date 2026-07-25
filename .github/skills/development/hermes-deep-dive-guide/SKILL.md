---
name: hermes-deep-dive-guide
title: "Hermes Deep Dive & Build-Your-Own Guide"
description: "Use when studying Hermes architecture, agent loop, system prompt assembly order, profile isolation, self-registration, and learning loop — from dev.to deep-dive article."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, architecture, agent-loop, system-prompt, profiles, self-registration, learning-loop]
---
# Hermes Deep Dive & Build-Your-Own Guide

## Purpose

Technical deep-dive into Hermes Agent internals from dev.to article — architecture, agent loop, system prompt assembly, profile isolation, and self-improving learning loop.

## When to Use

- Understanding Hermes internals
- Building custom agents on Hermes principles
- Debugging system prompt, profile, or skill loading
- Extending with custom tools/providers

## When NOT to Use

- Quick start (use quickstart guide)
- Course learning (use NetworkChuck course)
- Memory specifics (use memory guides)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug prompt assembly, profile isolation |
| `writing-plans` | Plan custom agent architecture |

## Workflow

### Phase 1: What Is Hermes

Model-agnostic, self-improving conversational agent running as:
- Local CLI/TUI
- Server messaging gateway (Telegram/Discord/Slack/WhatsApp/Signal)
- Scheduled cron worker

**Key differentiator:** Closed learning loop — writes reusable skills, curates persistent memory.

### Phase 2: Core Principles

1. **Platform-Agnostic Core** — All platform specifics in adapters
2. **Prompt Stability** — System prompt assembled once at session start (cache-friendly)
3. **Progressive Disclosure** — Level 0 (descriptions) → Level 1 (full skill) → Level 2 (referenced files)
4. **Self-Registration** — Tools register themselves at import time
5. **Profile Isolation** — Each agent owns HERMES_HOME directory
6. **Agent Owns Learning** — Skills via skill_manage, memory via MEMORY.md/USER.md

### Phase 3: Architecture

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

### Phase 4: Agent Loop

1. Receive input
2. Build system prompt (ONCE per session)
3. Resolve provider
4. Call model (chat_completions | codex_responses | anthropic_messages | bedrock_converse)
5. Parse response → dispatch tool calls → repeat
6. Persist to SQLite SessionDB

### Phase 5: System Prompt Assembly Order

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

### Phase 6: Profile Isolation

Each agent = own HERMES_HOME with:
- skills/
- plugins/
- cron/
- memories/ (USER.md, MEMORY.md)
- config.yaml
- state.db (session history)

### Phase 7: Learning Loop

- Successful task patterns → skill_manage(create)
- Important facts → memory(add)
- Reflection pass (daily) → synthesizes sessions → updates MEMORY.md or generates skills

## Pitfalls

- **Prompt cache invalidation** — SOUL.md changes need new session
- **Profile config drift** — Use `hermes config set`, not direct YAML
- **Skill regeneration** — Auto-skills may overwrite manual edits; use `user_locked: true`
- **Memory limits** — 2200/1375 char limits; consolidate when full

## Verification Checklist

- [ ] System prompt order understood
- [ ] Profile isolation mechanism clear
- [ ] Agent loop steps traceable
- [ ] Learning loop (skills + memory) understood

## References

- `references/system-prompt-order.md` — Detailed assembly with token estimates
- `references/profile-structure.md` — HERMES_HOME directory layout
- `references/learning-loop.md` — Skill generation and reflection triggers
- `references/hermes-architecture.md` — System architecture overview
- `references/hermes-deep-dive-patterns.md` — Platform detection, skill workflow, testing patterns

## Templates

- `templates/hermes-skill-template.md` — Skill creation template

## Scripts

- `scripts/hermes-verify-install.py` — Installation verification