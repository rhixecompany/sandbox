# Hermes Agent Documentation Implementation Plan

> **Generated:** 2026-06-08
> **Based on:** 13 extracted documentation files from official Hermes Agent docs + awesome-hermes-agent
> **Goal:** Implement all documentation as a working prompt/instruction system for Hermes Agent

---

## 📋 Executive Summary

This plan transforms 13 comprehensive documentation pages into a fully functional Hermes Agent setup with:

- **Global personality** (SOUL.md) — durable agent identity
- **Project context** (AGENTS.md) — workspace conventions and architecture
- **Core skills** — reusable workflows for MCP, tools, hooks, plugins
- **MCP integration** — external tool servers (GitHub, filesystem, browser)
- **Automation hooks** — session logging, auto-commit, governance audit
- **Plugin system** — extensibility for model providers, memory, tools
- **Subdirectory contexts** — monorepo-aware progressive discovery

---

## 🗂️ Phase Overview

| Phase | Focus           | Deliverables                                       | Est. Time |
| ----- | --------------- | -------------------------------------------------- | --------- |
| **1** | Foundation      | SOUL.md, root AGENTS.md                            | 30 min    |
| **2** | Skills System   | 6+ core skills in `~/AppData/local/hermes/skills/` | 45 min    |
| **3** | MCP Integration | Config + 3 server patterns                         | 30 min    |
| **4** | Automation      | 3 hooks + cron templates                           | 30 min    |
| **5** | Plugins         | Config + plugin template                           | 20 min    |
| **6** | Context Files   | Subdirectory AGENTS.md files                       | 20 min    |
| **7** | Verification    | End-to-end test                                    | 15 min    |

**Total Estimated Time:** ~3 hours

---

## 📦 Phase 1: Foundation — Global Identity & Project Context

### 1.1 Create SOUL.md (Global Personality)

**File:** `~/AppData/local/hermes/SOUL.md`
**Source:** `docs/user-guide/features/personality/README.md`

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

**Actions:**

- [ ] Write `~/AppData/local/hermes/SOUL.md` with production-ready template
- [ ] Verify loads correctly: `hermes chat -q "What's your personality?"`

### 1.2 Create Root AGENTS.md (Project Context)

**File:** `AGENTS.md` (workspace root)
**Source:** `docs/user-guide/features/context-files/README.md`, `docs/guides/tips/README.md`

````markdown
# Project Context

This is the SandBox multi-project workspace for automation scripts, prompt/instruction assets, and repository maintenance tooling.

## Architecture

- **Root orchestration:** PowerShell/Bun scripts for workspace management
- **Primary toolkit:** `Bash/` — Bun, TypeScript, shell automation
- **Subprojects:** 15+ projects under `projects/` (Next.js, Django, Python, full-stack)
- **Documentation:** `docs/` — extracted Hermes Agent documentation (13 pages)
- **Configuration:** `.github/` — Copilot agents, skills, prompts, hooks, plugins

## Conventions

- Use Bun for TypeScript execution (`bun run`, `bun install`)
- PowerShell 5.1+ for orchestration scripts
- Git for version control — never create .bak/.backup files
- Keep edits minimal and scoped to requested behavior
- Follow DRY: one concern per file, no duplication across AGENTS.md files

## Validation & Quality Gates

```bash
# Bash toolkit
cd Bash && bun run format && bun run typecheck && bun run lint:strict

# Subprojects: each has own validation (see local AGENTS.md)
```
````

## Important Notes

- Never commit secrets, tokens, credentials, or `.env` files
- Hermes profile: `adminbot` (model: openrouter/owl-alpha)
- Active skills: 289 in `.github/skills/`
- Active hooks: session-logger, session-auto-commit, governance-audit
- Active plugins: disk-cleanup, model-providers/openrouter, security-guidance

## Subdirectory Context Discovery

This workspace uses progressive subdirectory discovery. Each major project has its own AGENTS.md:

