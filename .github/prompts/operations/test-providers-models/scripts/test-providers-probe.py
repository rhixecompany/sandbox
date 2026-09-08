#!/usr/bin/env python3
"""
Test probe script for Hermes LLM providers and models.
Executes standardized test prompts and logs results.
"""

import json
import os
import subprocess
import time
from datetime import datetime

TEST_PROMPT = """You are an AI assistant testing your own capabilities. Please respond with a JSON object containing:
1. "provider": your provider name
2. "model": your model name
3. "context_window": your context window size in tokens
4. "max_output": your max output tokens
5. "capabilities": list of your capabilities (reasoning, tool_use, code, vision, etc.)
6. "reasoning": boolean - do you support extended reasoning?
7. "tool_use": boolean - do you support tool/function calling?

Keep the response concise and valid JSON only."""

MODELS = [
    {"provider": "openrouter", "model": "nvidia/nemotron-3-ultra-550b-a55b:free"},
    {"provider": "openrouter", "model": "meituan/longcat-2.0:free"},
    {"provider": "openrouter", "model": "google/gemini-2.5-flash:free"},
    {"provider": "openrouter", "model": "deepseek/deepseek-v4-flash:free"},
    {"provider": "openrouter", "model": "upstage/solar-pro4:free"},
    {"provider": "openrouter", "model": "minimax/mimo-v2.5-free"},
    {"provider": "openrouter", "model": "ling-3.0-flash-fin:free"},
    {"provider": "openrouter", "model": "inkling:free"},
    {"provider": "openrouter", "model": "nvidia/nemotron-3-nano-omni-30b-a3b"},
    {"provider": "openrouter", "model": "meta-llama/llama-4-maverick-17b-128e-instruct:free"},
]

def test_model(provider, model):
    """Test a single model via hermes chat"""
    start = time.time()
    try:
        result = subprocess.run(
            ["hermes", "chat", "--provider", provider, "--model", model,
             "-q", TEST_PROMPT, "--oneshot"],
            capture_output=True, text=True, timeout=120
        )
        elapsed = time.time() - start
        return {
            "provider": provider,
            "model": model,
            "status": "success" if result.returncode == 0 else "error",
            "stdout": result.stdout[:2000],
            "stderr": result.stderr[:1000],
            "returncode": result.returncode,
            "elapsed_seconds": round(elapsed, 2),
            "timestamp": datetime.now().isoformat()
        }
    except subprocess.TimeoutExpired:
        return {
            "provider": provider,
            "model": model,
            "status": "timeout",
            "elapsed_seconds": 120,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "provider": provider,
            "model": model,
            "status": "exception",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def main():
    results = []
    for m in MODELS:
        print(f"Testing {m['provider']}/{m['model']}...", flush=True)
        r = test_model(m["provider"], m["model"])
        results.append(r)
        print(f"  -> {r['status']} ({r.get('elapsed_seconds', '?')}s)", flush=True)
        time.sleep(2)  # Rate limit spacing

    out_path = os.path.join(os.path.dirname(__file__), "..", "test-providers-models-results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to {out_path}")

if __name__ == "__main__":
    main()
