---
name: test-providers-models
title: Test Providers and Models
description: "Use when testing and configuring provider fallback chains. Probes nous, opencode-zen, and openrouter providers live, builds a verified ordered fallback chain of working models, then configures Hermes and propagates to installed agents."
trigger: /test-providers-models
version: 2.0.0
author: Hermes Agent
tags: [providers, fallback, configuration, hermes]
metadata:
  hermes:
    tags: [providers, fallback, testing]
profile: code-architect
priority: high
copilot:
  model_required: sonnet
opencode:
  enabled: true
codex:
  enabled: true
toolsets:
  - terminal
  - delegation
  - filesystem
skills:
  - using-superpowers
  - hermes-profiles
dependencies: []
formatter: markdown
license: MIT
---

# Test Providers & Models

## Goal

Probe **nous**, **opencode-zen**, and **openrouter** providers live, build a verified ordered fallback chain of working models, configure Hermes, and propagate to installed agents.

## Context

This prompt targets three specific free-tier providers configured in Hermes:

| Provider | Auth Method | Known Models |
|---|---|---|
| **nous** | OAuth (device_code) | meituan/longcat-2.0:free, upstage/solar-pro4:free, nemotron-3-ultra-free |
| **opencode-zen** | API Key + OAuth | nemotron-3-ultra-free, deepseek-v4-flash-free |
| **openrouter** | API Key | nvidia/nemotron-3-ultra-550b-a55b:free, various free models |

**Working definition**: A model is "working" only after a live capability probe succeeds (returns valid response, no auth/rate-limit errors).

## Rules

1. **Inventory from authority** — Enumerate providers/models from `hermes auth list` and `hermes config show` only; never invent.
2. **Probe, don't assume** — A model counts as working only after a live capability probe succeeds.
3. **Working-model gating** — Non-working models are excluded from config and agent propagation.
4. **Deterministic ordering** — Rank by: verified working → vision → reasoning → context size (largest first).
5. **Agent propagation** — After Hermes config is locked, propagate verified chain to installed AI agents.
6. **Verify before claiming** — Run all verification gates before reporting completion.

## Subgoals

1. **Inventory** — `hermes auth list` + `hermes config show` to enumerate providers/models.
2. **Probe** — Live capability probe each candidate model via `hermes chat`.
3. **Rank** — Merge results, drop non-working, sort by capability rule.
4. **Configure** — Set Hermes primary model + fallback chain via `hermes config set`.
5. **Propagate** — Update installed agents to use only verified working models.
6. **Verify** — Confirm config, agent configs, and prompt guidance reflect verified chain.

## Phases

### Phase 1: Inventory

Run and capture output from:

```bash
hermes auth list
hermes config show
hermes profile list
```

Extract:
- Authorized providers (nous, opencode-zen, openrouter)
- Current primary model and fallback chain
- Available models per provider from config.yaml

### Phase 2: Probe

For each provider × model combination, run a live capability probe:

```bash
hermes chat --provider <provider> --model <model> -q "Reply with ONLY: vision=<yes|no> reasoning=<yes|no> ctx=<max_tokens>" --oneshot -Q --ignore-rules --ignore-user-config --timeout 30
```

Record: `provider | model | working=<bool> | vision=<bool> | reasoning=<bool> | ctx=<int> | notes`

**Probe criteria**:
- `working=true`: valid response, no auth/rate-limit errors
- `vision=true`: model accepts image inputs
- `reasoning=true`: model supports chain-of-thought
- `ctx`: maximum context window in tokens

### Phase 3: Rank

Apply ranking algorithm:

```python
def sort_key(m):
    working = 1 if m.working else 0
    vision = 2 if m.vision else 0
    reason = 1 if m.reasoning else 0
    ctx = min(m.ctx, 2_000_000) / 2_000_000
    return (working, vision, reason, ctx)

chain = sorted(working_models, key=sort_key, reverse=True)
```

Exclude any model with `working=false` from the chain.

### Phase 4: Configure Hermes

Set primary model and fallback chain:

```bash
# 1. Primary model (highest-ranked verified working)
hermes config set model.provider <top_provider>
hermes config set model.default <top_model>

# 2. Fallback chain — ordered list of provider names
hermes config set fallback_providers '["<provider1>","<provider2>","<provider3>"]'

# 3. Ensure each fallback provider resolves to a working model
hermes config set providers.<provider1>.default_model <model1>
hermes config set providers.<provider2>.default_model <model2>
hermes config set providers.<provider3>.default_model <model3>
```

**Verify YAML type**:
```bash
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print(type(c['fallback_providers']), c['fallback_providers'])"
```

`fallback_providers` must be a YAML list, not a string.

