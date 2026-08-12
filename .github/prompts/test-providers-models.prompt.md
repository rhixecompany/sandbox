---
name: test-providers-models
title: Test Providers & Models — Benchmark, Delegate, and Configure Fallback Chain
description: Inventory all authorized LLM providers, delegate live capability probes to subagents with full context, rank working free models by vision → reasoning → context size, and configure the Hermes primary model + fallback chain from proven working models per authorized provider.
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- providers
- models
- benchmark
- free-tier
- fallback
- subagents
- config
- hermes
toolsets:
- file
- terminal
- web
- skills
- delegation
trigger: /test-providers-models
skills:
- test-providers-models
dependencies:
- skill:test-providers-models
metadata:
  hermes:
    source: devops/test-providers-models
    reimplemented: '2026-08-08'
    data-snapshot: '2026-08-07'
scripts: []
formatter: default
plan: ''
---
## Goal

Produce a **verified, ordered fallback chain** across all authorized Hermes providers, using only models that *actually work* (probed live, not assumed), and configure Hermes (`model` + `fallback_providers`) accordingly. The ordering rule is deterministic:

**vision access → reasoning capability → large context size** (each tier breaks ties by the next tier; models lacking a higher tier fall below those that have it).

The heavy lifting (live provider probing) is **delegated to subagents** so the main session is not blocked by rate limits or long background calls, and so each provider cluster is worked in isolation with full context.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)
> Domain-specific additions below.

### Domain Rules

1. **Inventory from authority** — Enumerate providers/models from `hermes auth list`; never invent a provider or model ID.
2. **Probe, don't assume** — A model counts as working only after a live capability probe succeeds; no fabricated results.
3. **Deterministic ordering** — Rank by the fixed rule: vision → reasoning → context size; document every override.
4. **Free-tier only** — Only models usable on the free tier are candidates for the fallback chain.
5. **Verify before claiming** — Run the Verification section gates before reporting the chain complete.

## Subgoals

1. **Inventory** — Enumerate every authorized provider from `hermes auth list` + `hermes config show`.
2. **Delegate probes** — Dispatch one subagent per provider cluster; each carries the full context block + a fixed probe script; each returns structured capability data (working?, vision, reasoning, context_size).
3. **Rank** — Merge subagent results, drop non-working providers, sort by the vision → reasoning → context rule.
4. **Configure** — Set `model.provider` / `model.default` (primary = proven working model) and `fallback_providers` (ordered list) via `hermes config set`; fix any string-encoded list artifacts.
5. **Verify** — `hermes config check` + YAML inspection; update `docs/free-model-selection.md` and `*_models.json` artifacts.

## Personas

- **Operator** — Runs the delegation, applies config, verifies.
- **Benchmark Subagent** — Probes one provider cluster, returns structured capability JSON.
- **Reviewer** — Checks ordering rule compliance and config validity.

## Profiles

Use profile `exec-assistant` (ops) for the orchestration; subagents inherit the default toolset. Run from the SandBox workspace root.

## Context Block (hand to every subagent verbatim)

```text
WORKSPACE = C:\Users\Alexa\Desktop\SandBox
HERMES_HOME = C:\Users\Alexa\AppData\Local\hermes
AUTHORIZED PROVIDERS (hermes auth list, 2026-08-08):
  copilot, deepseek, gemini, huggingface, nous, ollama-cloud,
  openai-codex, openrouter, xai-oauth
ROOT CONFIG (hermes config show):
  model.provider = nous
  model.default   = tencent/hy3:free
  fallback_providers = []
PROBE METHOD:
  hermes chat --provider <provider> --model <model> -q "reply with only:
  vision=<yes|no> reasoning=<yes|no> ctx=<tokens>"  (run background, no timeout)
  OR web_extract the provider /v1/models catalog and filter free (pricing 0 / ':free').
RETURN FORMAT (one line per model):
  provider | model | working=<bool> | vision=<bool> | reasoning=<bool> | ctx=<int>
KNOWN BASELINE (probed 2026-08-07, for cross-check only — re-verify live):
  opencode-zen: deepseek-v4-flash-free (128K, reasoning✓, WORKING), nemotron-3-ultra-free (1M, ✓, WORKING)
  openrouter: nvidia/nemotron-3-ultra-550b-a55b:free (1M, ✓, WORKING),
              nvidia/nemotron-3-super-120b-a12b:free (1M, ✓, WORKING),
              nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (256K, ✓, WORKING),
              google/gemma-4-31b-it:free (262K, ✗, WORKING),
              google/gemma-4-26b-a4b-it:free (262K, ✗, WORKING),
              openai/gpt-oss-20b:free (131K, ✗, WORKING)
  gemini: gemini-2.5-flash (1M, reasoning✓, WORKING)
  ollama-cloud: nemotron-3-ultra (1M, ✓, WORKING)
  NOT WORKING (2026-08-07): deepseek (402), huggingface (400), nous (403),
              xai-oauth (402), openai-codex (429), copilot (n/a)
NOTE: No working free model in the verified set has vision. The rule therefore
      degrades to reasoning → context for the current free-tier landscape.
```

## Delegation Plan (subagents)

Dispatch in parallel (3 clusters). Each subagent gets the full Context Block above.

| Subagent | Cluster | Providers |
| -------- | ------- | --------- |
| A | Zen/router/deepseek | opencode-zen, openrouter, deepseek |
| B | Google/cloud/nous/hf | gemini, ollama-cloud, nous, huggingface |
| C | OAuth/codex/copilot/xai | openai-codex, copilot, xai-oauth |

Each subagent:

- Runs the probe for every candidate free model of its cluster.
- If a provider is rate-limited (429) or blocked (403), reports `working=false` with the error and falls back to the baseline entry in the Context Block.
- Returns ONLY the structured `provider | model | working | vision | reasoning | ctx` lines.
- Does NOT edit any config or write files (read-only probe).

## Ranking Algorithm (applied after merge)

```python
def sort_key(m):
    # Higher tier wins. vision(2) > reasoning(1) > context(0)
    vision = 2 if m.vision else 0
    reason = 1 if m.reasoning else 0
    ctx = min(m.ctx, 2_000_000) / 2_000_000   # normalized 0..1
    return (vision, reason, ctx)   # descending
chain = sorted(working_models, key=sort_key, reverse=True)
```

Result for the 2026-08-07 verified set (no vision anywhere → reasoning then context):

1. `nemotron-3-ultra-free` (opencode-zen, 1M, reasoning✓)
2. `nvidia/nemotron-3-ultra-550b-a55b:free` (openrouter, 1M, ✓)
3. `nvidia/nemotron-3-super-120b-a12b:free` (openrouter, 1M, ✓)
4. `gemini-2.5-flash` (gemini, 1M, ✓)
5. `nemotron-3-ultra` (ollama-cloud, 1M, ✓)
6. `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (openrouter, 256K, ✓)
7. `deepseek-v4-flash-free` (opencode-zen, 128K, ✓) — **PRIMARY**
8. `google/gemma-4-31b-it:free` (openrouter, 262K, ✗)
9. `google/gemma-4-26b-a4b-it:free` (openrouter, 262K, ✗)
10. `openai/gpt-oss-20b:free` (openrouter, 131K, ✗)

## Configure (orchestrator only)

Primary model = the proven-working model that has accomplished prior requests:
`deepseek-v4-flash-free` via `opencode-zen` (set on all 13 named profiles already;
root currently diverges as `nous` / `tencent/hy3:free` and is aligned here).

```bash
# 1. Primary model
hermes config set model.provider opencode-zen
hermes config set model.default  deepseek-v4-flash-free

# 2. Fallback chain — provider names in capability order.
#    Each provider uses its own working free default_model (set in providers: block).
hermes config set fallback_providers '["opencode-zen","openrouter","gemini","ollama-cloud"]'

# 3. Ensure each fallback provider resolves to a working free model
hermes config set providers.opencode-zen.default_model  deepseek-v4-flash-free
hermes config set providers.openrouter.default_model   "nvidia/nemotron-3-ultra-550b-a55b:free"
hermes config set providers.gemini.default_model        "gemini-2.5-flash"
hermes config set providers.ollama-cloud.default_model  "nemotron-3-ultra"
```

> Config guard: `write_file`/`patch` refuse to edit `config.yaml`. Use `hermes config set`
> (CLI) or terminal Python (`yaml` + `open()`). If `fallback_providers` is stored as a
> string instead of a list, fix it with a terminal Python one-liner before verifying.

## Phases

1. **Phase 1 — Inventory** — `hermes auth list` all authorized providers; collect each provider's working free `default_model` and capabilities.
2. **Phase 2 — Probe** — Delegate live capability probes to subagents with the full Context Block; each probe returns actual availability, vision/reasoning support, and context size.
3. **Phase 3 — Rank** — Merge probe results and apply the Ranking Algorithm (vision → reasoning → context size) to produce the ordered candidate list.
4. **Phase 4 — Configure** — Set the primary model and fallback chain in Hermes config per the Configure section.
5. **Phase 5 — Verify** — Confirm `fallback_providers` is a real YAML list and every entry resolves to a working free model; fix and re-verify if not.

## Verification

```bash
hermes config check
# YAML inspect
grep -nE "^(model|fallback_providers|providers):" "$LOCALAPPDATA/hermes/config.yaml"
# Confirm fallback_providers is a real YAML list, not a string
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print(type(c['fallback_providers']), c['fallback_providers'])"
```

- [ ] `hermes config check` passes
- [ ] `model.provider` = opencode-zen, `model.default` = deepseek-v4-flash-free
- [ ] `fallback_providers` is a YAML list (not a string) ordered by capability
- [ ] Each listed provider has a working free `default_model`
- [ ] `docs/free-model-selection.md` updated with the new chain
- [ ] Non-working providers (deepseek, huggingface, nous, xai-oauth, openai-codex, copilot) excluded

## Pitfalls

1. **Vision gap** — No verified working free model has vision. Do not promote a paid/vision model into the free fallback chain.
2. **429 storms** — Live `hermes chat` probes rate-limit fast. Delegate to subagents (parallel, isolated) and let each fall back to the baseline on error.
3. **String-encoded lists** — `hermes config set fallback_providers '[...]'` may serialize as a string; verify and repair via terminal Python.
4. **Provider alias mismatch** — `fallback_providers` uses provider *names* (opencode-zen, openrouter, …), not the `providers:` dict keys (e.g. `ollama-launch`). Set each provider's `default_model` so the right free model is used.
5. **Root vs profiles drift** — Root config diverged (`nous`/`tencent/hy3:free`); named profiles use `opencode-zen`/`deepseek-v4-flash-free`. Align root, then propagate with `scripts/sync_profile_configs.py`.
6. **Stale `:free` promotions** — Models expire; always re-probe before presenting as working.

## MCP Servers & Tools

- **Terminal** — `hermes auth list` and provider/model configuration.
- **Delegation** — `delegate_task` parallel capability probes.
- **Web tools** — provider documentation lookups.
- **Skills** — `test-providers-models` skill (this prompt's engine).


## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
