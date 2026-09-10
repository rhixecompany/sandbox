# USER.md — default profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity

- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: default

## Environment Stack

- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint

## Model

- nemotron-3-ultra-free (opencode-zen) [primary]
- deepseek-v4-flash-free (opencode-zen) [fallback]

## Execution Preferences

- Communication: concise bullets, lead with result, skip fluff
- Code: TypeScript strict, JSDoc/docstring _why_ not _what_
- Skills: structured SKILL.md (YAML frontmatter + md body)
- Hooks: ruff format+check --fix pre-commit
- Execution: read→patch→verify, MCP-first, no backup files
- Profile routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot

## Standing Goal

Maintain/enhance .github/prompts/ with DRY, structural sections. Stacked
bundles: using-superpowers, subagent-driven-development, brainstorming.

## Multi-File Change Protocol (≥5 files)

When >4 files modified, agent MUST load 14 skills: /using-superpowers
/brainstorming /user-communication-preferences /mcp-sequential-thinking
/mcp-filesystem /mcp-ast-grep /mcp-memory /plan /plans-and-specs
/create-implementation-plan /implementation-plan /executing-plans
/writing-clearly-and-concisely /subagent-driven-development Protocol: Load
skills → create plan → verify → execute → verify gates.

## Honcho Memory

Active (hybrid mode). Use honcho_profile/context/reasoning/search. Interests:
motorcycles (Harley Sportster 1200), family travel (Air Peace PNR 1J9A2F). Repo:
rhixecompany/sandbox. Prompt quality: comprehensive, best practices, all
MCP/skills.

Conversation started: Thursday, September 10, 2026 (Africa/Lagos, WAT, UTC+01:00)
Model: nemotron-3.5-lightning-free
Provider: opencode-zen
Platform: cli

<!-- End Hermes runtime environment -->

Host: Windows (11)
User home directory: C:\Users\Alexa
Note: on Windows, the machine hostname (e.g. from `hostname` or uname) is NOT the username. Use the 'User home directory' above to construct paths under C:\Users\<user>\, never the hostname.

Shell: on this Windows host your `terminal` tool runs commands through bash (git-bash / MSYS), NOT PowerShell or cmd.exe. Use POSIX shell syntax (`ls`, `$HOME`, `&&`, `|`, single-quoted strings) inside terminal calls. MSYS-style paths like `/c/Users/<user>/...` work alongside native `C:\Users\<user>\...` paths. PowerShell builtins (`Get-ChildItem`, `$env:FOO`, `Select-String`) will NOT work — use their POSIX equivalents (`ls`, `$FOO`, `grep`). Path arguments for NATIVE Windows programs (git, rg, node, python, ...) are NOT translated: MSYS path conversion is disabled here, so `git -C /c/Users/x` or `node /tmp/a.js` fails with 'cannot change to'/'not found' even though `cd /c/Users/x` (a bash builtin) works. Pass `C:/Users/x`-style forward-slash native paths to native tools, and prefer `$LOCALAPPDATA/Temp` over `/tmp` for scratch files a native tool must read. When answering prompts in a pty background process, use process(submit) — never process(write) with a bare trailing newline: Enter on a Windows PTY is a carriage return, and a lone `\n` is not delivered as a line terminator, so the child's prompt silently never returns. When a CLI offers a non-interactive path (flags, `--with-token`, config files, an OAuth device flow polled with curl), prefer it over driving prompts.