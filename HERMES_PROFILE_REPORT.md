# HERMES PROFILE REPORT

Generated: 2026-06-28 (Updated — full profile sync)

## Current Session Identity

| Field               | Value                                                       |
| ------------------- | ----------------------------------------------------------- |
| **Active Profile**  | `alexa`                                                     |
| **Persona**         | **OWL** — pragmatic senior engineer                         |
| **Primary Model**   | deepseek-v4-flash-free (opencode-zen)                       |
| **Current Runtime** | deepseek-v4-flash-free (opencode-zen) — *active primary*    |
| **Owner**           | Alexa                                                       |
| **OS**              | Windows 11                                                  |
| **Shell**           | VS Code Git Bash (bash via git-bash/MSYS)                   |
| **Editor**          | VS Code                                                     |

## Profile Inventory (7 Active + 17 Unconfigured)

| Profile           | Model                 | Provider     | Purpose                                |
| ----------------- | --------------------- | ------------ | -------------------------------------- |
| **alexa** ⬤      | deepseek-v4-flash-free | opencode-zen | System admin, operations — **active**  |
| default           | deepseek-v4-flash-free | opencode-zen | General purpose                        |
| code-architect    | deepseek-v4-flash-free | opencode-zen | Code changes, debugging, refactoring   |
| research-analyst  | deepseek-v4-flash-free | opencode-zen | Deep research, synthesis               |
| creative-director | deepseek-v4-flash-free | opencode-zen | Design, content, creative tasks        |
| exec-assistant    | deepseek-v4-flash-free | opencode-zen | Admin, planning, coordination          |
| patient-tutor     | deepseek-v4-flash-free | opencode-zen | Explanations, tutorials                |

**17 additional profiles** exist on filesystem (arch, architect, debugger, devops-expert, github-actions-expert, hermes, implementation-plan, mentor, planner, power-bi-data-modeling-expert, prd, prompt-engineer, qa-subagent, reviewer, specification, tanstack-start-shadcn-tailwind, terraform) — not in active routing table.

## MCP Servers (14 Configured)

| #   | Server              | Transport | Purpose                          |
| --- | ------------------- | --------- | -------------------------------- |
| 1   | ast-grep            | stdio     | AST-based code pattern searching |
| 2   | code-sandbox        | stdio     | Node.js code execution           |
| 3   | codex               | stdio     | Codex CLI integration            |
| 4   | copilot-mcp         | stdio     | GitHub Copilot MCP server        |
| 5   | fetch               | stdio     | Web content fetching             |
| 6   | filesystem          | stdio     | Project file access (sandboxed)  |
| 7   | github              | stdio     | GitHub API operations            |
| 8   | linear              | HTTP      | Linear project management        |
| 9   | mcp-docker          | stdio     | Docker container management      |
| 10  | memory              | stdio     | Persistent memory backend        |
| 11  | mindstudio          | stdio     | MindStudio integration           |
| 12  | playwright          | stdio     | Browser automation               |
| 13  | sequential-thinking | stdio     | Structured reasoning             |
| 14  | smithery            | HTTP      | Smithery registry                |

## Available Toolsets (18 Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`,
`moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`,
`clarify`, `delegation`, `cronjob`, `search`

## Plugins (15 Enabled, 49 Disabled)

| Plugin                | Category            | Status |
| --------------------- | ------------------- | ------ |
| basic                 | Core                | ✓      |
| copilot-provider      | Provider            | ✓      |
| custom-provider       | Provider            | ✓      |
| disk-cleanup          | Maintenance         | ✓      |
| huggingface-provider  | Provider            | ✓      |
| langfuse              | Observability       | ✓      |
| nous                  | Integration         | ✓      |
| nous-provider         | Provider            | ✓      |
| ollama-cloud-provider | Provider            | ✓      |
| openai-codex          | Provider            | ✓      |
| openai-codex-provider | Provider            | ✓      |
| opencode-zen-provider | Provider (fallback) | ✓      |
| openrouter-provider   | Provider            | ✓      |
| security-guidance     | Security            | ✓      |
| web-tavily            | Web search          | ✓      |

**Notable Disabled (50+):** anthropic-provider, bedrock-provider, deepseek-provider, gemini-provider, qwen-oauth-provider, nvidia-provider, xai-provider, and 42 others

