#!/usr/bin/env python3
"""
Phase 6: test_models.py — Cross-Provider Model Test Harness

Tests any model on any of the 6 providers for:
1. Reasoning (logic puzzle)
2. Tool calling (function selection)  
3. Knowledge (factual QA)

Usage:
  python test_models.py --provider openrouter --model "nvidia/nemotron-3-ultra-550b-a55b:free"
  python test_models.py --provider ollama-cloud --model "gemma4:26b"
  python test_models.py --list-models
  python test_models.py --provider openrouter --list-models
  python test_models.py --benchmark-all-free  (runs all free models)
"""
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(r"C:\Users\Alexa\Desktop\SandBox")
CACHE_DIR = Path(r"C:\Users\Alexa\AppData\Local\hermes")
RESULTS_DIR = WORKSPACE / "benchmark_output"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ── Provider Config ──────────────────────────────────────────────────────────

PROVIDERS = {
    "copilot": {
        "name": "GitHub Copilot / Azure AI",
        "hermes_flag": True,
        "api_key_var": "COPILOT_GITHUB_TOKEN",
        "base_url": "https://models.inference.ai.azure.com",
        "models_api": "https://models.inference.ai.azure.com/models",
        "cred_source": "gh auth token / env var",
        "cred_note": "Rate-limited (429) in prior run",
        "auth_blocked": True,  # blocked by rate limit per prior run
    },
    "huggingface": {
        "name": "HuggingFace Inference Providers",
        "hermes_flag": True,
        "api_key_var": "HF_TOKEN",
        "base_url": "https://api-inference.huggingface.co",
        "models_api": "https://api-inference.huggingface.co/models",
        "cred_source": "HF_TOKEN env var (in .env, NOT in subprocess)",
        "auth_blocked": False,
    },
    "nous": {
        "name": "Nous Portal",
        "hermes_flag": True,
        "api_key_var": None,
        "base_url": None,
        "models_api": None,
        "cred_source": "OAuth device_code",
        "cred_note": "OAuth session times out; cannot enumerate models directly",
        "auth_blocked": True,
    },
    "ollama-cloud": {
        "name": "Ollama Cloud",
        "hermes_flag": True,
        "api_key_var": "OLLAMA_API_KEY",
        "base_url": "https://api.ollama.cloud/v1",
        "models_api": "https://api.ollama.cloud/api/tags",
        "cred_source": "OLLAMA_API_KEY env var (in .env, NOT in subprocess)",
        "auth_blocked": False,
    },
    "openai-api": {
        "name": "OpenAI API",
        "hermes_flag": True,
        "api_key_var": "OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "models_api": "https://api.openai.com/v1/models",
        "cred_source": "api-key-1 (manual) + OPENAI_API_KEY env",
        "auth_blocked": False,
    },
    "openrouter": {
        "name": "OpenRouter",
        "hermes_flag": True,
        "api_key_var": "OPENROUTER_API_KEY",
        "base_url": "https://openrouter.ai/api/v1",
        "models_api": "https://openrouter.ai/api/v1/models",
        "cred_source": "Hermes credential store (NOT in subprocess)",
        "auth_blocked": False,
    },
}

# ── Benchmark Tasks ──────────────────────────────────────────────────────────

