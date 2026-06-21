#!/usr/bin/env python3
"""
test_models.py — Multi-provider model benchmark harness.

Usage:
  python test_models.py --list-free       # List all free models
  python test_models.py --benchmark       # Benchmark all free models
  python test_models.py --model MODEL     # Benchmark a specific model
  python test_models.py --provider ORG    # Benchmark all models from an org
"""

import json, os, sys, time, urllib.request, urllib.error

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmark_results")

# ── Tasks ────────────────────────────────────────────────────────────

TASKS = {
    "reasoning": {
        "messages": [
            {"role": "user", "content": "Calculate 30 / 6 = ? Then, if you start with $10 and spend $4, how much do you have left? Answer with just the two numbers separated by a comma."}
        ],
        "expect": lambda r: "5" in r and "6" in r
    },
    "tool_calling": {
        "messages": [
            {"role": "user", "content": "Explain in one sentence how an LLM agent calls a tool like a calculator or file reader."}
        ],
        "expect": lambda r: len(r) > 20
    },
    "knowledge": {
        "messages": [
            {"role": "user", "content": "What is the Hermes Agent built-in learning loop and how do you trigger an auto-generated skill? Answer in 2-3 sentences."}
        ],
        "expect": lambda r: "learning" in r.lower() or "skill" in r.lower() or "loop" in r.lower()
    }
}

# ── Helpers ──────────────────────────────────────────────────────────

def get_free_models():
    """Fetch all free models from OpenRouter API."""
    req = urllib.request.Request("https://openrouter.ai/api/v1/models")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    models = data.get("data", [])
    return [m for m in models if m.get("pricing") and any(v == "0" for k,v in m["pricing"].items())]

def test_model(model_id, task_name, task):
    """Run a single task on a model via OpenRouter API."""
    if not OPENROUTER_API_KEY:
        return {"status": "SKIP", "error": "No OPENROUTER_API_KEY"}

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://hermes-agent.local",
    }

    payload = {
        "model": model_id,
        "messages": task["messages"],
        "max_tokens": 150,
        "temperature": 0.1,
    }

    for attempt in range(2):
        try:
            req = urllib.request.Request(
                OPENROUTER_URL,
                data=json.dumps(payload).encode(),
                headers=headers
            )
            start = time.time()
            with urllib.request.urlopen(req, timeout=60) as r:
                resp = json.loads(r.read())
            elapsed = time.time() - start

            content = resp["choices"][0]["message"]["content"].strip()
            passed = task["expect"](content.lower())

            return {
                "status": "PASS" if passed else "FAIL",
                "response": content[:120],
                "latency": round(elapsed, 2),
                "error": None
            }
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 429:
                # Rate limited — wait and retry once
                time.sleep(5)
                continue
            return {"status": "ERROR", "error": f"HTTP {e.code}: {body[:100]}", "latency": None}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)[:100], "latency": None}

    return {"status": "RATE_LIMITED", "error": "429 after retry", "latency": None}

def print_table(results):
    """Print benchmark results as markdown table."""
    header = "| Model | Task 1 (Reason) | Task 2 (Tool) | Task 3 (Knowledge) | Errors | Latency |"
    sep = "|-------|--------|--------|--------|--------|---------|"
    print(header)
    print(sep)
    for model_id, tasks in sorted(results.items()):
        short = model_id.split("/")[-1][:30] if "/" in model_id else model_id[:30]
        t1 = tasks.get("reasoning", {}).get("status", "—")
        t2 = tasks.get("tool_calling", {}).get("status", "—")
        t3 = tasks.get("knowledge", {}).get("status", "—")
        errors = ", ".join(
            t.get("error", "") for t in tasks.values() if t.get("error")
        ) or "None"
        latencies = [t.get("latency", 0) for t in tasks.values() if t.get("latency")]
        avg_lat = f"{sum(latencies)/len(latencies):.1f}s" if latencies else "—"

        t1_sym = "✅ PASS" if t1 == "PASS" else ("❌ FAIL" if t1 == "FAIL" else ("⏭ SKIP" if t1 == "SKIP" else f"⚠️ {t1}"))
        t2_sym = "✅ PASS" if t2 == "PASS" else ("❌ FAIL" if t2 == "FAIL" else ("⏭ SKIP" if t2 == "SKIP" else f"⚠️ {t2}"))
        t3_sym = "✅ PASS" if t3 == "PASS" else ("❌ FAIL" if t3 == "FAIL" else ("⏭ SKIP" if t3 == "SKIP" else f"⚠️ {t3}"))

        print(f"| {short:30s} | {t1_sym} | {t2_sym} | {t3_sym} | {errors[:30]:30s} | {avg_lat:7s} |")

