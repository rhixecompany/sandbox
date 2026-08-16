# Cross-Platform AI Agent & MCP Server Sync — Detailed Specification

**Date:** 2026-08-16  
**Status:** draft  
**Linked Plan:** `.hermes/plans/2026-08-16_142300_cross-platform-agent-sync.md`

---

## 1. Purpose & Scope

### Purpose
Ensure all AI agent platforms (Hermes, OpenAI Codex, GitHub Copilot, OpenCode, VS Code MCP) in the Alexa workspace are:
- Fully operational with valid configurations
- Equipped with skills (SKILL.md files) that follow best practices
- Configured with working hooks for automation
- Equipped with quick commands for efficient use
- Connected to MCP servers where supported
- Synchronized where synchronization adds value

### Scope
**In scope:**
- Hermes Agent (primary — already mostly configured, needs audit + gap fill)
- OpenCode (needs auth + model config + skill wrappers)
- VS Code MCP (`.vscode/mcp.json` audit + MCP extension setup)
- GitHub Copilot CLI (discover + configure if installed)
- OpenAI Codex CLI (discover + configure if installed)
- Shell hooks across all platforms that support them
- Quick commands across all platforms
- Cross-platform documentation

**Out of scope:**
- Installing platforms that aren't present (only configure what exists)
- ReImplementing existing working configurations
- Platform-specific features that don't have cross-platform equivalents

---

## 2. Environment Inventory (Verified)

