---
name: hermes-personality
description: SOUL.md global identity, /personality command, built-in personalities, custom personalities
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, personality, soul, configuration]
    category: personality
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.personality.enabled
        description: "Enable personality skill"
        default: "true"
---

# Hermes Personality Skill

## When to Use
- Configuring global agent identity (SOUL.md)
- Switching session personalities (/personality command)
- Creating custom personalities via config.yaml
- Understanding prompt stack hierarchy

## Procedure
1. **SOUL.md — Global Identity** (File: `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`):
   - Loaded ONLY from `HERMES_HOME` — not from current working directory
   - First thing in system prompt (slot #1)
   - Durable, per-instance personality that persists across projects
   - Fallback: built-in default if empty/unreadable or `skip_context_files=true`

2. **SOUL.md vs AGENTS.md**:
   | Aspect | SOUL.md | AGENTS.md |
   |--------|---------|-----------|
   | Content | Voice, tone, values, principles | Project workflows, conventions |
   | Scope | Global, persistent default | Project-specific |
   | Location | `HERMES_HOME` only | Project root + subdirs |
   
   **Rule**: `SOUL.md` = *who you are* | `AGENTS.md` = *what you're doing*

3. **SOUL.md Template**:
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

4. **Built-in Personalities** (14 available):
   ```bash
   /personality              # List available
   /personality concise      # Brief, to-the-point
   /personality technical    # Detailed, accurate expert
   /personality teacher      # Patient educator with examples
   /personality creative     # Innovative, outside-the-box
   /personality kawaii       # Cute, sparkles, enthusiasm ★
   /personality catgirl      # Neko-chan, cat expressions, nya~
   /personality pirate       # Captain Hermes, tech-savvy buccaneer
   /personality shakespeare  # Bardic prose, dramatic flair
   /personality surfer       # Chill bro vibes
   /personality noir         # Hard-boiled detective narration
   /personality uwu          # Maximum cute uwu-speak
   /personality philosopher  # Deep contemplation
   /personality hype         # MAXIMUM ENERGY!!!
   ```

5. **/personality vs SOUL.md**:
   | Aspect | SOUL.md | `/personality` |
   |--------|---------|----------------|
   | Scope | Global, persistent default | Session-level overlay |
   | Persistence | Survives restarts | Resets per session |
   | Use case | Core identity | Temporary mode shifts |
   | Relationship | Foundation | Supplements/replaces for session |

6. **Custom Personalities** (config.yaml):
   ```yaml
   agent:
     personalities:
       codereviewer: >
         You are a meticulous code reviewer. Identify bugs, security issues,
         performance concerns, and unclear design choices. Be precise and constructive.
   ```
   Usage: `/personality codereviewer`

7. **Prompt Stack Hierarchy** (Bottom → Top):
   ```
   1. SOUL.md                    ← Foundation (agent identity)
   2. AGENTS.md                  ← Project context
   3. .cursorrules               ← Editor-specific rules
   4. /personality overlay       ← Session override
   ```

8. **Security**: SOUL.md content scanned for prompt injection before inclusion

## Pitfalls
- **SOUL.md not loading** → Verify at `~/.hermes/SOUL.md`, not project dir; check `skip_context_files`
- **Personality not switching** → Use `/personality <name>` exactly; check spelling
- **Custom personality not working** → Verify `config.yaml` syntax under `agent.personalities`

## Verification
- Edit `~/.hermes/SOUL.md` → restart chat → personality evident
- `/personality` lists all 14 built-in + custom
- `/personality concise` switches for session
- Custom personality in config.yaml works

## References
- `references/commands.md` — CLI commands
- `references/soul-template.md` — Production SOUL.md template
- `references/builtins.md` — All 14 built-in personalities