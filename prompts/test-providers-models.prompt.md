---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Test Providers & Models
name: test-providers-models
trigger: test-providers-models
description: >-
  Inventory all authorized LLM providers from hermes auth list, discover their
  free-tier models, run standardized benchmarks (reasoning, tool calling,
  knowledge), and produce a cross-provider comparison report. Covers 6
  providers: copilot, huggingface, nous, ollama-cloud, openai-api, openrouter.
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
Inventory and benchmark the free‑tier LLM models across all authorized providers in Hermes, producing a comparative report that includes performance, rate limits, and recommendations.

## Personas
| Persona | When to Use |
|---------|-------------|
| OWL (System Admin) | Overall orchestration, profile selection |
| Research Analyst | Data analysis, cross‑provider comparison |
| Code Architect | Benchmark execution, script development |
| DevOps Engineer (adminbot) | Rate‑limit analysis, fallback planning |

## Personality & Tone
- Concise, action‑first
- Technical, direct
- No unnecessary prose

## Profile Selection
| Task | Recommended Profile |
|------|----------------------|
| Provider inventory & auth check | `default` |
| Model catalog discovery | `research-analyst` |
| Free model extraction & script creation | `code-architect` |
| Benchmark execution | `code-architect` |
| Report compilation & analysis | `research-analyst` |
| Rate‑limit & fallback analysis | `adminbot` |

## When to Use
- To audit LLM provider credentials and usage limits.
- To evaluate free‑tier model capabilities before committing to paid plans.
- When planning multi‑provider AI deployments.

## When Not to Use
- If all required providers are already benchmarked and up‑to‑date.
- When only paid‑tier models are needed for production workloads.

# Test Providers & Models

> Comprehensive provider inventory and model benchmark for Hermes Agent.
> Covers all 6 authorized providers from `hermes auth list` with 3‑tier
> (Needed / Recommended / Optional) phase categorization.

## Description

This prompt performs a full-cycle provider audit and model benchmark. It starts
by inventorying all authorized providers from `hermes auth list`, then
discovers available models per provider, extracts free/zero-cost options, and
runs a standardized 3‑task benchmark (reasoning, tool calling, knowledge).
Results are compiled into a cross‑provider comparison report with pass/fail
status, rate limits, and recommendations.

**Critical rules:**

- Test EVERY provider from `hermes auth list` — do not skip any
- Log credential status (valid / rate‑limited / missing) per provider
- Report rate limits, API errors, and auth failures per model
- Categorize each phase as Needed ✓, Recommended ☆, or Optional ◇

## Context

- **Providers (from auth list):** copilot, huggingface, nous, ollama-cloud,
  openai-api, openrouter
