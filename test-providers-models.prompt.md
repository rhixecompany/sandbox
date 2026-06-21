---
trigger: /test-providers-models
description: >-
  Inventory all authorized LLM providers from hermes auth list, discover their
  free-tier models, run standardized benchmarks (reasoning, tool calling,
  knowledge), and produce a cross-provider comparison report. Covers 6
  providers: copilot, huggingface, nous, ollama-cloud, openai-api, openrouter.
tags:
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
  - provider:hermes-auth
  - skill:using-superpowers
  - skill:plans-and-specs
  - skill:user-communication-preferences
  - skill:verification-before-completion
skills:
  - using-superpowers
  - plans-and-specs
  - user-communication-preferences
  - verification-before-completion
---

# Test Providers & Models

> Comprehensive provider inventory and model benchmark for Hermes Agent.
> Covers all 6 authorized providers from `hermes auth list` with 3-tier
> (Needed / Recommended / Optional) phase categorization.

## Description

This prompt performs a full-cycle provider audit and model benchmark. It starts
by inventorying all authorized providers from `hermes auth list`, then
discovers available models per provider, extracts free/zero-cost options, and
runs a standardized 3-task benchmark (reasoning, tool calling, knowledge).
Results are compiled into a cross-provider comparison report with pass/fail
status, rate limits, and recommendations.

**Critical rules:**

- Test EVERY provider from `hermes auth list` — do not skip any
- Log credential status (valid / rate-limited / missing) per provider
- Report rate limits, API errors, and auth failures per model
- Categorize each phase as Needed ✓, Recommended ☆, or Optional ◇

## Context

- **Providers (from auth list):** copilot, huggingface, nous, ollama-cloud,
  openai-api, openrouter
