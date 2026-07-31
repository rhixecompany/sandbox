#!/usr/bin/env python3
"""Phase 3: CHANGELOG — document every enhancement change from git history.

Reads git diff stat for the enhancement commits, plus the ENHANCEMENT_REPORT
summary, and writes CHANGELOG.json + CHANGELOG.md to .copilot/session-state/.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_DIR = REPO_ROOT / ".copilot" / "session-state"
ENH_COMMITS = ["228eae32", "e0ef0aa4", "15f6e32b"]


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True)
    return r.stdout.strip()


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # File-level change stats across the enhancement commits (prompts only)
    stat_lines = git("diff", "--numstat", "04f216e9..228eae32", "--", ".github/prompts/").splitlines()
    entries = []
    for line in stat_lines:
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        if path == "-" or added == "-":
            continue
        entries.append({
            "file": path,
            "additions": int(added),
            "deletions": int(deleted),
            "change_type": "modify",
        })

    total_add = sum(e["additions"] for e in entries)
    total_del = sum(e["deletions"] for e in entries)

    changelog = {
        "generated": ts,
        "campaign": "Prompt Library Heading-Glue Repair + DRY Enhancement (2026-07-27 → 2026-07-31)",
        "commits": [
            {"sha": "228eae32", "subject": "fix(prompts): repair heading-glue corruption across prompt library"},
            {"sha": "15f6e32b", "subject": "chore(projects): bump 13 submodule gitlinks"},
            {"sha": "e0ef0aa4", "subject": "chore(projects): bump comicwise gitlink (formatting follow-up)"},
        ],
        "summary": {
            "files_changed": len(entries),
            "additions": total_add,
            "deletions": total_del,
        },
        "passes": [
            {"pass": 1, "script": "fix_glued_headings.py", "fixes": 256 + 48, "files": 121 + 28},
            {"pass": 2, "script": "fix_residual_glue.py", "fixes": 746 + 40, "files": 152 + 27},
            {"pass": 3, "script": "fix_tail_glue.py", "fixes": 64, "files": 37},
            {"pass": 4, "script": "fix_tail_glue2.py", "fixes": 297, "files": 107},
            {"pass": 5, "script": "normalize_lf.py", "fixes": "584 files -> LF", "files": 584},
            {"pass": 6, "script": "fix_fence_lang.py", "fixes": 8, "files": 5},
            {"pass": 7, "script": "fix_collapsed_bullets.py", "fixes": 3, "files": 2},
            {"pass": 8, "script": "fix_tail_manual.py + fix_tail_generic.py", "fixes": 25 + 48, "files": 17 + 17},
        ],
        "special_repairs": [
            "pl.prompt.md — full rebuild (stub description, collapsed template, broken fences, embedded duplicate removed)",
            "create-oo-component-documentation.prompt.md — collapsed template region restored from git history (879b4532)",
            "structured-autonomy-plan.prompt.md — camelCase + sentence glue split",
            "bigquery-pipeline-audit, postgresql-code-review, power-bi-* — orphan >/>> markers stripped",
        ],
        "changes": entries,
    }

    (OUT_DIR / "CHANGELOG.json").write_text(json.dumps(changelog, indent=2), encoding="utf-8")

    md = f"""# Prompt Library Enhancement CHANGELOG

> Generated: {ts}

## Campaign

**Prompt Library Heading-Glue Repair + DRY Enhancement** (2026-07-27 → 2026-07-31)

### Commits

| SHA | Subject |
|-----|---------|
| `228eae32` | fix(prompts): repair heading-glue corruption across prompt library |
| `15f6e32b` | chore(projects): bump 13 submodule gitlinks |
| `e0ef0aa4` | chore(projects): bump comicwise gitlink (formatting follow-up) |

### Totals

- **Files changed:** {len(entries)}
- **Additions:** {total_add}
- **Deletions:** {total_del}

## Fix Passes

| Pass | Script | Fixes | Files |
|------|--------|-------|-------|
"""
    for p in changelog["passes"]:
        md += f"| {p['pass']} | `{p['script']}` | {p['fixes']} | {p['files']} |\n"

    md += "\n## Special Repairs\n\n"
    for s in changelog["special_repairs"]:
        md += f"- {s}\n"

    md += f"\n## Per-File Changes ({len(entries)} files)\n\n| File | + | − |\n|------|---|---|\n"
    for e in sorted(entries, key=lambda x: -x["additions"])[:200]:
        md += f"| `{e['file']}` | {e['additions']} | {e['deletions']} |\n"
    if len(entries) > 200:
        md += f"\n_... and {len(entries) - 200} more (full list in CHANGELOG.json)_\n"

    (OUT_DIR / "CHANGELOG.md").write_text(md, encoding="utf-8")

    print(json.dumps({"files_changed": len(entries), "additions": total_add, "deletions": total_del,
                      "changelog_json": (OUT_DIR / "CHANGELOG.json").stat().st_size,
                      "changelog_md": (OUT_DIR / "CHANGELOG.md").stat().st_size}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
