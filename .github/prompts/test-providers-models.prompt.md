---
name: test-providers-models
...
title: Test Providers & Models
...
description: Inventory providers/models from Hermes auth/config, extract free model candidates,
  benchmark top free models via background Hermes chat runs, and adjust primary/fallback
  model config.
...
version: 1.0.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - terminal
- file
- web
scripts: []
skills: - using-superpowers
- user-communication-preferences
- verification-before-completion
formatter: default
...
plan: ''
dependencies: - skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
tags: - providers
- models
- benchmark
- free
- hermes
trigger: /test-providers-models
...
---

# Test Providers & Models

> Read-only inventory first. Any config change requires explicit authorization and verification afterward.

## Context

- **Reference skill:** `test-providers-models` at `C:\Users\Alexa\AppData\Local\hermes\skills\test-providers-models\SKILL.md`
- **Outputs:** inventory docs, optional `*_models.json` artifacts, benchmark results, and final summary

## Rules

1. Inventory before any network call.
2. Secrets stay in Hermes credential store; never print credentials.
3. Use background execution for chat-based benchmark calls without timeout.
4. After any config write, run config verification before reporting success.

## Phase 1: Provider Inventory

1. Run `hermes auth list`.
2. Run `hermes config show`.
3. Build provider/model inventory from config + auth output.
4. If a provider lacks a usable catalog, mark it explicitly.

**Exit:** inventory recorded; provider list finalized.

---

## Phase 2: Catalog Discovery

1. For each provider, fetch model catalog from known API paths or official docs:
   - OpenCode Zen: `/v1/models`
   - OpenRouter: `/api/v1/models`
   - NVIDIA NIM: `/v1/models`
   - NousResearch: `/v1/models`
2. Extract:
   - model id
   - prompt cost
   - completion cost
   - free-model identifiers

**Verification:** Only benchmark free or zero-cost candidates unless the user asks for paid models explicitly.

---

## Phase 3: Benchmark Top Free Models

1. Select top 2 free candidates per provider.
2. Run background benchmark chat calls with questions:
   - `what is your knowledge_cutoff date`
   - `how large is your context_length`
   - `do you have reasoning`
3. Capture results to `docs/benchmark-results.json`.

**Exit:** benchmark result file written for each tested model.

---

## Phase 4: Summarize Providers/models

1. Write `docs/providers-models-inventory.md` with:
   - provider summary
   - free-model list
   - benchmark winners
   - recommended primary + fallback alignment
2. If config/primary model write is authorized, run:
   - `hermes config check`
   - report current model/providers and whether change was applied.

**Exit:** summary report written; any requested config changes verified.

---

## Final Verification

- No secrets exposed
- Inventory written
- Benchmark file written if benchmarks were run
- Final summary report written
