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

## Hermes Agent Configuration

### Current Active Profile: `default`
- **Model:** `nvidia/nemotron-3-ultra:free` (via Nous Research API)
- **Base URL:** `https://inference-api.nousresearch.com/v1`
- **Config:** Global `C:\Users\Alexa\AppData\Local\hermes\config.yaml`

### Available Profiles (7 Total)

| Profile | Model | Purpose |
|---------|-------|---------|
| `code-architect` | `gpt-5.4-mini` (OpenAI Codex) | Code implementation, debugging, refactoring |
| `research-analyst` | inherits global | Deep research, literature review, synthesis |
| `creative-director` | inherits global | Design, content creation, brainstorming |
| `exec-assistant` | inherits global | Planning, coordination, admin |
| `patient-tutor` | inherits global | Tutorials, explanations, teaching |
| `adminbot` | inherits global | System operations, DevOps, infra |
| `default` | `nvidia/nemotron-3-ultra:free` (Nous) | General purpose — **currently active** |

> **Profile Selection Rule:** Always switch to the correct profile for the task (see SOUL.md Rule #3). For code/debug/refactor tasks, use `code-architect`.

### MCP Servers (10 Configured in `code-architect` profile)

| Server | Purpose |
|--------|---------|
| `ast-grep` | Code pattern searching (AST-based) |
| `cli` | Built-in CLI tools |
| `code-sandbox` | Node.js code execution |
| `fetch` | Web content fetching |
| `filesystem` | File system access (sandboxed to workspace) |
| `github` | GitHub API operations |
| `mcp-docker` | Docker container management |
| `memory` | Persistent memory backend |
| `playwright` | Browser automation |
| `sequential-thinking` | Structured reasoning |

> **MCP Tools Rule:** ALWAYS use MCP server tools when available to reduce token usage (SOUL.md Rule #2). Prefer MCP over equivalent native tools.

### Hooks (3 Active — All Profiles)

| Hook | Events |
|------|--------|
| `session-logger` | `on_session_start`, `on_session_end`, `pre_llm_call` |
| `session-auto-commit` | `on_session_end` |
| `governance-audit` | `on_session_start`, `on_session_end`, `pre_llm_call` |

Scripts located at: `C:\Users\Alexa\AppData\Local\hermes\hooks\`

### Plugins (5 Enabled)

`awesome-hermes-agent`, `disk-cleanup`, `memory/honcho`, `model-providers/openrouter`, `security-guidance`

### Skills Library

- **Total:** 289 skills (73 bundled + 216 community from `.github/skills/`)
- **code-architect profile:** 368 local skill directories (post-deduplication)
- **Categories:** software-development, devops, autonomous-ai-agents, github, mlops, research, creative, productivity, development, data-science, architecture, planning, qa, writing-skills, hermes-agent, hermes-hooks, hermes-mcp, hermes-skills, hermes-breakdown, hermes-system-maintenance, profile-maintenance, template, validate-memories, using-git-worktrees, subagent-driven-development, one-three-one-rule, openclaw-migration, skill-creator, skill-judge, make-repo-contribution

## Strict Rules (from SOUL.md — Non-Negotiable)

### Rule 1: Session Start
At the beginning of every session, you MUST:
1. Search `C:\Users\Alexa\Desktop\SandBox` for `SESSION_REPORT.md`
2. Read and understand it completely
3. Explain it back to the user before proceeding with any other work

### Rule 2: MCP Server Tools
ALWAYS use MCP server tools when available to reduce token usage:
- `filesystem` MCP for file operations
- `github` MCP for GitHub operations
- `ast-grep` MCP for code pattern searching
- `memory` MCP for persistent memory
- `playwright` MCP for browser automation
- `sequential-thinking` MCP for structured reasoning
- `cli` MCP for built-in CLI tools
- `code-sandbox` MCP for Node.js execution
- `fetch` MCP for web content fetching
- `mcp-docker` MCP for Docker container management

### Rule 3: Profile Selection
ALWAYS switch to the correct Hermes profile for the given task:
- `code-architect` — Code implementation, debugging, refactoring
- `research-analyst` — Deep research, literature review, synthesis
- `creative-director` — Design, content creation, brainstorming
- `exec-assistant` — Planning, coordination, admin
- `patient-tutor` — Tutorials, explanations, teaching
- `adminbot` — System operations, DevOps, infra
- `default` — General purpose (fallback only)

### Rule 4: Python Scripts
NEVER run inline Python scripts. Instead:
1. Create the script as a permanent file in `C:/Users/Alexa/AppData/Local/hermes/scripts/`
2. Execute it from there
3. If it fails, debug, fix, and rerun until zero issues
4. Keep the script for reuse — no throwaway inline code

## Important Notes

- Never commit secrets, tokens, credentials, or `.env` files
- **SESSION_REPORT.md** must be updated on session start/end with rolling 5-session summary
- Read before edit; backup before destructive changes; confirm scope before repo-wide operations
- Python toolchain: `python3=3.14.6`, `python=3.11.14`, `pip→python3.11` (mismatch), `uv=installed`

## Subdirectory Context Discovery

This workspace uses progressive subdirectory discovery. Each major project has its own AGENTS.md:
- `Bash/AGENTS.md` — Automation toolkit conventions
- `projects/*/AGENTS.md` — Per-project context (see Phase 6)