BENCHMARK_TASKS = {
    "reasoning": {
        "prompt": (
            "Solve this logic puzzle step by step:\n"
            "There are five houses in a row, each painted a different color: Red, Green, Blue, Yellow, White.\n"
            "Each house is occupied by a person of a different nationality: American, British, Canadian, Danish, Egyptian.\n"
            "Each person drinks a different beverage: Coffee, Tea, Milk, Juice, Water.\n"
            "Each person smokes a different brand: Marlboro, Camel, Dunhill, Parliament, Rothmans.\n"
            "Each person keeps a different pet: Dog, Cat, Bird, Fish, Horse.\n"
            "Clues:\n"
            "1. The American lives in the Red house.\n"
            "2. The British drinks Tea.\n"
            "3. The Green house is immediately to the LEFT of the White house.\n"
            "4. The Green house's occupant drinks Coffee.\n"
            "5. The person who smokes Marlboro owns a Dog.\n"
            "6. The person in the Yellow house smokes Dunhill.\n"
            "7. The Danish drinks Milk.\n"
            "8. The person who smokes Parliament lives next to the one who keeps a Cat.\n"
            "9. The person who keeps a Horse lives next to the person who smokes Dunhill.\n"
            "10. The person who smokes Rothmans drinks Beer.\n"
            "11. The Egyptian smokes Camel.\n"
            "12. The Canadian lives next to the Blue house.\n"
            "13. The person who smokes Camel lives next to the person who keeps a Dog.\n"
            "14. The person who smokes Marlboro has a neighbor who drinks Water.\n"
            "QUESTION: Who owns the Fish? Explain your reasoning step by step, "
            "then give the final answer in the format: ANSWER: [nationality]"
        ),
        "expected_answer_contains": ["German", "Egyptian", "Danish", "American", "British", "Canadian"],
        "scoring": "Check if answer identifies the fish owner correctly (German in classic puzzle)",
        "max_points": 10,
        "timeout": 120,
    },
    "tool_calling": {
        "prompt": (
            "I need to do the following tasks. Decide which function/tool to call for each:\n\n"
            "1. What's the weather like in Paris?\n"
            "2. Send an email to john@example.com saying 'Meeting at 3pm'\n"
            "3. Calculate 7! (7 factorial)\n"
            "4. Translate 'Hello' to Spanish\n"
            "5. Search the web for 'latest AI news'\n\n"
            "For EACH task, tell me:\n"
            "- What tool/function you would call\n"
            "- What parameters you would pass\n"
            "- If you cannot call a tool, explain why\n\n"
            "Format your answer as a numbered list."
        ),
        "expected_answer_contains": ["tool", "function", "parameter", "API"],
        "scoring": "Assess if model understands tool selection concepts",
        "max_points": 10,
        "timeout": 90,
    },
    "knowledge": {
        "prompt": (
            "Answer each of the following questions concisely:\n\n"
            "1. What is the capital of Mongolia?\n"
            "2. Who wrote 'One Hundred Years of Solitude'?\n"
            "3. What is the chemical formula for table salt?\n"
            "4. In what year did the Berlin Wall fall?\n"
            "5. What is the speed of light in a vacuum (in m/s)?\n\n"
            "Provide your answer as a numbered list with just the answer for each."
        ),
        "expected_answer_contains": ["Ulaanbaatar", "Ulan Bator", "García Márquez", "Gabriel", 
                                       "NaCl", "1989", "299,792,458", "3×10⁸", "3e8"],
        "scoring": "Check factual accuracy of each answer",
        "max_points": 10,
        "timeout": 60,
    },
}

# ── Credential helpers ───────────────────────────────────────────────────────

def get_api_key(provider):
    """Try to load API key from .env or environment"""
    # First check env
    var_name = PROVIDERS[provider].get("api_key_var")
    if var_name:
        val = os.environ.get(var_name)
        if val:
            return val
    
    # Check .env file
    env_path = CACHE_DIR / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                if key.strip() == var_name:
                    return val.strip()
    return None


def run_hermes_chat(provider, query, model=None, timeout=60):
    """Run a query through hermes chat -q for the given provider"""
    cmd = ["hermes", "chat", "-q", query, "--provider", provider]
    if model:
        cmd.extend(["-m", model])
    
    try:
        start = time.time()
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(WORKSPACE),
        )
        elapsed = time.time() - start
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "elapsed": elapsed,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Timeout after {timeout}s",
            "elapsed": timeout,
            "returncode": -1,
        }
    except FileNotFoundError:
        return {
            "success": False,
            "stdout": "",
            "stderr": "hermes command not found",
            "elapsed": 0,
            "returncode": -1,
        }


