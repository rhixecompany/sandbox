# Provider & Model Benchmark Report

> Generated: 2026-06-28 | Full re-execution of Phase 4

---

## Provider Inventory

| Provider | Credentials | Status |
|----------|------------|--------|
| copilot | 2 (gh auth token, GITHUB_TOKEN) | ⚠️ Rate-limited (429) |
| huggingface | 1 (HF_TOKEN) | ✅ Ready |
| nous | 1 (device_code OAuth) | ⚠️ Exhausted |
| ollama-cloud | 1 (OLLAMA_API_KEY) | ✅ Ready |
| openai-api | 2 (manual + env) | ✅ Ready |
| openrouter | 1 (OPENROUTER_API_KEY) | ⚠️ Rate-limited (429, ~1h left) |
| xai-oauth | 1 (loopback_pkce) | ✅ Ready |

## Model Catalogs

| Source | Models | Free Models |
|--------|--------|-------------|
| OpenRouter | 339 | 26 (including qwen3-coder, llama-3.3-70b, gemma-4-31b) |
| Opencode Zen | 49 | 6 (including deepseek-v4-flash-free, qwen3.6-plus-free) |
| NVIDIA NIM | 121 | 0 |

**Total accessible models:** 509 | **Free models:** 32

## Active Provider Chain

| Priority | Provider | Model | Context | Status |
|----------|----------|-------|---------|--------|
| 1 | opencode-zen | deepseek-v4-flash-free | — | ✅ Active (this session) |
| 2 | nous | stepfun/step-3.7-flash:free | — | ⚠️ Exhausted |
| 3 | openrouter | qwen/qwen3-coder:free | — | ⚠️ Rate-limited |
| 4 | openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | — | ⚠️ Rate-limited |

## Benchmark Results

### Code Generation Task
Both primary models successfully produced tested, production-quality code:

| Model | File Created | Functions | Tests | Quality |
|-------|-------------|-----------|-------|---------|
| deepseek-v4-flash-free | `lcs.py` (workspace) | 3 (lcs_length, lcs, lcs_all) | ✅ All passed + mypy | Generic Sequence[T], type-var generic |
| qwen/qwen3-coder:free | `lcs.py` (scripts/) | 2 (longest_common_subsequence, lcs_length) | ✅ Self-corrected test bug | Str-only, O(n) space opt |

### Summary
- **deepseek-v4-flash-free** → Production capability: wrote 97-line module, auto-tested, auto-type-checked. Writes to workspace root.
- **qwen/qwen3-coder:free** → Production capability: wrote 45-line module, found and fixed own test logic error. Writes to scripts dir.
- Both models demonstrate full autonomous coding (write → test → verify loop).

## Recommendations

1. **Primary:** Keep deepseek-v4-flash-free on opencode-zen — best feature set (generic types, mypy, comprehensive tests)
2. **Fallback:** qwen/qwen3-coder:free on openrouter — good alternative, self-debugging capability
3. **Free models to explore:** llama-3.3-70b-instruct:free (OpenRouter), gemma-4-31b-it:free (OpenRouter)
4. **Fix:** Nous provider auth exhausted — re-authenticate via `hermes auth login nous`
5. **Fix:** OpenRouter rate-limit auto-resets (~1h remaining as of benchmark)