### Phase 5: Propagate to Agents

Update installed AI agents to use only verified working models:

**Hermes profiles**:
- `~/AppData/Local/hermes/profiles/*/SOUL.md` — update model references
- `~/AppData/Local/hermes/profiles/*/memories/USER.md` — update model references
- `~/AppData/Local/hermes/profiles/*/memories/MEMORY.md` — update if stale

**Workspace context files**:
- `.hermes.md` — update provider/model tables
- `AGENTS.md` — update profile routing table
- `.github/copilot-instructions.md` — update model references

**Agent configs**:
- `~/.opencode/mcp.json` — update model if referenced
- `~/.codex/mcp.json` — update model if referenced

**Propagation rules**:
- Only models with `working=true` may be written
- Prefer `hermes config set` CLI; avoid raw YAML edits
- Record every changed file and command

### Phase 6: Verify

Run all verification gates:

```bash
hermes config check
hermes profile list
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); assert isinstance(c['fallback_providers'], list), 'fallback_providers must be a list'; print('OK:', c['fallback_providers'])"
```

**Verification checklist**:
- [ ] `hermes config check` passes
- [ ] `model.provider` and `model.default` set to verified working model
- [ ] `fallback_providers` is a YAML list ordered by capability
- [ ] Each listed provider has a working `default_model`
- [ ] Installed agents updated to verified working models only
- [ ] Non-working models excluded from config and instruction files
- [ ] No secrets/tokens introduced
- [ ] Documentation reflects verified chain

## Personas

| Persona | Role |
|---|---|
| **Operator** | Runs inventory, applies config, verifies |
| **Benchmark Subagent** | Probes one provider, returns structured capability JSON |
| **Reviewer** | Checks ordering rule compliance and config validity |
| **Propagator** | Applies minimal agent-config updates after Hermes config is locked |

## Context Block (Generated at Runtime)

```text
WORKSPACE = C:\Users\Alexa\Desktop\SandBox
HERMES_HOME = C:\Users\Alexa\AppData\Local\hermes
AUTHORIZED PROVIDERS (from `hermes auth list` at runtime):
  - nous (oauth, device_code)
  - opencode-zen (api_key + oauth)
  - openrouter (api_key)
ROOT CONFIG (from `hermes config show` at runtime):
  model.provider = <current>
  model.default = <current>
  fallback_providers = <current_chain>
PROBE METHOD:
  hermes chat --provider <provider> --model <model> -q "reply with only: vision=<yes|no> reasoning=<yes|no> ctx=<tokens>" --oneshot -Q --ignore-rules --ignore-user-config --timeout 30
VERIFIED WORKING MODELS (from live probes — re-probe before use):
  <populated during Phase 2>
EXCLUDED (from live probes):
  <populated during Phase 2>
```

## Pitfalls

1. **Stale promotions** — Models expire; always re-probe before treating as working.
2. **String-encoded lists** — `fallback_providers` may serialize as a string; verify and repair via terminal Python.
3. **Provider alias mismatch** — Use provider names in `fallback_providers`; set each provider's `default_model` separately.
4. **Root vs profiles drift** — Align root first, then propagate to named profiles.
5. **Vision gap** — If no verified working free model has vision, degrade to reasoning → context.
6. **Auth failures** — opencode-zen keys may be revoked; deepseek returns 401 with invalid key.
7. **Rate limits** — openrouter free models may hit 429; mark as `working=false` if rate-limited during probe.

## MCP Servers & Tools

- **Terminal** — `hermes auth list`, `hermes config set`, `hermes profile list`, `hermes chat`
- **Delegation** — `delegate_task` for parallel capability probes
- **Filesystem MCP** — read/update agent config and instruction files
- **Memory MCP** — record verified chain for cross-session recall

## Hooks

Shared workspace hooks run around this prompt's execution:
- `session-logger` — logs session start/end
- `session-auto-commit` — auto-commits at session end
- `governance-audit` — audits policy compliance
- `pre-exec-validate.sh` — validates before execution
- `post-exec-state-log.py` — logs state after execution

## Scripts

- `scripts/provider_executor.py` — non-interactive provider testing (enhanced in this session)
- `scripts/batch_skill_judge.py` — batch skill quality scoring

## Verification Checklist

- [ ] `hermes config check` passes
- [ ] `model.provider` and `model.default` set to verified working model
- [ ] `fallback_providers` is a YAML list ordered by capability
- [ ] Each listed provider has a working free `default_model`
- [ ] Installed agents updated to verified working models only
- [ ] Non-working models excluded from config and instruction files
- [ ] No secrets/tokens introduced
- [ ] Documentation reflects verified chain