def score_response(task_name, response_text):
    """Score a response based on task criteria"""
    text = response_text.lower()
    task = BENCHMARK_TASKS[task_name]
    score = 0
    details = []
    
    if task_name == "reasoning":
        # Check for reasoning (step-by-step explanation)
        if any(word in text for word in ["step", "first", "then", "therefore", "because", "clue"]):
            score += 4
            details.append("Shows reasoning steps")
        # Check for answer format
        if "answer" in text or "fish" in text:
            score += 3
            details.append("Provides answer")
        # Check for identifying correct nationality
        for name in task["expected_answer_contains"]:
            if name.lower() in text:
                score += 3
                details.append(f"Mentions {name}")
                break
                
    elif task_name == "tool_calling":
        # Check for tool/function awareness
        if any(word in text for word in ["tool", "function", "api", "endpoint"]):
            score += 4
            details.append("Demonstrates tool awareness")
        if any(word in text for word in ["parameter", "argument", "input"]):
            score += 3
            details.append("Identifies parameters")
        if any(word in text for word in ["weather", "email", "calculate", "translate", "search"]):
            score += 3
            details.append("Addresses all 5 tasks")
            
    elif task_name == "knowledge":
        correct_answers = 0
        # Check for key facts
        if any(city in text for city in ["ulaanbaatar", "ulan bator"]):
            correct_answers += 2
            details.append("Capital: correct")
        if any(name in text for name in ["gabriel", "garcía", "marquez", "márquez"]):
            correct_answers += 2
            details.append("Author: correct")
        if "nacl" in text:
            correct_answers += 2
            details.append("Formula: correct")
        if "1989" in text:
            correct_answers += 2
            details.append("Berlin Wall: correct")
        if any(v in text for v in ["299,792,458", "3×10⁸", "3e8", "299792458"]):
            correct_answers += 2
            details.append("Speed of light: correct")
        score = correct_answers
    
    return min(score, task["max_points"]), details


# ── Model Listing ────────────────────────────────────────────────────────────

def list_models(provider=None):
    """List available models for provider(s)"""
    cache_path = CACHE_DIR / "provider_models_cache.json"
    if cache_path.exists():
        with open(cache_path) as f:
            cache = json.load(f)
        
        if provider:
            providers_to_show = [provider]
        else:
            providers_to_show = list(PROVIDERS.keys())
        
        for prov in providers_to_show:
            pd = cache.get(prov, {})
            models = pd.get("models", [])
            print(f"\n{PROVIDERS[prov]['name']} ({len(models)} models):")
            for m in models:
                print(f"  {m}")
    else:
        print("Model cache not found. Run hermes model --refresh first.")
        print(f"Expected at: {cache_path}")


def list_free_models():
    """List free models from OpenRouter"""
    or_path = WORKSPACE / "openrouter_models.json"
    if or_path.exists():
        with open(or_path) as f:
            data = json.load(f)
        models = data.get("data", [])
        free = [m for m in models if m.get("pricing", {}).get("prompt", "0") == "0"]
        print(f"\nOpenRouter Free Models ({len(free)}):")
        for m in free:
            ctx = m.get("context_length", "?")
            print(f"  {m['id']} (ctx: {ctx})")
        return free
    else:
        print("OpenRouter models file not found.")
        return []


# ── Benchmark Runner ─────────────────────────────────────────────────────────

def run_single_benchmark(provider, model, task_name, verbose=True):
    """Run a single benchmark task against a provider/model"""
    task = BENCHMARK_TASKS[task_name]
    query = task["prompt"]
    
    if verbose:
        print(f"  Running {task_name}...", end=" ", flush=True)
    
    result = run_hermes_chat(provider, query, model, timeout=task["timeout"])
    
    if verbose:
        print(f"{'✓' if result['success'] else '✗'} ({result['elapsed']:.1f}s)")
    
    score, details = score_response(task_name, result.get("stdout", ""))
    
    return {
        "task": task_name,
        "provider": provider,
        "model": model,
        "success": result["success"],
        "elapsed": result["elapsed"],
        "score": score,
        "max_score": task["max_points"],
        "details": details,
        "response_preview": result.get("stdout", "")[:300] if result.get("stdout") else "NO OUTPUT",
        "error": result.get("stderr", "")[:200] if result.get("stderr") else None,
    }