- `Bash/AGENTS.md` — Automation toolkit conventions
- `projects/*/AGENTS.md` — Per-project context (see Phase 6)

````

**Actions:**
- [ ] Write root `AGENTS.md` with workspace overview
- [ ] Verify loads at session start

---

## 📦 Phase 2: Skills System — Core Reusable Workflows

### 2.1 Skill Directory Structure
**Location:** `~/AppData/local/hermes/skills/`
**Source:** `docs/user-guide/features/skills/README.md`, `docs/awesome-hermes-agent/README.md`

Create the following core skills (each as a directory with SKILL.md + references/):

| Skill Name | Category | Description | Source Doc |
|------------|----------|-------------|------------|
| `hermes-quickstart` | getting-started | Install, provider selection, verification | quickstart, learning-path |
| `hermes-skills` | skills | Skill discovery, creation, hub install | skills |
| `hermes-tools` | tools | Toolset configuration, terminal backends | tools |
| `hermes-mcp` | mcp | MCP catalog, server config, tool filtering | mcp, use-mcp-with-hermes |
| `hermes-hooks` | hooks | Hook creation, events, patterns | hooks |
| `hermes-plugins` | plugins | Plugin config, development, types | plugins |
| `hermes-personality` | personality | SOUL.md, /personality, custom personalities | personality |
| `hermes-context` | context-files | AGENTS.md, SOUL.md, .cursorrules, discovery | context-files |

### 2.2 Skill Template (Applied to Each)
**File:** `~/AppData/local/hermes/skills/<name>/SKILL.md`

```yaml
---
name: hermes-<name>
description: <one-sentence description>
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, <category>]
    category: <category>
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.<name>.enabled
        description: "Enable this skill"
        default: "true"
---

# Hermes <Name> Skill

## When to Use
- <trigger condition 1>
- <trigger condition 2>

## Procedure
1. <step 1>
2. <step 2>
3. <step 3>

## Pitfalls
- <known issue 1>: <fix>
- <known issue 2>: <fix>

## Verification
- <how to confirm it worked>

## References
- `references/commands.md` — CLI commands reference
- `references/config.yaml` — Configuration snippets
- `references/troubleshooting.md` — Common issues
````

### 2.3 Implementation Steps

For each of the 8 skills:

- [ ] Create directory `~/AppData/local/hermes/skills/hermes-<name>/`
- [ ] Write `SKILL.md` with frontmatter and procedure
- [ ] Create `references/` with commands.md, config.yaml, troubleshooting.md
- [ ] Test: `/hermes-<name> help` loads and works
- [ ] Verify: `hermes skills view hermes-<name>` returns content

---

## 📦 Phase 3: MCP Integration — External Tool Servers

### 3.1 Install MCP Dependencies

**Source:** `docs/user-guide/features/mcp/README.md`, `docs/guides/use-mcp-with-hermes/README.md`

```bash
cd ~/AppData/local/hermes/hermes-agent
uv pip install -e ".[mcp]"
```

### 3.2 Configure MCP Servers (config.yaml)

**File:** `~/AppData/local/hermes/config.yaml` → `mcp_servers` section

```yaml
mcp_servers:
  # Pattern 1: Local Project Assistant
  fs:
    command: "npx"
    args:
      ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    tools:
      include: [list_files, read_file, write_file]
      prompts: false
      resources: false

  git:
    command: "uvx"
    args: ["mcp-server-git", "--repository", "/home/user/projects"]
    tools:
      include: [git_status, git_log, git_diff]
      prompts: false
      resources: false

  # Pattern 2: GitHub Triage Assistant
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
      prompts: false
      resources: false

  # Pattern 3: Browser Bridge (WSL2 → Windows)
  chrome-devtools-win:
    command: "cmd.exe"
    args:
      [
        "/c",
        "npx",
        "-y",
        "chrome-devtools-mcp@latest",
        "--autoConnect",
        "--no-usage-statistics",
      ]
    tools:
      include: [list_pages, navigate, evaluate]
      prompts: false
      resources: false
