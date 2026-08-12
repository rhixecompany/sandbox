---
user: Alexa
---

# USER.md — default profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity

- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: default

## Environment Stack

- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint

## Model

- deepseek-v4-flash-free (opencode-zen) [primary — all profiles, live 2026-07-31]
- nemotron-3-ultra-free (opencode-zen) [fallback chain]

## Execution Preferences

- Communication: concise bullets, lead with result, skip fluff
- Code: TypeScript strict, JSDoc/docstring _why_ not _what_
- Skills: structured SKILL.md (YAML frontmatter + md body)
- Hooks: ruff format+check --fix pre-commit
- Execution: read→patch→verify, MCP-first, no backup files
- Profile routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→alexa

## Standing Goal

Maintain/enhance all prompts at .github/prompts/ with DRY, structural sections. Uses stacked skill bundles (using-superpowers, subagent-driven-development, brainstorming) for prompt work.

## Honcho Memory

Active (hybrid mode). Use honcho_profile/context/reasoning/search as needed.

Interested in motorcycles — evaluating a second-hand burgundy/purple Harley-Davidson Sportster 1200 Custom (photos Aug 2026, stored in a yard).
Manages family travel: books and handles Air Peace domestic NG flights for family (no-show refund case Aug 2026, PNR 1J9A2F LOS→ANA, passenger Adaeze Iseghohi).
Github repo: rhixecompany/sandbox.
Prompt quality expectation: comprehensive prompts incorporating best practices from the existing codebase and all relevant MCP servers/skills.
