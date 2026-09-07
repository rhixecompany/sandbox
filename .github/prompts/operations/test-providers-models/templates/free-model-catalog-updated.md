# Free-model catalog — rebuilt 2026-09-07

> Source: live `hermes config show`, `hermes auth list`, web-extracted docs (`openrouter-docs.md`, `opencode-zen-docs.md`), `hermes insights`, `test-providers-models-free-suffix-catalog.md`.
> Filter: `':free' in model id` OR `pricing.prompt == 0 && pricing.completion == 0` (confirmed per provider docs).
> Probe eligibility: only providers with at least one working key (`valid` / manual working) are probed. Rate-limited (`429`) or `auth-failed (401)` providers are excluded from Phase 3 live probes but still cataloged.

## Auth state (from `hermes auth list` 2026-09-07)

|| Provider | Working keys | Status (live) | Rate/auth notes | Probe? |
|---|---|---|---|---|---|
| `opencode-zen` | `OPENCODE_ZEN_API_KEY` env; `api-key-3` manual (potential); others 401 | mixed: 1 valid, 3 auth-failed 401 | Auth-failed on 3 manual keys; docs endpoint `https://opencode.ai/zen/v1` | Partial (env key) |
| `openrouter` | `OPENROUTER_API_KEY` env (rate-limited 429 57m 53s); `api-key-2` manual (rate-limited 429 4h 5m) | rate-limited | `https://openrouter.ai/docs/api_reference/authentication` | Skip (429) |
| `deepseek` | `DEEPSEEK_API_KEY` env (valid) | valid (but docs say excluded / wrapped via opencode-zen) | No native `:free` model; wrapped through zen | Excluded (no `:free`) |
| `gemini` | `GOOGLE_API_KEY` env (valid) | valid | No `:free` model in auth inventory | Catalog only (no `:free` model IDs) |
| `minimax` | `MINIMAX_API_KEY` env (valid, exhausted 402) | valid but exhausted | `sk-a...10jQ` | Partial (working key but exhausted) |
| `minimax-oauth` | `oauth` | oauth | logged in, access exp 2027-08-31 | Yes (oauth flow) |
| `nous` | `device_code` | oauth | device_code, portal logged in | Yes (device code flow) |
| `ollama-cloud` | `OLLAMA_API_KEY` | valid | `https://opencode.ai/zen/v1` | Yes |
| `openai-api` | 5 credentials, all exhausted (402) | all exhausted | No working keys | No |
| `openai-codex` | 3 credentials, rate-limited 429 (27d 2h left) | rate-limited | device_code oauth | Skip (429) |
| `xai` | `api-key-1` auth failed (403); `XAI_API_KEY` env | auth-failed 403 | Re-auth required | No |
| `xai-oauth` | `xai-oauth-oauth-1` | oauth | device_code | Yes (oauth flow) |
| `copilot` | 3 credentials | n/a | Not working | No |

## Free-model catalog entries (provider : free models with docs)

### opencode-zen free models (1 valid key via env)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `opencode-zen/deepseek-v4-flash-free` | 128K | ✓ | 4K | https://opencode.ai/docs/zen/ | Working (env key) |
| `opencode-zen/nemotron-3-ultra-free` | 1M | ✓ | — | https://opencode.ai/docs/zen/ | Working (env key) |
| `opencode-zen/nemotron-3.5-lightning-free` | 262K | — | — | https://opencode.ai/docs/zen/ | Working (env key) |
| `opencode-zen/big-pickle` | — | — | — | https://opencode.ai/docs/zen/ | Free (limited) |
| `opencode-zen/mimo-v2-pro-free` | — | — | — | https://opencode.ai/docs/zen/ | Free (limited) |
| `opencode-zen/minimax-m2.5-free` | 205K | — | — | https://opencode.ai/docs/zen/ | Free (limited) |
| `opencode-zen/minimax-m3` | 512K | — | — | https://opencode.ai/docs/zen/ | Paid ($0.30/$1) |
| `opencode-zen/nemotron-3-ultra-550b-a55b:free` | 1M | ✓ | — | https://opencode.ai/docs/zen/ | Via openrouter |

### openrouter :free models (rate-limited, catalog only)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | ✓ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/nvidia/nemotron-3-super-120b-a12b:free` | 1M | ✓ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 256K | ✓ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/google/gemma-4-31b-it:free` | 262K | ✗ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/google/gemma-4-26b-a4b-it:free` | 262K | ✗ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/openai/gpt-oss-20b:free` | 131K | ✗ | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/meta-llama/llama-4-maverick:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/meta-llama/llama-4-scout:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/moonshotai/kimi-vl-a3b-thinking:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/mistralai/mistral-small-3.1-24b-instruct:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/qwen/qwen2.5-vl-3b-instruct:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/deepseek/deepseek-v3-base:free` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/optimus-alpha` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |
| `openrouter/quasar-alpha` | — | — | — | https://openrouter.ai/docs/api_reference/authentication | Cataloged (429 skip) |

### gemini free-capable models (valid key, no :free suffix but API tier)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `gemini/gemini-2.5-flash` | 1M | ✓ | 4K | https://ai.google.dev/api/tuner/gemini | Working (GOOGLE_API_KEY) |
| `gemini/gemini-2.5-pro` | 1M | ✓ | 4K | https://ai.google.dev/api/tuner/gemini | Free tier eligible |
| `gemini/gemini-1.5-flash` | 1M | ✓ | 4K | https://ai.google.dev/api/tuner/gemini | Free tier eligible (1500 req/day) |

### minimax free models (configured, working)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `minimax/minimax-m3:free` | 1M | — | — | https://docs.minimax.ai | Working (configured) |
| `minimax/minimax-m2.5:free` | 205K | — | — | https://docs.minimax.ai | Free tier |
| `minimax/minimax-m2.7:free` | 205K | — | — | https://docs.minimax.ai | Free tier |

### nous free models (device code flow)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `nous/nemotron-3-ultra-free` | 1M | ✓ | — | https://portal.nousresearch.com | Via device code |

### ollama-cloud free models
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `ollama-cloud/nemotron-3-ultra` | 1M | ✓ | — | https://opencode.ai/zen/v1 | Working |

### xai-oauth free models (oauth flow)
| Model ID | Context | Reasoning | Max Output | Docs URL | Status |
|---|---|---|---|---|---|
| `xai-oauth/<model>:free` | — | — | — | xAI docs | OAuth flow pending |

## Working free model baseline (probed 2026-08-07, for cross-check)

| Provider | Model | Context | Reasoning | Working |
|---|---|---|---|---|
| `opencode-zen` | `deepseek-v4-flash-free` | 128K | ✓ | ✓ WORKING |
| `opencode-zen` | `nemotron-3-ultra-free` | 1M | ✓ | ✓ WORKING |
| `openrouter` | `nvidia/nemotron-3-ultra-550b-a55b:free` | 1M | ✓ | ✓ WORKING |
| `openrouter` | `nvidia/nemotron-3-super-120b-a12b:free` | 1M | ✓ | ✓ WORKING |
| `openrouter` | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 256K | ✓ | ✓ WORKING |
| `gemini` | `gemini-2.5-flash` | 1M | ✓ | ✓ WORKING |
| `ollama-cloud` | `nemotron-3-ultra` | 1M | ✓ | ✓ WORKING |

**Note:** No working free model in the verified set has vision. The rule therefore degrades to reasoning → context for the current free-tier landscape.