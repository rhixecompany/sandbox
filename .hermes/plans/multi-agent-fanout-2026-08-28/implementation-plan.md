---
title: Multi-Agent Fanout — Implementation Plan
plan: .hermes/plans/multi-agent-fanout-2026-08-28/PLAN.md
spec: .hermes/plans/multi-agent-fanout-2026-08-28/SPEC.md
status: ready
---

# Implementation Plan — Step by Step

> **Strict sequential.** Complete T(N) and verify before T(N+1).

## T1 · Create plans
- SPEC.md, PLAN.md, implementation-plan.md (this file)
- **Verify:** all 3 exist under `.hermes/plans/multi-agent-fanout-2026-08-28/`

## T2 · scripts/auth_inventory.py
- Parse `hermes auth list` text output
- Emit `scripts/.runtime/provider_inventory.json`
- **Verify:** JSON valid; 11 providers

## T3 · scripts/package_inspector.py
- Walk `packages/*/`
- Emit `scripts/.runtime/packages.json`
- **Verify:** JSON valid; 2 packages

## T4 · Provider adapters (`scripts/fanout/providers/`)
- `openrouter.py` — uses `packages/openrouter-client-py` (subprocess)
- `openai_compat.py` — generic OpenAI-compatible caller
- **Verify:** each file imports without error

## T5 · Agent adapters (`scripts/fanout/agents/`)
- `hermes.py`, `codex.py`, `opencode.py`, `copilot.py` — subprocess wrappers
- **Verify:** `subprocess.run([agent, '--version'])` works for each

## T6 · scripts/fanout.py
- Orchestrator: build cells, run, write report
- **Verify:** `--smoke` exits 0 with ≥1 real live `status: ok` cell

## T7 · Skill
- `~/AppData/Local/hermes/skills/agent-development/multi-agent-fanout/`
- 1 SKILL.md, 3 references, scripts (copies), 2 templates
- **Verify:** `hermes skills list | grep multi-agent` shows the skill

## T8 · Prompt
- `.github/prompts/multi-agent-fanout.prompt.md`
- **Verify:** file exists, has frontmatter

## T9 · Verification sweep
- All 8 verification gates from SPEC.md
- `bun run lint` clean on my files
- **Verify:** all gates PASS

## T10 · SESSION_REPORT.md
- Update with this session
- **Verify:** file updated
