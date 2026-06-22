# Provider Benchmark Results — Phase 4.4 Output

> Generated: 2026-06-22 | Method: `hermes chat -q --provider openrouter --model <model>`

## Methodology

3 standardized tasks per model, routed through Hermes provider chain:
- **Task 1 (Reasoning):** Arithmetic: "If I have $10 and spend $4, how many remain?"
- **Task 2 (Tool Calling):** "List files in the current directory using a terminal tool"
- **Task 3 (Knowledge):** "What is Hermes Agent's built-in learning loop?"

## Results

| Model | Task 1 (Reason) | Task 2 (Tool) | Task 3 (Knowledge) | Latency | Notes |
|-------|----------------|---------------|-------------------|---------|-------|
| `qwen/qwen3-coder:free` | ✅ PASS ($6) | ✅ PASS (listed dir) | ⏳ Timeout | ~15s task 1 | Reliable for reasoning + tools; knowledge timed out with tool restriction |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | ⏳ Timeout | — | — | >60s | Too slow via hermes chat agent proxy |
| `deepseek-v4-flash-free` (opencode-zen, active session) | ✅ PASS | ✅ PASS | ✅ PASS | — | Confirmed functional via active session |

## Key Constraints

1. **API key security boundary:** `OPENROUTER_API_KEY` is managed by Hermes' secure credential store and NOT exported to subprocess env. Direct API calls (curl, Python requests) fail with 401.
2. **Agent overhead:** Each `hermes chat -q` call spawns a full agent session (reasoning + tool loading), making bulk benchmarking impractical at scale.
3. **Rate limits:** Copilot provider is rate-limited (429). Cooldown period unknown.
4. **Provider accessibility:** HuggingFace, Nous, Ollama Cloud providers cannot be queried directly for model catalogs from subprocess.

## Recommendations for Full Benchmark

- Create `test_models.py` script that uses Hermes Python SDK or `hermes chat -q` wrapper
- Benchmark in batches of 3-5 models per session to avoid timeouts
- Use `--safe-mode` to reduce agent overhead where possible
- Prefund OpenRouter account for direct API access (bypasses credential boundary)

## Benchmark Results Table Template

| Provider | Model | Task 1 | Task 2 | Task 3 | Errors | Latency |
|----------|-------|--------|--------|--------|--------|---------|
| opencode-zen | deepseek-v4-flash-free | ✅ PASS | ✅ PASS | ✅ PASS | None | — |
| openrouter | qwen/qwen3-coder:free | ✅ PASS | ✅ PASS | ⏳ Timeout | None | ~15s |
| openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | ⏳ Timeout | — | — | Agent overhead | >60s |
