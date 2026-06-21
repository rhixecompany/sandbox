# HERMES PROFILE REPORT
Generated: 2026-06-21

## Current Session Identity
- **Active Profile:** `default`
- **Current Model:** gpt-5.4-mini (openai-codex) — *Note: conversation header shows nemotron-3-ultra-free (opencode-zen); possible profile switch or fallback*
- **Owner:** Alexa
- **OS:** Windows 11 (corrected from Windows 10)
- **Shell:** VS Code Git Bash terminal (bash via git-bash/MSYS)
- **Editor:** VS Code (corrected from notepad)

## Profile Inventory (7 Profiles)

| Profile | Model | Provider | Purpose |
|---------|-------|----------|---------|
| **default** ⬤ | gpt-5.4-mini | openai-codex | General purpose — **currently active** |
| code-architect | nemotron-3-ultra-free | opencode-zen | Code changes, debugging, refactoring |
| research-analyst | nemotron-3-ultra-free | opencode-zen | Deep research, synthesis, documentation |
| creative-director | nemotron-3-ultra-free | opencode-zen | Design, content, creative tasks |
| exec-assistant | nemotron-3-ultra-free | opencode-zen | Administrative, planning, coordination |
| patient-tutor | nemotron-3-ultra-free | opencode-zen | Explanations, tutorials, learning |
| adminbot | nemotron-3-ultra-free | opencode-zen | System admin, operations |

## MCP Servers (11 Configured)
1. **ast-grep** — AST-based code pattern searching
2. **cli** — Built-in CLI tools
3. **code-sandbox** — Node.js code execution
4. **fetch** — Web content fetching
5. **filesystem** — Project file access (sandboxed)
6. **github** — GitHub API operations
7. **linear** — Linear project management (disabled)
8. **mcp-docker** — Docker container management
9. **memory** — Persistent memory backend
10. **playwright** — Browser automation
11. **sequential-thinking** — Structured reasoning

## Plugins (15 Enabled)
- basic, copilot-provider, custom-provider, disk-cleanup
- huggingface-provider, langfuse, nous, nous-provider
- ollama-cloud-provider, openai-codex, openai-codex-provider
- opencode-zen-provider, openrouter-provider, security-guidance, web-tavily

## Hooks (3 Active, Shared at `~/AppData/Local/hermes/hooks/`)
- session-logger (on_session_start, on_session_end, pre_llm_call)
- session-auto-commit (on_session_end)
- governance-audit (on_session_start, on_session_end, pre_llm_call)

## Skills Library (373 Total Post-Dedup)
- 73 bundled skills across 16 categories
- 216 community skills from `.github/skills/`
- 84 local skills (post-deduplication)
- Key categories: software-development, devops, autonomous-ai-agents, github, mlops, research

## Toolsets (21 Enabled)
web, browser, terminal, file, code_execution, vision, image_gen, moa, tts, skills, todo, memory, context_engine, session_search, clarify, delegation, cronjob, search

## Provider Chain
1. openai-codex (primary) — gpt-5.4-mini ✓ Configured
2. opencode-zen (fallback) — nemotron-3-ultra-free, nemotron-3-super-free ✓ In chain
3. openrouter (via plugin) ✓ Enabled
4. nous (via plugin) ✓ Enabled

## Workspace Paths
- **Root:** C:\Users\Alexa\Desktop\SandBox
- **Hermes Root:** C:\Users\Alexa\AppData\Local\hermes
- **Scripts:** C:\Users\Alexa\AppData\Local\hermes\scripts
- **Hooks:** C:\Users\Alexa\AppData\Local\hermes\hooks
- **Profiles:** C:\Users\Alexa\AppData\Local\hermes\profiles\<name>\
- **Skills:** C:\Users\Alexa\AppData\Local\hermes\skills\
- **Memories:** C:\Users\Alexa\AppData\Local\hermes\memories\

## Python Toolchain
- python3 = 3.13.14
- python = 3.11.15
- pip → python3.11
- PEP 668 = yes (use venv or uv)
- uv = installed

## Key Corrections Applied
- OS: Windows 11 (was Windows 10)
- Editor: VS Code (was notepad)
- Terminal: VS Code Git Bash (was generic git-bash/MSYS)