#!/usr/bin/env python3
"""enhance_soul.py — validate and repair SOUL.md across Hermes profiles.

Implements the /soul-enhancer skill contract:

  --check            validate structure + identity headers (default action)
  --fix              repair `**Profile:**` header and missing `**Identity:**`
  --apply-template   regenerate `**Identity:**` from profile.yaml description
                     using the persona mapping table in the skill
  --profile NAME     scope to a single profile name (default: all + root/default)
  --mirror           also validate the workspace mirror at ~/Desktop/SandBox/hermes-profiles
  --hermes-home DIR  override hermes home (default: ~/AppData/Local/hermes)

Exit code 0 = all checks passed; 1 = failures found (or fixed nothing pending).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Persona",
    "## Cognitive Style",
    "## Execution Frameworks",
    "## Architectural Invariants",
    "## Standing Rules",
    "## Memory Hierarchy",
]

PROFILE_RE = re.compile(r"^\*\*Profile:\*\*\s*(\S+)", re.M)
IDENTITY_RE = re.compile(r"^\*\*Identity:\*\*\s*(.+)$", re.M)

# profile.yaml description substring -> persona label (skill mapping table)
PERSONA_MAP = [
    ("Operations", "Operations engineer"),
    ("Code implementation, debugging, refactoring, TDD", "Senior software engineer"),
    ("Design, content creation, brainstorming, visual media", "Creative director"),
    ("Planning, coordination, admin, project management", "Executive assistant"),
    ("Tutorials, explanations, teaching, documentation", "Patient tutor"),
    ("Deep research, literature review, data synthesis", "Research analyst"),
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate/repair SOUL.md across profiles")
    p.add_argument("--check", action="store_true", help="validate only (default)")
    p.add_argument("--fix", action="store_true", help="repair headers in place")
    p.add_argument("--apply-template", action="store_true", help="regenerate Identity from profile.yaml")
    p.add_argument("--profile", default=None, help="single profile name")
    p.add_argument("--mirror", action="store_true", help="also validate workspace mirror")
    p.add_argument("--hermes-home", default=str(Path.home() / "AppData" / "Local" / "hermes"))
    return p.parse_args()


def persona_from_description(description: str) -> str | None:
    for needle, persona in PERSONA_MAP:
        if needle in description:
            return persona
    return None


def targets(home: Path, profile: str | None) -> list[tuple[str, Path]]:
    """Return [(label, SOUL.md path), ...] for root/default + live profiles."""
    out: list[tuple[str, Path]] = [("default", home / "SOUL.md")]
    profiles_dir = home / "profiles"
    if profiles_dir.exists():
        names = sorted(d.name for d in profiles_dir.iterdir() if d.is_dir())
        if profile:
            names = [n for n in names if n == profile]
        for name in names:
            p = profiles_dir / name / "SOUL.md"
            if p.exists():
                out.append((name, p))
    if profile == "default":
        out = [("default", home / "SOUL.md")]
    return out


def check_one(label: str, path: Path) -> list[str]:
    """Return list of problems for one SOUL.md (empty = OK)."""
    problems: list[str] = []
    if not path.exists():
        return [f"{label}: MISSING {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            problems.append(f"{label}: missing section `{section}`")
    m = PROFILE_RE.search(text)
    if not m:
        problems.append(f"{label}: missing `**Profile:**` header")
    elif m.group(1) != label:
        problems.append(f"{label}: header says `{m.group(1)}`, expected `{label}`")
    if not IDENTITY_RE.search(text):
        problems.append(f"{label}: missing `**Identity:**` line")
    return problems


def fix_one(label: str, path: Path, apply_template: bool, profile_yaml: Path | None) -> list[str]:
    """Repair header issues in place. Returns applied changes."""
    changes: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    m = PROFILE_RE.search(text)
    if m and m.group(1) != label:
        text = PROFILE_RE.sub(f"**Profile:** {label}", text, count=1)
        changes.append(f"{label}: fixed `**Profile:**` header")
    if apply_template and not IDENTITY_RE.search(text) and profile_yaml and profile_yaml.exists():
        desc = profile_yaml.read_text(encoding="utf-8", errors="replace")
        persona = persona_from_description(desc)
        if persona:
            identity = f"**Identity:** OWL: {persona}."
            # insert after the Profile/Model/Owner header block, before first section
            anchor = re.search(r"^(---\n|\*\*Identity:\*\*)", text, re.M)
            if anchor:
                text = text[: anchor.start()] + identity + "\n" + text[anchor.start() :]
            else:
                text += "\n" + identity + "\n"
            changes.append(f"{label}: added `**Identity:**` from profile.yaml")
    if changes:
        path.write_text(text, encoding="utf-8")
    return changes


def main() -> int:
    args = parse_args()
    home = Path(args.hermes_home)
    tgt = targets(home, args.profile)
    if args.mirror:
        mirror = Path.home() / "Desktop" / "SandBox" / "hermes-profiles"
        tgt += [("default", mirror / "profiles" / "default" / "SOUL.md")]
        for name, _ in targets(home, args.profile):
            if name != "default":
                p = mirror / "profiles" / name / "SOUL.md"
                if p.exists():
                    tgt.append((name, p))

    all_ok = True
    fixed: list[str] = []
    for label, path in tgt:
        problems = check_one(label, path)
        if not problems:
            continue
        all_ok = False
        if args.fix or args.apply_template:
            profile_yaml = home / "profiles" / label / "profile.yaml" if label != "default" else None
            changes = fix_one(label, path, args.apply_template, profile_yaml)
            fixed.extend(changes)
            if changes:
                problems = check_one(label, path)  # re-check after fix
                if not problems:
                    all_ok = True  # fixed
                    continue
        for problem in problems:
            print(f"  - {problem}")

    if fixed:
        print("Fixed:")
        for f in fixed:
            print(f"  + {f}")
    if args.fix or args.apply_template:
        print("FIX PASS COMPLETE (re-check to confirm zero failures)")
    print("OK: all SOUL.md structurally valid" if all_ok else "FAIL: problems remain")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
