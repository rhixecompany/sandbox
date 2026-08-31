---
name: test-providers-models
title: Test Providers and Models
description: Probe authorized Hermes providers live, build a verified ordered fallback chain of working models, then configure Hermes and propagate to installed agents.
trigger: /test-providers-models
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Probe authorized Hermes providers live, build a verified ordered fallback chain of working models, then configure Hermes and propagate to installed agents.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Rules](#rules)
  - [Core Rules](#core-rules)
  - [Domain Rules](#domain-rules)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Profiles](#profiles)
- [Context Block (Generated at Runtime)](#context-block-generated-at-runtime)
- [Delegation Plan (subagents)](#delegation-plan-subagents)
- [Ranking Algorithm](#ranking-algorithm)
- [Configure Hermes](#configure-hermes)
- [Propagate to Installed Agents](#propagate-to-installed-agents)
- [Phases](#phases)
- [Verification](#verification)
- [Pitfalls](#pitfalls)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Rules](#rules)
- [Core Rules](#core-rules)
- [Domain Rules](#domain-rules)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Profiles](#profiles)
- [Context Block (Generated at Runtime)](#context-block-generated-at-runtime)
- [Delegation Plan (subagents)](#delegation-plan-subagents)
- [Ranking Algorithm](#ranking-algorithm)
- [Configure Hermes](#configure-hermes)
- [Propagate to Installed Agents](#propagate-to-installed-agents)
- [Phases](#phases)
- [Verification](#verification)
- [Pitfalls](#pitfalls)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)





Produce a **verified, ordered fallback chain** across authorized Hermes providers using only models that *actually work* after live probing, then configure Hermes and update installed agents accordingly. The ordering rule is deterministic:

**working verified status → vision access → reasoning capability → context size**

Models that are not verified working are excluded from the chain and must not be written into config or agent instructions.

## Rules

### Core Rules
See `templates/_shared/rules-core.md`.

### Domain Rules
1. **Inventory from authority** — Enumerate providers/models from `hermes auth list` and installed agent configs; never invent a provider or model ID.
2. **Probe, don't assume** — A model counts as working only after a live capability probe succeeds; no fabricated results.
3. **Working-model gating** — Non-working models are excluded from config updates and agent propagation.
4. **Deterministic ordering** — Rank by verified working status first, then vision → reasoning → context size; document every override.
5. **Agent propagation** — After Hermes config is updated, propagate the verified chain to installed AI agents with minimal, traceable edits.
6. **Verify before claiming** — Run all verification gates before reporting completion.

## Subgoals

1. **Inventory** — Enumerate every authorized provider from `hermes auth list` + `hermes config show` + installed agent configs.
2. **Probe** — Dispatch live capability probes and return structured capability data for each candidate free model.
3. **Rank** — Merge results, drop non-working providers/models, sort by working status → vision → reasoning → context rule.
4. **Configure Hermes** — Set primary model and fallback chain via `hermes config set`.
5. **Propagate** — Update installed AI agents to use only verified working models from the ranked chain.
6. **Verify** — Confirm Hermes config, agent configs, and prompt guidance all reflect the verified working set.

## Personas

- **Operator** — Runs inventory, applies config, verifies.
- **Benchmark Subagent** — Probes one provider cluster, returns structured capability JSON.
- **Reviewer** — Checks ordering rule compliance and config validity.
- **Propagator** — Applies minimal agent-config updates after Hermes config is locked.

## Profiles

Use profile `exec-assistant` for orchestration; subagents inherit the default toolset. Run from the SandBox workspace root.

## Context Block (Generated at Runtime)

```text
WORKSPACE = {{WORKSPACE_ROOT}}
HERMES_HOME = {{HERMES_HOME}}
AUTHORIZED PROVIDERS (from `hermes auth list` at runtime):
{{AUTHORIZED_PROVIDERS_LIST}}
ROOT CONFIG (from `hermes config show` at runtime):
model.provider = {{CURRENT_PROVIDER}}
model.default = {{CURRENT_MODEL}}
fallback_providers = {{CURRENT_FALLBACK_CHAIN}}
PROBE METHOD:
hermes chat --provider <provider> --model <model> -q "reply with only: vision=<yes|no> reasoning=<yes|no> ctx=<tokens>"
RETURN FORMAT (one line per model):
provider | model | working=<bool> | vision=<bool> | reasoning=<bool> | ctx=<int> | notes=<string>
VERIFIED WORKING MODELS (from live probes — re-probe before use):
{{VERIFIED_MODELS_LIST}}
EXCLUDED (from live probes):
{{EXCLUDED_MODELS_LIST}}
```

## Delegation Plan (subagents)

Dispatch in parallel by provider cluster. Each subagent gets the Context Block verbatim.

| Subagent | Cluster | Providers |
| -------- | ------- | --------- |
| A | Zen/router/deepseek | opencode-zen, openrouter, deepseek |
| B | Google/cloud/nous/hf | gemini, ollama-cloud, nous, huggingface |
| C | OAuth/codex/copilot/xai | openai-codex, copilot, xai-oauth, xai |

Each subagent:
- Probes candidate free models for its cluster.
- Reports `working=false` with error on rate-limit or auth failures.
- Returns only structured capability lines.
- Does not edit config or write files.

## Ranking Algorithm

```python
def sort_key(m):
working = 1 if m.working else 0
vision = 2 if m.vision else 0
reason = 1 if m.reasoning else 0
ctx = min(m.ctx, 2_000_000) / 2_000_000
return (working, vision, reason, ctx)

chain = sorted(working_models, key=sort_key, reverse=True)
```

## Configure Hermes

Primary model = highest-ranked verified working model.

```bash
# 1. Primary model
hermes config set model.provider <provider>
hermes config set model.default <model>

# 2. Fallback chain — provider names only, ordered by capability.
hermes config set fallback_providers '["<provider1>","<provider2>","<provider3>"]'

# 3. Ensure each fallback provider resolves to a working free model
hermes config set providers.<provider1>.default_model <model1>
hermes config set providers.<provider2>.default_model <model2>
hermes config set providers.<provider3>.default_model <model3>
```

## Propagate to Installed Agents

Propagation rules:
- Only models marked `working=true` may be written into agent configs.
- Prefer native agent CLI/config commands; avoid raw file edits unless required.
- Record every changed file and command for verification.

Propagation targets:
- Hermes profiles: `~/AppData/Local/hermes/profiles/*/SOUL.md`, `memories/USER.md`, `memories/MEMORY.md`
- Workspace context files: `.hermes.md`, `AGENTS.md`, `.github/copilot-instructions.md`
- Agent configs: `opencode.json`, `~/.opencode/*`, Codex/Copilot instruction files if present


1. **Phase 1 — Inventory** — `hermes auth list`; collect installed agent configs.
2. **Phase 2 — Probe** — Delegate live capability probes; return structured capability JSON.
3. **Phase 3 — Rank** — Apply ranking algorithm; exclude non-working models.
4. **Phase 4 — Configure** — Set Hermes primary + fallback chain via `hermes config set`; validate YAML/list type.
5. **Phase 5 — Propagate** — Update installed agents to verified working models only.
6. **Phase 6 — Verify** — Run verification gates; re-probe if drift suspected.

## Verification

```bash
hermes config check
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print(type(c['fallback_providers']), c['fallback_providers'])"
hermes profile list
```

- [ ] `hermes config check` passes
- [ ] `model.provider` and `model.default` set to verified working model
- [ ] `fallback_providers` is a YAML list ordered by capability
- [ ] Each listed provider has a working free `default_model`
- [ ] Installed agents updated to verified working models only
- [ ] Non-working models excluded from config and instruction files
- [ ] No secrets/tokens introduced
- [ ] Documentation reflects verified chain

## Pitfalls

1. **Stale promotions** — Models expire; always re-probe before treating as working.
2. **String-encoded lists** — `fallback_providers` may serialize as a string; verify and repair via terminal Python if needed.
3. **Provider alias mismatch** — Use provider names in `fallback_providers`; set each provider's `default_model`.
4. **Root vs profiles drift** — Align root first, then propagate to named profiles.
5. **Vision gap** — If no verified working free model has vision, degrade to reasoning → context; do not promote paid models into the free fallback chain.

## MCP Servers & Tools

- **Terminal** — `hermes auth list`, `hermes config set`, `hermes profile list`
- **Delegation** — `delegate_task` parallel capability probes
- **Web tools** — provider documentation lookups
- **Filesystem** — read/update agent config and instruction files

## Hooks

Shared workspace hooks run around this prompt's execution — see `.github/hooks/README.md`: `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

## Workflow

<content>

- `.enhance/analyze_prompts.py` — prompt-library analyzer
- `.enhance/verify_phase3.py` — repair/verify tooling