# Cross-Platform AI Agent & MCP Server Sync — Master Implementation Plan

**Date:** 2026-08-16  
**Status:** in_progress  
**Goal:** Create if not exists / update / debug / fix / enhance skills, hooks, and quick commands for ALL AI agents (Hermes, OpenAI Codex, GitHub Copilot, OpenCode, VS Code MCP) across all platforms — making them fully operational and synchronized.

---

## Environment Inventory

### Installed Tools & Versions

| Tool | Version | Path |
|------|---------|------|
| Hermes Agent | v0.20.1 (2026.8.13) | pip install |
| OpenCode | v1.18.13 | `C:\nvm4w\nodejs\opencode.cmd` |
| GitHub CLI (gh) | v2.97.0 | `C:\Program Files\GitHub CLI\gh.exe` |
| VS Code | v1.132.0 | `C:\Program Files\Microsoft VS Code\Code.exe` |
| Python | 3.13.14 + 3.11.15 | System + venv |
| Node.js | v26.5.0 | `C:\nvm4w\nodejs` |
| npm | v10.x | `C:\nvm4w\nodejs\npm.cmd` |
| Bun | v1.3.14 | `C:\Users\Alexa\.bun\bin\bun.exe` |
| Docker | v29.7.2 | `C:\Program Files\Docker` |
| Git | v2.55.0 | `C:\Program Files\Git` |

### Hermes State

| Dimension | Value |
|-----------|-------|
| Config | `C:\Users\Alexa\AppData\Local\hermes\config.yaml` |
| Skills | 105 installed (local + hub) |
| MCP Servers | 21 enabled |
| Profiles | 14 (default + 13 stopped) |
| Default model | upstage/solar-pro4:free (Nous Portal) |
| Stopped profiles | deepseek-v4-flash-free (opencode-zen) |

### OpenCode State
- v1.18.13 installed, no models listed (needs auth/config)

### GitHub CLI State
- gh v2.97.0 available, needs auth check

### VS Code State
- v1.132.0 installed
- `.vscode/mcp.json` exists (from previous session)
- `.vscode/settings.json` may have MCP config

### Disk State
- C: 237G total, 231G used, **6.3G free (98% full)**
- SandBox: large (multiple subrepos, skills, node_modules)

### `.github/skills/` — 311 items (NOT SKILL.md files)
These are files/directories in `.github/skills/`. Need to determine which are actual skill directories with SKILL.md files vs other content.

### `.hermes/skills/` — 105 items
Hermes-installed skills (local + hub). These are the canonical skill locations.

---

## Open Questions

1. **VS Code MCP integration:** Are the MCP servers in `.vscode/mcp.json` actually functional? Does the user want VS Code to use the same 21 MCP servers as Hermes?
2. **OpenCode setup:** Does the user want OpenCode configured with the same providers/models as Hermes (deepseek-v4-flash-free via opencode-zen)?
3. **GitHub Copilot:** Is Copilot CLI (`copilot`) installed? What's the current Copilot integration state?
4. **OpenAI Codex:** Is Codex CLI installed? What's its integration state?
5. **Skill sync scope:** Should `.github/skills/` mirror `.hermes/skills/`? Or should each platform have independent skills?
6. **Hooks:** Are shell hooks needed for OpenCode, Copilot, Codex, or VS Code? What hooks are currently configured?
7. **Quick commands:** What quick commands exist for each platform? Which need creating/enhancing?

---

## Implementation Phases

### Phase 1: Audit & Inventory (COMPLETE)
- [x] Hermes: config, skills, MCP servers, profiles, hooks — inventoried
- [x] OpenCode: version confirmed, models/auth TBD
- [x] GitHub CLI: version confirmed, auth TBD
- [x] VS Code: version confirmed, MCP config exists (.vscode/mcp.json)
- [x] Disk space: 98% full — cleanup needed before heavy operations
- [x] `.github/skills/`: 311 items — need SKILL.md audit
- [x] `.hermes/skills/`: 105 items — canonical skill library

### Phase 2: Discovery & Research (PENDING)
For each platform, discover:
- What skills exist (SKILL.md files with proper frontmatter)
- What hooks are configured
- What quick commands are available
- What MCP servers are connected
- What's missing vs Hermes baseline

### Phase 3: Create/Update Skills (PENDING)
For each platform:
- Create SKILL.md files where missing (following SKILL.md best practices: YAML frontmatter, progressive disclosure, helper scripts)
- Update existing SKILL.md files that are stale or incomplete
- Sync skill content across platforms where appropriate

### Phase 4: Create/Update Hooks (PENDING)
For each platform:
- Create shell hook wrappers where missing
- Ensure hooks follow the established pattern (hook.sh + hook.py + hooks.json)
- Test hook execution

### Phase 5: Create/Update Quick Commands (PENDING)
For each platform:
- Document available quick commands
- Create missing quick command aliases
- Ensure consistency across platforms

### Phase 6: MCP Server Configuration (PENDING)
- VS Code: verify `.vscode/mcp.json` works
- OpenCode: configure MCP servers if supported
- Copilot/Codex: configure MCP servers if supported

### Phase 7: Testing & Verification (PENDING)
- Test each platform's skills load correctly
- Test hooks execute properly
- Test quick commands work
- Test MCP server connectivity from each platform