- **Model catalog:** `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI
- **Scripts dir:** `~/AppData/Local/hermes/scripts/`
- **Prior artifacts:** `docs/test-providers-models-*` (archived from prior run)

## Provider Inventory (from `hermes auth list`) — Actual (2026-06-21)

| #   | Provider     | Auth Method                       | Credential Status     | Notes                                                             |
| --- | ------------ | --------------------------------- | --------------------- | ----------------------------------------------------------------- |
| 1   | copilot      | gh auth token, GITHUB_TOKEN       | ⚠️ Rate-limited (429) | Both creds in cooldown (~22m remaining)                           |
| 2   | huggingface  | HF_TOKEN (env)                    | ✓ Active              | —                                                                 |
| 3   | nous         | device_code OAuth                 | ✓ Active              | —                                                                 |
| 4   | ollama-cloud | OLLAMA_API_KEY (env)              | ✓ Active              | —                                                                 |
| 5   | openai-api   | manual key + OPENAI_API_KEY (env) | ✓ Keys present        | Not exported to subprocess env                                    |
| 6   | openrouter   | OPENROUTER_API_KEY (env)          | ✓ Active              | Stored in Hermes credential store, NOT exported to subprocess env |

**IMPORTANT:** The OpenRouter API key is managed by Hermes' secure credential store and is NOT available as an environment variable in subprocesses (curl, Python). API calls must go through the Hermes provider chain (`hermes chat -q --provider openrouter`). The key IS accessible to the Hermes agent itself — direct API benchmarking via subprocess is BLOCKED by this security boundary.

## Skills Required

| Skill                              | Purpose                                         | Needed?       |
| ---------------------------------- | ----------------------------------------------- | ------------- |
| `using-superpowers`                | Workflow foundation, tool use conventions       | ✓ Needed      |
| `plans-and-specs`                  | Phase planning, progress tracking               | ✓ Needed      |
| `user-communication-preferences`   | Execution style and preferences                 | ✓ Needed      |
| `verification-before-completion`   | Cross-reference all phases before claiming done | ✓ Needed      |
| `gh-cli`                           | GitHub Copilot provider interaction             | ☆ Recommended |
| `provider-reliability-diagnostics` | Diagnose provider auth/rate-limit issues        | ◇ Optional    |

## Tools Required

| Tool                    | Type | Purpose                        | Needed?       |
| ----------------------- | ---- | ------------------------------ | ------------- |
| `hermes auth list`      | CLI  | Inventory authorized providers | ✓ Needed      |
| `hermes config show`    | CLI  | Check provider config chain    | ✓ Needed      |
| `terminal`              | MCP  | Run scripts, CLI commands      | ✓ Needed      |
| `fetch` / `web_extract` | MCP  | Fetch model catalogs           | ✓ Needed      |
| `execute_code` (Python) | MCP  | Run benchmark harness          | ☆ Recommended |
| `memory`                | MCP  | Save provider findings         | ☆ Recommended |
| `skills`                | MCP  | Load provider-specific skills  | ◇ Optional    |

## Phase Map

| Phase | Title                                | Tier          | Profile            | Est. Time |
| ----- | ------------------------------------ | ------------- | ------------------ | --------- |
| 0     | Auth & Provider Inventory            | ✓ Needed      | `default`          | 5 min     |
| 1     | Model Catalog Discovery              | ✓ Needed      | `research-analyst` | 15 min    |
| 2     | Free Model Extraction                | ✓ Needed      | `code-architect`   | 10 min    |
| 3     | Provider-by-Provider Benchmarking    | ☆ Recommended | `code-architect`   | 30 min    |
| 4     | Cross-Provider Comparison & Report   | ☆ Recommended | `research-analyst` | 15 min    |
| 5     | Rate Limit & Fallback Chain Analysis | ◇ Optional    | `adminbot`         | 20 min    |
| 6     | Script Creation & Automation         | ☆ Recommended | `code-architect`   | 20 min    |

---

## Phase 0: Auth & Provider Inventory (Needed ✓)

**Profile:** `default` | **Persona:** OWL (System Admin)

**Goal:** Run `hermes auth list` to inventory all authorized LLM providers,
their credential status, and auth methods.

**Tools:** `terminal`, `hermes auth list`, `hermes config show`

**Skills:** `using-superpowers`

**Inputs:** Hermes CLI

**Outputs:** Provider inventory table (as shown above)

### Steps

| Step | Action                                    | Tools    | Output                |
| ---- | ----------------------------------------- | -------- | --------------------- |
| 0.1  | Run `hermes auth list`                    | terminal | Raw auth list         |
| 0.2  | Run `hermes config show \| grep provider` | terminal | Provider config chain |
| 0.3  | Check rate-limit status for each provider | terminal | Rate limit report     |
| 0.4  | Compile into provider inventory table     | terminal | Markdown table        |
| 0.5  | Log results to memory                     | memory   | Saved findings        |

### Verification

- [ ] All 6 providers from auth list are captured
- [ ] Credential status documented per provider
- [ ] Rate-limit cooldowns noted where applicable
- [ ] Provider config chain matches auth list

---

## Phase 1: Model Catalog Discovery (Needed ✓)

**Profile:** `research-analyst` | **Persona:** Research Analyst

**Goal:** For each provider, discover available models through their
respective model discovery mechanisms.

**Tools:** `fetch`/`web_extract`, `terminal`, `execute_code`

**Skills:** `plans-and-specs`

**Inputs:** Provider inventory from Phase 0

**Outputs:** Per-provider model catalog table

### Provider Discovery Methods — Results (2026-06-21)

| Provider     | Discovery Method     | Models Found | Free Models | Status                       |
| ------------ | -------------------- | ------------ | ----------- | ---------------------------- |
| openrouter   | OpenRouter Live API  | 340 total    | 27 free     | ✅ Live data                 |
| openai-api   | OpenAI models API    | N/A          | N/A         | ❌ Key not in subprocess env |
| huggingface  | HF Inference API     | 10+ warm     | Varies      | ✅ API query worked          |
| nous         | Hermes model catalog | 24 curated   | TBD live    | ✅ From catalog JSON         |
| ollama-cloud | Ollama tags API      | TBD          | TBD         | ◇ Not queried                |
| copilot      | GitHub Copilot API   | TBD          | TBD         | ⚠️ Rate-limited              |

**Key Discovery:** The Hermes Model Catalog (v1, updated 2026-06-16) contains only **33 curated OpenRouter models** and **24 Nous models**. The live OpenRouter API has **340 models** — 10× more. Always prefer the live API over the curated catalog for discovery.

### Steps

| Step | Action                             | Tools    | Output                |
| ---- | ---------------------------------- | -------- | --------------------- |
| 1.1  | Fetch OpenRouter model catalog     | fetch    | OpenRouter model list |
| 1.2  | Fetch OpenAI model catalog         | fetch    | OpenAI model list     |
| 1.3  | Fetch HuggingFace inference models | fetch    | HF model list         |
| 1.4  | Fetch Nous Hermes catalog          | fetch    | Nous model list       |
| 1.5  | Fetch Ollama cloud catalog         | fetch    | Ollama model list     |
| 1.6  | Fetch Copilot available models     | terminal | Copilot model list    |
| 1.7  | Compile per-provider model tables  | terminal | Catalog summary       |

### Verification

- [ ] All 6 providers queried for models
- [ ] Results captured in structured format
- [ ] Failed/disconnected providers noted
- [ ] Models with context window sizes recorded

---

## Phase 2: Free Model Extraction (Needed ✓)

**Profile:** `code-architect` | **Persona:** Tech Lead

**Goal:** Filter and extract zero-cost / free-tier models from each provider's
catalog.

**Tools:** `execute_code` (Python), `terminal`

**Skills:** `plans-and-specs`

**Inputs:** Per-provider catalogs from Phase 1

**Outputs:** Comprehensive free models table

### Free Model Identification Heuristics

| Heuristic             | Description                      | Example                                  |
| --------------------- | -------------------------------- | ---------------------------------------- |
| `:free` suffix        | Model ID ends with `:free`       | `nvidia/nemotron-3-ultra-550b-a55b:free` |
| `free` in description | Tag/category contains "free"     | —                                        |
| `free` in tier field  | Pricing tier = free              | —                                        |
| Known free models     | Hardcoded known free models      | GPT-4o mini free tier                    |
| No-cost inference     | Models available without API key | Some HF inference models                 |

### Steps

| Step | Action                                              | Output                |
| ---- | --------------------------------------------------- | --------------------- |
| 2.1  | Parse OpenRouter catalog for `:free` models         | OpenRouter free table |
| 2.2  | Parse OpenAI catalog for free-tier models           | OpenAI free table     |
| 2.3  | Parse HuggingFace catalog for free inference models | HF free table         |
| 2.4  | Parse Nous catalog for free models                  | Nous free table       |
| 2.5  | Parse Ollama cloud catalog for free models          | Ollama free table     |
| 2.6  | Parse Copilot catalog for free models               | Copilot free table    |
| 2.7  | Compile master free models table                    | Master table          |

### Free Models Table — Actual (27 free models from OpenRouter)

| Provider              | Model                                       | Context | Type                                |
| --------------------- | ------------------------------------------- | ------- | ----------------------------------- |
| cognitivecomputations | dolphin-mistral-24b-venice-edition:free     | 32K     | Uncensored general                  |
| cohere                | north-mini-code:free                        | 256K    | Agentic coding (30B MoE, 3B active) |
| google                | gemma-4-26b-a4b-it:free                     | 262K    | MoE instruction-tuned               |
| google                | gemma-4-31b-it:free                         | 262K    | Dense multimodal 31B                |
| google                | lyria-3-clip-preview                        | 1M      | Music generation (non-text)         |
| google                | lyria-3-pro-preview                         | 1M      | Music generation (non-text)         |
| liquid                | lfm-2.5-1.2b-instruct:free                  | 32K     | Compact 1.2B instruct               |
| liquid                | lfm-2.5-1.2b-thinking:free                  | 32K     | Compact 1.2B reasoning              |
| meta-llama            | llama-3.2-3b-instruct:free                  | 131K    | Multilingual 3B                     |
| meta-llama            | llama-3.3-70b-instruct:free                 | 131K    | Multilingual 70B                    |
| nex-agi               | nex-n2-pro:free                             | 262K    | Agentic 397B MoE (17B active)       |
| nousresearch          | hermes-3-llama-3.1-405b:free                | 131K    | Generalist 405B                     |
| nvidia                | nemotron-3-nano-30b-a3b:free                | 256K    | Small MoE 30B                       |
| nvidia                | nemotron-3-nano-omni-30b-a3b-reasoning:free | 256K    | Reasoning MoE 30B                   |
| nvidia                | nemotron-3-super-120b-a12b:free             | 1M      | Hybrid MoE 120B                     |
| nvidia                | nemotron-3-ultra-550b-a55b:free             | 1M      | Frontier reasoning 550B             |
| nvidia                | nemotron-3.5-content-safety:free            | 128K    | Content safety guardrail            |
| nvidia                | nemotron-nano-12b-v2-vl:free                | 128K    | Multimodal VL 12B                   |
| nvidia                | nemotron-nano-9b-v2:free                    | 128K    | LLM 9B                              |
| openai                | gpt-oss-120b:free                           | 131K    | Open-weight 117B MoE                |
| openai                | gpt-oss-20b:free                            | 131K    | Open-weight 21B                     |
| openrouter            | free (router)                               | 200K    | Auto-router to free models          |
| openrouter            | owl-alpha                                   | 1M+     | Agentic foundation model            |
| poolside              | laguna-m.1:free                             | 262K    | Coding agent model                  |
| poolside              | laguna-xs.2:free                            | 262K    | Coding agent model (XS)             |
| qwen                  | qwen3-coder:free                            | 1M      | MoE code model 480B                 |
| qwen                  | qwen3-next-80b-a3b-instruct:free            | 262K    | MoE instruct 80B                    |

### Verification

- [ ] All `:free` suffix models captured
- [ ] No models with known cost included
- [ ] Context window size recorded per model
- [ ] Master table sorted by provider then model name

---

## Phase 3: Provider-by-Provider Benchmarking (Recommended ☆)

**Profile:** `code-architect` | **Persona:** QA Engineer

**Goal:** Run a standardized 3-task benchmark on each free model across all
providers.

**Tools:** `terminal`, `execute_code`, `skills`, `memory`

**Skills:** `user-communication-preferences`, `verification-before-completion`

**Scripts:** `~/AppData/Local/hermes/scripts/test_models.py` (create or update)

**Inputs:** Free models table from Phase 2

**Outputs:** Per-model benchmark results

### Standardized Benchmark Tasks

| Task   | Category        | Description                                                       | Expected             |
| ------ | --------------- | ----------------------------------------------------------------- | -------------------- |
| Task 1 | Reasoning/Logic | `30 ÷ 6 = 5`, then deduce: start $10 spend $4 remaining?          | $6                   |
| Task 2 | Tool Calling    | Execute a basic file/terminal tool (list directory, print string) | Tool executed        |
| Task 3 | Knowledge       | Describe Hermes built-in learning loop and auto-skill trigger     | Accurate description |

### Provider Testing Strategy

| Provider     | Test Strategy                                               | Auth Required     | Notes                                                  |
| ------------ | ----------------------------------------------------------- | ----------------- | ------------------------------------------------------ |
| openrouter   | Route through Hermes `hermes chat -q --provider openrouter` | Managed by Hermes | ⚠️ Key NOT in env; must go through Hermes agent itself |
| openai-api   | Route through Hermes provider chain                         | Managed by Hermes | Same constraint — key not in subprocess env            |
| huggingface  | HF_INFERENCE_ENDPOINT or hermes provider                    | HF_TOKEN          | May be accessible differently                          |
| nous         | Nous Portal OAuth (managed)                                 | device_code       | Auto-managed by Hermes                                 |
| ollama-cloud | Ollama cloud API                                            | OLLAMA_API_KEY    | Check env availability                                 |
| copilot      | GitHub Copilot API                                          | gh auth token     | ⚠️ Rate-limited (429) 22m+ cooldown                    |

**⚠️ CRITICAL CONSTRAINT:** API keys (especially `OPENROUTER_API_KEY`) are stored in Hermes' secure credential store and NOT exported to subprocess environments. Direct API benchmarking via curl/Python subprocess is BLOCKED. All tests must route through the Hermes provider chain using:

```bash
hermes chat -q '<prompt>' --model '<model>' --provider openrouter -Q --yolo
```

**Pragmatic approach for benchmarking:**

1. Use `delegate_task` to spawn subagents that test through Hermes' provider chain
2. Use `hermes chat -q -Q --yolo` with tool-restricted mode
3. Verify free models by checking `pricing: {prompt: "0", completion: "0"}` in the OpenRouter API first

### Steps

| Step | Action                                                                   | Output                                       |
| ---- | ------------------------------------------------------------------------ | -------------------------------------------- |
| 3.1  | Read model catalog (Hermes catalog JSON + OpenRouter live API)           | Model candidate list                         |
| 3.2  | Create/update test harness script                                        | `test_models.py` with multi-provider support |
| 3.3  | Run Task 1 on all free models via `hermes chat -q --provider openrouter` | Reasoning results table                      |
| 3.4  | Run Task 2 on all free models (agentic tool calling)                     | Tool calling results table                   |
| 3.5  | Run Task 3 on all free models (Hermes knowledge)                         | Knowledge results table                      |
| 3.6  | Log rate limits, errors, latency per model                               | Benchmark metrics log                        |
| 3.7  | Save results to memory                                                   | `memory target=memory`                       |

### Important Constraint (Discovered 2026-06-21)

The OpenRouter API key (`OPENROUTER_API_KEY`) is stored in Hermes' secure credential store and is NOT exported to subprocess environments. Direct API calls via `curl` or Python's `urllib`/`requests` in subprocesses will FAIL with empty or redacted credentials.

**Workaround:** Route all model tests through the Hermes provider chain:

```bash
hermes chat -q '<prompt>' --model <model_id> --provider openrouter -Q --yolo -t ""
```

**Alternative:** Use `delegate_task` to spawn subagents that inherit the Hermes provider configuration from the parent session.

**Advanced alternative (for scripted automation):** Use `execute_code` with `terminal()` calls that invoke `hermes chat` — the `terminal()` helper inherits the Hermes runtime environment.

### Benchmark Results — Spot Check (2026-06-21)

| Model                               | Task 1 (Reason) | Task 2 (Tool) | Task 3 (Knowledge) | Notes               |
| ----------------------------------- | --------------- | ------------- | ------------------ | ------------------- |
| `openrouter/elephant-alpha`         | ⏳ Pending      | ⏳ Pending    | ⏳ Pending         | Tested via subagent |
| _(Full 27-model benchmark pending)_ |                 |               |                    |                     |

**Note:** Full 27-model benchmarking is a multi-hour process when routing through `hermes chat -q` due to sequential agent sessions. For automated bulk testing, consider pre-funding the OpenRouter account with credits and using direct API calls (avoids the credential redaction issue).

### Benchmark Results Table Template

| Provider     | Model                 | Task 1  | Task 2  | Task 3  | Errors | Latency |
| ------------ | --------------------- | ------- | ------- | ------- | ------ | ------- |
| opencode-zen | nemotron-3-ultra-free | ✅ PASS | ✅ PASS | ✅ PASS | None   | —       |
| ...          | ...                   | ...     | ...     | ...     | ...    | ...     |

### Verification

- [ ] All free models from Phase 2 are benchmarked
- [ ] Rate limits and API errors logged per model
- [ ] Test harness script handles all 6 providers
- [ ] Results saved for Phase 4 analysis

---

## Phase 4: Cross-Provider Comparison & Report (Recommended ☆)

**Profile:** `research-analyst` | **Persona:** Data Analyst

**Goal:** Compile benchmark results into a cross-provider comparison report
with recommendations.

**Tools:** `terminal`, `memory`, `skills`

**Skills:** `plans-and-specs`, `verification-before-completion`

**Inputs:** Benchmark results from Phase 3

**Outputs:** Final comparison report with recommendations

### Steps

| Step | Action                                     | Output                 |
| ---- | ------------------------------------------ | ---------------------- |
| 4.1  | Aggregate results by provider              | Provider summary table |
| 4.2  | Score each provider on reliability + speed | Provider scores        |
| 4.3  | Rank providers by task type suitability    | Ranked comparisons     |
| 4.4  | Write final report with recommendations    | Comparison report      |
| 4.5  | Save report to memory                      | `memory target=memory` |

### Report Sections

1. **Provider Overview** — Which providers have usable free models
2. **Benchmark Ranking** — Models ranked by task performance
3. **Reliability Score** — Rate limits, uptime, error rates per provider
4. **Recommendations** — Best provider per task type (reasoning, tools, knowledge)
5. **Fallback Chain** — Optimal provider fallback order

### Verification

- [ ] All providers from Phase 0 included in comparison
- [ ] Pass/fail status clear per model per task
- [ ] Rate-limit issues documented
- [ ] Recommendations are actionable and prioritized

---

## Phase 5: Rate Limit & Fallback Chain Analysis (Optional ◇)

**Profile:** `adminbot` | **Persona:** DevOps Engineer

**Goal:** Analyze provider rate limits, cooldown periods, and optimal fallback
chain configuration.

**Tools:** `terminal`, `provider-reliability-diagnostics` skill

**Skills:** `plans-and-specs`

**Inputs:** Rate limit data from Phase 3

**Outputs:** Fallback chain recommendation

### Steps

| Step | Action                                   | Output                |
| ---- | ---------------------------------------- | --------------------- |
| 5.1  | Analyze rate-limit patterns per provider | Rate limit report     |
| 5.2  | Test fallback chain switching            | Fallback test results |
| 5.3  | Recommend optimal provider order         | Config recommendation |
| 5.4  | Document cooldown periods per provider   | Cooldown reference    |

### Verification

- [ ] Provider failover works end-to-end
- [ ] Cooldown periods are empirically measured
- [ ] Fallback chain config is documented

---

## Phase 6: Script Creation & Automation (Recommended ☆)

**Profile:** `code-architect` | **Persona:** Developer

**Goal:** Create or update the `test_models.py` test harness to support all
6 providers with a unified CLI interface.

**Tools:** `terminal`, `execute_code`, `write_file`

**Skills:** `user-communication-preferences`

**Script target:** `~/AppData/Local/hermes/scripts/test_models.py`

**Inputs:** Provider discovery methods from Phase 1

**Outputs:** Working multi-provider test harness

### Script Requirements

| Requirement            | Priority      | Description                                    |
| ---------------------- | ------------- | ---------------------------------------------- |
| `--list-providers`     | ✓ Needed      | List all configured providers with auth status |
| `--list-free`          | ✓ Needed      | List free models from all providers            |
| `--all-free`           | ✓ Needed      | Benchmark all free models across all providers |
| `--provider NAME`      | ✓ Needed      | Test specific provider only                    |
| `--model MODEL`        | ☆ Recommended | Test specific model only                       |
| `--output FORMAT`      | ◇ Optional    | Output format (table/json/markdown)            |
| Multi-provider support | ✓ Needed      | Handle all 6 auth methods                      |
| Rate-limit handling    | ✓ Needed      | Retry, backoff, and error logging              |

### Steps

| Step | Action                                                 | Output              |
| ---- | ------------------------------------------------------ | ------------------- |
| 6.1  | Read existing `test_models.py` if present              | Current script      |
| 6.2  | Design unified multi-provider interface                | Script spec         |
| 6.3  | Implement provider modules per auth type               | Provider modules    |
| 6.4  | Implement benchmark tasks (reasoning, tool, knowledge) | Benchmark engine    |
| 6.5  | Add CLI argument parsing                               | CLI interface       |
| 6.6  | Add rate-limit handling and retry logic                | Resilient execution |
| 6.7  | Test with `--list-free` and `--provider openrouter`    | Verified script     |

### Verification

- [ ] Script runs without errors
- [ ] All 6 providers discoverable via `--list-providers`
- [ ] Free models listed for at least authenticated providers
- [ ] Benchmark runs produce markdown output
- [ ] Rate-limit errors are caught and logged, not fatal

---

## Actions Summary

| #   | Action                                          | Phase | Tier        |
| --- | ----------------------------------------------- | ----- | ----------- |
| 1   | Inventory all providers via `hermes auth list`  | 0     | Needed      |
| 2   | Discover model catalogs per provider            | 1     | Needed      |
| 3   | Extract free models across all providers        | 2     | Needed      |
| 4   | Create multi-provider test harness script       | 6     | Recommended |
| 5   | Benchmark each free model on 3 standard tasks   | 3     | Recommended |
| 6   | Compile cross-provider comparison report        | 4     | Recommended |
| 7   | Analyze rate limits and optimize fallback chain | 5     | Optional    |

## Related Prompts

| Prompt                                       | Relation                                               |
| -------------------------------------------- | ------------------------------------------------------ |
| `audit-skills-judge-fix.prompt.md`           | Same skill family (using-superpowers, plans-and-specs) |
| `sync-hermes-copilot-codex.prompt.md`        | Provider sync workflow                                 |
| `agents-system-prompt-context-fix.prompt.md` | Hermes context debugging                               |

## Verification Checklist (Final)

- [ ] **Phase 0:** All 6 providers captured from `hermes auth list`
- [ ] **Phase 1:** Model catalogs queried per provider
- [ ] **Phase 2:** Free models extracted and tabulated
- [ ] **Phase 3:** Benchmark run on all accessible free models
- [ ] **Phase 4:** Cross-provider comparison report generated
- [ ] **Phase 5:** Fallback chain documented (Optional)
- [ ] **Phase 6:** Test harness script supports all 6 providers
- [ ] Rate limits and errors documented per provider
- [ ] Recommendations included for best provider per task type