- **Model catalog:** `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI
- **Scripts dir:** `~/AppData/Local/hermes/scripts/`
- **Prior artifacts:** `docs/test‑providers‑models‑*` (archived from prior run)

## Provider Inventory (from `hermes auth list`) — Actual (2026-06-21)

| #   | Provider     | Auth Method                       | Credential Status     | Notes                                                             |
| --- | ------------ | --------------------------------- | --------------------- | ----------------------------------------------------------------- |
| 1   | copilot      | gh auth token, GITHUB_TOKEN       | ⚠️ Rate‑limited (429) | Both creds in cooldown (~22m remaining)                           |
| 2   | huggingface  | HF_TOKEN (env)                    | ✓ Active              | —                                                                 |
| 3   | nous         | device_code OAuth                 | ✓ Active              | —                                                                 |
| 4   | ollama-cloud | OLLAMA_API_KEY (env)              | ✓ Active              | —                                                                 |
| 5   | openai‑api   | manual key + OPENAI_API_KEY (env) | ✓ Keys present        | Not exported to subprocess env                                    |
| 6   | openrouter   | OPENROUTER_API_KEY (env)          | ✓ Active              | Stored in Hermes credential store, NOT exported to subprocess env |

**IMPORTANT:** The OpenRouter API key is managed by Hermes' secure credential store and is NOT available as an environment variable in subprocesses (curl, Python). API calls must go through the Hermes provider chain (`hermes chat -q --provider openrouter`). The key IS accessible to the Hermes agent itself — direct API benchmarking via subprocess is BLOCKED by this security boundary.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#test-providers-models)

| Skill                              | Purpose                                         | Needed? |
| ---------------------------------- | ----------------------------------------------- | ------- |
| `using-superpowers`                | Workflow foundation, tool use conventions       | ✓ Needed |
| `plans-and-specs`                  | Phase planning, progress tracking               | ✓ Needed |
| `user-communication-preferences`   | Execution style and preferences                 | ✓ Needed |
| `verification-before-completion`   | Cross‑reference all phases before claiming done | ✓ Needed |
| `gh-cli`                           | GitHub Copilot provider interaction             | ☆ Recommended |
| `provider-reliability-diagnostics` | Diagnose provider auth/rate‑limit issues        | ◇ Optional |

## Tools Required

| Tool                    | Type | Purpose                        | Needed? |
| ----------------------- | ---- | ------------------------------ | ------- |
| `hermes auth list`      | CLI  | Inventory authorized providers | ✓ Needed |
| `hermes config show`    | CLI  | Check provider config chain    | ✓ Needed |
| `terminal`              | MCP  | Run scripts, CLI commands      | ✓ Needed |
| `fetch` / `web_extract` | MCP  | Fetch model catalogs           | ✓ Needed |
| `execute_code` (Python) | MCP  | Run benchmark harness          | ☆ Recommended |
| `memory`                | MCP  | Save provider findings         | ☆ Recommended |
| `skills`                | MCP  | Load provider‑specific skills  | ◇ Optional |

## Phase Map

| Phase | Title                                | Tier          | Profile            | Est. Time |
| ----- | ------------------------------------ | ------------- | ------------------ | --------- |
| 0     | Auth & Provider Inventory            | ✓ Needed      | `default`          | 5 min     |
| 1     | Model Catalog Discovery              | ✓ Needed      | `research-analyst` | 15 min    |
| 2     | Free Model Extraction                | ✓ Needed      | `code-architect`   | 10 min    |
| 3     | Provider‑by‑Provider Benchmarking    | ☆ Recommended | `code-architect`   | 30 min    |
| 4     | Cross‑Provider Comparison & Report   | ☆ Recommended | `research-analyst` | 15 min    |
| 5     | Rate Limit & Fallback Chain Analysis | ◇ Optional    | `adminbot`         | 20 min    |
| 6     | Script Creation & Automation         | ☆ Recommended | `code-architect`   | 20 min    |

---

## Phase 0: Auth & Provider Inventory (Needed ✓)

> **Profile:** `default` | **Persona:** OWL (System Admin)
> **Goal:** Run `hermes auth list` to inventory all authorized LLM providers,

> **Full content:** `templates/test‑providers‑models/phase_0_auth__provider_invento.md`

## Phase 1: Model Catalog Discovery (Needed ✓)

> **Profile:** `research-analyst` | **Persona:** Research Analyst
> **Goal:** For each provider, discover available models through their

> **Full content:** `templates/test‑providers‑models/phase_1_model_catalog_discover.md`

## Phase 2: Free Model Extraction (Needed ✓)

> **Profile:** `code-architect` | **Persona:** Tech Lead
> **Goal:** Filter and extract zero‑cost / free‑tier models from each provider's

> **Full content:** `templates/test‑providers‑models/phase_2_free_model_extraction_.md`

## Phase 3: Provider‑by‑Provider Benchmarking (Recommended ☆)

> **Profile:** `code-architect` | **Persona:** QA Engineer
> **Goal:** Run a standardized 3‑task benchmark on each free model across all

> **Full content:** `templates/test‑providers‑models/phase_3_provider‑by‑provider_b.md`

## Phase 4: Cross‑Provider Comparison & Report (Recommended ☆)

> **Profile:** `research-analyst` | **Persona:** Data Analyst
> **Goal:** Compile benchmark results into a cross‑provider comparison report

> **Full content:** `templates/test‑providers‑models/phase_4_cross‑provider_compari.md`

## Phase 5: Rate Limit & Fallback Chain Analysis (Optional ◇)

> **Profile:** `adminbot` | **Persona:** DevOps Engineer
> **Goal:** Analyze provider rate limits, cooldown periods, and optimal fallback

> **Full content:** `templates/test‑providers‑models/phase_5_rate_limit__fallback_c.md`

## Phase 6: Script Creation & Automation (Recommended ☆)

> **Profile:** `code-architect` | **Persona:** Developer
> **Goal:** Create or update the `test_models.py` test harness to support all

> **Full content:** `templates/test‑providers‑models/phase_6_script_creation__autom.md`

## Actions Summary

| #   | Action                                          | Phase | Tier        |
| --- | ----------------------------------------------- | ----- | ----------- |
| 1   | Inventory all providers via `hermes auth list`  | 0     | Needed      |
| 2   | Discover model catalogs per provider            | 1     | Needed      |
| 3   | Extract free models across all providers        | 2     | Needed      |
| 4   | Create multi‑provider test harness script       | 6     | Recommended |
| 5   | Benchmark each free model on 3 standard tasks   | 3     | Recommended |
| 6   | Compile cross‑provider comparison report        | 4     | Recommended |
| 7   | Analyze rate limits and optimize fallback chain | 5     | Optional    |

## Related Prompts

| Prompt                                       | Relation                                               |
| -------------------------------------------- | ------------------------------------------------------ |
| `audit-skills-judge-fix.prompt.md`           | Same skill family (using‑superpowers, plans‑and‑specs) |
| `sync-hermes-copilot-codex.prompt.md`        | Provider sync workflow                                 |
| `agents-system-prompt-context-fix.prompt.md` | Hermes context debugging                               |

## Verification Checklist (Final)

- [ ] **Phase 0:** All 6 providers captured from `hermes auth list`
- [ ] **Phase 1:** Model catalogs queried per provider
- [ ] **Phase 2:** Free models extracted and tabulated
- [ ] **Phase 3:** Benchmark run on all accessible free models
- [ ] **Phase 4:** Cross‑provider comparison report generated
- [ ] **Phase 5:** Fallback chain documented (Optional)
- [ ] **Phase 6:** Test harness script supports all 6 providers
- [ ] Rate limits and errors documented per provider
- [ ] Recommendations included for best provider per task type

## Template References

Detailed section templates in `templates/test‑providers‑models/`:
- `phase_0_auth__provider_invento.md`
- `phase_1_model_catalog_discover.md`
- `phase_2_free_model_extraction_.md`
- `phase_3_provider‑by‑provider_b.md`
- `phase_4_cross‑provider_compari.md`
- `phase_5_rate_limit__fallback_c.md`
- `phase_6_script_creation__autom.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
