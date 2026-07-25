---
name: hermes-personality-soul
title: "Hermes Personality & SOUL.md (Official Docs)"
description: "Use when customizing Hermes agent personality — covers SOUL.md as primary identity, built-in /personality presets, custom personalities in config, SOUL.md vs AGENTS.md distinction, and prompt stack order."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, personality, soul-md, agents-md, prompt-stack, custom-personalities]
---
# Hermes Personality & SOUL.md (Official Documentation)

## Purpose

Complete guide to Hermes Agent personality system — SOUL.md as durable identity, built-in `/personality` overlays, custom personalities in config, and how they layer in the prompt stack.

## When to Use

- Changing Hermes' default personality
- Creating project-specific personas
- Understanding SOUL.md vs AGENTS.md
- Debugging personality conflicts

## When NOT to Use

- Quick personality switch (use `/personality` command)
- Memory management (different system)
- Skill creation (different system)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-skills` | Craft effective personality descriptions |
| `systematic-debugging` | Debug personality not loading, prompt stack issues |

## Workflow

### Phase 1: SOUL.md — Primary Identity

**Location:** `~/.hermes/SOUL.md` (always from `HERMES_HOME`, never cwd)

**Behavior:**
- Slot #1 in system prompt — replaces hardcoded default identity
- Auto-created if missing (starter persona)
- Never overwrites existing user SOUL.md
- Empty/missing/unreadable → built-in fallback identity
- Security scanned + truncated if too large

**What belongs in SOUL.md:**
- Tone, communication style, directness level
- Default interaction style
- How to handle uncertainty, disagreement, ambiguity
- What to avoid stylistically (sycophancy, hype, over-explaining)
- Technical posture (simple vs clever systems, edge cases)

**What does NOT belong:**
- One-off project instructions → AGENTS.md
- File paths, repo conventions → AGENTS.md
- Temporary workflow details → AGENTS.md

**Rule:** If it follows you everywhere → SOUL.md. If it belongs to a project → AGENTS.md.

### Phase 2: Built-in Personalities (`/personality`)

Session-level overlays that supplement or shift SOUL.md:

| Name | Description |
|------|-------------|
| **helpful** | Friendly, general-purpose assistant |
| **concise** | Brief, to-the-point responses |
| **technical** | Detailed, accurate technical expert |
| **creative** | Innovative, outside-the-box thinking |
| **teacher** | Patient educator with clear examples |
| **kawaii** | Cute expressions, sparkles, enthusiasm ★ |
| **catgirl** | Neko-chan with cat-like expressions, nya~ |
| **pirate** | Captain Hermes, tech-savvy buccaneer |
| **shakespeare** | Bardic prose with dramatic flair |
| **surfer** | Totally chill bro vibes |
| **noir** | Hard-boiled detective narration |
| **uwu** | Maximum cute with uwu-speak |
| **philosopher** | Deep contemplation on every query |
| **hype** | MAXIMUM ENERGY AND ENTHUSIASM!!! |

**Usage:**
```text
/personality           # List available
/personality concise  # Switch to concise
/personality teacher  # Switch to teacher
```

### Phase 3: Custom Personalities in Config

```yaml
agent:
  personalities:
    codereviewer: >
      You are a meticulous code reviewer. Identify bugs, security issues,
      performance concerns, and unclear design choices. Be precise and constructive.
    debugger: >
      You are a systematic debugger. Follow root-cause investigation before fixing.
      Never guess. Trace data flow. Question architecture after 3 failed fixes.
```

**Switch:** `/personality codereviewer`

### Phase 4: Prompt Stack Order (High Level)

1. **SOUL.md** (agent identity — or built-in fallback)
2. Tool-aware behavior guidance
3. Memory/user context (MEMORY.md, USER.md)
4. Skills guidance
5. Context files (`AGENTS.md`, `.cursorrules`, `.hermes.md`)
6. Timestamp
7. Platform-specific formatting hints
8. **Optional: `/personality` overlay**

SOUL.md is the foundation — everything builds on it.

### Phase 5: CLI & Messaging Platforms

**CLI/TUI:**
```text
/personality
/personality technical
```

**Messaging (Telegram/Discord/Slack/WhatsApp/Signal):**
```text
/personality teacher
```

### Phase 6: Skins vs Personality (Separate)

- `SOUL.md`, `agent.system_prompt`, `/personality` → **How Hermes speaks**
- `display.skin`, `/skin` → **How Hermes looks in terminal**

Completely independent systems.

## Pitfalls

- **SOUL.md in cwd ignored** — Only `HERMES_HOME/SOUL.md` loads
- **Empty SOUL.md = fallback** — Not "no personality"
- **Personality overlay ≠ replacement** — Adds to SOUL.md, doesn't replace
- **Custom personalities need config reload** — Restart Hermes after config.yaml edit
- **Security scan blocks injection attempts** — Keep personality instructions clean

## Verification Checklist

- [ ] SOUL.md exists at `~/.hermes/SOUL.md`
- [ ] `/personality` lists built-in + custom
- [ ] Custom personality switches work
- [ ] SOUL.md content appears in `/context` dump
- [ ] Personality doesn't conflict with SOUL.md tone

## References

- `references/prompt-stack-order.md` — Full prompt assembly order
- `references/built-in-personalities.md` — Full text of each built-in
- `references/custom-personality-examples.md` — More examples

## Templates

- `templates/soul-template.md` — Starter SOUL.md
- `templates/custom-personality.yaml` — Config snippet

## Scripts

- `scripts/verify-soul-load.py` — Confirm SOUL.md loads correctly