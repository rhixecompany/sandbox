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

## Execution Preferences (DRY — owned by `user-communication-preferences` skill, verified loaded; cross-referenced here, NOT duplicated)

Per `user-communication-preferences` (verified in this session; see `.hermes/plans/debug-subgoal-plan-2026-09-13.md`):
- Communication: concise bullets, table-first, lead with result, skip filler.
- Code: TypeScript strict; docstring explains `_why_` not `_what_`.
- Safety / destructive ops: explain risk before destructive command (`rm -rf`, `git reset --hard`, etc.); never commit/push without approval.
- Verification: after each action, show minimal verification (file list / command stdout / git status) — applied in `.hermes/plans/debug-run-logs.md` (47,178 B real sequential outputs) and `.hermes/specs/debug-subgoal-final-verification.md` (5,631 B gate checklist).
- Multi-file change protocol (>6 files): 14-skill stack loaded (28 verified/mapped per `.hermes/specs/skill-verification-evidence.md`); sequential phases with gates; parallel subagent delegation for independent profile identity files (per clarification turn 3: parallel selected).
- DRY enforcement: no duplicate identity/persona rules in this file; identity rules live in `SOUL.md` (verified: identity = pragmatic senior engineer, alias `default`); execution preferences live in `user-communication-preferences` and cross-referenced here.
- Profile routing: code→architect, research→analyst, design→creative, plan→exec, teach→tutor, ops→adminbot.
- Standing goal continuation (`[Continuing toward your standing goal]`): continue end-to-end without intermediate confirmation; only pause on critical failure or explicit superseding request. Applied: full subgoal executed sequentially + parallel profile refactor without intermediate pauses (user committed full scope in single request with `/subgoal begin ...`).
- Explicit blocker reporting: `bun run check` exit 1 (41 parsing errors real — architecture concern); `hermes security audit` exit 1 (26 real vulnerabilities preserved); GitHub rate-limit 403 documented (previous subgoal); MSYS2 bash WSL Relay FAIL (50 real) — all reported in `.hermes/specs/debug-analysis-2026-09-13.md`. No hidden errors.
- No synthetic results / no synthetic session IDs: verified in `.hermes/specs/debug-subgoal-final-verification.md` and `.hermes/plans/debug-run-logs.md`. No synthetic capabilities claimed.

## Environment Stack (DRY — environment facts live in `.hermes.md` + workspace files; cross-referenced, not duplicated)

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
