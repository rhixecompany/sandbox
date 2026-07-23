#!/usr/bin/env python3
"""Benchmark LLM models for performance comparison within the Hermes ecosystem.

Usage:
    python benchmark_models.py [--providers NAMES] [--models NAMES] [--test-file PATH]
                              [--iterations N] [--output FORMAT] [--report FILE]
                              [--warm-up N] [--timeout N]
"""

import asyncio
import argparse
import json
import sys
import time
import statistics
from pathlib import Path
from dataclasses import dataclass, asdict


@dataclass
class BenchmarkResult:
    provider: str
    model: str
    avg_latency: float
    avg_tokens_per_sec: float
    total_tokens: int
    error_rate: float
    iterations: int


TEST_PROMPTS = [
    "What is the capital of France?",
    "Write a Python function to sort a list of numbers.",
    "Explain quantum computing in simple terms.",
    "Write a short poem about artificial intelligence.",
    "Solve: 2 + 2 = ?",
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark LLM models")
    parser.add_argument("--providers", default=None, help="Comma-separated provider names")
    parser.add_argument("--models", default=None, help="Comma-separated model IDs")
    parser.add_argument("--test-file", default=None, help="Path to JSON test prompts file")
    parser.add_argument("--iterations", type=int, default=3, help="Iterations per test")
    parser.add_argument("--warm-up", type=int, default=1, help="Warm-up iterations")
    parser.add_argument("--timeout", type=int, default=60, help="Timeout per request (s)")
    parser.add_argument("--output", choices=["table", "json", "markdown", "csv"], default="table")
    parser.add_argument("--report", default=None, help="Save report to file")
    return parser.parse_args(argv)


def load_test_prompts(path: str | None) -> list[str]:
    """Load test prompts from file or use defaults."""
    if path:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, list) else data.get("prompts", TEST_PROMPTS)
    return TEST_PROMPTS


async def simulate_model_call(model: str, prompt: str, timeout: int) -> tuple[float, int]:
    """Simulate a model API call. In production, this would call an actual LLM API."""
    # Simulate variable latency and token generation
    sim_time = 0.3 + (hash(model + prompt) % 100) / 100  # 0.3-1.3s
    await asyncio.sleep(sim_time)
    tokens = len(prompt.split()) * 2 + (hash(model) % 50)
    return sim_time, tokens


async def benchmark_model(provider: str, model: str, prompts: list[str],
                          iterations: int, warm_up: int, timeout: int) -> BenchmarkResult:
    """Benchmark a single model with given prompts."""
    latencies: list[float] = []
    tokens_per_sec: list[float] = []
    errors = 0

    all_prompts = prompts * (iterations + warm_up)
    for i, prompt in enumerate(all_prompts):
        try:
            start = time.monotonic()
            sim_time, tokens = await simulate_model_call(model, prompt, timeout)
            elapsed = time.monotonic() - start
            if i >= warm_up:
                latencies.append(elapsed)
                tokens_per_sec.append(tokens / max(elapsed, 0.001))
        except Exception:
            if i >= warm_up:
                errors += 1

    if not latencies:
        return BenchmarkResult(provider=provider, model=model,
                               avg_latency=0, avg_tokens_per_sec=0,
                               total_tokens=0, error_rate=1.0, iterations=0)

    return BenchmarkResult(
        provider=provider,
        model=model,
        avg_latency=statistics.mean(latencies),
        avg_tokens_per_sec=statistics.mean(tokens_per_sec),
        total_tokens=int(sum(t for _, t in [(0, 0)]) + 1),  # placeholder
        error_rate=errors / max(len(prompts) * iterations, 1),
        iterations=len(latencies),
    )


def format_table(results: list[BenchmarkResult]) -> str:
    """Format results as a table."""
    lines = [
        f"{'Provider':<20} {'Model':<25} {'Latency(s)':<12} {'Tok/s':<10} {'Err%':<8} {'Iters':<6}",
        "-" * 81,
    ]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(
            f"{r.provider:<20} {r.model:<25} {r.avg_latency:<12.3f} "
            f"{r.avg_tokens_per_sec:<10.1f} {r.error_rate*100:<8.1f} {r.iterations:<6}"
        )
    return "\n".join(lines)


def format_markdown(results: list[BenchmarkResult]) -> str:
    """Format results as markdown."""
    lines = [
        "| Provider | Model | Latency (s) | Tok/s | Error % | Iterations |",
        "|---------|-------|------------|------|--------|-----------|",
    ]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(
            f"| {r.provider} | {r.model} | {r.avg_latency:.3f} | "
            f"{r.avg_tokens_per_sec:.1f} | {r.error_rate*100:.1f}% | {r.iterations} |"
        )
    return "\n".join(lines)


def format_csv(results: list[BenchmarkResult]) -> str:
    """Format results as CSV."""
    lines = ["provider,model,avg_latency,avg_tokens_per_sec,error_rate,iterations"]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(f"{r.provider},{r.model},{r.avg_latency:.3f},{r.avg_tokens_per_sec:.1f},{r.error_rate},{r.iterations}")
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    prompts = load_test_prompts(args.test_file)

    providers = args.providers.split(",") if args.providers else ["default"]
    models = args.models.split(",") if args.models else ["gpt-3.5-turbo", "gpt-4"]

    print(f"Benchmarking {len(providers)} providers × {len(models)} models × {len(prompts)} prompts")
    print(f"Iterations: {args.iterations} (+ {args.warm_up} warm-up)")
    print()

    tasks = []
    for provider in providers:
        for model in models:
            tasks.append(benchmark_model(provider.strip(), model.strip(), prompts,
                                         args.iterations, args.warm_up, args.timeout))

    results = await asyncio.gather(*tasks)

    if args.output == "table":
        print(format_table(results))
    elif args.output == "markdown":
        print(format_markdown(results))
    elif args.output == "csv":
        print(format_csv(results))
    elif args.output == "json":
        print(json.dumps([asdict(r) for r in results], indent=2))

    if args.report:
        report_path = Path(args.report)
        if args.output == "json":
            report_path.write_text(json.dumps([asdict(r) for r in results], indent=2), encoding="utf-8")
        elif args.output == "markdown":
            report_path.write_text(format_markdown(results), encoding="utf-8")
        elif args.output == "csv":
            report_path.write_text(format_csv(results), encoding="utf-8")
        else:
            report_path.write_text(format_table(results), encoding="utf-8")
        print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
