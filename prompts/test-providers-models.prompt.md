---
license: MIT
author: Hermes Agent
version: 1.2.0
title: Test Providers & Models
name: test-providers-models
trigger: test-providers-models
description: >-
  Inventory all authorized LLM providers, discover free-tier models from local
  *_models.json catalogs, run standardized benchmarks, and produce a
  cross-provider comparison report. Uses Hermes chat background execution for
  model selection.
tags:
  - ai-assistant
  - architecture
  - data
  - performance
  - prompts
  - testing
  - typescript
  - workflow
  - hermes
  - providers
  - models
  - benchmark
  - free-tier
  - auth-inventory
  - copilot
  - huggingface
  - nous
  - ollama
  - openai
  - openrouter
  - models-json
dependencies:
  - skill:test-providers-models
  - skill:using-superpowers
  - skill:plans-and-specs
  - skill:user-communication-preferences
  - skill:verification-before-completion
skills:
  - using-superpowers
  - plans-and-specs
  - user-communication-preferences
  - verification-before-completion
metadata:
  hermes:
    related_skills: []
    tags:
    - test-providers-models.prompt
---

## Goal
Inventory all authorized LLM providers from `hermes auth list` + `hermes config show`, determine authorization errors with courteous retry guidance, use web-search and mcp-fetch on provider model URLs, extract and save markdown docs from model URLs when needed, update/create/delete `*_models.json` and existing artifacts as appropriate, run best-2 free-model validation with background Hermes chat execution, and update Hermes config/model + fallback.

## Personas
| Persona | When to Use |
|---------|-------------|
| OWL (System Admin) | Overall orchestration, profile selection |
| Research Analyst | Model discovery, catalog analysis |
| Code Architect | Benchmark execution, background Hermes chat workflows |
| DevOps Engineer (adminbot) | Config updates and fallback chain |

## Profile Selection
| Task | Recommended Profile |
|------|----------------------|
| Provider inventory & auth check | `default` |
| Model catalog discovery | `research-analyst` |
| Free model extraction | `code-architect` |
| Benchmark execution | `code-architect` |
| Report compilation | `research-analyst` |
| Config update | `adminbot` |

## When to Use
- To audit LLM provider credentials and usage limits.
- To evaluate free-tier model capabilities before committing to paid plans.
- To use an offline-model-catalog workflow from existing `*_models.json`.

## When NOT to Use
- If all required providers are already benchmarked and up-to-date.
- When only paid-tier models are needed.

# Test Providers & Models

> Comprehensive provider inventory and model benchmark for Hermes Agent.
> Uses local catalog files and Hermes chat background execution for verification.

## Description

This prompt performs a full-cycle provider audit and model benchmark using the Hermes CLI, local `*_models.json`, and captured artifacts:
1. Inventory providers via Hermes CLI.
2. Discover free models from local `*_models.json`.
3. Validate the best 2 free models per provider using Hermes chat background execution:
   `hermes chat --toolsets "skills,web,terminal,file" -q "wgat is you knowledge_cutoff date, how large is your context_length, do you have reasoning " --provider <provider> --model <model>`
4. Compile the final selection and update config/fallbacks.

## Key Rule
Use only verified free models or recommended fallbacks documented in this repository. Skill-authoritative sources should override unverifiable free conversions.

## Context
- **Providers/artifacts:** see `C:\Users\Alexa\Desktop\SandBox\docs\provider-benchmark-report.md`
- **Local catalogs:** prefer workspace `*_models.json` files as model evidence of truth
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required
| Skill | Purpose | Needed? |
|-------|---------|---------|
| `using-superpowers` | Workflow foundation | ✓ Needed |
| `plans-and-specs` | Phase planning, execution tracking | ✓ Needed |
| `user-communication-preferences` | Execution style | ✓ Needed |
| `verification-before-completion` | Final verification gate | ✓ Needed |
| `provider-reliability-diagnostics` | Auth/rate limit troubleshooting | ◇ Optional |