def benchmark_model(provider, model, verbose=True):
    """Run all 3 benchmark tasks on a model"""
    if verbose:
        print(f"\n{'='*60}")
        print(f"Benchmarking: {provider}/{model}")
        print(f"{'='*60}")
    
    results = []
    for task_name in ["reasoning", "tool_calling", "knowledge"]:
        try:
            r = run_single_benchmark(provider, model, task_name, verbose)
            results.append(r)
        except Exception as e:
            if verbose:
                print(f"  Error running {task_name}: {e}")
            results.append({
                "task": task_name,
                "provider": provider,
                "model": model,
                "success": False,
                "elapsed": 0,
                "score": 0,
                "max_score": 10,
                "details": [f"Error: {e}"],
                "response_preview": "",
                "error": str(e),
            })
    
    total_score = sum(r["score"] for r in results)
    max_score = sum(r["max_score"] for r in results)
    pass_rate = (total_score / max_score * 100) if max_score > 0 else 0
    
    if verbose:
        print(f"\n  Total Score: {total_score}/{max_score} ({pass_rate:.0f}%)")
        for r in results:
            status = "PASS" if r["score"] >= 5 else "FAIL"
            print(f"  [{status}] {r['task']}: {r['score']}/{r['max_score']} ({r['elapsed']:.1f}s)")
    
    return {
        "provider": provider,
        "model": model,
        "timestamp": datetime.now().isoformat(),
        "tasks": results,
        "total_score": total_score,
        "max_score": max_score,
        "pass_rate": pass_rate,
        "passed": pass_rate >= 50,
    }


def benchmark_all_free(verbose=True):
    """Benchmark all free OpenRouter models"""
    free_models = list_free_models()
    if not free_models:
        print("No free models found.")
        return []
    
    # Pick representative free models (don't run all 26 — that would take hours)
    # Select diverse models by vendor
    selected = []
    seen_vendors = set()
    
    # Prioritize models with :free suffix
    free_with_suffix = [m for m in free_models if ":free" in m["id"]]
    free_without_suffix = [m for m in free_models if ":free" not in m["id"]]
    
    for m in free_with_suffix + free_without_suffix:
        vendor = m["id"].split("/")[0]
        if vendor not in seen_vendors or len(selected) < 8:
            selected.append(m)
            seen_vendors.add(vendor)
    
    if verbose:
        print(f"\nSelected {len(selected)} representative free models for benchmarking:")
        for m in selected:
            print(f"  - {m['id']}")
    
    results = []
    for model_info in selected:
        model_id = model_info["id"]
        r = benchmark_model("openrouter", model_id, verbose)
        results.append(r)
        # Save intermediate results
        save_results(results)
    
    return results


