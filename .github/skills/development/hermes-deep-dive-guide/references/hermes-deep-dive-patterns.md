# Hermes Deep Dive Patterns

## Architecture Overview

```
┌─────────────────────────────────────┐
│          System Prompt              │
│  SOUL.md (slot #1) + AGENTS.md      │
├─────────────────────────────────────┤
│          Profile Config             │
│  ~/.hermes/config.yaml              │
├─────────────────────────────────────┤
│         Memory Injection            │
│  USER.md + MEMORY.md (header)       │
├─────────────────────────────────────┤
│          Skill System               │
│  Auto-load on trigger + workflows   │
├─────────────────────────────────────┤
│          Agent Loop                 │
│  Think → Act → Observe → Reflect    │
└─────────────────────────────────────┘
```

## Key Components

| Component | Location | Purpose |
|-----------|----------|---------|
| SOUL.md | `~/.hermes/SOUL.md` | Identity, core rules, profile routing |
| Config | `~/.hermes/config.yaml` | Providers, models, tools, hooks |
| USER.md | `~/.hermes/memories/USER.md` | User profile (1375 chars) |
| MEMORY.md | `~/.hermes/memories/MEMORY.md` | Agent notes (2200 chars) |
| Skills | `~/.hermes/skills/` | SKILL.md with workflows |
| MCP Servers | Config | External tool integration |

## Profile Isolation

- Each profile: separate `memories/`, `skills/`, `plugins/`, `cron/`
- SOUL.md shared at root
- Cross-profile reads blocked by default

## Learning Loop

```
Interaction → Skill Triggered → Execution → Result → 
  → Memory Update (auto/explicit) → Skill Improve → Next Interaction
```

## Hook System

| Hook | Trigger |
|------|---------|
| session-logger | Session start/end |
| session-auto-commit | Session end |
| governance-audit | Config changes |

## Error Handling Patterns

```python
# Skill error handling
try:
    result = await execute_skill(skill_name, params)
except SkillNotFoundError:
    # Fallback to base behavior
    pass
except SkillExecutionError as e:
    logger.error(f"Skill {skill_name} failed: {e}")
    # Graceful degradation
```

## Platform Detection

```python
import sys
import platform

def get_platform():
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "macos"
    elif system == "linux":
        return "linux"
    return "unknown"

# Usage in skills
if get_platform() == "windows":
    # Windows-specific paths/commands
    pass
else:
    # Unix-like paths/commands
    pass
```

## Skill Workflow Example

```yaml
# In SKILL.md
workflow:
  phase_1: "Setup"
  phase_2: "Execute"
  phase_3: "Verify"
```

## Testing Skills

```bash
# Test skill
hermes skill test my-skill

# Debug skill
hermes --debug "use my-skill to do X"
```