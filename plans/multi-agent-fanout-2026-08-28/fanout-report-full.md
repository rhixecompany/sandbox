# Fanout Report — 2026-08-28T18:12:17

**Prompt:** `Reply with the word OK.`

**Total:** 11 cells | fail=7 | auth_failed=3 | ok=1

| # | Provider | Model | Agent | Status | Latency | Output tokens |
|---|----------|-------|-------|--------|---------|---------------|
| 1 | `copilot` | `gpt-4o` | `copilot-cli` | fail | 27955ms | - |
| 2 | `deepseek` | `deepseek-chat` | `openai-compat` | fail | 936ms | - |
| 3 | `gemini` | `gemini-2.0-flash` | `openai-compat` | fail | 409ms | - |
| 4 | `huggingface` | `meta-llama/Meta-Llama-3-8B-Instruct` | `openai-compat` | fail | 4546ms | - |
| 5 | `nous` | `solar-pro4` | `openai-compat` | auth_failed | 0ms | - |
| 6 | `ollama-cloud` | `llama3.3` | `openai-compat` | fail | 983ms | - |
| 7 | `openai-codex` | `gpt-4o` | `codex-cli` | fail | 26941ms | - |
| 8 | `opencode-zen` | `big-pickle` | `openai-compat` | auth_failed | 644ms | - |
| 9 | `openrouter` | `openrouter/auto` | `openai-compat (matches in-tree openrouter-client-py protocol)` | ok | 3347ms | 29 |
| 10 | `xai` | `grok-2` | `openai-compat` | fail | 675ms | - |
| 11 | `xai-oauth` | `grok-2` | `openai-compat` | auth_failed | 0ms | - |
