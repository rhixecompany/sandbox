---
trigger: /test-providers-models
description: >-
  List all authorized LLM providers, extract free-tier models, and run a
  standardized benchmark (reasoning, tool calling, knowledge) on each.
tags: [hermes, copilot, opencode, providers, models, benchmark, free-tier]
dependencies:
  - skill:using-superpowers
  - skill:user-communication-preferences
  - skill:plans-and-specs
skills:
  - using-superpowers — Establishes workflow foundation
  - user-communication-preferences — Loads user prefs for execution style
  - plans-and-specs — Creates implementation plan from goal
---

# Test Providers Models

> Acts as Hermes System Administrator: lists providers, extracts free models, and benchmarks each with reasoning, tool-calling, and knowledge tasks.

## Description

This prompt performs a comprehensive benchmark of all free-tier LLM models across authorized providers. It fetches the Hermes model catalog, identifies zero-cost models, and runs a standardized 3-task benchmark on each: arithmetic reasoning, tool calling, and Hermes internals knowledge. Results are logged with performance metrics, rate limits, and pass/fail status.

**Critical rules:**
- Test ALL free models from the catalog — do not skip any
- Log rate limit or API errors for each model
- Report success/failure for each micro-task

## Context

- **Source reference:** `./test-providers-models.prompt.txt`
- **Model catalog URL:** `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

| Skill | Purpose |
| --- | --- |
| `using-superpowers` | Establishes workflow foundation |
| `user-communication-preferences` | Loads user prefs for execution style |
| `plans-and-specs` | Creates implementation plan from goal |

## Rules

1. **Exhaustive testing** — Every free model in the catalog must be tested
2. **Standardized benchmark** — All models run the same 3 micro-tasks
3. **Error logging** — Rate limits and API errors must be reported per model

## Phases

### Phase 1: List Authorized Providers

**Goal:** Fetch and display all LLM providers supported by this Hermes instance.

**Inputs:** Hermes config and model catalog

**Outputs:** Provider list with metadata

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read Hermes config for configured providers | Config provider list |
| 1.2 | Fetch model catalog JSON | Full model catalog |
| 1.3 | Display all authorized providers | Provider summary |

---

### Phase 2: Extract Free Models

**Goal:** Identify all zero-cost/free-tier models from the catalog.

**Inputs:** Model catalog from Phase 1

**Outputs:** Markdown table of free models

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Filter models with `:free` suffix or `free` description | Free model list |
| 2.2 | Compile into Markdown table (Provider, Model, Context Window) | Free models table |

**Free Models Identified (from catalog):**

| Provider | Model | Context Window |
| --- | --- | --- |
| OpenRouter | `openrouter/elephant-alpha` | 128K |
| OpenRouter | `openrouter/owl-alpha` | 128K |
| OpenRouter | `poolside/laguna-m.1:free` | 128K |
| OpenRouter | `tencent/hy3-preview:free` | 128K |
| OpenRouter | `nvidia/nemotron-3-super-120b-a12b:free` | 128K |
| OpenRouter | `nvidia/nemotron-3-ultra-550b-a55b:free` | 128K |
| OpenRouter | `inclusionai/ring-2.6-1t:free` | 128K |

---

### Phase 3: Benchmark Free Models

**Goal:** Run standardized 3-task benchmark on each free model.

**Inputs:** Free model list from Phase 2

**Outputs:** Benchmark results per model

**Benchmark Tasks:**

- **Task 1 — Reasoning/Logic:** Calculate `30 ÷ 6 = 5`, then deduce remaining balance if you start with $10 and spend $4.
- **Task 2 — Tool Calling:** Use a basic file or terminal tool (e.g., check workspace directory or print a string).
- **Task 3 — Knowledge:** Describe the built-in learning loop and how to trigger an auto-generated skill in Hermes Agent.

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | For each free model, run Task 1 | Reasoning results |
| 3.2 | For each free model, run Task 2 | Tool calling results |
| 3.3 | For each free model, run Task 3 | Knowledge results |
| 3.4 | Log performance, rate limits, errors per model | Benchmark log |

**Benchmark Results (tested model):**

| Model | Task 1 | Task 2 | Task 3 | Errors |
| --- | --- | --- | --- | --- |
| `nemotron-3-ultra-free` (opencode-zen) | ✅ PASS | ✅ PASS | ✅ PASS | None |

**Note:** Other free models require valid API keys for direct testing. See `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py` for the test harness.

---

### Phase 4: Report Results

**Goal:** Compile and present final benchmark report.

**Inputs:** All benchmark results from Phase 3

**Outputs:** Final report with pass/fail summary

**Steps:**

| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Compile all results into summary table | Summary table |
| 4.2 | Report any rate limits or API errors | Error report |
| 4.3 | Note models that completed vs failed | Completion status |

## Actions Summary

1. List all authorized LLM providers from config and catalog
2. Extract free-tier models into Markdown table
3. Run 3-task benchmark on each free model
4. Compile results, report errors, note pass/fail status