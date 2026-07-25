# Benchmark Harness Fix & Live-Run Recipe

> Lessons from the 2026-07-10 live re-run of `test-providers-models`.

## 1. The resume bug (fixed 2026-07-10)

Symptom: re-running `benchmark_providers.py` duplicated work AND merged stale rows from
an existing `benchmark_results.json` into the new run, corrupting the Phase 4 report.

Root cause: `benchmark_model()` never received the `completed` set, so the per-task
skip-check (which lived in `main()`) was dead code.

### Fix

```python
# BEFORE (broken — ignore completed, re-run all 3 tasks)
def benchmark_model(provider: str, model: str) -> list[BenchmarkResult]:
    results = []
    for task_name, prompt in BENCHMARK_TASKS.items():
        results.append(run_one(...))
    return results

# AFTER (skip already-completed tuples)
def benchmark_model(provider: str, model: str, completed: set) -> list[BenchmarkResult]:
    results = []
    for task_name, prompt in BENCHMARK_TASKS.items():
        key = (provider, model, task_name)
        if key in completed:
            print(f"  Skipping {task_name} (already done)")
            continue
        results.append(run_one(...))
    return results
```

```python
# main(): pass completed in, then extend it
for provider, model in ACCESSIBLE_MODELS:
    model_results = benchmark_model(provider, model, completed)
    all_results.extend(model_results)
    save_results(all_results)
    completed.update((r.provider, r.model, r.task) for r in model_results)
    time.sleep(5)
```

### Mandatory before any re-run

```bash
# clear stale data so resume can't merge old rows
rm -f ~/AppData/Local/hermes/scripts/benchmark_results.json
# OR write to a datestamped path (preferred):
OUTPUT_FILE = Path.home() / "AppData" / "Local" / "hermes" / "scripts" / "benchmark_results_2026-07-10.json"
```

## 2. Live-run invocation pattern (verified working)

```bash
# smoke test a single call first (confirms the harness path + measures latency)
time hermes chat -q "What is the capital of Kazakhstan? One word answer." \
  --provider nous --model stepfun/step-3.7-flash:free

# full harness (background — ~12-15 min for 5 models x 3 tasks)
cd ~/AppData/Local/hermes/scripts
python benchmark_providers.py 2>&1 | tee benchmark_run_$(date +%F).log
```

- `hermes chat` runs in the FOREGROUND of a subprocess; long runs go in
  `terminal(background=True, notify_on_complete=True)`.
- The `wait` action on a background process clamps at ~60s — POLL in ~50s increments
  rather than blocking; read the log tail to see per-task OK/FAIL lines.

## 3. Live ACCESSIBLE_MODELS set (2026-07-10)

```python
ACCESSIBLE_MODELS = [
    ("nous", "stepfun/step-3.7-flash:free"),
    ("openrouter", "tencent/hy3:free"),
    ("huggingface", "auto"),
    ("ollama-cloud", "auto"),
    ("xai-oauth", "auto"),
]
# rate-limited / no-free-tier at run time:
#   gemini (429), copilot (429), openai-codex (29d cooldown), openai-api (paid only)
```

Re-derive this from `hermes auth list` every run — do NOT copy the list above as gospel.
