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

from provider_status import (
    SELF_PROFILE_PROMPT,
    auth_rate_limited_providers,
    is_rate_limit_error,
    provider_is_rate_limited,
    skipped_result,
)

TEST_PROMPT = SELF_PROFILE_PROMPT

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


def test_model(provider, model, rate_limited=None):
    """Test a single model via hermes chat"""
    if rate_limited is None:
        rate_limited, _ = auth_rate_limited_providers()
    if provider_is_rate_limited(provider, rate_limited):
        return {**skipped_result(provider, model), "timestamp": datetime.now().isoformat()}

    start = time.time()
    try:
        result = subprocess.run(
            ["hermes", "chat", "--provider", provider, "--model", model, "-q", TEST_PROMPT, "--oneshot"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        elapsed = time.time() - start
        rate_limited = is_rate_limit_error(result.stdout, result.stderr, result.returncode)
        return {
            "provider": provider,
            "model": model,
            "status": "rate_limited" if rate_limited else ("success" if result.returncode == 0 else "error"),
            "stdout": result.stdout[:2000],
            "stderr": result.stderr[:1000],
            "returncode": result.returncode,
            "elapsed_seconds": round(elapsed, 2),
            "timestamp": datetime.now().isoformat(),
            "provider_rate_limited": rate_limited,
        }
    except subprocess.TimeoutExpired:
        return {
            "provider": provider,
            "model": model,
            "status": "timeout",
            "elapsed_seconds": 120,
            "timestamp": datetime.now().isoformat(),
        }
    except Exception as e:
        return {
            "provider": provider,
            "model": model,
            "status": "exception",
            "error": str(e),
            "timestamp": datetime.now().isoformat(),
        }


def main():
    results = []
    rate_limited, inventory_error = auth_rate_limited_providers()
    if inventory_error:
        print(f"WARNING: {inventory_error}; runtime rate-limit detection remains enabled", flush=True)
    if rate_limited:
        print(f"Skipping providers from auth preflight: {', '.join(sorted(rate_limited))}", flush=True)

    grouped = {}
    for model in MODELS:
        grouped.setdefault(model["provider"], []).append(model)

    for provider, provider_models in grouped.items():
        if provider_is_rate_limited(provider, rate_limited):
            for model in provider_models:
                results.append({**skipped_result(provider, model["model"]), "timestamp": datetime.now().isoformat()})
            continue

        for position, model in enumerate(provider_models):
            print(f"Testing {provider}/{model['model']}...", flush=True)
            result = test_model(provider, model["model"], rate_limited)
            results.append(result)
            print(f"  -> {result['status']} ({result.get('elapsed_seconds', '?')}s)", flush=True)
            if result.get("provider_rate_limited") or result["status"] == "rate_limited":
                for skipped_model in provider_models[position + 1 :]:
                    results.append(
                        {
                            **skipped_result(provider, skipped_model["model"]),
                            "timestamp": datetime.now().isoformat(),
                        }
                    )
                break
            time.sleep(2)  # Space healthy requests without retrying a 429.

    out_path = os.path.join(os.path.dirname(__file__), "..", "test-providers-models-results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults written to {out_path}")


if __name__ == "__main__":
    main()