### Phase 8: Documentation (PENDING)
- Create cross-platform quick reference
- Document platform-specific setup instructions
- Document sync patterns and divergence points

---

## Platform-Specific Tasks

### Hermes (baseline — already mostly configured)
- [ ] Verify all 105 skills have valid SKILL.md files
- [ ] Verify all 21 MCP servers are functional
- [ ] Verify all profiles are configured correctly
- [ ] Check for stale/duplicate skills

### VS Code
- [ ] Audit `.vscode/mcp.json` — verify all 21 MCP servers configured
- [ ] Check `.vscode/settings.json` for MCP-related settings
- [ ] Install VS Code extensions for MCP support (if needed)
- [ ] Create VS Code-specific skill wrappers if needed
- [ ] Create VS Code quick command aliases
- [ ] Test MCP server connectivity from VS Code

### OpenCode
- [ ] Configure authentication (API keys for providers)
- [ ] Configure models (deepseek-v4-flash-free via opencode-zen)
- [ ] Configure MCP servers (if OpenCode supports MCP)
- [ ] Create OpenCode-specific skill wrappers
- [ ] Create OpenCode quick command aliases
- [ ] Test model connectivity

### GitHub Copilot
- [ ] Check if Copilot CLI is installed
- [ ] Configure Copilot authentication
- [ ] Configure Copilot MCP servers (if supported)
- [ ] Create Copilot-specific skill wrappers
- [ ] Create Copilot quick command aliases

### OpenAI Codex
- [ ] Check if Codex CLI is installed
- [ ] Configure Codex authentication
- [ ] Configure Codex MCP servers (if supported)
- [ ] Create Codex-specific skill wrappers
- [ ] Create Codex quick command aliases

---

## Skill Creation Standards

All new SKILL.md files must follow:

1. **YAML frontmatter** with: `name`, `description`, `version`, `author`, `license`, `tags`
2. **Progressive disclosure** — most common workflow first, edge cases later
3. **Helper scripts** in `scripts/` directory where deterministic operations are needed
4. **References** in `references/` directory for long-form content
5. ** templates** in `templates/` directory for output skeletons
6. **No external dependencies** — prefer stdlib Python, curl, existing Hermes tools
7. **Cross-platform paths** — use env-based paths (`$HOME`, `%USERPROFILE%`)

---

## Hook Creation Standards

All new hooks must follow:

1. **Canonical structure:** `<hook-name>/hook.sh` + `<hook-name>/hook.py` + `<hook-name>/hooks.json`
2. **Wrapper script** for deployment if needed
3. **Registration** via `hermes hooks register` or platform-equivalent
4. **Testing** — verify hook fires correctly on trigger

---

## Quick Command Standards

All quick commands must:

1. Be documented with exact invocation syntax
2. Work across platforms where possible (same command name, platform-specific implementation)
3. Have fallback behavior when platform doesn't support the command

---

## Dependencies

- Phase 1 (audit) must complete before Phase 2 (discovery)
- Phase 2 (discovery) must complete before Phase 3-6 (implementation)
- Phase 3-6 can run in parallel per platform
- Phase 7 (testing) requires all implementation phases complete
- Phase 8 (documentation) requires Phase 7 complete

---

## Approval Gates

- **Phase 2 → Phase 3:** Review discovered gaps before creating skills
- **Phase 5 → Phase 6:** Review quick commands before MCP config changes
- **Phase 7:** Full verification before marking complete
- **Disk cleanup (if needed):** Destructive — requires explicit approval

---

## Verification Checklist (final)

- [ ] All platforms have skills with valid SKILL.md files
- [ ] All platforms have hooks configured and tested
- [ ] All platforms have quick commands documented and working
- [ ] MCP servers functional on each platform that supports them
- [ ] Cross-platform quick reference document created
- [ ] Platform-specific setup instructions documented
- [ ] No broken references or stale configurations
- [ ] All SKILL.md files pass frontmatter validation
- [ ] All hooks pass execution tests
- [ ] Disk space is reasonable after cleanup

---

## Research Notes (from environment inventory)

### Hermes
- 105 skills, 21 MCP servers, 14 profiles
- Default: upstage/solar-pro4:free via Nous Portal
- 13 stopped profiles all on deepseek-v4-flash-free via opencode-zen
- config.yaml has providers: opencode-zen, openrouter, gemini, ollama-cloud, xai, huggingface, deepseek, nous
- Fallback chain: opencode-zen → openrouter → gemini → ollama-cloud

### VS Code
- `.vscode/mcp.json` exists — needs content audit
- MCP servers in VS Code use the same MCP protocol as Hermes
- VS Code MCP extension needed for MCP server integration

### OpenCode
- v1.18.13 — similar to Hermes in capability
- Uses `opencode.json` for config
- May support MCP servers via extension/plugin system
- Model configuration via `opencode models` command

### GitHub CLI (gh)
- v2.97.0 — primarily for GitHub operations
- Can be used as a tool by AI agents via subprocess
- Not an AI agent itself but a critical tool

### Disk Space
- 6.3G free of 237G (98% full) — cleanup recommended before heavy operations
- Consider running `cleanup_disk.py` on SandBox and Hermes root
