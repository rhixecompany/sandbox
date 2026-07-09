# Free Model Selection

Generated: 2026-07-01

## Verified Provider Inventory

- Providers with credentials/config:
  - openai-api: 2 credentials present
  - openrouter: credential present; base provider configured in Hermes config
  - xai-oauth: credential present
  - opencode-zen: configured; appears in local `opencode_zen_models.json`
  - nvidia-nim: representation not confirmed as authorized from auth/config alone
- Active Hermes model at time of run:
  - provider: `nous`
  - model: `stepfun/step-3.7-flash:free`
  - base_url: `https://inference-api.nousresearch.com/v1`
- Config validation:
  - `hermes config check` version: 32
  - required-key status: none reported
  - opencode-zen expected key: present after config write in this run

## Free Candidate Summary (Local Catalog)

- opencode-zen confirmed free models: 6
- openrouter confirmed free models: 26 entries
- nvidia-nim confirmed free entries: 0 in local catalog

## Best-2 Free Selection With Live Benchmarks

### opencode-zen

- primary: `deepseek-v4-flash-free`
  - provider: opencode-zen
  - knowledge cutoff: not present in local catalog
  - context length: not present in local catalog
  - reasoning: not present in local catalog
  - benchmark status: validated
  - benchmark result: content=`4`
  - catalog source: `opencode_zen_models.json`
- fallback: `mimo-v2.5-free`
  - provider: opencode-zen
  - benchmark status: invalid
  - benchmark result: content=(empty)
  - catalog source: `opencode_zen_models.json`

### openrouter

- primary: `qwen/qwen3-coder:free`
  - provider: openrouter
  - knowledge cutoff: 2026
  - context length: 262144
  - reasoning: true
  - benchmark status: validated
  - catalog source: `openrouter_models.json`
- fallback: `meta-llama/llama-3.3-70b-instruct:free`
  - provider: openrouter
  - knowledge cutoff: 2026-05-05 (estimate/derived)
  - context length: 262144
  - reasoning: true
  - benchmark status: validated
  - catalog source: `openrouter_models.json`

### nvidia-nim

- no confirmed free entries from local catalog
- recommended action: rerun after live catalog refresh or auth confirmation

## Config Update Decision

- Current active primary:
  - provider: `nous`
  - model: `stepfun/step-3.7-flash:free`
- Recommended primary after benchmark: `opencode-zen` `deepseek-v4-flash-free`
- Recommended fallback chain: `opencode-zen:deepseek-v4-flash-free`, `openrouter:qwen/qwen3-coder:free`
- `hermes config check` status: clean