# ── Main ─────────────────────────────────────────────────────────────

def main():
    if not OPENROUTER_API_KEY:
        print("⚠️  No OPENROUTER_API_KEY set. Set it or use the Hermes provider chain.")
        print("    export OPENROUTER_API_KEY=sk-or-v1-...")
        sys.exit(1)

    print("🔍 Fetching free models from OpenRouter...")
    free_models = get_free_models()
    print(f"✅ Found {len(free_models)} free models\n")

    if "--list-free" in sys.argv:
        print(f"| {'Model':55s} | {'Context':10s} | {'Vendor':20s} |")
        print(f"| {'-'*55} | {'-'*10} | {'-'*20} |")
        for m in sorted(free_models, key=lambda x: x["id"]):
            cid = m["id"]
            ctx = m.get("context_length", "?")
            vendor = cid.split("/")[0] if "/" in cid else "?"
            print(f"| {cid:55s} | {str(ctx):10s} | {vendor:20s} |")
        return

    if "--benchmark" in sys.argv or len(sys.argv) == 1:
        # Filter by provider if --provider specified
        models_to_test = free_models
        for i, arg in enumerate(sys.argv):
            if arg == "--provider" and i+1 < len(sys.argv):
                models_to_test = [m for m in free_models if m["id"].startswith(sys.argv[i+1])]
                print(f"🎯 Filtered to provider: {sys.argv[i+1]} ({len(models_to_test)} models)")
            if arg == "--model" and i+1 < len(sys.argv):
                models_to_test = [m for m in free_models if sys.argv[i+1] in m["id"]]
                print(f"🎯 Specific model: {sys.argv[i+1]} ({len(models_to_test)} models)")

        results = {}
        total = len(models_to_test)
        print(f"\n🧪 Benchmarking {total} models × {len(TASKS)} tasks = {total * len(TASKS)} API calls\n")

        for idx, model in enumerate(models_to_test, 1):
            mid = model["id"]
            print(f"  [{idx}/{total}] {mid}...", end=" ", flush=True)
            results[mid] = {}
            for task_name, task in TASKS.items():
                result = test_model(mid, task_name, task)
                results[mid][task_name] = result
                sym = "✅" if result["status"] == "PASS" else ("❌" if result["status"] == "FAIL" else "⏭")
                lat = f"({result.get('latency','?')}s)" if result.get("latency") else ""
                err = f" [{result.get('error','')}]" if result.get("error") else ""
                print(f"{sym} {task_name}{lat}{err}", end=" ", flush=True)
            print()

        print("\n\n## Benchmark Results\n")
        print_table(results)

        # Summary
        total_tests = total * len(TASKS)
        passed = sum(1 for t in results.values() for tr in t.values() if tr["status"] == "PASS")
        failed = sum(1 for t in results.values() for tr in t.values() if tr["status"] == "FAIL")
        errors = sum(1 for t in results.values() for tr in t.values() if tr["status"] in ("ERROR", "RATE_LIMITED"))
        skipped = sum(1 for t in results.values() for tr in t.values() if tr["status"] == "SKIP")

        print(f"\n### Summary")
        print(f"- **Total tests:** {total_tests}")
        print(f"- **Passed:** {passed}")
        print(f"- **Failed:** {failed}")
        print(f"- **Errors:** {errors}")
        print(f"- **Skipped:** {skipped}")

if __name__ == "__main__":
    main()
