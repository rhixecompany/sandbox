# Comprehensive Hermes Maintenance — Template Body

## Goal

Keep the SandBox workspace and the local Hermes installation (`~/AppData/Local/hermes`)
healthy, synchronized, and free of stale or duplicate state. Cover quick-commands,
config/`.env` parity, MCP client sync, hooks/plugins/agents integrity, Docker and
AI-agent cleanup, and the quality score bar for specs/plans/prompts/scripts/hooks/plugins
judges (≥99).

## When to Use

- After adding or removing root scripts, plugins, or hooks
- After a Hermes upgrade that touches `config.yaml`, `.env`, or `auth.json`
- After modifying `.mcp/registry.json` (OpenCode, Codex, Copilot, VS Code clients)
- Before a release branch is cut
- Whenever a `hermes doctor` or judge-skill run returns below target

## Required Sections in the Spec

| Section | Required | Notes |
|---|---|---|
| `## Goal` | yes | one sentence |
| `## Scope` | yes | repo + Hermes root paths |
| `## Phases` | yes | ordered, with concrete file/line targets |
| `## Verification` | yes | how each phase passes (commands + expected output) |
| `## Risks` | yes | destructive ops, secrets, rate-limits |
| `## Rollback` | yes | exact inverse per phase |
| `## Milestones & Timelines` | yes | table of date → milestone |

## When NOT to Use

- Read-only audits (use `verify-full-implementation.py` + the six QA judge skills)
- Profile-only drift (use `hermes-profile-sync` skill)
- Secret-value extraction (always redacted; use env-var-name inventory only)

## Verification Checklist

- [ ] `hermes doctor` exits 0
- [ ] `hermes security audit` exits 0
- [ ] All six judge skills (specs/plans/prompts/scripts/hooks/plugins) report ≥99
- [ ] `python scripts/hermes_quick_commands.py inventory` shows every root script mapped
- [ ] `python scripts/mcp_sync.py --dry-run` reports "no change" against the 4 client configs
- [ ] `git status` is clean (or only intended modifications)
- [ ] No `.env` values were read into context
