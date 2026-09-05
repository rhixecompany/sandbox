---
name: test-providers-models
trigger: "/test-providers-models /goal /using-superpowers"
title: "Test Providers & Models"
description: "Use when auditing, probing, or configuring model/auth providers across Hermes (opencode-zen, nous/openrouter, deepseek, gemini, openai-codex, xai). Produces verified inventory, probes, and rebuild specs."
version: 2.0.0
author: "Alexa"
license: MIT
tags: [auth, model, provider, probe, audit, opencode-zen, openrouter, deepseek, gemini, openai-codex]
metadata:
  hermes:
    auth_providers: [opencode-zen, nous, openrouter, deepseek, gemini, openai-codex, huggingface, minimax-oauth, xai, xai-oauth, ollama-cloud]
    verified_states:
      opencode-zen: "key1 valid; keys 2-3 auth-failed 401; key4 manual"
      openrouter: "rate-limited 429 (42m-16h)"
      openai-api: "keys 1/2/3/5 exhausted 402; key4 manual"
      openai-codex: "oauth rate-limited 429 (29d)"
      deepseek: "key valid"
      gemini: "key valid"
      nous: "device_code oauth logged in (exp 2026-09-05 08:59 WCA)"
      xai: "key1 auth-failed 403; key2 env XAI_API_KEY valid"
      huggingface: "HF_TOKEN valid"
---

# Test Providers & Models — Rebuilt 2026-09-05

## When to use
- Before claiming "all auth providers configured"
- Before ranking `:free` model suffixes (line 11 goal)
- After any `hermes auth list` / `hermes config show` change
- When `hermes doctor` reports missing tokens or rate limits

## Auth provider inventory (verified live 2026-09-05)
| Provider | Key state | Rate / limit | URL / docs |
|---|---|---|---|
| opencode-zen | OPENCODE_ZEN_API_KEY env ✓; 3 manual keys (1 valid, 2 401, 1 401) | — | `https://opencode.ai/` |
| nous (openrouter base) | device_code oauth logged in | exp 2026-09-05 08:59; portal credits 0 (no paid) | `https://inference-api.nousresearch.com/v1` |
| openrouter | OPENROUTER_API_KEY env ✓ | rate-limited 429 (42m / 16h) | `https://openrouter.ai/` |
| deepseek | DEEPSEEK_API_KEY env ✓ | — | `https://platform.deepseek.com/` |
| gemini | GOOGLE_API_KEY env ✓ | — | `https://ai.google.dev/` |
| openai-codex | device_code oauth logged in | rate-limited 429 (29d); `auth.json` refreshed 2026-09-04 | `https://github.com/features/copilot` |
| openai-api | OPENAI_API_KEY env (exhausted 402); 4 manual keys (1 valid) | multiple 402 / rate-limited | `https://platform.openai.com/` |
| huggingface | HF_TOKEN env ✓ | — | `https://huggingface.co/` |
| minimax-oauth | oauth global (exp 2027-08-31) | — | — |
| xai | XAI_API_KEY env ✓; 1 auth-failed 403 | — | `https://x.ai/` |
| ollama-cloud | OLLAMA_API_KEY env ✓ | — | `https://ollama.com/` |
| copilot | 3 credentials (GITHUB_TOKEN env, COPILOT_GITHUB_TOKEN env, api-key-3 manual) | — | `https://github.com/features/copilot` |

## Probe commands (tested)
```
hermes auth list
hermes config show
hermes status
hermes doctor
hermes doctor --fix
hermes insights
hermes fallback list
hermes model
```

## Scripts
- `scripts/test-providers-probe.py` — runs auth/config probes and writes `.hermes/reports/` output
- `scripts/sync-providers-config.py` — syncs `.env` + `auth.json` state to prompt templates

## Templates
- `templates/auth-inventory-template.md`
- `templates/probe-live-template.md`
- `templates/provider-docs-template.md`

## Scripts (rebuilt)
- `scripts/test-providers-probe.py`

## Verification checklist
- [ ] `hermes auth list` executed; all 11 providers listed
- [ ] Rate-limit / auth-failure flags captured per provider (see inventory above)
- [ ] `hermes config show` model/provider verified (`gpt-5.6-luna` / openai-api default; openrouter/nous fallbacks configured)
- [ ] `hermes status` shows valid tokens for opencode-zen/deepseek/gemini/openai-codex
- [ ] `.env` and `~/AppData/Local/hermes/auth.json` present and non-corrupt
- [ ] `templates/` and `scripts/` rebuilt (not empty/stubs)
- [ ] Prompt .md matches trigger (`test-providers-models`) and folder (`general/test-providers-models/` or `.github/prompts/test-providers-models/`)
- [ ] Score ≥98: frontmatter, 4 phases, verification checklist, references, ≤250 lines, no placeholder text, DRY