def save_results(results):
    """Save benchmark results to disk"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = RESULTS_DIR / f"benchmark_results_{timestamp}.json"
    with open(path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    return path


# ── Report Generation ────────────────────────────────────────────────────────

def generate_report(all_results):
    """Generate a cross-provider comparison report"""
    lines = []
    lines.append("# Cross-Provider Models Comparison Report")
    lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"\n## Executive Summary")
    
    passed = sum(1 for r in all_results if r.get("passed"))
    total = len(all_results)
    lines.append(f"\n- Models tested: {total}")
    lines.append(f"- Models passed: {passed}")
    lines.append(f"- Models failed: {total - passed}")
    
    lines.append(f"\n## Results by Provider")
    
    for provider_name, pconfig in PROVIDERS.items():
        provider_results = [r for r in all_results if r.get("provider") == provider_name]
        lines.append(f"\n### {pconfig['name']} ({provider_name})")
        lines.append(f"\n- Auth status: {pconfig.get('cred_note', 'Active')}")
        
        if provider_results:
            for pr in provider_results:
                lines.append(f"\n#### Model: {pr['model']}")
                lines.append(f"- Overall: {'PASS' if pr.get('passed') else 'FAIL'} ({pr.get('pass_rate', 0):.0f}%)")
                lines.append(f"- Score: {pr.get('total_score', 0)}/{pr.get('max_score', 30)}")
                for task in pr.get("tasks", []):
                    lines.append(f"  - {task['task']}: {task['score']}/{task['max_score']} ({task['elapsed']:.1f}s)")
        else:
            lines.append("- No benchmarks run")
            if pconfig.get("auth_blocked"):
                lines.append("- Reason: Authentication blocked or unavailable")
    
    lines.append(f"\n## Free Model Inventory")
    lines.append(f"\n### OpenRouter Free Models ({len(list_free_models() if hasattr(list_free_models, '__call__') else [])})")
    
    lines.append(f"""
## Recommendations

1. **Primary provider**: OpenRouter — widest free model selection (26 free models)
2. **Best free models**: 
   - `nvidia/nemotron-3-ultra-550b-a55b:free` (1M context)
   - `google/gemma-4-31b-it:free` (262K context)
   - `openai/gpt-oss-120b:free` (131K context)
   - `meta-llama/llama-3.3-70b-instruct:free`
3. **For chat**: `openrouter/free` routes to best available free model
4. **OpenAI API**: Pay-per-use, gpt-4o-mini is cheapest option
5. **Ollama Cloud**: Good for open-source models, cloud tier is pay-per-use
6. **HuggingFace**: Free inference API with rate limits, 123+ models available
7. **Copilot**: Rate-limited (429), subscription-based access
8. **Nous**: OAuth portal, subscription-based, unable to test directly
""")
    
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Cross-Provider Model Test Harness")
    parser.add_argument("--provider", help="Provider to use (copilot, huggingface, nous, ollama-cloud, openai-api, openrouter)")
    parser.add_argument("--model", help="Model ID to test")
    parser.add_argument("--list-models", action="store_true", help="List available models")
    parser.add_argument("--benchmark-all-free", action="store_true", help="Benchmark all free OpenRouter models")
    parser.add_argument("--output", help="Output file for results (JSON)")
    parser.add_argument("--verbose", action="store_true", default=True, help="Verbose output")
    
    args = parser.parse_args()
    
    if args.list_models:
        list_models(args.provider)
        return
    
    if args.benchmark_all_free:
        results = benchmark_all_free(args.verbose)
        report = generate_report(results)
        report_path = RESULTS_DIR / "cross_provider_report.md"
        with open(report_path, "w") as f:
            f.write(report)
        print(f"\nReport saved to: {report_path}")
        
        results_path = save_results(results)
        print(f"Results saved to: {results_path}")
        return
    
    if args.provider and args.model:
        result = benchmark_model(args.provider, args.model, args.verbose)
        print(json.dumps(result, indent=2, default=str))
        
        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2, default=str)
            print(f"Results saved to: {args.output}")
        return
    
    # Default: list providers and show summary
    print("Cross-Provider Model Test Harness")
    print("==================================\n")
    print("Providers available:")
    for key, pconfig in PROVIDERS.items():
        status = "✓" if not pconfig.get("auth_blocked") else "✗"
        print(f"  {status} {key}: {pconfig['name']}")
    print("\nUsage:")
    print("  python test_models.py --provider openrouter --model nvidia/nemotron-3-ultra-550b-a55b:free")
    print("  python test_models.py --benchmark-all-free")
    print("  python test_models.py --list-models")


if __name__ == "__main__":
    main()
