# Repo-Side Hook/Plugin Audit Reference

Session-specific detail captured after auditing a workspace whose canonical repo-side `.github/`
artifacts include hook wrappers, plugin-materialization workflows, and a documented hook inventory
in `copilot-instructions.md`.

## Artifact Inventory

- Hook wrapper scripts: `session-logger`, `session-auto-commit`, `governance-audit`
- Hook auditors: `add_hooks_to_config.py`, `fix_duplicate_hooks.py`, `hook-health-check.sh`
- Plugin/workflow artifacts: `check-plugin-structure.yml`, webhook-caller workflow, publish workflow
- Documentation: `copilot-instructions.md` with canonical lifecycle count and live path pointers

## Stale-Reference Findings

- `hook-health-check.sh` defaults to `.github/hooks` instead of the live Hermes hook directory
- `plugins/**` semantic assumptions in workflows despite no `plugins/` tree at repo root
- `publish.yml` references external materialization logic that may not exist in the local repo

## Triage Summary

- No `.github/approvals/` or `.github/archive/` directories present
- Live Hermes runtime artifacts are outside the repo; repo-side assets are thin wrappers or auditors
- Safe updates: documentation counts, new canonical assets under existing directories, workflow doc fixes
- Destructive updates: plugin-materialization workflow edits, bulk script/workflow deletion, new directory semantics
- Approval gating: repo PR review for instructions/scripts; repo PR plus owner confirmation for plugin materialization workflows; owner sign-off for new `.github/*` directories

## Context

- Local hooks live under `%LOCALAPPDATA%\hermes\hooks\`
- Local plugins live under `%LOCALAPPDATA%\hermes\plugins\`
- Repo-side paths may diverge from live paths after migration or profile changes
