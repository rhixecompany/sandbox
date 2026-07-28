#!/usr/bin/env python3
"""Provider health check - offline mode using documented research."""

import json
import sys
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ProviderHealth:
    name: str
    status: str  # documented_healthy, documented_rate_limited, documented_unavailable
    latency_ms: float
    error: str = ""
    model_tested: str = ""


def main():
    print("=" * 60)
    print("PROVIDER HEALTH CHECK (Documented Research - Offline)")
    print("=" * 60)

    # Based on web research (2026-07-27) and Hermes auth list
    results = [
        ProviderHealth(
            name="opencode-zen",
            status="documented_healthy",
            latency_ms=500,  # estimated
            model_tested="deepseek-v4-flash-free (primary), nemotron-3-ultra-free (fallback)",
            error=None,
        ),
        ProviderHealth(
            name="openrouter",
            status="documented_healthy",
            latency_ms=600,  # estimated
            model_tested="18 free models available (qwen3-coder, nemotron-ultra, gemma-4, poolside)",
            error=None,
        ),
        ProviderHealth(
            name="google-ai-studio",
            status="documented_healthy",
            latency_ms=400,  # estimated
            model_tested="gemini-2.5-flash, gemma-4 (via browser)",
            error=None,
        ),
        ProviderHealth(
            name="huggingface-inference",
            status="documented_healthy",
            latency_ms=800,  # estimated
            model_tested="100s via providers (Kimi, GLM, DeepSeek, Qwen)",
            error=None,
        ),
        ProviderHealth(
            name="copilot-cli",
            status="documented_healthy",
            latency_ms=3000,  # measured earlier
            model_tested="gpt-5-mini (verified working)",
            error=None,
        ),
        ProviderHealth(
            name="nous",
            status="documented_unknown",
            latency_ms=0,
            model_tested="hermes-3, nemotron-ultra (OAuth configured)",
            error="Free tier unknown - check nousresearch.com",
        ),
        ProviderHealth(
            name="ollama-cloud",
            status="documented_unknown",
            latency_ms=0,
            model_tested="Ollama-compatible models (API key configured)",
            error="Free tier unknown - check ollama.com/cloud",
        ),
        ProviderHealth(
            name="xai",
            status="documented_unknown",
            latency_ms=0,
            model_tested="Grok series (OAuth configured)",
            error="Free tier unknown - check x.ai/api",
        ),
        ProviderHealth(
            name="deepseek",
            status="documented_unavailable",
            latency_ms=0,
            model_tested="deepseek-v4, coder, r1",
            error="API key exhausted (402 Payment Required)",
        ),
        ProviderHealth(
            name="gemini-api",
            status="documented_rate_limited",
            latency_ms=0,
            model_tested="gemini-1.5-flash, 2.5-flash",
            error="API key rate limited (429) - use AI Studio instead",
        ),
        ProviderHealth(
            name="openai-codex",
            status="documented_rate_limited",
            latency_ms=0,
            model_tested="Codex CLI models",
            error="OAuth rate limited (429) - 11d 15h reset",
        ),
        ProviderHealth(
            name="openai-api",
            status="documented_unknown",
            latency_ms=0,
            model_tested="GPT-4o, GPT-4o mini, o1, o3-mini",
            error="Keys configured but no free tier credits",
        ),
    ]

    healthy = []
    rate_limited = []
    unknown = []
    unavailable = []

    for r in results:
        print(f"\n{r.name.upper()}:")
        print(f"  Status:  {r.status}")
        print(f"  Latency: {r.latency_ms:.0f}ms (estimated)")
        if r.model_tested:
            print(f"  Models:  {r.model_tested}")
        if r.error:
            print(f"  Note:    {r.error}")

        if "healthy" in r.status:
            healthy.append(r)
        elif "rate_limited" in r.status:
            rate_limited.append(r)
        elif "unknown" in r.status:
            unknown.append(r)
        else:
            unavailable.append(r)

    print("\n" + "=" * 60)
    print("RECOMMENDED FALLBACK CHAIN (Production)")
    print("=" * 60)

    # Priority chain for production use
    chain = [
        ("opencode-zen", "Primary gateway (deepseek-v4-flash-free / nemotron-3-ultra-free)"),
        ("openrouter", "Secondary (18 free models: qwen3-coder, nemotron-ultra, gemma-4, poolside)"),
        ("google-ai-studio", "Tertiary (browser access, high limits, 1M+ context, multimodal)"),
        ("huggingface-inference", "Quaternary (100s models via providers: Kimi, GLM, DeepSeek, Qwen)"),
        ("copilot-cli", "Quinary (GitHub-integrated, GPT-5-mini, 50 req/mo free)"),
    ]

    for i, (name, desc) in enumerate(chain, 1):
        status = next((r.status for r in results if r.name == name), "unknown")
        print(f"  {i}. {name} - {desc}")

    # Save results
    out = Path("docs/research/health-check-results.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps([{
        "name": r.name,
        "status": r.status,
        "latency_ms": r.latency_ms,
        "model_tested": r.model_tested,
        "error": r.error,
    } for r in results], indent=2))

    print(f"\nResults saved to {out}")
    print("\nNote: This is an offline assessment based on web research (2026-07-27)")
    print("and Hermes auth list. Live testing requires network access.")

    sys.exit(0)


if __name__ == "__main__":
    main()