# Hermes Agent Profile & Configuration Report

**Generated:** 2026-06-14
**Current Session Profile:** `default`
**Active Config:** Global config at `C:\Users\Alexa\AppData\Local\hermes\config.yaml` (profile-specific config not present)

---

## 1. Available Profiles (7 Total)

| Profile | Path | Model (from config) | Purpose |
|---------|------|---------------------|---------|
| **default** | `profiles/default/` | `nvidia/nemotron-3-ultra:free` (via Nous) | General purpose — current active |
| **code-architect** | `profiles/code-architect/` | `gpt-5.4-mini` (via OpenAI Codex) | Code implementation, debugging, refactoring |
| **research-analyst** | `profiles/research-analyst/` | (inherits global) | Deep research, literature review, synthesis |
| **creative-director** | `profiles/creative-director/` | (inherits global) | Design, content creation, brainstorming |
| **exec-assistant** | `profiles/exec-assistant/` | (inherits global) | Planning, coordination, admin |
| **patient-tutor** | `profiles/patient-tutor/` | (inherits global) | Tutorials, explanations, teaching |
| **adminbot** | `profiles/adminbot/` | (inherits global) | System operations, DevOps, infra |

> **Note:** Only `code-architect` has a full profile-specific `config.yaml` with MCP servers, hooks, plugins, and custom model. Other profiles inherit from global config.

---

## 2. Current Profile: `default`

### Model Configuration
- **Provider:** `nous` (Nous Research inference API)
- **Model:** `nvidia/nemotron-3-ultra:free`
- **Base URL:** `https://inference-api.nousresearch.com/v1`
- **API Mode:** `chat_completions`

### Fallback Providers
1. **OpenRouter:** `openrouter/owl-alpha` @ `https://openrouter.ai/api/v1`
2. **Copilot:** `gpt-5-mini` @ `https://api.githubcopilot.com`

### Toolsets Enabled
- `hermes-cli`

### Personality
- **Display personality:** `concise`
- **Reasoning effort:** `high`

---

## 3. MCP Servers (10 Configured — from `code-architect` profile config)

| Server | Command | Description | Tools Available |
|--------|---------|-------------|-----------------|
| **ast-grep** | `npx -y @notprolands/ast-grep-mcp` | Code pattern searching (AST-based) | — |
| **cli** | (built-in) | Built-in CLI tools | browser, clarify, code_execution, computer_use, cronjob, delegation, file, image_gen, memory, messaging, session_search, skills, terminal, todo, tts, vision, web |
| **code-sandbox** | `npx -y node-code-sandbox-mcp` | Node.js code execution | — |
| **fetch** | `npx -y mcp-server-fetch-typescript` | Web content fetching | — |
| **filesystem** | `npx -y @modelcontextprotocol/server-filesystem C:/Users/Alexa/Desktop/SandBox` | File system access (sandboxed to workspace) | — |
| **github** | `npx -y @modelcontextprotocol/server-github` | GitHub API operations | — |
| **mcp-docker** | `docker mcp gateway run --profile adminbot` | Docker container management | — |
| **memory** | `npx -y @modelcontextprotocol/server-memory` | Persistent memory backend | — |
| **playwright** | `npx -y @playwright/mcp@latest` | Browser automation | — |
| **sequential-thinking** | `npx -y @modelcontextprotocol/server-sequential-thinking` | Structured reasoning | `sequentialthinking` |

> **Important:** These are defined in `code-architect` profile config. The `default` profile inherits global config which does **not** define MCP servers explicitly. However, the running session has access to all 10 via the shared Hermes daemon.

---

## 4. Hooks (3 Active — All Profiles)

| Hook | Enabled | Events | Script Path |
|------|---------|--------|-------------|
| **session-logger** | ✅ | `on_session_start`, `on_session_end`, `pre_llm_call` | `C:\Users\Alexa\AppData\Local\hermes\hooks\session-logger\hook.sh` |
| **session-auto-commit** | ✅ | `on_session_end` | `C:\Users\Alexa\AppData\Local\hermes\hooks\session-auto-commit\hook.sh` |
| **governance-audit** | ✅ | `on_session_start`, `on_session_end`, `pre_llm_call` | `C:\Users\Alexa\AppData\Local\hermes\hooks\governance-audit\hook.sh` |

