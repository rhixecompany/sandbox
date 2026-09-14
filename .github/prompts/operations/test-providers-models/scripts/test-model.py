#!/usr/bin/env python3
"""Test individual provider models and record results."""

import json
import subprocess
import sys
import time

from provider_status import (
    SELF_PROFILE_PROMPT,
    auth_rate_limited_providers,
    is_rate_limit_error,
    provider_is_rate_limited,
    skipped_result,
)

TEST_PROMPT = SELF_PROFILE_PROMPT


def test_model(provider, model, rate_limited=None):
    if rate_limited is None:
        rate_limited, _ = auth_rate_limited_providers()
    if provider_is_rate_limited(provider, rate_limited):
        return skipped_result(provider, model)

    cmd = ["hermes", "chat", "--provider", provider, "--model", model, "-q", TEST_PROMPT, "--oneshot"]
    start = time.time()
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        latency = time.time() - start
        rate_limited = is_rate_limit_error(result.stdout, result.stderr, result.returncode)
        return {
            "provider": provider,
            "model": model,
            "latency": latency,
            "success": result.returncode == 0 and not rate_limited,
            "status": "rate_limited" if rate_limited else ("success" if result.returncode == 0 else "error"),
            "output": result.stdout[:500],
            "error": result.stderr[:500],
            "returncode": result.returncode,
            "provider_rate_limited": rate_limited,
        }
    except Exception as e:
        return {
            "provider": provider,
            "model": model,
            "latency": None,
            "success": False,
            "status": "exception",
            "error": str(e),
        }


if __name__ == "__main__":
    models = json.loads(sys.argv[1]) if len(sys.argv) > 1 else []
    rate_limited, inventory_error = auth_rate_limited_providers()
    if inventory_error:
        print(f"WARNING: {inventory_error}; runtime rate-limit detection remains enabled", file=sys.stderr)

    grouped = {}
    for model in models:
        grouped.setdefault(model["provider"], []).append(model)

    results = []
    for provider, provider_models in grouped.items():
        if provider_is_rate_limited(provider, rate_limited):
            results.extend(skipped_result(provider, model["model"]) for model in provider_models)
            continue
        for position, model in enumerate(provider_models):
            result = test_model(provider, model["model"], rate_limited=rate_limited)
            results.append(result)
            if result.get("provider_rate_limited"):
                results.extend(
                    skipped_result(provider, skipped_model["model"])
                    for skipped_model in provider_models[position + 1 :]
                )
                break
    print(json.dumps(results, indent=2))