## Hooks (3 Active — Shared at `~/AppData/Local/hermes/hooks/`)

| Hook                | Events                                         | Script  |
| ------------------- | ---------------------------------------------- | ------- |
| session-logger      | on_session_start, on_session_end, pre_llm_call | hook.sh |
| session-auto-commit | on_session_end                                 | hook.sh |
| governance-audit    | on_session_start, on_session_end, pre_llm_call | hook.sh |

All hooks verified: JSON configs + shell scripts present and properly structured.

## Skills Library (373 Total Post-Dedup)

- **73** bundled skills across 16 categories
- **216** community skills from `.github/skills/`
- **84** local skills (post-deduplication 2026-06-15)
- **Key categories:** software-development, devops, autonomous-ai-agents, github, mlops, research, creative, productivity, data-science, mcp, media, gaming, planning, qa, red-teaming, smart-home

## Provider Chain

| Priority     | Provider     | Model(s)                               | Status       |
| ------------ | ------------ | -------------------------------------- | ------------ |
| 1 (primary)  | opencode-zen | deepseek-v4-flash-free                 | ✓ Active     |
| 2            | nous         | stepfun/step-3.7-flash:free            | ✓ In chain   |
| 3            | openrouter   | qwen/qwen3-coder:free                  | ✓ Fallback   |

## Workspace Paths

- **Root:** `C:\Users\Alexa\Desktop\SandBox`
- **Hermes Root:** `C:\Users\Alexa\AppData\Local\hermes`
- **Scripts:** `C:\Users\Alexa\AppData\Local\hermes\scripts`
- **Hooks:** `C:\Users\Alexa\AppData\Local\hermes\hooks`
- **Profiles:** `C:\Users\Alexa\AppData\Local\hermes\profiles\<name>\`
- **Skills:** `C:\Users\Alexa\AppData\Local\hermes\skills\`
- **Memories:** `C:\Users\Alexa\AppData\Local\hermes\memories\`

## Python Toolchain

- python3 = 3.13.14
- python = 3.11.15
- pip → python3.11
- PEP 668 = yes (use venv or uv)
- uv = installed

## Audit Issues

| #   | Severity | File                       | Issue                                                                                                                                      | Status     |
| --- | -------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| 1   | **MED**  | `profiles/*/memories/SOUL.md` | Profile-specific SOUL.md was missing for 17 profiles — now created for all 17 unconfigured profiles. All 24 profiles have SOUL.md ✓ | RESOLVED   |
| 2   | **MED**  | `HERMES_PROFILE_REPORT.md` | MCP server list was missing 4 entries (codex, copilot-mcp, mindstudio, smithery) — now updated to 14                                       | RESOLVED   |
| 3   | **HIGH** | `USER.md`                  | Broken paths `~/Alexa/...` — RESOLVED (current USER.md has correct paths)                                                                  | RESOLVED   |
| 4   | **MED**  | `USER.md:41`               | Copy-paste artifact — RESOLVED (no artifact in current file)                                                                               | RESOLVED   |
| 5   | **LOW**  | `.hermes.md`                 | Stale reference "368 local skill directories" — no longer in file. Skills: root=118, alexa=119, code-architect=118 | RESOLVED   |
| 6   | **MED**  | Git repos                  | 846 files had merge conflict markers from rebase — RESOLVED (all cleaned, committed, pushed on 2026-06-25)                                   | RESOLVED   |

## Verification Gate Status

| Gate                       | Status                                            |
| -------------------------- | ------------------------------------------------- |
| Skills audit passed        | `hermes skills audit && hermes skills update` — ✓ |
| Config hierarchy valid     | `.hermes.md` → `AGENTS.md` → `PROJECT_RULES.md` — ✓ |
| Context files synced       | All context files updated for model/provider       |
| MCP servers reachable      | 14 servers configured — ✓                         |
| Profile SOUL.md customized | ✅ All 24 profiles have SOUL.md (7 configured + 17 unconfigured) |

## Environment Corrections (Applied 2026-06-21)

- **OS:** Windows 11 (was incorrectly reported as Windows 10)
- **Editor:** VS Code (was incorrectly reported as notepad)
- **Terminal:** VS Code Git Bash (bash via git-bash/MSYS)
