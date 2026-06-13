# Phase 6: Configuration Hierarchy Audit — Log

**Date:** 2026-06-13  
**Scope:** Full configuration hierarchy validation per `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules` order

---

## 1. Context File Hierarchy Validation

### File Presence Across Workspace

| File | Root | Bash/ | projects/*/ | docs/hermes/ | Profiles |
|------|------|-------|-------------|--------------|----------|
| `.hermes.md` | ❌ | ❌ | ❌ | ❌ | ❌ |
| `AGENTS.md` | ✅ | ✅ | 16/16 ✅ | ❌ | ❌ |
| `CLAUDE.md` | ❌ | ❌ | ❌ | ❌ | ❌ |
| `.cursorrules` | ❌ | ❌ | ❌ | ❌ | ❌ |
| `SOUL.md` | N/A | N/A | N/A | N/A | ✅ (per-profile, in `HERMES_HOME`) |

### Loading Priority (First Match Wins)
```
.hermes.md → AGENTS.md → CLAUDE.md → .cursorrules
```
**SOUL.md** loaded independently from `HERMES_HOME` as agent identity (slot #1).

### Validation Result
- **No `.hermes.md`** anywhere — AGENTS.md is the effective project context file
- **AGENTS.md** present at root + all 16 subprojects + Bash/ + Bash/docs/ = 19 total
- **No CLAUDE.md** anywhere — no Claude Code context contamination
- **No .cursorrules** anywhere — no Cursor IDE rules to inherit
- **Progressive discovery** works: subdirectory AGENTS.md files loaded when agent navigates

---

## 2. Global Configuration Audit (`~/.hermes/config.yaml`)

### Model & Provider
```yaml
model:
  default: gpt-5.4-mini
  provider: openai-codex
  base_url: https://chatgpt.com/backend-api/codex
fallback_providers:
  - provider: openrouter
    model: openrouter/owl-alpha
```

### Toolsets Enabled
`hermes-cli` (single toolset) — includes: web, terminal, file, search, skills, memory, cronjob, code_execution, delegation, messaging, github, etc.

### Terminal Backend
```yaml
terminal:
  backend: local
  timeout: 180
  container_persistent: true
```

### Hooks (3 Active)
| Hook | Enabled | Events | Script |
|------|---------|--------|--------|
| governance-audit | ✅ | on_session_start, on_session_end, pre_llm_call | `C:\Users\Alexa\AppData\Local\hermes\hooks\governance-audit\hook.sh` |
| session-auto-commit | ✅ | on_session_end | `C:\Users\Alexa\AppData\Local\hermes\hooks\session-auto-commit\hook.sh` |
| session-logger | ✅ | on_session_start, on_session_end, pre_llm_call | `C:\Users\Alexa\AppData\Local\hermes\hooks\session-logger\hook.sh` |

### MCP Servers (10 Configured)
| Server | Type | Command | Tools Filtered |
|--------|------|---------|----------------|
| ast-grep | stdio | npx @notprolands/ast-grep-mcp | include: [] |
| cli | stdio | npx (builtin) | include: [browser, clarify, code_execution, ...] |
| code-sandbox | stdio | npx node-code-sandbox-mcp | include: [] |
| fetch | stdio | npx mcp-server-fetch-typescript | prompts: false, resources: false |
| filesystem | stdio | npx @modelcontextprotocol/server-filesystem | prompts: false, resources: false |
| github | stdio | npx @modelcontextprotocol/server-github | prompts: false, resources: false |
| mcp-docker | stdio | docker mcp gateway run | enabled: true |
| memory | stdio | npx @modelcontextprotocol/server-memory | prompts: false, resources: false |
| playwright | stdio | npx @playwright/mcp@latest | include: [] |
| sequential-thinking | stdio | npx @modelcontextprotocol/server-sequential-thinking | include: [sequentialthinking] |

### Plugins (5 Enabled)
| Plugin | Type | Status |
|--------|------|--------|
| awesome-hermes-agent | standalone | ✅ |
| disk-cleanup | standalone | ✅ |
| memory/honcho | memory backend | ✅ |
| model-providers/openrouter | model provider | ✅ |
| security-guidance | standalone | ✅ |

### Personality Configuration
- 14 built-in personalities defined in `agent.personalities`
- SOUL.md loaded from `~/.hermes/SOUL.md` (pragmatic senior engineer)

---

## 3. Profile Configuration Comparison (UPDATED — `--clone-all` FIXED)

| Setting | default | adminbot | code-architect | research-analyst | creative-director | exec-assistant | patient-tutor |
|---------|---------|----------|----------------|------------------|-------------------|----------------|---------------|
| Model | gpt-5.4-mini | stepfun/step-3.7-flash | gpt-5.4-mini | gpt-5.4-mini | gpt-5.4-mini | gpt-5.4-mini | gpt-5.4-mini |
| config.yaml | Full | Full (pre-existing) | **Full clone** ✅ | **Full clone** ✅ | **Full clone** ✅ | **Full clone** ✅ | **Full clone** ✅ |
| SOUL.md | Default | Custom? | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ |
| Skills | 289 | 289 | **289** ✅ | **289** ✅ | **289** ✅ | **289** ✅ | **289** ✅ |
| Hooks (3) | ✅ | ✅ | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** |
| Plugins (5) | ✅ | ✅ | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** | **✅ Cloned** |
| MCP Servers | 10 | 10 | **10 Cloned** ✅ | **10 Cloned** ✅ | **10 Cloned** ✅ | **10 Cloned** ✅ | **10 Cloned** ✅ |
| .env | Full | Full | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ | **Cloned** ✅ |

> **✅ FIXED:** `hermes profile create <name> --clone-all` **now works** (was timing out, now completes in ~5 seconds). All profiles created after fix have full configuration parity with `default` profile including hooks, plugins, MCP servers, config.yaml, .env, and all 289 skills.

---

## 4. Skills Configuration Audit

### Skills Settings (from config.yaml)
```yaml
skills:
  external_dirs: []           # No external skill directories
  template_vars: true         # Template variable interpolation enabled
  inline_shell: false         # Inline shell execution disabled
  inline_shell_timeout: 10    # N/A
  guard_agent_created: false  # No guard on agent-created skills
  write_approval: false       # No approval needed for skill writes
  creation_nudge_interval: 15 # Skill creation nudge every 15 turns
```

### Curator Settings
```yaml
curator:
  enabled: true
  interval_hours: 168         # 7-day cycle
  min_idle_hours: 2
  stale_after_days: 30
  archive_after_days: 90
  prune_builtins: true
  backup:
    enabled: true
    keep: 5
```

### Local Skills Directory
- `~/.hermes/skills/` — Primary skill directory (16 category dirs, 73 bundled skills)
- `.github/skills/` — 289 skills (repo-local, copied to profiles via `--clone-all`)
- Profiles now have all 289 skills via `--clone-all`

---

## 5. Memory Configuration Audit

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true
  memory_char_limit: 2200     # MEMORY.md cap
  user_char_limit: 1375       # USER.md cap
  flush_min_turns: 6
  nudge_interval: 10
```

### Current Memory State
- MEMORY.md: ~1,513/2,200 chars (68% used)
- USER.md: ~133/1,375 chars (9% used)

---

## 6. Delegation Configuration Audit

```yaml
delegation:
  max_concurrent_children: 3
  max_spawn_depth: 1
  orchestrator_enabled: true
  subagent_auto_approve: false
  inherit_mcp_toolsets: true
  child_timeout_seconds: 600
```

### Subagent Toolsets
Children inherit: terminal, file, web, search, browser, code_execution, delegation, cronjob, skills, memory, session_search, etc.

---

## 7. Security Configuration Audit

```yaml
security:
  allow_private_urls: false
  redact_secrets: true
  tirith_enabled: true       # Redis-based rate limiting
  tirith_timeout: 5
  tirith_fail_open: true
```

### Approvals
```yaml
approvals:
  mode: manual
  timeout: 60
  cron_mode: deny
  mcp_reload_confirm: true
  destructive_slash_confirm: true
```

### Command Allowlist
```yaml
command_allowlist:
  - execute_code
  - "kill hermes/gateway process (self-termination)"
```

---

## 8. Per-Project AGENTS.md Inventory (19 files)

| Project | AGENTS.md Present | Key Content |
|---------|-------------------|-------------|
| Root (SandBox) | ✅ | Workspace context, conventions, validation gates |
| Bash/ | ✅ | Automation toolkit conventions, quality gates |
| Bash/docs/ | ✅ | Documentation conventions |
| projects/Banking/ | ✅ | Banking domain examples |
| projects/comicwise/ | ✅ | Comic project |
| projects/Django-Scrapy-Selenium/ | ✅ | Django + Scrapy + Selenium |
| projects/ecom/ | ✅ | E-commerce |
| projects/profile/ | ✅ | Profile management |
| projects/Python-projects/ | ✅ | Python projects |
| projects/Resume_maker/ | ✅ | Resume maker |
| projects/rhixe_scans/ | ✅ | Scans project |
| projects/rhixecompany-comics/ | ✅ | Comics company |
| projects/selenium_webdriver/ | ✅ | Selenium WebDriver |
| projects/university-libary-jsm/ | ✅ | Library JSM |
| projects/xamehi/ | ✅ | xamehi |
| projects/xamehi.tv/ | ✅ | xamehi.tv |
| projects/youtube-downloader/ | ✅ | YouTube downloader |
| projects/cookiecutter-django-tailwind/ | ✅ | Cookiecutter template |

**Convention Compliance:** All projects have AGENTS.md — progressive discovery works.

---

## 9. Missing/Needed Items (UPDATED)

### ✅ RESOLVED: `--clone-all` Blocker Fixed
All 5 task-specific profiles now have full configuration parity:
1. **Hooks** — 3 hooks cloned ✅
2. **Plugins** — 5 plugins cloned ✅
3. **MCP Servers** — 10 servers with tool filtering cloned ✅
4. **config.yaml** — Full config cloned ✅
5. **.env** — API keys/secrets cloned ✅
6. **Skills** — All 289 skills cloned ✅
7. **SOUL.md** — Personality file cloned ✅

### Configuration Hierarchy Enhancements (Optional)
1. Consider adding `.hermes.md` at root for Hermes-specific overrides (highest priority)
2. No CLAUDE.md or .cursorrules needed — no IDE conflicts
3. **SOUL.md per-profile customization recommended** — align personality with profile purpose:
   - `code-architect` → technical personality
   - `research-analyst` → technical/analytical
   - `creative-director` → creative personality
   - `exec-assistant` → concise/helpful
   - `patient-tutor` → teacher personality

---

## 10. Verification Checklist

| Check | Status | Notes |
|-------|--------|-------|
| Context file priority respected | ✅ | AGENTS.md is effective project context |
| No conflicting CLAUDE.md/.cursorrules | ✅ | None present |
| Progressive subdirectory discovery | ✅ | 19 AGENTS.md files across workspace |
| SOUL.md loaded from HERMES_HOME | ✅ | Per-profile in `~/.hermes/profiles/<name>/SOUL.md` |
| Global config.yaml valid | ✅ | All sections parse correctly |
| **Hooks configured in ALL profiles** | ✅ | 3 hooks active in all 7 profiles |
| **MCP servers in ALL profiles** | ✅ | 10 servers, tools filtered |
| **Plugins in ALL profiles** | ✅ | 5 plugins active |
| **Skills in ALL profiles** | ✅ | 289 skills (not just 73 bundled) |
| Curator enabled | ✅ | 7-day cycle, backups kept |
| Memory limits configured | ✅ | 2200/1375 char limits |
| Delegation limits set | ✅ | 3 concurrent, depth 1 |
| Security settings active | ✅ | Tirith, redaction, approvals |

---

## 11. Recommendations (UPDATED)

1. ✅ **`--clone-all` timeout FIXED** — now completes in ~5 seconds
2. **Customize SOUL.md per profile** — align personality with profile purpose (high priority)
3. **Add `.hermes.md` at root** — for Hermes-specific project overrides if needed
4. **Document profile usage matrix** — which profile for which task type
5. **Run `hermes skills audit`** in each profile to validate skill library health