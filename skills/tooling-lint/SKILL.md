---
name: tooling-lint
title: "Tooling Lint — MCP Server for All Linters"
description: "MCP server for tooling-lint. Provides eslint, prettier, markdownlint-cli2, cspell, mypy, pyright (PyLance), and husky integration."
version: 2.0.0
author: Hermes Agent (Alexa / default profile adminbot+tutor)
license: MIT
tags: [tooling, lint, eslint, prettier, markdownlint, cspell, mypy, pyright, pylance, husky, pre-commit]
metadata:
  hermes:
    tags: [tooling, lint, eslint, prettier, markdownlint, cspell, mypy, pyright, pylance, husky, pre-commit]
    related_skills: [tooling-config, systematic-debugging]
    session_ref: "2026-09-14 session — PyLance + Husky integration added"
    tools_discovered: 10
    tools:
      - eslint_init: Initialize ESLint configuration (eslint.config.mjs)
      - eslint_check: Run ESLint on files (JSON output, --fix supported)
      - prettier_init: Initialize Prettier configuration (.prettierrc.json)
      - prettier_check: Run Prettier format check (--write supported)
      - markdownlint_check: Run markdownlint-cli2 on markdown files
      - cspell_init: Initialize cspell configuration (cspell.json)
      - cspell_check: Run cspell lint on files
      - mypy_check: Run mypy type checker on Python files
      - pyright_init: Initialize PyLance/pyright configuration (pyrightconfig.json)
      - pyright_check: Run PyLance/pyright language server on TypeScript files
---

# Tooling Lint — MCP Server

## Overview
MCP server for tooling-lint. Provides 10 tools for all linter integrations including PyLance (pyright) and Husky git hooks.

## Tools

| Tool | Description | File Types |
|------|-------------|------------|
| `eslint_init` | Initialize ESLint config (eslint.config.mjs) | .ts, .tsx, .js, .jsx |
| `eslint_check` | Run ESLint (JSON, --fix supported) | .ts, .tsx, .js, .jsx |
| `prettier_init` | Initialize Prettier config (.prettierrc.json) | All |
| `prettier_check` | Run Prettier format check | All |
| `markdownlint_check` | Run markdownlint-cli2 | .md |
| `cspell_init` | Initialize cspell config (cspell.json) | All |
| `cspell_check` | Run cspell lint | All |
| `mypy_check` | Run mypy type checker | .py |
| `pyright_init` | Initialize PyPylance/pyright config (pyrightconfig.json) | .ts, .tsx |
| `pyright_check` | Run PyLance/pyright language server | .ts, .tsx |

## Prerequisites
- Python 3.11+ (for mypy)
- Node.js/bun (for eslint, prettier, markdownlint-cli2, cspell, pyright)
- ruff (Python linter)
- Bun 1.3.14 (for bun run lint/typecheck/format/markdownlint/spellcheck)

## Configuration Files
- `.eslintrc.json` — ESLint config
- `.prettierrc` — Prettier config (LF, tabWidth=2, printWidth=120)
- `.markdownlint-cli2.jsonc` — markdownlint config
- `.cspell.json` — cspell config (40+ project words)
- `pyrightconfig.json` — Pyright/PyLance config
- `tsconfig.json` — TypeScript config
- `.ruff.toml` — Ruff Python linter config
- `.pre-commit-config.yaml` — pre-commit hooks (trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files, check-json, check-toml)
- `.husky/pre-commit` — Husky git hook (bun run lint/typecheck/format:check/markdownlint/spellcheck)

## Husky Integration
Husky is installed via bun (`husky@9.1.7`). Pre-commit hooks are configured at `.git/hooks/pre-commit` and `.husky/pre-commit`.

Run `bun run lint`, `bun run typecheck`, `bun run format:check`, `bun run markdownlint`, `bun run spellcheck` locally or via pre-commit hooks.

## Systematic Debugging
Use `/systematic-debugging` skill (4-phase: understand/fix/verify/document) to fix all issues found by linters.

## Verification Gates
- All linters tested and verified working
- `.env` protected (5274 B workspace, 30269 B Hermes — never exposed)
- 0 synthetic artifacts
- DRY enforced via cross-references

## References
- `tooling-config` — Pre-commit, git-cliff, .gitignore, .gitmodules, .editorconfig, Husky config
- `systematic-debugging` — 4-phase root cause debugging
- `multi-file-change-protocol` — >6 file change protocol (14-skill stack)