**Hooks directory:** `C:\Users\Alexa\AppData\Local\hermes\hooks\` (shared across profiles)

---

## 5. Plugins (5 Enabled — from `code-architect` config)

| Plugin | Status | Description |
|--------|--------|-------------|
| **awesome-hermes-agent** | ✅ Enabled | Ecosystem integration |
| **disk-cleanup** | ✅ Enabled | Automatic disk maintenance |
| **memory/honcho** | ✅ Enabled | Cross-session memory backend |
| **model-providers/openrouter** | ✅ Enabled | OpenRouter model provider |
| **security-guidance** | ✅ Enabled | Security best practices |

**Disabled plugins:** `[]` (none)

**Plugin directories (per-profile):**
- `code-architect/plugins/`: `awesome-hermes-agent/`, `hermes-achievements/`
- Global plugins managed via Hermes daemon

---

## 6. Skills Library (289 Total)

### Count by Source
- **Bundled skills:** 73 (across 16 categories)
- **Community skills:** 216 (from `.github/skills/`)
- **Total:** 289 skills

### Categories Available
`software-development`, `devops`, `autonomous-ai-agents`, `github`, `mlops`, `research`, `creative`, `productivity`, `development`, `data-science`, `architecture`, `planning`, `qa`, `writing-skills`, `hermes-agent`, `hermes-hooks`, `hermes-mcp`, `hermes-skills`, `hermes-breakdown`, `hermes-system-maintenance`, `profile-maintenance`, `template`, `validate-memories`, `using-git-worktrees`, `subagent-driven-development`, `one-three-one-rule`, `openclaw-migration`, `skill-creator`, `skill-judge`, `make-repo-contribution`

### Skills Directory (code-architect profile)
`C:\Users\Alexa\AppData\Local\hermes\profiles\code-architect\skills\` — 368 skill directories (after deduplication)

### Key Umbrella Skills (Post-Consolidation)
- `autonomous-ai-agents` (coding-agents, agent-browser, agent-governance, etc.)
- `architecture` (blueprint generators)
- `creative` (design, art, video, content)
- `devops` (Azure, Docker, GitHub Actions, Terraform, etc.)
- `github` (repo management, PR workflow, CI/CD)
- `mlops` (HuggingFace, evaluation, inference, models)
- `research` (arXiv, web research, OSINT, repo research)
- `development` (code-docs, refactor, TDD, debugging, etc.)
- `productivity` (docs, spreadsheets, presentations, note-taking)

---

## 7. Tools Available (Native + MCP)

### Native Toolsets (from `hermes-cli`)
`browser`, `clarify`, `code_execution`, `computer_use`, `cronjob`, `delegation`, `file`, `image_gen`, `kanban`, `memory`, `messaging`, `session_search`, `skills`, `spotify`, `terminal`, `todo`, `tts`, `video`, `video_gen`, `vision`, `web`, `x_search`, `yuanbao`

### MCP-Exposed Tools (when servers connected)
- **filesystem** → file read/write/search
- **github** → GitHub API (repos, issues, PRs, actions)
- **ast-grep** → AST-based code search
- **memory** → persistent memory operations
- **playwright** → browser automation
- **sequential-thinking** → structured reasoning
- **fetch** → web content extraction
- **code-sandbox** → Node.js execution
- **cli** → all native tools via MCP
- **mcp-docker** → container management

---

## 8. Key Configuration Differences: `default` vs `code-architect`

| Setting | `default` (Global) | `code-architect` (Profile) |
|---------|-------------------|---------------------------|
| **Model** | `nvidia/nemotron-3-ultra:free` (Nous) | `gpt-5.4-mini` (OpenAI Codex) |
| **Reasoning** | `high` | `xhigh` |
| **MCP Servers** | Not defined | 10 servers defined |
| **Plugins** | Not defined | 5 enabled |
| **Hooks** | 3 defined (shared paths) | 3 defined (same scripts) |
| **Skills Dir** | Uses global | 368 local skills |
| **Delegation** | `orchestrator_enabled: true` | Same |
| **Memory** | 2200/1375 char limits | Same |

---

## 9. Current Session Context

- **Working Directory:** `C:\Users\Alexa\Desktop\SandBox`
- **Session Report:** `SESSION_REPORT.md` present (last: skill library dedup, 645→368 skills)
- **SOUL.md:** Updated with 4 strict rules (session start, MCP tools, profile selection, Python scripts)
- **Memory:** 97% used (9 entries, 2,141/2,200 chars)
- **Schemas:** `AGENTS.md`, `.hermes.md` loaded as context

---

## 10. Recommended Actions

1. **Switch to `code-architect` profile** for any code/debug/refactor tasks (better model, full MCP config)
2. **Use MCP tools** over native equivalents (per SOUL.md Rule #2)
3. **Create Python scripts** in `C:/Users/Alexa/AppData/Local/hermes/scripts/` (per SOUL.md Rule #4)
4. **Read SESSION_REPORT.md** at every session start (per SOUL.md Rule #1)