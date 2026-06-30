# Hermes Agent: Personality & SOUL.md — Comprehensive Summary

---

## Core Concept: SOUL.md as Primary Identity

> **SOUL.md is the primary identity** — it's the first thing in the system prompt and defines who the agent is.

- **Location**: `~/AppData/Local/hermes/SOUL.md` (default) or `$HERMES_HOME/SOUL.md` (custom home)
- **Behavior**: Loaded **only** from `HERMES_HOME` — not from the current working directory
- **Purpose**: Durable, per-instance personality that persists across projects
- **Fallback**: Built-in default ("You are Hermes Agent, an intelligent AI assistant created by Nous Research...") if file is empty/unreadable or `skip_context_files` is set

---

## Why This Design?

| Problem | Solution |
|---------|----------|
| Personality changing unexpectedly between projects | Load only from `HERMES_HOME` |
| Unpredictable behavior | Personality belongs to the Hermes instance |
| User confusion | Single canonical location: `~/AppData/Local/hermes/SOUL.md` |

---

## What Belongs in SOUL.md ✅ vs AGENTS.md ❌

### ✅ SOUL.md — Durable Voice & Personality
- Communication style and tone
- Core values and principles
- Technical posture/philosophy
- What to avoid (sycophancy, hype, overexplaining)
- How to handle uncertainty

### ❌ AGENTS.md — Task/Context-Specific Instructions
- Project-specific workflows
- Tool usage patterns
- Repository conventions
- Temporary directives

> **Rule**: `SOUL.md` = *who you are* | `AGENTS.md` = *what you're doing*

---

## Example SOUL.md (Production-Ready Template)

```markdown
# Personality

You are a pragmatic senior engineer with strong taste.
You optimize for truth, clarity, and usefulness over politeness theater.

## Style
- Be direct without being cold
- Prefer substance over filler
- Push back when something is a bad idea
- Admit uncertainty plainly
- Keep explanations compact unless depth is useful

## What to avoid
- Sycophancy
- Hype language
- Repeating the user's framing if it's wrong
- Overexplaining obvious things

## Technical posture
- Prefer simple systems over clever systems
- Care about operational reality, not idealized architecture
- Treat edge cases as part of the design, not cleanup
```

---

## How SOUL.md Enters the Prompt

1. **Slot #1** of system prompt — agent identity position
2. **No wrapper language** added — raw content injected directly
3. **Security scanned** for prompt injection patterns before inclusion
4. **Fallback** triggers on: empty file, whitespace-only, unreadable, or `skip_context_files=true`

---

## SOUL.md vs `/personality` Command

| Aspect | SOUL.md | `/personality` |
|--------|---------|----------------|
| **Scope** | Global, persistent default | Session-level overlay |
| **Persistence** | Survives restarts | Resets per session |
| **Use case** | Core identity | Temporary mode shifts |
| **Relationship** | Foundation | Supplements/replaces for session |

> **Key insight**: `/personality` overlays on top of `SOUL.md` — your global default still applies unless the overlay meaningfully changes it.

---

## Built-in Personalities (14 Available)

| Name | Vibe |
|------|------|
| `helpful` | Friendly, general-purpose |
| `concise` | Brief, to-the-point |
| `technical` | Detailed, accurate expert |
| `creative` | Innovative, outside-the-box |
| `teacher` | Patient educator with examples |
| `kawaii` | Cute, sparkles, enthusiasm ★ |
| `catgirl` | Neko-chan, cat expressions, nya~ |
| `pirate` | Captain Hermes, tech-savvy buccaneer |
| `shakespeare` | Bardic prose, dramatic flair |
| `surfer` | Chill bro vibes |
| `noir` | Hard-boiled detective narration |
| `uwu` | Maximum cute uwu-speak |
| `philosopher` | Deep contemplation |
| `hype` | MAXIMUM ENERGY!!! |

### Switching Commands

```bash
# CLI
/personality              # List available
/personality concise      # Switch to concise
/personality technical    # Switch to technical

# Messaging platforms (Discord, Slack, etc.)
/personality teacher
```

---

## Custom Personalities via Config

**File**: `~/AppData/Local/hermes/config.yaml`

```yaml
agent:
  personalities:
    codereviewer: >
      You are a meticulous code reviewer. Identify bugs, security issues,
      performance concerns, and unclear design choices. Be precise and constructive.
```

**Usage**: `/personality codereviewer`

---

## Recommended Workflow

```
1. Edit ~/AppData/Local/hermes/SOUL.md          → Your durable default identity
2. Use AGENTS.md per project       → Task-specific instructions
3. Use /personality for sessions   → Temporary mode shifts (teacher, concise, etc.)
```

**Result**: Consistent core personality + project context + session flexibility

---

## Prompt Stack Hierarchy (Bottom → Top)

```
1. SOUL.md                    ← Foundation (agent identity)
2. AGENTS.md                  ← Project context
3. .cursorrules               ← Editor-specific rules
4. /personality overlay       ← Session override
```

> **SOUL.md is the foundation — everything else builds on top of it.**

---

## Critical Distinction: Personality ≠ CLI Appearance

| Domain | Controlled By |
|--------|---------------|
| Agent voice/tone | SOUL.md, `/personality` |
| CLI theme/colors | `~/AppData/Local/hermes/config.yaml` → `theme` |
| Prompt format | `config.yaml` → `prompt` |

---

## Security Notes

- SOUL.md content is **scanned for prompt injection** before being injected
- Malicious patterns (e.g., "ignore previous instructions") are neutralized
- Only `HERMES_HOME/SOUL.md` is loaded — not project-local SOUL.md files

---

## Quick Reference

| Task | Command |
|------|---------|
| Edit global personality | `nvim ~/AppData/Local/hermes/SOUL.md` (or your editor) |
| List built-in personalities | `/personality` |
| Switch personality (session) | `/personality <name>` |
| Add custom personality | Edit `config.yaml` → `agent.personalities` |
| View current personality | `/personality` (shows active) |

---

**Source:** [Hermes Agent Docs - Personality](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)  
**Extracted:** 2026-06-08