### 2.1 Hermes Agent
- **Version:** v0.20.1 (2026.8.13) via pip
- **Config:** `C:\Users\Alexa\AppData\Local\hermes\config.yaml`
- **Skills:** 105 installed (`C:\Users\Alexa\AppData\Local\hermes\skills\`)
- **MCP Servers:** 21 enabled (honcho, ast-grep, code-sandbox, fetch, filesystem, github, mcp-docker, memory, mindstudio, neon, playwright, sequential-thinking, python-quality, tooling-lint, tooling-config, context7, sentry, tavily, parallel-search, parallel-task, smithery)
- **Profiles:** 14 total (default + 13 stopped)
- **Default model:** upstage/solar-pro4:free (Nous Portal)
- **Stopped profiles:** All 13 on deepseek-v4-flash-free (opencode-zen)
- **Providers:** opencode-zen, openrouter, gemini, ollama-cloud, xai, huggingface, deepseek, nous
- **Fallback chain:** opencode-zen → openrouter → gemini → ollama-cloud

### 2.2 OpenCode
- **Version:** v1.18.13
- **Path:** `C:\nvm4w\nodejs\opencode.cmd`
- **Config:** `C:\Users\Alexa\.opencode\opencode.json` (may exist)
- **Models:** Not listed (needs auth)
- **Skills:** TBD (OpenCode has its own skills system)

### 2.3 GitHub CLI (gh)
- **Version:** v2.97.0
- **Path:** `C:\Program Files\GitHub CLI\gh.exe`
- **Auth:** TBD (needs `gh auth status`)
- **Skills:** Not applicable (gh is a CLI tool, not an AI agent)

### 2.4 VS Code
- **Version:** v1.132.0
- **Path:** `C:\Program Files\Microsoft VS Code\Code.exe`
- **MCP config:** `.vscode/mcp.json` exists (needs audit)
- **Settings:** `.vscode/settings.json` may have MCP settings
- **Extensions:** TBD (MCP-related extensions needed)

### 2.5 OpenAI Codex
- **Status:** TBD (check if installed: `which codex` or `where codex`)
- **Version:** TBD
- **Auth:** TBD

### 2.6 GitHub Copilot CLI
- **Status:** TBD (check if installed: `which copilot` or `where copilot`)
- **Version:** TBD
- **Auth:** TBD

### 2.7 Disk Space
- **C: drive:** 237G total, 231G used, 6.3G free (98% full)
- **Recommendation:** Run cleanup before heavy operations

---

## 3. Platform-Specific Specifications

### 3.1 Hermes Agent (Baseline Platform)

**Current state:** Well-configured but needs audit + gap fill

**Tasks:**
1. Audit all 105 skills — verify each has valid SKILL.md with proper YAML frontmatter
2. Audit all 21 MCP servers — verify each is functional (hermes mcp test)
3. Audit all 14 profiles — verify configuration is correct
4. Check for stale/duplicate skills
5. Verify hooks are registered and functional
6. Verify quick commands are available

**Acceptance criteria:**
- All skills pass frontmatter validation
- All MCP servers respond to test requests
- All profiles have correct model/provider configuration
- No duplicate or stale skills
- Hooks fire correctly on trigger
- Quick commands are documented and working

### 3.2 OpenCode

**Current state:** Installed (v1.18.13) but not configured

**Tasks:**
1. Configure authentication (API keys for providers)
   - Set OPENCODE_ZEN_API_KEY if using opencode-zen
   - Set other provider API keys as needed
2. Configure models
   - Select deepseek-v4-flash-free via opencode-zen (matching Hermes stopped profiles)
   - Or configure other preferred models
3. Configure MCP servers (if OpenCode supports MCP)
   - Check OpenCode MCP support: `opencode mcp` or similar
   - Configure supported MCP servers
4. Create OpenCode-specific skill wrappers
   - Wrap key Hermes skills for OpenCode use
   - Create OpenCode-specific SKILL.md files
5. Create OpenCode quick command aliases
6. Test model connectivity

**Acceptance criteria:**
- OpenCode authenticates successfully
- Models are selectable and responsive
- MCP servers (if supported) are configured
- Skill wrappers load correctly
- Quick commands work

### 3.3 VS Code MCP

**Current state:** `.vscode/mcp.json` exists (needs audit), VS Code v1.132.0 installed

**Tasks:**
1. Audit `.vscode/mcp.json`
   - Read current content
   - Verify all 21 Hermes MCP servers are configured
   - Check for broken references
2. Check `.vscode/settings.json` for MCP-related settings
3. Install VS Code extensions for MCP support
   - Check for existing MCP extensions
   - Install if missing (e.g., "MCP Server" extensions)
4. Create VS Code-specific skill wrappers (if needed)
5. Create VS Code quick command aliases
6. Test MCP server connectivity from VS Code

**Acceptance criteria:**
- `.vscode/mcp.json` contains valid MCP server configurations
- All configured MCP servers are reachable
- VS Code MCP extensions are installed and functional
- Quick commands work within VS Code

### 3.4 GitHub Copilot CLI

**Current state:** TBD (check installation)

**Tasks:**
1. Check if Copilot CLI is installed
   - `where copilot` or `Get-Command copilot` on Windows
2. If installed:
   - Configure authentication (`copilot auth` or similar)
   - Configure models/settings
   - Configure MCP servers (if supported)
   - Create Copilot-specific skill wrappers
   - Create Copilot quick command aliases
3. If not installed:
   - Document as out-of-scope (user can install separately)

**Acceptance criteria:**
- If installed: Copilot authenticates, models work, skills/hooks/commands configured
- If not installed: Documented in cross-platform report

### 3.5 OpenAI Codex CLI

**Current state:** TBD (check installation)

**Tasks:**
1. Check if Codex CLI is installed
   - `where codex` or `Get-Command codex` on Windows
2. If installed:
   - Configure authentication
   - Configure models/settings
   - Configure MCP servers (if supported)
   - Create Codex-specific skill wrappers
   - Create Codex quick command aliases
3. If not installed:
   - Document as out-of-scope

**Acceptance criteria:**
- If installed: Codex authenticates, models work, skills/hooks/commands configured
- If not installed: Documented in cross-platform report

---

## 4. Cross-Platform Skill Design

### 4.1 Skill Format Standard

All skills across all platforms must follow this structure:

```
<skill-name>/
├── SKILL.md           # Main skill definition (YAML frontmatter + markdown body)
├── references/        # Long-form reference content
│   └── *.md
├── scripts/           # Deterministic helper scripts
│   └── *.py / *.sh
├── templates/         # Output templates
│   └── *
└── assets/            # Static assets (images, etc.)
    └── *
```

### 4.2 SKILL.md Frontmatter Standard

```yaml
---
name: <skill-name>
description: <Clear, concise description of what the skill does>
version: 1.0.0
author: <author name>
license: MIT
tags: [<tag1>, <tag2>]
metadata:
  platforms:
    - hermes
    - opencode (if applicable)
    - vscode (if applicable)
    - copilot (if applicable)
    - codex (if applicable)
  mcp_servers:
    - <mcp-server-name> (if skill uses an MCP server)
---
```

### 4.3 Platform Adaptation Patterns

**Hermes:** Native SKILL.md support — skills load via `skill_view` or `/skill` slash command

**OpenCode:** May support SKILL.md via plugin system or custom integration — wrap Hermes skills

**VS Code:** Skills implemented as VS Code extensions or snippets — wrap as snippets/extensions

**Copilot/Codex:** Skills implemented as prompt files or configuration — wrap as prompt templates

### 4.4 Shared Skill Catalog

Skills that should exist on all platforms (where supported):

| Skill | Hermes | OpenCode | VS Code | Copilot | Codex |
|-------|--------|----------|---------|---------|-------|
| brainstorming | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| plans-and-specs | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| sequential-thinking | ✅ (MCP) | 🔄 | 🔄 | 🔄 | 🔄 |
| disk-cleanup | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| github-pr-workflow | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| code-review | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| test-driven-development | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| subagent-driven-development | ✅ | ❌ | ❌ | ❌ | ❌ |

🔄 = Wrap/adapter needed, ❌ = Not applicable to platform

---

## 5. Hook Design

### 5.1 Hook Structure Standard

```
<hook-name>/
├── hook.sh          # Shell entry point
├── hook.py          # Python logic (if needed)
├── hooks.json       # Hook configuration (trigger, event, etc.)
└── README.md        # Hook documentation
```

### 5.2 Hooks to Create/Configure

| Hook | Hermes | OpenCode | VS Code | Copilot | Codex |
|------|--------|----------|---------|---------|-------|
| session-logger | ✅ | 🔄 | ❌ | ❌ | ❌ |
| pre-exec-validate | ✅ | 🔄 | ❌ | ❌ | ❌ |
| post-exec-state-log | ✅ | 🔄 | ❌ | ❌ | ❌ |
| governance-audit | ✅ | ❌ | ❌ | ❌ | ❌ |

🔄 = Platform-equivalent hook needed, ❌ = Not applicable

### 5.3 Hook Registration

**Hermes:** `hermes hooks register <hook-name>` or via config.yaml

**OpenCode:** TBD — check OpenCode hook/extension system

**VS Code:** Hooks via VS Code extensions or tasks.json

**Copilot/Codex:** TBD — check respective hook/extension systems

---

## 6. Quick Command Design

### 6.1 Quick Command Standard

All quick commands must be:
- Invoked with a consistent name across platforms (where possible)
- Documented with exact syntax
- Have fallback behavior on platforms that don't support them

### 6.2 Quick Commands to Create

| Command | Hermes | OpenCode | VS Code | Copilot | Codex |
|---------|--------|----------|---------|---------|-------|
| `/skill <name>` | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| `/plan` | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| `/brainstorm` | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| `/mcp-test` | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| `/disk-cleanup` | ✅ (plugin) | 🔄 | 🔄 | ❌ | ❌ |
| `/doctor` | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| `/model` | ✅ | 🔄 | 🔄 | 🔄 | 🔄 |
| `/profiles` | ✅ | ❌ | ❌ | ❌ | ❌ |

🔄 = Platform-equivalent command needed, ❌ = Not applicable

---

## 7. MCP Server Configuration

### 7.1 MCP Servers (21 total — Hermes baseline)

| # | Name | Transport | Hermes | OpenCode | VS Code | Copilot | Codex |
|---|------|---------|--------|----------|---------|---------|-------|
| 1 | honcho | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 2 | ast-grep | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 3 | code-sandbox | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 4 | fetch | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 5 | filesystem | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 6 | github | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 7 | mcp-docker | docker | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 8 | memory | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 9 | mindstudio | mindstudio | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 10 | neon | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 11 | playwright | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 12 | sequential-thinking | npx | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 13 | python-quality | local | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 14 | tooling-lint | local | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 15 | tooling-config | local | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 16 | context7 | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 17 | sentry | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 18 | tavily | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 19 | parallel-search | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 20 | parallel-task | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |
| 21 | smithery | HTTPS | ✅ | 🔄 | 🔄 | ❌ | ❌ |

🔄 = Configure if platform supports MCP, ❌ = Platform doesn't support MCP

### 7.2 VS Code MCP Configuration (.vscode/mcp.json)

Expected format:
```json
{
  "mcpServers": {
    "honcho": {
      "url": "https://mcp.honcho.dev/"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    },
    ...
  }
}
```

### 7.3 OpenCode MCP Configuration

TBD — check OpenCode MCP configuration format

---

## 8. Implementation Phases & Tasks

### Phase 1: Audit & Inventory [COMPLETE]
- [x] Hermes: full inventory (skills, MCP, profiles, hooks) — DONE
- [x] OpenCode: version confirmed — DONE
- [x] GitHub CLI: version confirmed — DONE
- [x] VS Code: version + MCP config confirmed — DONE
- [x] Disk space: measured — DONE
- [x] `.github/skills/`: counted (311 items) — DONE
- [x] `.hermes/skills/`: counted (105 items) — DONE

### Phase 2: Discovery (PENDING)
- [ ] Check OpenCode auth status: `opencode auth` or check config
- [ ] Check gh auth status: `gh auth status`
- [ ] Read `.vscode/mcp.json` — audit existing MCP config
- [ ] Read `.vscode/settings.json` — check for MCP settings
- [ ] Check for Copilot CLI: `where copilot`
- [ ] Check for Codex CLI: `where codex`
- [ ] List VS Code extensions: `code --list-extensions`
- [ ] Audit `.github/skills/` — find which items are actual SKILL.md directories

### Phase 3: Create/Update Skills (PENDING)
- [ ] Hermes: audit 105 skills — verify SKILL.md quality
- [ ] Create missing skills on Hermes (if any gaps found)
- [ ] OpenCode: create skill wrappers for key Hermes skills
- [ ] VS Code: create skill snippets/extensions for key skills
- [ ] Copilot/Codex: create prompt templates for key skills (if installed)

### Phase 4: Create/Update Hooks (PENDING)
- [ ] Hermes: verify existing hooks work
- [ ] OpenCode: create platform-equivalent hooks (if supported)
- [ ] VS Code: create tasks.json hooks (if applicable)

### Phase 5: Create/Update Quick Commands (PENDING)
- [ ] Hermes: document existing quick commands
- [ ] OpenCode: create quick command aliases
- [ ] VS Code: create keyboard shortcuts / commands for quick operations
- [ ] Copilot/Codex: create prompt shortcuts (if installed)

### Phase 6: MCP Server Configuration (PENDING)
- [ ] VS Code: update `.vscode/mcp.json` with all 21 MCP servers
- [ ] OpenCode: configure MCP servers (if supported)
- [ ] Test MCP connectivity from each platform

### Phase 7: Testing & Verification (PENDING)
- [ ] Test each platform's skills load correctly
- [ ] Test hooks execute properly
- [ ] Test quick commands work
- [ ] Test MCP server connectivity from each platform
- [ ] Cross-platform smoke tests

### Phase 8: Documentation (PENDING)
- [ ] Create cross-platform quick reference document
- [ ] Document platform-specific setup instructions
- [ ] Document sync patterns and divergence points
- [ ] Update AGENTS.md with cross-platform guidance

---

## 9. Acceptance Criteria (Summary)

### Hermes
- [ ] All 105 skills have valid SKILL.md with proper frontmatter
- [ ] All 21 MCP servers pass `hermes mcp test`
- [ ] All 14 profiles are correctly configured
- [ ] No stale or duplicate skills
- [ ] Hooks are registered and functional
- [ ] Quick commands are documented

### OpenCode
- [ ] Authenticated with at least one provider
- [ ] Models are selectable and responsive
- [ ] MCP servers configured (if supported)
- [ ] Key skill wrappers created and loadable
- [ ] Quick commands work

### VS Code
- [ ] `.vscode/mcp.json` has valid MCP server configs for all 21 servers
- [ ] MCP extensions installed and functional
- [ ] MCP servers reachable from VS Code
- [ ] Quick commands/snippets work
- [ ] Skill snippets/extensions load correctly

### Copilot (if installed)
- [ ] Authenticated
- [ ] Models/configured
- [ ] Skills/hooks/commands configured

### Codex (if installed)
- [ ] Authenticated
- [ ] Models/configured
- [ ] Skills/hooks/commands configured

### Cross-Platform
- [ ] Cross-platform quick reference document exists
- [ ] Platform-specific setup instructions documented
- [ ] Sync patterns documented
- [ ] AGENTS.md updated with cross-platform guidance

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| OpenCode MCP support unknown | Medium | Medium | Check first; fall back to skill wrappers only |
| VS Code MCP extensions may conflict | Low | Medium | Test one extension at a time |
| Disk space may block operations | High | Medium | Run cleanup first (Phase 0) |
| Copilot/Codex may not be installed | Medium | Low | Check first; skip if absent |
| Skill content divergence across platforms | Medium | Low | Use shared SKILL.md as source of truth; wrap don't rewrite |
| MCP server auth credentials differ per platform | High | High | Use same credentials where possible; document per-platform auth |
| OpenCode auth setup may require interactive steps | Medium | Medium | Use config file where possible |

---

## 11. Open Questions (to resolve before Phase 3)

1. **VS Code MCP:** What's currently in `.vscode/mcp.json`? Are the MCP servers functional?
2. **OpenCode auth:** Is OpenCode already authenticated? What providers are configured?
3. **Copilot/Codex:** Are these CLIs installed? If so, what state are they in?
4. **Skill sync depth:** Should we create full SKILL.md copies on each platform, or lightweight wrappers?
5. **Hook parity:** Do OpenCode/VS Code/Copilot/Codex support hooks similar to Hermes? If not, skip.
6. **Quick command format:** What's the equivalent of `/skill` on each platform?
7. **MCP transport compatibility:** VS Code MCP uses JSON config — do all 21 Hermes MCP servers work with this format?

---

## 12. Reference Documents

- [Cross-Platform Agent Sync Plan](.hermes/plans/2026-08-16_142300_cross-platform-agent-sync.md)
- [Hermes Agent Skill Authoring Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
- [Hermes Agent MCP Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [OpenCode Documentation](https://opencode.ai/docs)
- [VS Code MCP Extensions](https://marketplace.visualstudio.com/search?term=mcp)
- [GitHub Copilot CLI](https://github.com/github/copilot-cli)
- [OpenAI Codex CLI](https://github.com/openai/codex)
