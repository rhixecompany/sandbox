# Phase 3: Provider-by-Provider Benchmarking (Recommended ☆)

> Extracted from `test-providers-models.prompt.md` for DRY templating.

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
