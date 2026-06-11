# Decision: .github/plugins/ are NOT Hermes Plugins

**Date:** 2026-06-11
**Status:** Accepted

## Context
The workspace `.github/plugins/` directory contains 46 GitHub Copilot agent configurations (e.g., `awesome-copilot`, `azure-cloud-development`, `hermes-achievements`). These are **not** Hermes plugins.

## Evidence
- No `plugin.yaml` manifest in any directory
- Content structure: `agents/`, `commands/`, `.github/` — Copilot agent format
- Hermes plugins require `plugin.yaml` with `type`, `entry_point`, `config_schema`

## Decision
Do NOT attempt to install `.github/plugins/` as Hermes plugins. Manage Hermes plugins exclusively via `config.yaml` `plugins.enabled` list.

## Consequences
- Workspace plugin configs remain for Copilot/VS Code use
- Hermes profile uses built-in plugins only (current 4: disk-cleanup, model-providers/openrouter, security-guidance, memory/honcho)
- Future custom Hermes plugins would go in `~/.hermes/plugins/<name>/` with `plugin.yaml`