```

### 3.3 Tool Filtering Strategy

**Rule:** Always use whitelist (`tools.include`) for sensitive systems (GitHub, Stripe, internal APIs). Use blacklist (`tools.exclude`) only for well-understood dangerous actions.

### 3.4 Verification Commands

```bash
# Reload MCP config
/reload-mcp

# List available MCP tools
hermes mcp catalog
hermes tools --platform cli | grep mcp-

# Test specific server
hermes mcp test fs
hermes mcp test github
```

**Actions:**

- [ ] Install MCP dependencies
- [ ] Configure 3 server patterns in config.yaml
- [ ] Set required env vars in `~/AppData/local/hermes/.env` (GITHUB_TOKEN, etc.)
- [ ] Run `/reload-mcp` and verify tools appear
- [ ] Test each pattern with sample prompts

---

## 📦 Phase 4: Automation — Hooks & Cron Jobs

### 4.1 Built-in Hooks Configuration

**File:** `~/AppData/local/hermes/config.yaml` → `hooks` section
**Source:** `docs/user-guide/features/hooks/README.md`

```yaml
hooks:
  session-logger:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/AppData/local/hermes/hooks/session-logger/hook.sh"

  session-auto-commit:
    enabled: true
    events: [on_session_end]
    script: "~/AppData/local/hermes/hooks/session-auto-commit/hook.sh"

  governance-audit:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/AppData/local/hermes/hooks/governance-audit/hook.sh"
```

### 4.2 Hook Scripts Implementation

#### session-logger/hook.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

# Skip flag
[[ "${SKIP_LOGGING:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

input=$(cat)
event=$(echo "$input" | jq -r '.event')
session_id=$(echo "$input" | jq -r '.session_id')
timestamp=$(echo "$input" | jq -r '.timestamp')

log_dir=~/AppData/local/hermes/logs/hermes
mkdir -p "$log_dir"
log_file="$log_dir/session-${session_id}.log"

case "$event" in
  on_session_start)
    echo "$(date -Iseconds) SESSION_START $session_id" >> "$log_file"
    ;;
  on_session_end)
    duration=$(echo "$input" | jq -r '.duration_seconds')
    msg_count=$(echo "$input" | jq -r '.message_count')
    tool_calls=$(echo "$input" | jq -r '.tool_calls')
    echo "$(date -Iseconds) SESSION_END $session_id duration=${duration}s msgs=$msg_count tools=$tool_calls" >> "$log_file"
    ;;
  pre_llm_call)
    prompt=$(echo "$input" | jq -r '.prompt' | head -c 100)
    echo "$(date -Iseconds) PROMPT $session_id: $prompt..." >> "$log_file"
    ;;
esac

echo '{"status": "ok"}'
```

#### session-auto-commit/hook.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

