# Phase 2: Free Model Extraction (Needed ✓)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

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
