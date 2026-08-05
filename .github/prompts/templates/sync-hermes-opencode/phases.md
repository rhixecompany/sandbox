# Sync Hermes ↔ OpenCode Phases

## Phase 1: Inventory Instructions & Agents

### Objective

Build complete inventories of all syncable assets across all 3 platforms.

### Steps

1. **Hermes Inventory**
   - `skills/` — List all `SKILL.md` files with frontmatter (name, description, tags)
   - `plugins/` — List all enabled plugins
   - `hooks/` — List all hook scripts with triggers
   - `profiles/` — List profiles with their SOUL/USER/MEMORY
   - `config.yaml` — Extract model, toolsets, MCP servers

2. **OpenAI Codex Inventory**
   - `~/.codex/agents/*.toml` — Parse agent definitions
   - `~/.codex/skills/` — List skills if present
   - `~/.codex/config.toml` — Extract configuration

3. **OpenCode Inventory**
   - `~/.opencode/config` — Parse configuration
   - Workspace `opencode.json` — Project-level settings
   - `~/.opencode/agent/` — Agent configurations if any

### Gate

- [ ] Inventories complete for all 3 platforms
- [ ] Personality/profile mappings created (Hermes profile ↔ OpenCode agent ↔ Codex agent)

---

## Phase 2: Identify Agent Roots

### Objective

Confirm and document the canonical root paths for each platform.

### Steps

1. Verify each root exists and is accessible
2. Document absolute paths (Windows-style for consistency)
3. Note any platform-specific path quirks

### Expected Roots

| Platform | Root Path |
|----------|-----------|
| Hermes | `C:\Users\Alexa\AppData\Local\hermes\` |
| OpenAI Codex | `%USERPROFILE%\.codex\` |
| OpenCode | `%USERPROFILE%\.opencode\` + workspace `opencode.json` |

### Gate

- [ ] All 3 roots confirmed
- [ ] Paths documented in `docs/orchestrator-progress.md`

---

## Phase 3: Bidirectional Sync

### Objective

Sync assets between platforms, resolving conflicts.

### Sync Map

| Asset Type | Hermes → Codex | Hermes → OpenCode | Codex ↔ OpenCode |
|------------|----------------|-------------------|------------------|
| Skills | `skills/` → `~/.codex/skills/` | `skills/` → workspace skills | Manual review |
| Plugins | `plugins/` → N/A | `plugins/` → N/A | N/A |
| Hooks | `hooks/` → N/A | `hooks/` → N/A | N/A |
| Agents | `profiles/*.md` → `~/.codex/agents/*.toml` | `profiles/*.md` → `~/.opencode/agent/` | Format conversion |
| Config | `config.yaml` ↔ `~/.codex/config.toml` | `config.yaml` ↔ `~/.opencode/config` | Cross-validate |

### Conflict Resolution

1. **Hermes wins** for profile identity (SOUL/USER/MEMORY)
2. **OpenCode wins** for workspace-specific config (`opencode.json`)
3. **Codex wins** for agent TOML format
4. Document all conflicts in `docs/orchestrator-progress.md`

### Gate

- [ ] Sync report written
- [ ] Conflicts resolved or documented

---

## Phase 4: Verify Completion

### Objective

Verify all critical assets are in sync across platforms.

### Checks

- [ ] All Hermes skills have Codex/OpenCode equivalents (or documented gap)
- [ ] All profiles map to agents on both platforms
- [ ] Config values consistent (model, toolsets, MCP servers)
- [ ] No orphaned files on any platform
- [ ] Verification report written to `docs/orchestrator-verification.md`

### Gate

- [ ] Verification report complete
- [ ] All critical assets in sync