## Phase Map
| Phase | Title | Tier | Profile | Time |
|-------|-------|------|---------|-------|
| 0 | Provider Inventory | ✓ Needed | `default` | 5 min |
| 1 | Local Catalog Discovery | ✓ Needed | `research-analyst` | 10 min |
| 2 | Best-2 Free Selection | ✓ Needed | `code-architect` | 20 min |
| 3 | Config Update & Verification | ✓ Needed | `adminbot` | 10 min |

## Phase 0: Provider Inventory (Needed)
**Profile:** `default`
**Goal:** Run Hermes CLI inventory and capture current credentials/config without changing anything.

Deliverables:
- Auth status per provider
- Active model/provider
- Any noted rate limit or auth issues

## Phase 1: Local Catalog Discovery (Needed)
**Profile:** `research-analyst`
**Goal:** Use the latest local `*_models.json` artifact to extract valid free candidates.

Selectors:
- Provider = file basename minus `_models.json` and normalized to kebab-case
- Free record = `pricing.prompt == 0` and `pricing.completion == 0`
- Include `:free`-tagged ids if present and supported

Deliverables:
- `docs/model-summary.json`
- `docs/best-free-models.md`

## Phase 2: Best-2 Free Selection (Needed)
**Profile:** `code-architect`
**Goal:** Validate the top 2 free models per provider by running background Hermes chat task execution for each candidate.

Use Hermes chat background execution:
```bash
hermes chat --toolsets "skills,web,terminal,file" -q "wgat is you knowledge_cutoff date, how large is your context_length, do you have reasoning " --provider <provider> --model <model>
```

Validation checks:
- knowledge_cutoff_date extracted or represented consistently
- context_length reported or represented consistently
- reasoning flag true/false or unknown
- finish state captured if available

If validation fails:
- replace failing candidate with the next free candidate from the same local catalog
- rerun background Hermes chat task execution

Deliverables:
- `docs/benchmark-results.json`
- `docs/free-model-selection.md`

## Phase 3: Config Update & Verification (Needed)
**Profile:** `adminbot`
**Goal:** Set/changed global model + fallback chain only if current config differs from the recommendation. Else document: unchanged.

```bash
hermes config set model.default <model>
hermes config set model.provider <provider>
hermes config set fallback_providers '[...]'
```

Verification:
- `hermes config check`
- inspect ` ~/AppData/Local/hermes/config.yaml`
- fix malformed JSON-string-list artifacts if present

Deliverables:
- Updated config state summary
- Verified fallback list format
- Final report in `docs/free-model-selection.md`

## Known Free Models by Provider (2026-06-28)
Source: benchmark references, local catalog parsing, Hermes artifact reports.

### opencode-zen
- `deepseek-v4-flash-free`
- `mimo-v2.5-free`
- `nemotron-3-ultra-free`

### OpenRouter (26 free models)
Key candidates:
- `qwen/qwen3-coder:free`
- `nvidia/nemotron-3-ultra-550b-a55b:free`
- `google/gemma-4-31b-it:free`
- `openrouter/owl-alpha`
- `meta-llama/llama-3.3-70b-instruct:free`
- `poolside/laguna-m.1:free`

## Actions Summary
1. Inventory providers via Hermes CLI
2. Parse `*_models.json` for free candidates
3. Run background Hermes chat task execution to validate top 2 free models per provider
4. Update config/fallbacks
5. Compile final report

## Verification Checklist (Final)
- [ ] Phase 0: All providers captured without changing credentials
- [ ] Phase 1: Local catalog free candidates parsed and summarized
- [ ] Phase 2: Best 2 free models per provider validated using Hermes chat background execution
- [ ] Phase 3: Config verified with `hermes config check`
- [ ] Final report includes best 2 free models per provider with source rationale

## Template References
- `templates/test-providers-models/phase_0_auth__provider_invento.md`
- `templates/test-providers-models/phase_1_model_catalog_discover.md`
- `templates/test-providers-models/phase_2_best2_free_selection.md`
- `templates/test-providers-models/phase_3_config_update.md`
