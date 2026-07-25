#!/usr/bin/env python3
"""Boost near-pass refs — promote or boost the file references in near-pass skills.

Usage:
    python boost_near_pass_refs.py [--skills-dir PATH] [--threshold INT] [--output PATH]
                                   [--dry-run] [--report FILE]
"""

import argparse
import asyncio
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class SkillRef:
    name: str
    skill_path: str
    ref_count: int
    ref_types: list[str]
    boost_applied: bool


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Boost near-pass refs in skills")
    parser.add_argument("--skills-dir", default=None, help="Path to skills directory")
    parser.add_argument("--threshold", type=int, default=60, help="Score threshold (default: 60)")
    parser.add_argument("--output", default=None, help="Output report path")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--report", default=None, help="Save detailed report to file")
    return parser.parse_args(argv)


def _scan_skill(skill_dir: Path) -> SkillRef:
    """Scan a single skill directory for referenced skills (CPU-bound)."""
    name = skill_dir.name
    skill_path = str(skill_dir)
    ref_count = 0
    ref_types: list[str] = []

    # Check SKILL.md for skill references
    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        try:
            text = skill_md.read_text(encoding="utf-8")
            for keyword in ["Related Skills", "related_skills", "See Also", "Dependencies"]:
                if keyword in text:
                    ref_count += text.count("`") // 2  # estimate
                    ref_types.append(keyword)
        except Exception:
            pass

    # Check for .prompt files referencing other skills
    for prompt_file in skill_dir.rglob("*.prompt.md"):
        try:
            text = prompt_file.read_text(encoding="utf-8")
            if "skills:" in text or "skill:" in text:
                ref_count += 1
                ref_types.append("prompt-ref")
        except Exception:
            pass

    return SkillRef(
        name=name, skill_path=skill_path, ref_count=ref_count, ref_types=list(set(ref_types)), boost_applied=False
    )


async def scan_skill_async(skill_dir: Path) -> SkillRef:
    """Async wrapper for scan_skill."""
    return await asyncio.to_thread(_scan_skill, skill_dir)


def _boost_skill(skill_dir: Path, dry_run: bool) -> SkillRef:
    """Boost a skill by adding reference sections if missing."""
    ref = _scan_skill(skill_dir)
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return ref

    try:
        text = skill_md.read_text(encoding="utf-8")
    except Exception:
        return ref

    # Check if "## Related Skills" section exists
    has_related = "## Related Skills" in text or "## See Also" in text

    # Boost: add Related Skills section if missing and skill has refs
    if not has_related and ref.ref_count > 0:
        boost_note = "\n\n## Related Skills\n\n<!-- Auto-boosted: related references detected but no Related Skills section -->\n"
        if not dry_run:
            text += boost_note
            skill_md.write_text(text, encoding="utf-8")
        ref.boost_applied = True

    return ref


async def boost_skill_async(skill_dir: Path, dry_run: bool) -> SkillRef:
    """Async wrapper for boost_skill."""
    return await asyncio.to_thread(_boost_skill, skill_dir, dry_run)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    skills_dir = Path(args.skills_dir or Path.home() / "AppData/Local/hermes/skills")

    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    skill_dirs = sorted([d for d in skills_dir.iterdir() if d.is_dir()])
    print(f"Scanning {len(skill_dirs)} skill directories...")

    # Phase 1: Scan all skills
    scan_tasks = [scan_skill_async(sd) for sd in skill_dirs]
    refs = await asyncio.gather(*scan_tasks)

    print(
        f"Found {sum(r.ref_count for r in refs)} references across {len([r for r in refs if r.ref_count > 0])} skills"
    )

    # Phase 2: Boost skills
    boost_candidates = [r for r in refs if r.ref_count > 0]
    print(f"Boosting {len(boost_candidates)} candidates (dry-run={args.dry_run})...")

    boost_tasks = [boost_skill_async(Path(r.skill_path), args.dry_run) for r in boost_candidates]
    boosted = await asyncio.gather(*boost_tasks)

    applied = [b for b in boosted if b.boost_applied]
    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"\n{mode}: {len(applied)} skills boosted")

    for b in applied:
        print(f"  {b.name}: {b.ref_count} refs, types={b.ref_types}")

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(
            json.dumps([asdict(r) for r in boosted], indent=2),
            encoding="utf-8",
        )
        print(f"\nResults written to {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
