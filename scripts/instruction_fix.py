#!/usr/bin/env python3
"""
Instruction File Fix — Goal 1 (Whitelist Auto-Fixer)
=====================================================

Applies ONLY whitelisted, mechanical replacements to instruction files.
Never merges blocks, never changes frontmatter structure, never deletes content.

Usage:
    python scripts/instruction_fix.py --dry-run              # default; show diffs, write nothing
    python scripts/instruction_fix.py --apply                # actually write
    python scripts/instruction_fix.py --type .cursorrules --apply
    python scripts/instruction_fix.py --path "**/mindstudio*" --apply

Whitelist rules live in: templates/whitelist-fixes.json (editable)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# --- Whitelist rules ---------------------------------------------------------
# Loaded from templates/whitelist-fixes.json (fallback to inline default)

DEFAULT_RULES: list[dict] = [
    {
        "id": "bash_path_migration",
        "description": "Bash/ migrated to projects/Bash/",
        "pattern": r"(?<!projects/)Bash/(?!projects)",
        "replacement": "projects/Bash/",
        "enabled": True,
    },
    {
        "id": "resume_maker_migration",
        "description": "Resume_maker/ migrated to projects/Resume_maker/",
        "pattern": r"(?<!projects/)Resume_maker/(?!projects)",
        "replacement": "projects/Resume_maker/",
        "enabled": True,
    },
    {
        "id": "trim_trailing_whitespace",
        "description": "Strip trailing whitespace (markdownlint MD009)",
        "pattern": r"[ \t]+$",
        "replacement": "",
        "flags": ["MULTILINE"],
        "enabled": True,
    },
    {
        "id": "collapse_excess_newlines",
        "description": "Collapse 3+ consecutive newlines to 2",
        "pattern": r"\n{3,}",
        "replacement": "\n\n",
        "enabled": True,
    },
    {
        "id": "zen_backup_deprecated",
        "description": "zen-backup reference: collapse to single opencode-zen key",
        "pattern": r"zen-backup",
        "replacement": "(see opencode-zen pool)",
        "enabled": True,
    },
]


def load_rules(custom_path: Path | None) -> list[dict]:
    if custom_path and custom_path.exists():
        try:
            data = json.loads(custom_path.read_text(encoding="utf-8"))
            return [r for r in data.get("rules", []) if r.get("enabled", True)]
        except Exception as e:
            print(f"WARN: failed to load {custom_path}: {e}; using defaults", file=sys.stderr)
    return [r for r in DEFAULT_RULES if r.get("enabled", True)]


# --- Data classes ------------------------------------------------------------

@dataclass
class FileChange:
    path: str
    rules_applied: list[str]
    lines_changed: int


# --- Core logic --------------------------------------------------------------

def compile_rule(rule: dict) -> re.Pattern:
    flags = 0
    for f in rule.get("flags", []):
        f_upper = f.upper()
        if hasattr(re, f_upper):
            flags |= getattr(re, f_upper)
    return re.compile(rule["pattern"], flags)


def is_instruction_file(path: Path) -> bool:
    name = path.name
    if name in {"SOUL.md", "USER.md", "MEMORY.md", ".hermes.md", "AGENTS.md",
                "CLAUDE.md", ".cursorrules", "copilot-instructions.md"}:
        return True
    if str(path).replace("\\", "/").endswith(".github/copilot-instructions.md"):
        return True
    return False


SKIP_SUBSTRINGS = [
    "/.git/", "/cache/", "/spawn-trees/", "/pending/", "/.curator_backups/",
    "/pastes/", "/.venv", "/node_modules/", "/desktop/dist/",
    "/hermes-agent/website/", "/hermes-agent/apps/", "/hermes-agent/docs/",
    "/hermes-agent/cli/", "/hermes-agent/scripts/", "/hermes-agent/hermes/",
    "/hermes-agent/src/", "/hermes-agent/tests/",
    "/hermes-agent/skills/", "/hermes-agent/hooks/", "/hermes-agent/plugins/",
    "/hermes-agent/cron/", "/hermes-agent/data/", "/hermes-agent/docker/",
]


def is_skipped(path: Path) -> bool:
    norm = str(path).replace("\\", "/")
    return any(sub in norm for sub in SKIP_SUBSTRINGS)


def apply_rules(content: str, rules: list[dict]) -> tuple[str, list[str]]:
    """Apply each rule, return (new_content, list_of_rule_ids_applied)."""
    applied: list[str] = []
    new = content
    for rule in rules:
        try:
            pat = compile_rule(rule)
        except re.error as e:
            print(f"WARN: bad pattern in rule {rule.get('id')}: {e}", file=sys.stderr)
            continue
        new, n = pat.subn(rule["replacement"], new)
        if n > 0:
            applied.append(f"{rule['id']} ({n} sub)")
    return new, applied


def diff_lines(old: str, new: str) -> int:
    """Naive line-diff count: number of lines that differ."""
    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)
    if old_lines == new_lines:
        return 0
    return max(len(old_lines), len(new_lines)) - min(
        sum(1 for o, n in zip(old_lines, new_lines) if o == n),
        min(len(old_lines), len(new_lines))
    )


def fix(roots: list[Path], rules: list[dict], path_glob: str | None = None) -> list[FileChange]:
    changes: list[FileChange] = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if is_skipped(p):
                continue
            if not is_instruction_file(p):
                continue
            if path_glob and not p.match(path_glob):
                continue
            try:
                original = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            new, applied = apply_rules(original, rules)
            if not applied:
                continue
            delta = diff_lines(original, new)
            changes.append(FileChange(path=str(p), rules_applied=applied, lines_changed=delta))
    return changes


# --- CLI ---------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Whitelist-only instruction file fixer")
    ap.add_argument("--apply", action="store_true", help="Actually write changes (default: dry-run)")
    ap.add_argument("--rules", "-r", type=Path, default=None, help="Path to whitelist-fixes.json")
    ap.add_argument("--path", "-p", default=None, help="Glob filter (e.g. '**/mindstudio*')")
    ap.add_argument("--type", "-t", default=None, choices=[
        "SOUL.md", "USER.md", "MEMORY.md", ".hermes.md", "AGENTS.md",
        "CLAUDE.md", ".cursorrules", "copilot-instructions.md"
    ])
    args = ap.parse_args()

    rules = load_rules(args.rules)
    if args.type:
        # Restrict to files of this type
        roots = [Path("C:/Users/Alexa/Desktop/SandBox"), Path("C:/Users/Alexa/AppData/Local/hermes")]
        all_changes: list[FileChange] = []
        for root in roots:
            if not root.exists():
                continue
            for p in root.rglob(args.type):
                if not p.is_file() or is_skipped(p):
                    continue
                try:
                    original = p.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                new, applied = apply_rules(original, rules)
                if applied:
                    delta = diff_lines(original, new)
                    all_changes.append(FileChange(path=str(p), rules_applied=applied, lines_changed=delta))
                    if args.apply:
                        p.write_text(new, encoding="utf-8")
        print(json.dumps({"dry_run": not args.apply, "files_would_change": len(all_changes),
                          "files_changed": len(all_changes) if args.apply else 0,
                          "rules_loaded": [r["id"] for r in rules]}, indent=2))
        for c in all_changes[:20]:
            print(f"  {c.path}  →  {', '.join(c.rules_applied)}")
        return 0

    # Otherwise walk all
    roots = [Path("C:/Users/Alexa/Desktop/SandBox"), Path("C:/Users/Alexa/AppData/Local/hermes")]
    changes = fix(roots, rules, path_glob=args.path)
    if args.apply:
        for c in changes:
            p = Path(c.path)
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
                new, _ = apply_rules(content, rules)
                p.write_text(new, encoding="utf-8")
            except Exception as e:
                print(f"ERR: {p}: {e}", file=sys.stderr)
    summary = {
        "dry_run": not args.apply,
        "files_would_change": len(changes),
        "files_changed": len(changes) if args.apply else 0,
        "rules_loaded": [r["id"] for r in rules],
    }
    print(json.dumps(summary, indent=2))
    for c in changes[:20]:
        print(f"  {c.path}  →  {', '.join(c.rules_applied)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
