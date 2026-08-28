#!/usr/bin/env python3
"""
Instruction File Audit — Goal 1
================================

Read-only triage of all instruction-style files across the SandBox workspace
and all Hermes profiles. Stdlib only. Emits JSON per SPEC §4.

Usage:
    python scripts/instruction_audit.py
    python scripts/instruction_audit.py --output PATH
    python scripts/instruction_audit.py --scope sandbox|hermes|both

Classifications: canonical | duplicate | bloat | stale | conflicting | unknown
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration -----------------------------------------------------------

INSTRUCTION_PATTERNS = [
    "SOUL.md",
    "USER.md",
    "MEMORY.md",
    ".hermes.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".cursorrules",
    "copilot-instructions.md",
    ".github/copilot-instructions.md",
]

# Walk roots
DEFAULT_ROOTS = [
    Path("C:/Users/Alexa/Desktop/SandBox"),
    Path("C:/Users/Alexa/AppData/Local/hermes"),
]

# Skip any path matching one of these substrings (case-insensitive on Windows)
SKIP_SUBSTRINGS = [
    "/.git/",
    "/cache/",
    "/spawn-trees/",
    "/pending/",
    "/.curator_backups/",
    "/pastes/",
    "/.venv",
    "/node_modules/",
    "/desktop/dist/",
    "/packages/openrouter-client/node_modules/",
    "/packages/openrouter-client-py/",
    # hermes-agent source (different governance)
    "/hermes-agent/website/",
    "/hermes-agent/apps/",
    "/hermes-agent/docs/",
    "/hermes-agent/cli/",
    "/hermes-agent/scripts/",
    "/hermes-agent/hermes/",
    "/hermes-agent/src/",
    "/hermes-agent/tests/",
    "/hermes-agent/profiles/",
    "/hermes-agent/skills/",
    "/hermes-agent/hooks/",
    "/hermes-agent/plugins/",
    "/hermes-agent/cron/",
    "/hermes-agent/data/",
    "/hermes-agent/__pycache__/",
    "/hermes-agent/benchmark_results/",
    "/hermes-agent/build_artifacts/",
    "/hermes-agent/docker/",
    "/hermes-agent/scripts_repo/",
    "/hermes-agent/dev_assets/",
    "/hermes-agent/payload/",
    "/hermes-agent/specs/",
]

# Classification thresholds
LINE_CAP = 250
BLOAT_SIZE_KB = 10
BLOAT_H1_COUNT = 5
BLOAT_BULLET_COUNT = 30

# Known-stale references → flagged as `stale`
STALE_PATTERNS = [
    (r"minimax/minimax-m3:free", "minimax/minimax-m3:free retired; current default is minimax/minimax-m3:free via openrouter"),  # tracked but flagged for review
    (r"\bBash/(?!\.\.)", "Bash/ migrated to projects/Bash/"),
    (r"\bResume_maker/(?!\.\.)", "Resume_maker/ migrated to projects/Resume_maker/"),
    (r"opencode-zen.*zen-backup", "deprecated reference"),
]

# Conflicting markers (when one of these appears, it's flagged)
CONFLICTING_RULES = [
    (r"always use PowerShell", "PowerShell is user-only; agent terminal is bash"),
    (r"never use PowerShell", "PowerShell is user-only; agent terminal is bash"),
    (r"never commit\b", "user-communication-prefs: commit only with explicit ask"),
]

# Cross-reference detection (these rules appear in many files; duplicates counted here)
CANONICAL_RULES = [
    ("mcp_first", r"MCP[- ]?first|use MCP server"),
    ("profile_routing", r"profile.*routing|profile-per-task"),
    ("dry_principle", r"\bDRY\b|do not repeat"),
    ("session_startup", r"session[- ]?start protocol|5-skill startup"),
]


# --- Data classes ------------------------------------------------------------

@dataclass
class FileEntry:
    path: str
    type: str
    size_bytes: int
    line_count: int
    classification: str
    issues: list[str] = field(default_factory=list)
    last_modified: str = ""


@dataclass
class AuditReport:
    schema_version: int
    generated_at: str
    scope: str
    totals: dict
    files: list[FileEntry]
    cross_refs: dict
    notes: list[str] = field(default_factory=list)


# --- Classification ----------------------------------------------------------

def classify(file_path: Path, content: str, all_files: list[FileEntry]) -> tuple[str, list[str]]:
    """Return (classification, issues) for a single file."""
    issues: list[str] = []
    text = content
    line_count = text.count("\n") + 1 if text else 0
    size_kb = file_path.stat().st_size / 1024

    # Bloat
    if line_count > LINE_CAP:
        issues.append(f"exceeds_{LINE_CAP}_line_cap ({line_count} lines)")
    if size_kb > BLOAT_SIZE_KB:
        issues.append(f"exceeds_{BLOAT_SIZE_KB}KB ({size_kb:.1f}KB)")
    h1_count = len(re.findall(r"^# .+$", text, re.MULTILINE))
    if h1_count > BLOAT_H1_COUNT:
        issues.append(f"too_many_H1 ({h1_count})")

    # Stale
    for pattern, reason in STALE_PATTERNS:
        if re.search(pattern, text):
            issues.append(f"stale: {reason}")

    # Conflicting
    for pattern, reason in CONFLICTING_RULES:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f"conflicting: {reason}")

    # Duplicate detection: same type in same parent dir
    parent = file_path.parent
    same_parent_same_type = [f for f in all_files
                             if Path(f.path).parent == parent and f.type == str(file_path.name)]
    if len(same_parent_same_type) > 1:
        issues.append("duplicate_in_parent_dir")

    # Decide class
    if any(i.startswith("conflicting:") for i in issues):
        return "conflicting", issues
    if any(i.startswith("stale:") for i in issues):
        return "stale", issues
    if any(i.startswith("exceeds_") or i.startswith("too_many_") for i in issues):
        return "bloat", issues
    if any(i == "duplicate_in_parent_dir" for i in issues):
        return "duplicate", issues
    # Heuristic canonical: short, at known roots
    is_root = any(
        file_path.match(str(p / "SOUL.md")) or
        file_path.match(str(p / "USER.md")) or
        file_path.match(str(p / "MEMORY.md")) or
        file_path.match(str(p / "AGENTS.md")) or
        file_path.match(str(p / "CLAUDE.md")) or
        file_path.match(str(p / ".hermes.md")) or
        file_path.match(str(p / ".cursorrules"))
        for p in DEFAULT_ROOTS
    )
    if is_root and line_count <= LINE_CAP and not issues:
        return "canonical", issues
    return "unknown", issues


def is_instruction_file(path: Path) -> bool:
    """Check if a path matches one of the instruction patterns."""
    name = path.name
    if name in INSTRUCTION_PATTERNS:
        return True
    # Also check .github/copilot-instructions.md
    rel = path.relative_to(path.parents[len(path.parents) - 3]) if len(path.parts) > 3 else path
    if str(rel).replace("\\", "/").endswith(".github/copilot-instructions.md"):
        return True
    return False


def is_skipped(path: Path) -> bool:
    norm = str(path).replace("\\", "/")
    return any(sub in norm for sub in SKIP_SUBSTRINGS)


# --- Audit walk --------------------------------------------------------------

def audit(roots: list[Path]) -> AuditReport:
    entries: list[FileEntry] = []

    # First pass: collect all instruction files
    raw: list[tuple[Path, str, str]] = []  # (path, type, content)
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
            try:
                content = p.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                content = f"<<READ_ERROR: {e}>>"
            raw.append((p, p.name, content))

    # Second pass: classify (needs full list for duplicate detection)
    for p, ftype, content in raw:
        # Build a stub entry first
        try:
            stat = p.stat()
            lm = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
        except Exception:
            lm = ""
        stub = FileEntry(
            path=str(p),
            type=ftype,
            size_bytes=stat.st_size if "stat" in dir() else 0,
            line_count=content.count("\n") + 1 if content else 0,
            classification="unknown",
            issues=[],
            last_modified=lm,
        )
        all_stubs = [FileEntry(
            path=str(pp), type=tt, size_bytes=0, line_count=0,
            classification="", issues=[], last_modified=""
        ) for pp, tt, _ in raw]
        classification, issues = classify(p, content, all_stubs)
        stub.classification = classification
        stub.issues = issues
        entries.append(stub)

    # Cross-ref analysis
    cross_refs: dict[str, list[str]] = {name: [] for name, _ in CANONICAL_RULES}
    for p, ftype, content in raw:
        for rule_name, pattern in CANONICAL_RULES:
            if re.search(pattern, content, re.IGNORECASE):
                cross_refs[rule_name].append(ftype)

    # Totals
    counts: dict[str, int] = {
        "canonical": 0, "duplicate": 0, "bloat": 0,
        "stale": 0, "conflicting": 0, "unknown": 0,
    }
    for e in entries:
        counts[e.classification] = counts.get(e.classification, 0) + 1

    # Notes
    notes = [
        f"Found {len(entries)} instruction files across {len(roots)} roots",
        f"Counts: {json.dumps(counts)}",
        f"Cross-ref rule distribution: { {k: len(set(v)) for k, v in cross_refs.items()} }",
        "Classification order: conflicting > stale > bloat > duplicate > canonical > unknown",
    ]

    return AuditReport(
        schema_version=1,
        generated_at=datetime.now(tz=timezone.utc).isoformat(),
        scope=" + ".join(str(r) for r in roots),
        totals={"files": len(entries), **counts},
        files=entries,
        cross_refs=cross_refs,
        notes=notes,
    )


# --- Output ------------------------------------------------------------------

def to_dict(report: AuditReport) -> dict:
    d = asdict(report)
    d["files"] = [asdict(f) for f in report.files]
    return d


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit instruction files")
    ap.add_argument("--output", "-o", default=None, help="Output JSON path")
    ap.add_argument("--scope", choices=["sandbox", "hermes", "both"], default="both")
    args = ap.parse_args()

    roots = []
    if args.scope in ("sandbox", "both"):
        roots.append(Path("C:/Users/Alexa/Desktop/SandBox"))
    if args.scope in ("hermes", "both"):
        roots.append(Path("C:/Users/Alexa/AppData/Local/hermes"))

    report = audit(roots)
    data = to_dict(report)

    # Print to stdout
    print(json.dumps(data, indent=2))

    # Optionally write to file
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"\nWrote: {out}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
