---
name: tooling-config
title: "Tooling Config — MCP Server for All Config & Hooks"
description: "MCP server for tooling-config. Provides pre-commit, git-cliff, .gitignore, .gitmodules, .editorconfig, and Husky configuration."
version: 2.0.0
author: Hermes Agent (Alexa / default profile adminbot+tutor)
license: MIT
tags: [tooling, config, pre-commit, git-cliff, gitignore, gitmodules, editorconfig, husky]
metadata:
  hermes:
    tags: [tooling, config, pre-commit, git-cliff, gitignore, gitmodules, editorconfig, husky]
    related_skills: [tooling-lint, systematic-debugging]
    session_ref: "2026-09-14 session — Husky integration added"
    tools_discovered: 13
    tools:
      - precommit_init: Initialize pre-commit config (.pre-commit-config.yaml)
      - precommit_install: Install pre-commit hooks
      - precommit_run: Run pre-commit hooks
      - changelog_init: Initialize git-cliff changelog config
      - changelog_generate: Generate changelog
      - gitignore_init: Initialize .gitignore
      - gitignore_validate: Validate .gitignore
      - gitmodules_validate: Validate .gitmodules
      - editorconfig_init: Initialize .editorconfig
      - editorconfig_validate: Validate .editorconfig
      - husky_init: Initialize Husky git hooks (.husky/)
      - husky_install: Install Husky hooks into git
      - husky_run: Run Husky hooks
---

# Tooling Config — MCP Server

## Overview
MCP server for tooling-config. Provides 13 tools for all configuration and git hook management including Husky.

## Tools

| Tool | Description | File Types |
|------|-------------|------------|
| `precommit_init` | Initialize pre-commit config | .yaml |
| `precommit_install` | Install pre-commit hooks | Git hooks |
| `precommit_run` | Run pre-commit hooks | All |
| `changelog_init` | Initialize git-cliff changelog | .toml |
| `changelog_generate` | Generate changelog | .md |
| `gitignore_init` | Initialize .gitignore | .gitignore |
| `gitignore_validate` | Validate .gitignore | .gitignore |
| `gitmodules_validate` | Validate .gitmodules | .gitmodules |
| `editorconfig_init` | Initialize .editorconfig | .editorconfig |
| `editorconfig_validate` | Validate .editorconfig | .editorconfig |
| `husky_init` | Initialize Husky git hooks | .husky/ |
| `husky_install` | Install Husky into git config | Git config |
| `husky_run` | Run Husky hooks | All |

## Prerequisites
- pre-commit (Python)
- Husky 9.1.7 (bun)
- git-cliff (optional)
- editorconfig-checker (optional)

## Configuration Files
- `.pre-commit-config.yaml` — pre-commit hooks (trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files, check-json, check-toml)
- `.husky/pre-commit` — Husky git hook (bun run lint/typecheck/format:check/markdownlint/spellcheck)
- `.editorconfig` — EditorConfig (UTF-8, LF, indent_size=2)
- `.gitignore` — Git ignore patterns
- `cliff.toml` — git-cliff changelog config

## Husky Integration
Husky is installed via bun (`husky@9.1.7`). The `.husky/pre-commit` hook runs:
```
bun run lint
bun run typecheck
bun run format:check
bun run markdownlint
bun run spellcheck
```

## Systematic Debugging
Use `/systematic-debugging` skill (4-phase: understand/fix/verify/document) to fix all issues found by tooling-config tools.

## References
- `tooling-lint` — All linter integrations (eslint, prettier, markdownlint, cspell, mypy, pyright, husky)
- `systematic-debugging` — 4-phase root cause debugging
- `multi-file-change-protocol` — >6 file change protocol
