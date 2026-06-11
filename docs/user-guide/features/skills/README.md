# Hermes Agent Skills System — Comprehensive Summary

## Overview

**Skills** are on-demand knowledge documents the agent loads when needed, following a **progressive disclosure** pattern to minimize token usage. They're compatible with the [agentskills.io](https://agentskills.io/specification) open standard.

**Primary directory (source of truth):** `~/.hermes/skills/`
- Bundled skills copied here on fresh install
- Hub-installed and agent-created skills also stored here
- Agent can modify or delete any skill

**External skill directories** can be added for shared/multi-tool skill collections.

---

## Starting with a Blank Slate

By default, profiles are seeded with bundled skills on install and `hermes update`. To disable:

| Method | Command |
|--------|---------|
| **At install** | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash -s -- --no-skills` |
| **At profile creation** | `hermes profile create research --no-skills` |
| **On existing profile** | `hermes skills opt-out` (stops future seeding) |
| **Also remove unmodified bundled skills** | `hermes skills opt-out --remove` |
| **Re-enable** | `hermes skills opt-in --sync` |

All methods write a `.no-bundled-skills` marker to the profile directory. Delete marker or run `opt-in` to re-enable.

> **Key:** `opt-out` only stops *future* seeding — never deletes existing skills. `--remove` only deletes **unmodified** bundled skills (byte-identical to installed version). Edited, hub-installed, and custom skills are always preserved.

---

## Using Skills

Every installed skill is automatically available as a **slash command**:

```bash
# In CLI or any messaging platform:
/gif-search funny cats
/axolotl help me fine-tune Llama 3 on my dataset
/github-pr-workflow create a PR for the auth refactor
/plan design a rollout for migrating our auth provider

# Just the skill name loads it and lets the agent ask what you need:
/excalidraw
```

**Example:** The bundled `plan` skill — running `/plan [request]` loads instructions telling Hermes to inspect context, write a markdown implementation plan (not execute), and save under `.hermes/plans/` relative to workspace.

**Natural conversation:**
```bash
hermes chat --toolsets skills -q "What skills do you have?"
hermes chat --toolsets skills -q "Show me the axolotl skill"
```

---

## Progressive Disclosure (Token-Efficient Loading)

| Level | Call | Returns | Approx. Tokens |
|-------|------|---------|----------------|
| **0** | `skills_list()` | `[{name, description, category}, ...]` | ~3k |
| **1** | `skill_view(name)` | Full content + metadata | Varies |
| **2** | `skill_view(name, path)` | Specific reference file | Varies |

Agent only loads full skill content when actually needed.

---

## SKILL.md Format

```yaml
---
name: my-skill
description: Brief description of what this skill does
version: 1.0.0
platforms: [macos, linux]  # Optional — restrict to specific OS platforms
metadata:
  hermes:
    tags: [python, automation]
    category: devops
    fallback_for_toolsets: [web]      # Optional — conditional activation
    requires_toolsets: [terminal]     # Optional — conditional activation
    config:                           # Optional — config.yaml settings
      - key: my.setting
        description: "What this controls"
        default: "value"
        prompt: "Prompt for setup"
---

# Skill Title

## When to Use
Trigger conditions for this skill.

## Procedure
1. Step one
2. Step two

## Pitfalls
- Known failure modes and fixes

## Verification
How to confirm it worked.
```

### Platform-Specific Skills

| Value | Matches |
|-------|---------|
| `macos` | macOS (Darwin) |
| `linux` | Linux |
| `windows` | Windows |

```yaml
platforms: [macos]              # macOS only (e.g., iMessage, Apple Reminders, FindMy)
platforms: [macos, linux]       # macOS and Linux
```

When set, skill is **automatically hidden** from system prompt, `skills_list()`, and slash commands on incompatible platforms. Omitted = loads on all platforms.

---

## Skill Output & Media Delivery

### Automatic Media Detection

When a response includes a **bare absolute path** to a media file (e.g., `/home/user/screenshots/diagram.png`), the gateway:
1. Auto-detects it
2. Strips it from visible text
3. Delivers natively to chat (Telegram photo, Discord attachment, etc.)

### Audio as Voice Messages

`[[audio_as_voice]]` directive promotes audio files to native voice-message bubbles on supported platforms (Telegram, WhatsApp).

### Forcing Document-Style Delivery: `[[as_document]]`

```markdown
Here is your rendered chart:

/home/user/.hermes/cache/chart-q4-2025.png

[[as_document]]
```

- Delivers **every** media path in that response as a downloadable document/attachment (not re-compressed image bubble)
- Critical for high-res screenshots/charts — Telegram's `sendPhoto` recompresses to ~200 KB at 1280px; `sendDocument` keeps original bytes
- Directive is stripped before delivery (users never see it)
- All-or-nothing per response

---

## Hub Installation (agentskills.io)

Skills from the open [agentskills.io](https://agentskills.io) registry can be installed:

```bash
# Interactive picker (recommended)
/skill install

# Or from CLI
hermes skill install <name>
```

### Installation Flow

1. User runs `/skill install` or `hermes skill install <name>`
2. Skill downloaded from `agentskills.io` registry
3. Saved to `~/.hermes/skills/<name>/SKILL.md` + references/
4. Immediately available as `/skillname`

### Version Pinning

```yaml
# In SKILL.md
version: 1.2.3
```

Agent tracks installed version vs. registry. `/skill update` shows available updates.

---

## Skill Discovery

```bash
# List all available skills
/skills

# View skill details
/excalidraw help
/hermes-agent  # Loads and prompts for intent
```

**CLI commands:**
```bash
hermes skills list
hermes skills view <name>
```

---

## Creating Custom Skills

### Quick Start

```bash
hermes skill create my-skill
```

This scaffolds `~/.hermes/skills/my-skill/` with:
- `SKILL.md` (with frontmatter template)
- `references/` directory

### Required Fields

| Field | Required | Notes |
|-------|----------|-------|
| `name` | ✅ | Lowercase, hyphens/underscores, max 64 chars |
| `description` | ✅ | One sentence, shown in `skills_list()` |
| `version` | ✅ | Semver |
| `platforms` | ❌ | Restricts OS platforms |
| `metadata.hermes.category` | ❌ | For grouping in listings |

### Best Practices

1. **Single responsibility** — one skill = one workflow/task type
2. **Actionable steps** — numbered procedures, not conceptual overviews
3. **Pitfalls section** — document known failures and fixes
4. **Verification steps** — how to confirm success
5. **Token efficiency** — keep SKILL.md under ~500 lines; large refs go to `references/`

---

## Skill Lifecycle

```
create → edit → use → update → (consolidate) → delete
```

### Autonomous Curator (v0.12.0+)

- Runs on a **7-day cycle**
- Grades skills by usage, success rate, freshness
- Consolidates near-duplicates
- Prunes stale/unused skills
- Logs decisions to `~/.hermes/logs/curator/`

---

## Integration with Other Features

| Feature | Interaction |
|---------|-------------|
| **Memory** | Skills can `memory add` facts; memory can reference skill names |
| **Tools** | `requires_toolsets` / `fallback_for_toolsets` for conditional loading |
| **MCP** | Skills can invoke MCP tools via `execute_code` |
| **Delegation** | Skills can spawn subagents with `delegate_task` |
| **Hooks** | Skills can register hooks in `config.yaml` |

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Skill not showing in `/skills` | Check `platforms` field; verify `SKILL.md` syntax |
| Slash command not working | Ensure skill directory name matches `name` field; restart Hermes |
| Hub install fails | Check network; verify `agentskills.io` is reachable |
| Version conflict | Run `/skill update` or manually delete and reinstall |

---

## Verification Checklist

- [ ] `skills_list()` returns the skill
- [ ] `/skillname` loads and works
- [ ] `skill_view(name)` returns full content
- [ ] References load with `skill_view(name, "references/file.md")`
- [ ] Platform restrictions work correctly (if set)

---

**Source:** [Hermes Agent Docs - Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)  
**Extracted:** 2026-06-08