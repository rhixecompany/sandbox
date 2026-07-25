#!/usr/bin/env python3
"""Batch skill judge — run skill-judge on all skills in parallel with aggregated reporting.

Usage:
    python batch_skill_judge.py [--skills-dir PATH] [--output PATH] [--json PATH] [--threshold INT]
"""

import argparse
import asyncio
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class SkillResult:
    name: str
    score: int
    passed: bool
    errors: list[str]
    duration: float


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run skill-judge on all skills in parallel")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--output", default=None, help="Path to output report file")
    parser.add_argument("--json", default=None, help="Path to JSON results file")
    parser.add_argument("--threshold", type=int, default=60, help="Pass threshold (default: 60)")
    return parser.parse_args(argv)


def load_skills(skills_dir: str | Path) -> list[Path]:
    """Discover all SKILL.md files in the skills directory tree."""
    base = Path(skills_dir).expanduser().resolve()
    if not base.is_dir():
        print(f"ERROR: skills directory not found: {base}", file=sys.stderr)
        sys.exit(1)
    return sorted(base.rglob("SKILL.md"))


def judge_skill(skill_path: Path) -> SkillResult:
    """Run judgement logic on a single skill. CPU-bound scoring logic."""
    start = time.monotonic()
    name = skill_path.parent.name
    errors: list[str] = []
    score = 100

    try:
        text = skill_path.read_text(encoding="utf-8")
    except Exception as e:
        return SkillResult(
            name=name, score=0, passed=False, errors=[f"Cannot read: {e}"], duration=time.monotonic() - start
        )

    # Simple scoring heuristics (CPU-bound, no IO)
    if not text.startswith("---"):
        errors.append("Missing YAML frontmatter")
        score -= 20

    required_fields = ["name", "title", "description", "version", "author"]
    for field in required_fields:
        if f"{field}:" not in text.split("---")[1] if "---" in text else "":
            errors.append(f"Missing frontmatter field: {field}")
            score -= 10

    if len(text.strip()) < 100:
        errors.append("Content too short (< 100 chars)")
        score -= 15

    if "## Overview" not in text:
        errors.append("Missing Overview section")
        score -= 10

    if "## Pitfalls" not in text:
        errors.append("Missing Pitfalls section")
        score -= 5

    if "## Workflow" not in text and "## When to Use" not in text:
        errors.append("Missing Workflow or When to Use section")
        score -= 10

    score = max(0, min(100, score))
    passed = score >= 60
    return SkillResult(name=name, score=score, passed=passed, errors=errors, duration=time.monotonic() - start)


async def judge_skill_async(skill_path: Path) -> SkillResult:
    """Async wrapper for judge_skill — runs CPU-bound scoring in a thread."""
    return await asyncio.to_thread(judge_skill, skill_path)


def generate_report(results: list[SkillResult], threshold: int) -> str:
    """Generate a text report from results."""
    passed = [r for r in results if r.passed]
    failed = [r for r in results if not r.passed]
    lines = [
        "=" * 60,
        "SKILL JUDGE REPORT",
        "=" * 60,
        f"Total: {len(results)} | Passed: {len(passed)} | Failed: {len(failed)} | Threshold: {threshold}",
        "",
    ]
    if failed:
        lines.append("--- FAILED ---")
        for r in failed:
            lines.append(f"  [{r.score:3d}] {r.name} ({r.duration:.2f}s)")
            for e in r.errors:
                lines.append(f"         - {e}")
        lines.append("")
    if passed:
        lines.append("--- PASSED ---")
        for r in sorted(passed, key=lambda x: x.score, reverse=True):
            lines.append(f"  [{r.score:3d}] {r.name} ({r.duration:.2f}s)")
    lines.append("")
    lines.append(f"Average score: {sum(r.score for r in results) / len(results) if results else 0:.1f}")
    lines.append(f"Total time: {sum(r.duration for r in results):.2f}s")
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = args.skills_dir or Path.home() / "AppData/Local/hermes/skills"
    skill_files = load_skills(skills_dir)

    if not skill_files:
        print("No skills found.", file=sys.stderr)
        sys.exit(1)

    print(f"Judging {len(skill_files)} skills (threshold={args.threshold})...")

    tasks = [judge_skill_async(sf) for sf in skill_files]
    results = await asyncio.gather(*tasks)

    report = generate_report(results, args.threshold)
    print(report)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(report, encoding="utf-8")
        print(f"\nReport written to {output_path}")

    if args.json:
        json_path = Path(args.json)
        json_path.write_text(
            json.dumps([asdict(r) for r in results], indent=2),
            encoding="utf-8",
        )
        print(f"JSON results written to {json_path}")


if __name__ == "__main__":
    asyncio.run(main())
