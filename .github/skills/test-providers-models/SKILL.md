---
name: test-providers-models
title: "Test Providers & Models"
description: "Inventory all authorized LLM providers from hermes auth + config, use web-search/mcp-fetch on provider model URLs, update/create/delete *_models.json artifacts, run benchmark tests, and configure the optimal primary model + fallback chain."
category: devops
version: 1.3.0
author: Alexa
license: MIT
tags: [providers, models, benchmark, free-tier, hermes, config, models-json, web-search, mcp-fetch]
---
# Test Providers & Models

## Overview

Automated reasoning and workflow tool for `test-providers-models`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## Goal
Inventory all authorized LLM providers from `hermes auth list` + `hermes config show`, use web-search and mcp-fetch to extract model catalogs from provider URLs, update/create/delete local `*_models.json` artifacts, discover free/zero-cost models, run standardized benchmarks as background Hermes chat calls, and configure the global model + fallback chain optimally.

## When to Use
- Auditing LLM provider credentials
- Evaluating free-tier model capabilities
- Reconfiguring primary model or fallback chain
- After adding new provider credentials
- After provider catalog changes

## When NOT to Use
- Providers already benchmarked and up-to-date
- Only paid-tier models needed

## Workflow

### Phase 0: Provider Inventory (Background)
Run auth and config discovery as a non-blocking background task.

```bash
# Run in background without timeout
hermes auth list
hermes config show
```

Build provider list:
- Root config provider from `hermes config show`
- Each credential entry from `hermes auth list` becomes a provider candidate
- Skip providers with no usable catalog endpoint

### Phase 1: Catalog Discovery via Web-Search + MCP-Fetch
Use web-search and mcp-fetch tools to extract model data from provider URLs.

**Primary sources (via web-search/mcp-fetch):**
- OpenCode Zen: search for `opencode.ai/zen/v1/models` or use direct API
- OpenRouter: search for `openrouter.ai/api/v1/models` or use direct API
- NVIDIA NIM: search for `integrate.api.nvidia.com/v1/models` or use direct API
- NousResearch: search for `inference-api.nousresearch.com/v1/models` or use direct API
- Any other providers from Phase 0

**Tool sequence:**
1. `web_search` for provider model catalog URLs and current free-model listings
2. `web_extract` / `mcp-fetch` on confirmed model catalog endpoints
3. Parse JSON response and extract model data

**Catalog file lifecycle:**
- **create** when provider URL succeeds and no local artifact exists
- **update** when provider URL succeeds and parsed rows differ from current file
- **delete** when a provider is confirmed unavailable, deprecated, or has no free models

**Update rules:**
- Only update if fetched data differs from local file (by model count or free-model set)
- Preserve local metadata/free-model annotations when possible
- Timestamp updates in file content

**Parse rule:**
- Provider = file basename minus `_models.json` and normalized to kebab-case
- Free record = `pricing.prompt == 0` and `pricing.completion == 0`, OR naming/tag includes `:free`
- Capture: id / provider / prompt_cost / completion_cost / known_source

**Outputs:**
- Updated/created/deleted `*_models.json` files
- `docs/model-summary.json`
- `docs/best-free-models.md`

### Phase 2: Model Evaluation via Background Hermes Chat
Run best-2 free model selection per provider using background Hermes chat execution:

```bash
hermes chat --toolsets "skills,web,terminal,file" -q "wgat is you knowledge_cutoff date, how large is your context_length, do you have reasoning " --provider <provider> --model <model>
```

Rules:
- Launch in background without timeouts
- If one of the top 2 candidates fails validation, replace with the next free candidate from the same provider/local catalog
- Record validation result for each: knowledge_cutoff / context_length / reasoning

Output:
- `docs/benchmark-results.json`

### Phase 3: Configure Model & Fallbacks
Apply benchmark winner as primary if different from current config; set fallback chain.

```bash
hermes config set model.default <model>
hermes config set model.provider <provider>
hermes config set fallback_providers '[...]'
```

After any config write, verify with:
- `hermes config check`
- direct YAML inspection of `~/AppData/Local/hermes/config.yaml`

Fix string-encoded list artifacts if needed with Python patching.

### Phase 4: Verify
```bash
hermes config check
```

## Known Free Models by Provider (2026-06-28)

Use live catalog parsing as source of truth:
- `opencode-zen`: look for `deepseek-v4-flash-free`, `mimo-v2.5-free`, `nemotron-3-ultra-free`
- `openrouter`: filter `pricing.prompt == 0` and `pricing.completion == 0` or naming includes `:free`
- `nvidia-nim`: confirm via live catalog fetch
- `nous`: confirm via live catalog fetch

## Output Contract

Final user-facing deliverable MUST include:
- Best 2 free models per provider
- For each model:
  - provider
  - model id
  - knowledge_cutoff date
  - context_length
  - reasoning flag
  - benchmark status
  - catalog source (local file + provider URL)

Save to:
- `docs/free-model-selection.md`

## Pitfalls

1. `hermes chat` may hang — background execution with no timeout is required
2. `hermes config set` + JSON lists — stored as YAML strings; verify and fix manually
3. OpenRouter key is in Hermes credential store, NOT available as env var in subprocesses
4. Release date vs knowledge cutoff — do not confuse
5. Model promotion expiry — filter/verify fresh before presenting
6. Reasoning vs content — some models output in `reasoning_content`
7. Config guard prevents direct `config.yaml` writes from repo-local tools; use Hermes CLI or Python terminal edits only
8. MCP fetch may require specific endpoint paths; verify URL patterns before bulk fetch
9. Web-search results may be indirect; always verify against provider API when possible

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] "Test Providers & Models" operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