[[ "${SKIP_AUTO_COMMIT:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

# Only auto-commit if in a git repo with changes
git_dir=$(git rev-parse --git-dir 2>/dev/null) || { echo '{"status": "ignored"}'; exit 0; }
[[ -n $(git status --porcelain) ]] || { echo '{"status": "no-changes"}'; exit 0; }

git add -A
git commit -m "chore: auto-commit at session end [$(date -Iseconds)]" >/dev/null 2>&1
echo '{"status": "committed"}'
```

#### governance-audit/hook.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

[[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0

input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')

# Simple threat detection patterns
threats=("ignore previous" "system prompt" "reveal your" "bypass" "jailbreak")
for threat in "${threats[@]}"; do
  if echo "$prompt" | grep -qi "$threat"; then
    echo "{\"status\": \"threat-detected\", \"pattern\": \"$threat\"}" >&2
    # Log but don't block (agent continues)
    logger -t hermes-governance "THREAT: $threat in session ${input%%\"*}"
    break
  fi
done

echo '{"status": "ok"}'
```

### 4.3 Cron Job Templates

**Source:** `docs/guides/tips/README.md` (cron section), `docs/getting-started/quickstart/README.md`

```bash
# Create cron jobs via CLI
hermes cron create "daily-summary" "0 9 * * *" "Summarize yesterday's commits and changes"
hermes cron create "weekly-skill-review" "0 10 * * 1" "Review and consolidate unused skills"
hermes cron create "memory-cleanup" "0 2 * * 0" "Clean up old memory entries and consolidate"
```

### 4.4 Implementation Steps

- [ ] Create hook directories: `~/AppData/local/hermes/hooks/{session-logger,session-auto-commit,governance-audit}/`
- [ ] Write hook.sh scripts for each (make executable: `chmod +x`)
- [ ] Add hooks section to `~/AppData/local/hermes/config.yaml`
- [ ] Test: start session, verify logs in `~/AppData/local/hermes/logs/hermes/`
- [ ] Create 3 cron jobs via `hermes cron create`
- [ ] Verify: `hermes cron list` shows all jobs

---

## 📦 Phase 5: Plugins — Extensibility Configuration

### 5.1 Plugin Configuration

**File:** `~/AppData/local/hermes/config.yaml` → `plugins` section
**Source:** `docs/user-guide/features/plugins/README.md`

```yaml
plugins:
  enabled:
    - disk-cleanup
    - model-providers/openrouter
    - security-guidance
    - memory/honcho # Cross-session memory (optional)
  disabled: []
```

### 5.2 Plugin Development Template

**Create:** `~/AppData/local/hermes/plugins/my-plugin/` (for local development)

```
my-plugin/
├── plugin.yaml
├── main.py
└── requirements.txt
```

**plugin.yaml:**

```yaml
name: my-plugin
version: 1.0.0
description: "Custom plugin template"
author: "User"
license: "MIT"
type: tool # or: model_provider, memory_provider, auth, utility
entry_point: main.py
config_schema:
  type: object
  properties:
    api_key:
      type: string
      description: "API key for service"
tools:
  - name: my_tool
    description: "Does something useful"
    parameters:
      type: object
      properties:
        query:
          type: string
```

**main.py:**

```python
from hermes.plugins import PluginBase, Tool

class MyPlugin(PluginBase):
    name = "my-plugin"

    def initialize(self, config: dict):
        self.api_key = config.get("api_key")

    def get_tools(self):
        return [
            Tool(
                name="my_tool",
                description="Does something useful",
                parameters={"type": "object", "properties": {"query": {"type": "string"}}},
                handler=self.handle_my_tool
            )
        ]

    async def handle_my_tool(self, query: str):
        return {"result": f"Processed: {query}"}
```

### 5.3 Model Provider Plugin (OpenRouter)

**Config in config.yaml:**

```yaml
model:
  provider: openrouter
  openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    model: "anthropic/claude-3.5-sonnet"
```

### 5.4 Memory Provider Plugin (Honcho)

**Config in config.yaml:**

```yaml
memory:
  provider: honcho
  honcho:
    api_key: "${HONCHO_API_KEY}"
    workspace: "my-project"
```

### 5.5 Implementation Steps

- [ ] Add plugins section to `~/AppData/local/hermes/config.yaml`
- [ ] Create plugin template directory `~/AppData/local/hermes/plugins/my-plugin/`
- [ ] Write plugin.yaml and main.py
- [ ] Set required env vars in `~/AppData/local/hermes/.env` (OPENROUTER_API_KEY, HONCHO_API_KEY)
- [ ] Restart Hermes and verify: `hermes plugins list`
- [ ] Test custom tool: `/my_tool hello`

---

## 📦 Phase 6: Context Files — Subdirectory Discovery

### 6.1 Subdirectory AGENTS.md Files

**Source:** `docs/user-guide/features/context-files/README.md`, `docs/guides/tips/README.md`

Create AGENTS.md in each major subdirectory for progressive discovery:

| Path                                       | Purpose             | Key Content                                                |
| ------------------------------------------ | ------------------- | ---------------------------------------------------------- |
| `Bash/AGENTS.md`                           | Automation toolkit  | Bun/TypeScript conventions, test commands, script patterns |
| `projects/Banking/AGENTS.md`               | Next.js fintech app | Next.js 16, Drizzle, Plaid/Dwolla, Docker                  |
| `projects/comicwise/AGENTS.md`             | Comic streaming     | Next.js 15, Prisma, Stripe                                 |
| `projects/ecom/AGENTS.md`                  | Ecommerce platform  | DRF + React/Redux, PayPal                                  |
| `projects/profile/AGENTS.md`               | Django blog/CMS     | Django, GCS, CKEditor                                      |
| `projects/rhixecompany-comics/AGENTS.md`   | Comic platform      | Django + Next.js 16, Celery                                |
| `projects/university-libary-jsm/AGENTS.md` | Library management  | Next.js 15, Drizzle, Neon, Redis                           |

### 6.2 Template for Subdirectory AGENTS.md

````markdown
# <Project Name> Context

Brief description of the project.

## Architecture

- Framework: <framework>
- Language: <language>
- Database: <database>
- Deployment: <deployment>

## Conventions

- <convention 1>
- <convention 2>
- <convention 3>

## Important Notes

- <note 1>
- <note 2>

## Commands

```bash
# Dev server
<command>

# Tests
<command>

# Build
<command>
```
````

````

### 6.3 .cursorrules Compatibility
**Source:** `docs/user-guide/features/context-files/README.md`

If any project uses Cursor, ensure `.cursorrules` exists at root — Hermes will auto-detect it (priority 4).

### 6.4 Implementation Steps
- [ ] Create AGENTS.md for each subdirectory listed above
- [ ] Use template, customize per project
- [ ] Verify progressive discovery: navigate to subdirectory, check context loads
- [ ] Ensure no duplication with root AGENTS.md

---

## 📦 Phase 7: Verification — End-to-End Testing

### 7.1 Foundation Verification
```bash
# 1. SOUL.md loads
hermes chat -q "Describe your personality in 3 words"

# 2. Root AGENTS.md loads
hermes chat -q "What is this workspace about?"

# 3. Subdirectory AGENTS.md discovery
cd projects/Banking && hermes chat -q "What project am I in?"
````

### 7.2 Skills Verification

```bash
# List all skills
hermes skills list

# Test each core skill
/hermes-quickstart
/hermes-skills
/hermes-tools
/hermes-mcp
/hermes-hooks
/hermes-plugins
/hermes-personality
/hermes-context
```

### 7.3 MCP Verification

```bash
# Reload and list
/reload-mcp
hermes mcp catalog

# Test each server
hermes mcp test fs
hermes mcp test github
# Prompt: "List files in /home/user/projects via MCP"
```

### 7.4 Hooks Verification

```bash
# Start session, send prompt, end session
hermes chat -q "Test hook logging"
# Check ~/AppData/local/hermes/logs/hermes/session-*.log

# Verify auto-commit
# Make a change, end session, check git log
```

### 7.5 Plugins Verification

```bash
hermes plugins list
hermes plugins info disk-cleanup
# Test custom tool if created
```

### 7.6 Integration Test

```bash
# Full workflow test
hermes chat --toolsets "web,terminal,file,skills,mcp,memory" -q "
1. Use MCP filesystem to list projects
2. Create a skill for weekly review
3. Set a cron job for daily summary
4. Remember this workflow for next time
"
```

### 7.7 Checklist

- [ ] SOUL.md personality evident in responses
- [ ] Root AGENTS.md context loaded
- [ ] Subdirectory AGENTS.md progressively discovered
- [ ] All 8 core skills load and execute
- [ ] MCP servers connect and tools available
- [ ] Hooks fire on session events (check logs)
- [ ] Cron jobs created and listed
- [ ] Plugins enabled and functional
- [ ] Memory persists across sessions
- [ ] Full integration workflow completes

---

## 🔧 Configuration Files Summary

### ~/AppData/local/hermes/config.yaml (Complete)

```yaml
# Terminal
terminal:
  backend: local
  cwd: "."
  timeout: 180

# Model (example: OpenRouter via plugin)
model:
  provider: openrouter
  openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    model: "anthropic/claude-3.5-sonnet"

# MCP Servers
mcp_servers:
  fs:
    command: "npx"
    args:
      ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    tools:
      include: [list_files, read_file, write_file]
      prompts: false
      resources: false
  git:
    command: "uvx"
    args: ["mcp-server-git", "--repository", "/home/user/projects"]
    tools:
      include: [git_status, git_log, git_diff]
      prompts: false
      resources: false
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"
    tools:
      include: [list_issues, create_issue, update_issue, search_code]
      prompts: false
      resources: false
  chrome-devtools-win:
    command: "cmd.exe"
    args:
      [
        "/c",
        "npx",
        "-y",
        "chrome-devtools-mcp@latest",
        "--autoConnect",
        "--no-usage-statistics",
      ]
    tools:
      include: [list_pages, navigate, evaluate]
      prompts: false
      resources: false

# Hooks
hooks:
  session-logger:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/AppData/local/hermes/hooks/session-logger/hook.sh"
  session-auto-commit:
    enabled: true
    events: [on_session_end]
    script: "~/AppData/local/hermes/hooks/session-auto-commit/hook.sh"
  governance-audit:
    enabled: true
    events: [on_session_start, on_session_end, pre_llm_call]
    script: "~/AppData/local/hermes/hooks/governance-audit/hook.sh"

# Plugins
plugins:
  enabled:
    - disk-cleanup
    - model-providers/openrouter
    - security-guidance
    - memory/honcho
  disabled: []

# Memory
memory:
  provider: honcho
  honcho:
    api_key: "${HONCHO_API_KEY}"
    workspace: "my-project"
```

### ~/AppData/local/hermes/.env (Required Secrets)

```bash
# MCP
GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# Model Provider
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxx

# Memory (Honcho)
HONCHO_API_KEY=honcho_xxxxxxxxxxxx

# Optional: Other providers
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxx
# OPENAI_API_KEY=sk-xxxxxxxxxxxx
```

---

## 📚 Reference: Source Documentation Mapping

| Plan Section       | Source File                                          | Key Concepts                                                               |
| ------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------- |
| Phase 1: SOUL.md   | `personality/README.md`                              | Global identity, 14 built-in personalities, prompt stack                   |
| Phase 1: AGENTS.md | `context-files/README.md`, `tips/README.md`          | Priority order, progressive discovery, monorepo patterns                   |
| Phase 2: Skills    | `skills/README.md`, `awesome-hermes-agent/README.md` | SKILL.md format, progressive disclosure, hub install, curator              |
| Phase 3: MCP       | `mcp/README.md`, `use-mcp-with-hermes/README.md`     | Catalog, manifests, stdio/HTTP/OAuth, filtering, WSL2 bridge               |
| Phase 4: Hooks     | `hooks/README.md`                                    | Events, skip flags, jq/awk rules, patterns (audit, format, cost, security) |
| Phase 4: Cron      | `tips/README.md`, `quickstart/README.md`             | cronjob create, daily/weekly patterns                                      |
| Phase 5: Plugins   | `plugins/README.md`                                  | Types, manifest, Python/JS templates, Honcho, OpenRouter                   |
| Phase 6: Subdirs   | `context-files/README.md`                            | Progressive discovery, per-component contexts                              |

---

## ⚠️ Known Pitfalls & Mitigations

| Pitfall                             | Mitigation                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| SOUL.md not loading                 | Verify at `~/AppData/local/hermes/SOUL.md`, not project dir; check `skip_context_files` |
| Skills not appearing                | Check `platforms` field; restart Hermes after creation                                  |
| MCP tools missing                   | Use `/reload-mcp`; verify `tools.include` whitelist; check env vars                     |
| Hooks not firing                    | Verify script executable (`chmod +x`); check `config.yaml` events list; check logs      |
| Cron jobs silent                    | Ensure `notify_on_complete=true`; check `~/AppData/local/hermes/logs/hermes/`           |
| Plugin not loading                  | Verify `plugin.yaml` syntax; check `config.yaml` enabled list; restart Hermes           |
| Subdirectory context not discovered | Each dir checked once/session; restart session to re-discover                           |
| Prompt cache broken                 | Keep system prompt stable (same context files, memory, model)                           |

---

## ✅ Success Criteria

The implementation is complete when:

1. **New session** starts with SOUL.md personality + root AGENTS.md context
2. **Navigating** to any project subdirectory loads its AGENTS.md
3. **Typing `/hermes-<skill>`** loads and executes the corresponding skill
4. **Running `hermes mcp test <server>`** succeeds for all 4 configured servers
5. **Session logs** appear in `~/AppData/local/hermes/logs/hermes/` with proper JSON format
6. **Auto-commit** creates git commits on session end when changes exist
7. **Governance audit** detects and logs threat patterns
8. **Cron jobs** appear in `hermes cron list` and execute on schedule
9. **Plugins** show as enabled in `hermes plugins list`
10. **Full workflow** (MCP → skill → cron → memory) completes in one conversation

---

\_Plan generated from 13 Hermes Agent documentation sources — ready for implementation_rmat, progressive disclosure, hub install, curator |
| Phase 3: MCP | `mcp/README.md`, `use-mcp-with-hermes/README.md` | Catalog, manifests, stdio/HTTP/OAuth, filtering, WSL2 bridge |
| Phase 4: Hooks | `hooks/README.md` | Events, skip flags, jq/awk rules, patterns (audit, format, cost, security) |
| Phase 4: Cron | `tips/README.md`, `quickstart/README.md` | cronjob create, daily/weekly patterns |
| Phase 5: Plugins | `plugins/README.md` | Types, manifest, Python/JS templates, Honcho, OpenRouter |
| Phase 6: Subdirs | `context-files/README.md` | Progressive discovery, per-component contexts |

---

## ⚠️ Known Pitfalls & Mitigations

| Pitfall                             | Mitigation                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| SOUL.md not loading                 | Verify at `~/AppData/local/hermes/SOUL.md`, not project dir; check `skip_context_files` |
| Skills not appearing                | Check `platforms` field; restart Hermes after creation                                  |
| MCP tools missing                   | Use `/reload-mcp`; verify `tools.include` whitelist; check env vars                     |
| Hooks not firing                    | Verify script executable (`chmod +x`); check `config.yaml` events list; check logs      |
| Cron jobs silent                    | Ensure `notify_on_complete=true`; check `~/AppData/local/hermes/logs/hermes/`           |
| Plugin not loading                  | Verify `plugin.yaml` syntax; check `config.yaml` enabled list; restart Hermes           |
| Subdirectory context not discovered | Each dir checked once/session; restart session to re-discover                           |
| Prompt cache broken                 | Keep system prompt stable (same context files, memory, model)                           |

---

## ✅ Success Criteria

The implementation is complete when:

1. **New session** starts with SOUL.md personality + root AGENTS.md context
2. **Navigating** to any project subdirectory loads its AGENTS.md
3. **Typing `/hermes-<skill>`** loads and executes the corresponding skill
4. **Running `hermes mcp test <server>`** succeeds for all 4 configured servers
5. **Session logs** appear in `~/AppData/local/hermes/logs/hermes/` with proper JSON format
6. **Auto-commit** creates git commits on session end when changes exist
7. **Governance audit** detects and logs threat patterns
8. **Cron jobs** appear in `hermes cron list` and execute on schedule
9. **Plugins** show as enabled in `hermes plugins list`
10. **Full workflow** (MCP → skill → cron → memory) completes in one conversation

---

_Plan generated from 13 Hermes Agent documentation sources — ready for implementation_
