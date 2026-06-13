# Phase 5: Docs Inventory — Log

**Date:** 2026-06-13  
**Scope:** `docs/` root and subdirectories — hooks, skills, plugins, MCP servers, configuration files

---

## 1. Hooks Inventory

### Installed Hooks (Active Profile: `default`)

| Hook | Path | Events | Status |
|------|------|--------|--------|
| session-logger | `~/.hermes/hooks/session-logger/` | on_session_start, on_session_end, pre_llm_call | ✅ Active |
| session-auto-commit | `~/.hermes/hooks/session-auto-commit/` | on_session_end | ✅ Active |
| governance-audit | `~/.hermes/hooks/governance-audit/` | on_session_start, on_session_end, pre_llm_call | ✅ Active |

### Profile Hooks Availability

| Profile | Hooks Copied? | Notes |
|---------|---------------|-------|
| default | ✅ (native) | 3 hooks active |
| adminbot | ✅ | Pre-existing, has hooks |
| code-architect | ❌ | Created without `--clone-all`, no hooks dir |
| research-analyst | ❌ | Created without `--clone-all`, no hooks dir |
| creative-director | ❌ | Created without `--clone-all`, no hooks dir |
| exec-assistant | ❌ | Created without `--clone-all`, no hooks dir |
| patient-tutor | ❌ | Created without `--clone-all`, no hooks dir |

> **Blocker:** `hermes profile create <name> --clone-all` times out (60s+). Hooks not propagated to new profiles.

### Documentation References
- `docs/user-guide/features/hooks/README.md` — comprehensive hook guide (extracted from Hermes docs)
- `docs/hermes/hermes-agent.nousresearch.com_docs_user-guide_features_hooks.md` — full official docs extraction

---

## 2. Skills Inventory

### Bundled Skills (per new profile: 73 skills across 16 categories)

| Category | Skills Count | Example Skills |
|----------|-------------|----------------|
| software-development | 9 | systematic-debugging, test-driven-development, spike, plan, requesting-code-review |
| devops | 2 | kanban-orchestrator, kanban-worker |
| autonomous-ai-agents | — | (category dir exists) |
| creative | — | |
| data-science | — | |
| dogfood | — | |
| email | — | |
| github | — | |
| media | — | |
| mlops | — | |
| note-taking | — | |
| productivity | — | |
| research | — | |
| smart-home | — | |
| social-media | — | |
| yuanbao | — | |

> **Verification:** `ls ~/.hermes/profiles/code-architect/skills/software-development/` → 9 skills

### Available Skill Hub (per `hermes skills browse`)
- 289 skills in `.github/skills/` (local repo)
- Agentskills.io ecosystem skills
- Community skills (wondelai/skills, litprog-skill, etc.)

### Documentation References
- `docs/hermes/hermes-agent.nousresearch.com_docs_user-guide_features_skills.md` — full skills system docs
- `docs/phase1-skills-audit.md` — prior audit
- `docs/phase1-skills-audit-log.md` — prior audit log

---

## 3. Plugins Inventory

### Installed Plugins (Active Profile: `default`)

| Plugin | Path | Type | Status |
|--------|------|------|--------|
| disk-cleanup | `~/.hermes/plugins/disk-cleanup/` | standalone | ✅ Active |
| model-providers/openrouter | `~/.hermes/plugins/model-providers/openrouter/` | model-provider | ✅ Active |
| security-guidance | `~/.hermes/plugins/security-guidance/` | standalone | ✅ Active |

### Profile Plugins Availability

| Profile | Plugins Copied? |
|---------|-----------------|
| default | ✅ (3 plugins) |
| adminbot | ✅ (pre-existing) |
| code-architect | ❌ (no plugins dir) |
| research-analyst | ❌ |
| creative-director | ❌ |
| exec-assistant | ❌ |
| patient-tutor | ❌ |

> **Blocker:** Same `--clone-all` timeout prevents plugin propagation.

### Documentation References
- `docs/hermes/hermes-agent.nousresearch.com_docs_user-guide_features_plugins.md` — full plugin system docs
- `docs/hermes/github.com_0xNyk_awesome-hermes-agent.md` — ecosystem plugins list

---

## 4. MCP Servers Inventory

### Configured MCP Servers (from `config.yaml`)

| Server | Type | Status | Tools Filtered |
|--------|------|--------|----------------|
| filesystem | stdio (npx) | Available | — |
| github | stdio (npx) | Installed (disabled) | include: [create_issue, list_issues, search_code] |
| linear | HTTP (OAuth) | Enabled | — |
| n8n | HTTP | Available | — |

> **Source:** `~/.hermes/config.yaml` → `mcp_servers:` section

### Available MCP Catalog (per `hermes mcp catalog`)
- n8n, linear, github, filesystem, stripe, googledrive, codex, and 20+ more

### Documentation References
- `docs/hermes/hermes-agent.nousresearch.com_docs_user-guide_features_mcp.md` — MCP core docs
- `docs/hermes/hermes-agent.nousresearch.com_docs_guides_use-mcp-with-hermes.md` — practical usage guide
- `docs/phase2-mcp-research-log.md` — Phase 2 research on specific MCP servers

---

## 5. Configuration Files Inventory

### Global Config (`~/.hermes/config.yaml`)
- Model: `stepfun/step-3.7-flash:free`
- Terminal backend: local
- Toolsets: web, terminal, file, search, skills, memory, cronjob, etc.
- MCP servers: 4 configured
- Hooks: 3 enabled
- Plugins: 3 enabled

### Project Config (`.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`)
- **Root:** `AGENTS.md` (this workspace)
- **Bash/:** `AGENTS.md` (automation toolkit)
- **projects/:** various per-project `AGENTS.md`
- **docs/hermes/:** extracted documentation (no context files)

### Context File Loading Priority
```
.hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
```
SOUL.md loaded independently from `HERMES_HOME`

---

## 6. Verification Summary

| Component | Global (default) | New Profiles (x6) | Blocker |
|-----------|------------------|-------------------|---------|
| Hooks (3) | ✅ | ❌ | `--clone-all` timeout |
| Skills (73) | ✅ | ✅ (bundled synced) | — |
| Plugins (3) | ✅ | ❌ | `--clone-all` timeout |
| MCP Servers (4) | ✅ | ❌ (config not cloned) | `--clone-all` timeout |
| SOUL.md | ✅ | ✅ (seeded) | — |
| config.yaml | ✅ | ❌ | `--clone-all` timeout |
| .env | ✅ | ✅ (created empty) | — |

---

## Next Actions (Phase 6)
1. Configuration Hierarchy Audit across all profiles
2. Attempt manual hook/plugin copy to new profiles as workaround
3. Validate config hierarchy: `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`