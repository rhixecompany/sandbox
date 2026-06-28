# SandBox Root — Architecture Overview

## Overview
Monorepo workspace hosting 18+ subprojects across multiple technology stacks (Python/Django, TypeScript/Next.js, Bun scripts, MCP servers).

## Key Components
- **Bash/** — Automation toolkit (TypeScript/Bun scripts for workspace management)
- **Resume_maker/** — Resume/CV generation tool (TypeScript/Bun)
- **projects/** — 16 subprojects across Python, TypeScript, Node.js, Go, Rust, and more
- **docs/** — Hermes documentation and reference materials
- **prompts/** — 250+ prompt files for Hermes/Copilot agent workflows

## Infrastructure
- All subprojects have `.vscode/` IDE configs
- Context files (AGENTS.md, SOUL.md) placed at every project level
- GitHub Actions CI/CD workflows in select projects

Last updated: 2026-06-28
