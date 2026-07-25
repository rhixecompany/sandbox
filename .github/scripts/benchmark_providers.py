#!/usr/bin/env python3
"""Benchmark LLM providers — compare latency, throughput, and error rates across providers.

Usage:
    python benchmark_providers.py [--providers NAMES] [--test-file PATH]
                                 [--iterations N] [--output FORMAT] [--report FILE] [--timeout N]
"""

import argparse
import asyncio
import json
import statistics
import time
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class ProviderResult:
    provider: str
    avg_latency: float
    min_latency: float
    max_latency: float
    p95_latency: float
    success_rate: float
    iterations: int
    errors: int


TEST_PROMPTS = [
    "What is the capital of France?",
    "Write a Python function to sort a list.",
    "Explain AI in simple terms.",
]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Benchmark LLM providers")
    parser.add_argument("--providers", default=None, help="Comma-separated provider names")
    parser.add_argument("--test-file", default=None, help="Path to JSON test prompts file")
    parser.add_argument("--iterations", type=int, default=5, help="Iterations per provider")
    parser.add_argument("--output", choices=["table", "json", "markdown", "csv"], default="table")
    parser.add_argument("--report", default=None, help="Save report to file")
    parser.add_argument("--timeout", type=int, default=30, help="Timeout per request (s)")
    return parser.parse_args(argv)


def load_test_prompts(path: str | None) -> list[str]:
    if path:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return data if isinstance(data, list) else data.get("prompts", TEST_PROMPTS)
    return TEST_PROMPTS


async def benchmark_provider(provider: str, prompts: list[str], iterations: int, timeout: int) -> ProviderResult:
    """Benchmark a single provider by simulating API calls."""
    latencies: list[float] = []
    errors = 0

    for prompt in prompts * iterations:
        try:
            start = time.monotonic()
            # Simulate provider-specific latency
            sim_time = 0.2 + (hash(provider + prompt) % 150) / 100  # 0.2-1.7s
            await asyncio.sleep(sim_time)
            elapsed = time.monotonic() - start
            latencies.append(elapsed)
        except Exception:
            errors += 1

    if not latencies:
        return ProviderResult(
            provider=provider,
            avg_latency=0,
            min_latency=0,
            max_latency=0,
            p95_latency=0,
            success_rate=0,
            iterations=0,
            errors=errors,
        )

    sorted_lat = sorted(latencies)
    p95_idx = max(0, int(len(sorted_lat) * 0.95) - 1)
    return ProviderResult(
        provider=provider,
        avg_latency=statistics.mean(latencies),
        min_latency=min(latencies),
        max_latency=max(latencies),
        p95_latency=sorted_lat[min(p95_idx, len(sorted_lat) - 1)],
        success_rate=(len(latencies) / max(len(prompts) * iterations, 1)),
        iterations=len(latencies),
        errors=errors,
    )


def format_table(results: list[ProviderResult]) -> str:
    lines = [
        f"{'Provider':<20} {'Avg(s)':<10} {'Min(s)':<10} {'Max(s)':<10} {'P95(s)':<10} {'Success%':<10} {'Err':<6}",
        "-" * 76,
    ]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(
            f"{r.provider:<20} {r.avg_latency:<10.3f} {r.min_latency:<10.3f} "
            f"{r.max_latency:<10.3f} {r.p95_latency:<10.3f} "
            f"{r.success_rate * 100:<10.1f} {r.errors:<6}"
        )
    return "\n".join(lines)


def format_markdown(results: list[ProviderResult]) -> str:
    lines = [
        "| Provider | Avg (s) | Min (s) | Max (s) | P95 (s) | Success % | Errors |",
        "|---------|--------|--------|--------|--------|---------|-------|",
    ]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(
            f"| {r.provider} | {r.avg_latency:.3f} | {r.min_latency:.3f} | "
            f"{r.max_latency:.3f} | {r.p95_latency:.3f} | "
            f"{r.success_rate * 100:.1f}% | {r.errors} |"
        )
    return "\n".join(lines)


def format_csv(results: list[ProviderResult]) -> str:
    lines = ["provider,avg_latency,min_latency,max_latency,p95_latency,success_rate,errors"]
    for r in sorted(results, key=lambda x: x.avg_latency):
        lines.append(
            f"{r.provider},{r.avg_latency:.3f},{r.min_latency:.3f},{r.max_latency:.3f},{r.p95_latency:.3f},{r.success_rate},{r.errors}"
        )
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    prompts = load_test_prompts(args.test_file)
    provider_list = (
        [p.strip() for p in args.providers.split(",")] if args.providers else ["openai", "anthropic", "mistral"]
    )

    print(f"Benchmarking {len(provider_list)} providers × {args.iterations} iterations")
    print()

    tasks = [benchmark_provider(p, prompts, args.iterations, args.timeout) for p in provider_list]
    results = await asyncio.gather(*tasks)

    output = ""
    if args.output == "table":
        output = format_table(results)
    elif args.output == "markdown":
        output = format_markdown(results)
    elif args.output == "csv":
        output = format_csv(results)
    elif args.output == "json":
        output = json.dumps([asdict(r) for r in results], indent=2)

    print(output)

    if args.report:
        Path(args.report).write_text(output, encoding="utf-8")
        print(f"\nReport saved to {args.report}")


if __name__ == "__main__":
    asyncio.run(main())
