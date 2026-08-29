---
name: multi-agent-fanout
title: "Multi-Agent Fanout"
description: "Use when you need to enumerate authorized LLM providers, inspect installed SDK packages, and run a prompt non-interactively across the (provider × agent) matrix. Returns structured per-cell results with provider, model, context, max_output, capabilities, status, latency, output."
trigger: /multi-agent-fanout
agent: adminbot
model: minimax/minimax-m3:free
tools: [terminal, read_file, write_file, patch, search_files, skill_view]
metadata:
  hermes:
    tags: [multi-agent, providers, fanout, devops]
---
## Table of Contents

## Goal

## Context

## Phases


# /multi-agent-fanout — Run Multi-Provider / Multi-Agent Fanout

## When to Invoke

- "Show me all authorized providers"
- "Run this prompt on every available model"
- "Smoke-test my provider setup"
- "Document packages/**/*"
- "Compare latency across providers"

## Workflow (strict sequential, "only then" is a hard constraint)

### Phase 1: Discover providers

```bash
hermes auth list
python scripts/auth_inventory.py
# Wrote: scripts/.runtime/provider_inventory.json
```

### Phase 2: Inspect packages (only after Phase 1)

```bash
python scripts/package_inspector.py
# Wrote: scripts/.runtime/packages.json
```

### Phase 3: Smoke test (only after Phase 2)

```bash
python scripts/fanout.py --smoke
# 1 cell: openrouter via openai-compat
# Must show status: ok
```

### Phase 4: Targeted run (only after Phase 3 PASS)

```bash
python scripts/fanout.py --provider gemini
python scripts/fanout.py --provider deepseek
```

### Phase 5: Full fanout (only after Phase 4)

```bash
python scripts/fanout.py --prompt "Reply with the word OK."
# Wrote: .hermes/plans/multi-agent-fanout-<date>/fanout-report.{json,md}
```

### Phase 6: Report (only after Phase 5)

Read the markdown report, summarize:

```
Fanout complete. 11 cells, 1 ok, 7 fail, 3 auth_failed.
- openrouter/minimax-m3:free: ok (3.3s)
- deepseek/deepseek-chat: 402 Insufficient Balance
- gemini/gemini-2.0-flash: 404 model retired
- (etc.)
```

## Hard Rules

1. **Never edit `provider_inventory.json` or `packages.json` directly** — they are generated artifacts. Re-run the scripts.
2. **Never run `--prompt` with destructive instructions** — fanout runs the same prompt across many providers. Keep prompts safe and idempotent.
3. **Never hardcode API keys in scripts** — always use env vars + the hermes `.env` loader.
4. **Never mark a task complete if `--smoke` does not show `status: ok`** — the smoke test is the minimum proof the pipeline works.
5. **Treat `auth_failed` and `fail` honestly in the report** — do not paper over upstream issues (e.g. `402 Insufficient Balance`) by retrying or hiding them.

## Reference

- Skill: `multi-agent-fanout` (load with `skill_view name="agent-development\multi-agent-fanout"`)
- Plan: `.hermes/plans/multi-agent-fanout-<date>/`
- Spec: `.hermes/plans/multi-agent-fanout-<date>/SPEC.md`
- In-tree SDKs: `packages/openrouter-client` (TS), `packages/openrouter-client-py` (Python)

## Verification Checklist

- [ ] `auth_inventory.py` exits 0, reports 11 providers
- [ ] `package_inspector.py` exits 0, reports ≥1 package
- [ ] `fanout.py --smoke` exits 0 with `status: ok` on at least 1 cell
- [ ] Full `fanout.py` writes report with all 11 cells
- [ ] All my files pass `bun run lint`
- [ ] `hermes skills list | grep multi-agent` shows the skill
- [ ] SESSION_REPORT.md updated
