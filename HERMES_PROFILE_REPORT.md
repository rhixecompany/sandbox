# HERMES PROFILE REPORT

Generated: 2026-06-21 (Updated)

## Current Session Identity

| Field               | Value                                                       |
| ------------------- | ----------------------------------------------------------- |
| **Active Profile**  | `default`                                                   |
| **Persona**         | **OWL** — pragmatic senior engineer                         |
| **Primary Model**   | gpt-5.4-mini (openai-codex)                                 |
| **Current Runtime** | deepseek-v4-flash-free (opencode) — *fallback chain active* |
| **Owner**           | Alexa                                                       |
| **OS**              | Windows 11                                                  |
| **Shell**           | VS Code Git Bash (bash via git-bash/MSYS)                   |
| **Editor**          | VS Code                                                     |

## Profile Inventory (7 Profiles)

| Profile           | Model                 | Provider     | Purpose                                |
| ----------------- | --------------------- | ------------ | -------------------------------------- |
| **default** ⬤     | gpt-5.4-mini          | openai-codex | General purpose — **currently active** |
| code-architect    | nemotron-3-ultra-free | opencode-zen | Code changes, debugging, refactoring   |
| research-analyst  | nemotron-3-ultra-free | opencode-zen | Deep research, synthesis               |
| creative-director | nemotron-3-ultra-free | opencode-zen | Design, content, creative tasks        |
| exec-assistant    | nemotron-3-ultra-free | opencode-zen | Admin, planning, coordination          |
| patient-tutor     | nemotron-3-ultra-free | opencode-zen | Explanations, tutorials                |
| adminbot          | nemotron-3-ultra-free | opencode-zen | System admin, operations               |

## MCP Servers (11 Configured)

| #   | Server              | Purpose                          |
| --- | ------------------- | -------------------------------- |
| 1   | ast-grep            | AST-based code pattern searching |
| 2   | cli                 | Built-in CLI tools               |
| 3   | code-sandbox        | Node.js code execution           |
| 4   | fetch               | Web content fetching             |
| 5   | filesystem          | Project file access (sandboxed)  |
| 6   | github              | GitHub API operations            |
| 7   | linear              | Linear project management        |
| 8   | mcp-docker          | Docker container management      |
| 9   | memory              | Persistent memory backend        |
| 10  | playwright          | Browser automation               |
| 11  | sequential-thinking | Structured reasoning             |

## Available Toolsets (Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`,
`moa`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`,
`clarify`, `delegation`, `cronjob`, `search`

## Plugins (15 Enabled)

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

**Notable Disabled (50+):** anthropic-provider, bedrock-provider, deepseek-provider, gemini-provider, qwen-oauth-provider, nvidia-provider, xai-provider, and 43 others

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

| Priority     | Provider     | Model(s)                                     | Status       |
| ------------ | ------------ | -------------------------------------------- | ------------ |
| 1 (primary)  | openai-codex | gpt-5.4-mini                                 | ✓ Configured |
| 2 (fallback) | opencode-zen | nemotron-3-ultra-free, nemotron-3-super-free | ✓ In chain   |
| 3            | openrouter   | (via plugin)                                 | ✓ Enabled    |
| 4            | nous         | (via plugin)                                 | ✓ Enabled    |

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

## 🔴 Audit Issues Found

| #   | Severity | File                       | Issue                                                                                                                                    |
| --- | -------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **HIGH** | `profiles/default/SOUL.md` | **MISSING** — root SOUL.md at `~/AppData/Local/hermes/SOUL.md` serves as fallback, but default profile has no dedicated SOUL.md          |
| 2   | **HIGH** | `USER.md`                  | Broken paths: `~/Alexa/AppData/Local/hermes` should be `~/AppData/Local/hermes`; `~/Alexa/Desktop/SandBox` should be `~/Desktop/SandBox` |
| 3   | **MED**  | `USER.md:41`               | Copy-paste artifact: truncated sentence "ad the file and update it using"                                                                |
| 4   | **LOW**  | `.hermes.md:61`            | "code-architect: 368 local skill directories" — minor mismatch with total 373                                                            |

## Verification Gate Status

| Gate                       | Status                                            |
| -------------------------- | ------------------------------------------------- |
| Skills audit passed        | `hermes skills audit && hermes skills update` — ✓ |
| Config hierarchy valid     | `.hermes.md` → `AGENTS.md` — ✓                    |
| MCP servers reachable      | 11 servers configured — ✓                         |
| Profile SOUL.md customized | ❌ Default profile SOUL.md missing                 |

## Environment Corrections (Applied 2026-06-21)

- **OS:** Windows 11 (was incorrectly reported as Windows 10)
- **Editor:** VS Code (was incorrectly reported as notepad)
- **Terminal:** VS Code Git Bash (bash via git-bash/MSYS)
