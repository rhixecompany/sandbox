# sync-hermes-copilot-codex — Dependency Context Catalog

> Generated: 2026-06-20T01:30:00Z | Source: `sync-hermes-copilot-codex.prompt.md`

## Purpose Resolution

- **Purpose slug:** `sync-hermes-copilot-codex`
- **Trigger:** `/sync-hermes-copilot-codex`
- **Source file:** `sync-hermes-copilot-codex.prompt.md`
- **Source reference:** `sync-hermes-copilot-codex.prompt.txt`

---

## Forward Dependencies (from this file)

### External Paths Referenced
| Path | Line | Context |
|------|------|---------|
| `.github/agents/` | 57, 63, 67, 113 | Copilot agent definitions (199 `.agent.md` files) |
| `.github/instructions/` | 57, 61, 65, 113 | Copilot instruction files (200+ `.instructions.md` files) |
| `~/.hermes/` | 34, 89 | Hermes root: skills, plugins, hooks, profiles |
| `.github/` | 34, 91 | Copilot root (VS Code workspace) |
| `~/.codex/` | 34, 92 | Codex root (agents, config.toml) |
| `~/.opencode/` | 34 | Alternative Codex root |

### Skill Dependencies (from frontmatter `skills:` and `dependencies:`)
| Skill | Type | Purpose |
|-------|------|---------|
| `using-superpowers` | workflow | Establishes workflow foundation |
| `user-communication-preferences` | config | Loads user prefs for execution style |
| `plans-and-specs` | planning | Creates implementation plan from goal |

### Commands / Triggers
| Command | Line | Context |
|---------|------|---------|
| `/sync-hermes-copilot-codex` | 2 | This prompt's trigger |

---

## Reverse Dependencies (files referencing this file/trigger)

| File | Line | Reference Type |
|------|------|----------------|
| `sync-hermes-copilot-codex.prompt.txt` | 1 | Source TXT version with skill triggers |
| `docs/test-providers-models-context.md` | 55 | Related prompt family entry |

---

## Related Prompt Family (same skill pattern)

| File | Shared Skills |
|------|---------------|
| `test-providers-models.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `audit-skills-judge-fix.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |
| `agents-system-prompt-context-fix.prompt.md` | using-superpowers, user-communication-preferences, plans-and-specs |

---

## Target Environment Inventory

### Hermes (`C:\Users\Alexa\AppData\Local\hermes\`)
| Component | Path | Count/Status |
|-----------|------|--------------|
| Skills | `skills/` | 30-80+ dirs (including .archive) |
| Plugins | `plugins/` | 4 plugins |
| Hooks | `hooks/` | 3 hooks (session-logger, session-auto-commit, governance-audit) |
| Profiles | `profiles/` | 6 profiles (adminbot, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst) |
| Config | `config.yaml` | Main config with MCP servers, providers, etc. |

### Copilot (`.github/`)
| Component | Path | Count |
|-----------|------|-------|
| Agents | `.github/agents/` | 199 `.agent.md` files |
| Instructions | `.github/instructions/` | 200+ `.instructions.md` files |
| Workflows | `.github/workflows/` | CI/CD workflows |
| Hooks | `.github/hooks/` | Reference hooks (disposable) |

### Codex (`~/.codex/`)
| Component | Path | Count |
|-----------|------|-------|
| Agents | `.codex/agents/` | 100+ `.toml` agent files |
| Config | `.codex/config.toml` | Main config |
| Auth | `.codex/auth.json` | Authentication |

### OpenCode Alternative (`~/.opencode/`)
| Component | Path | Status |
|-----------|------|--------|
| Config | `.opencode/config` | Not found |
| Agents | `.opencode/agent/` | Not found |

---

## File Structure Summary

| File | Lines | Size | Frontmatter | Tables | Code Blocks |
|------|-------|------|-------------|--------|-------------|
| `sync-hermes-copilot-codex.prompt.md` | 139 | 5.0 KB | ✅ Valid YAML | 5 tables | 0 |
| `sync-hermes-copilot-codex.prompt.txt` | 2 | 582 B | ❌ No frontmatter | 0 | 0 |

---

## Audit Target Files (for batch processing)

1. `sync-hermes-copilot-codex.prompt.md` — Primary audit target
2. `sync-hermes-copilot-codex.prompt.txt` — Source reference, potential TXT→MD conversion