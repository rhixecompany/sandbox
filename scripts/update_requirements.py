#!/usr/bin/env python3
"""Regenerate requirements.txt as union of installed packages + python-packages.md.

Sources (in priority order per package):
  1. `uv pip freeze --python .venv/Scripts/python.exe` (installed pins win)
  2. python-packages.md Unique Package Index rows (| Package | Versions | Used by | Cheat-Sheet |)
     - multi-version rows keep the highest semver
  3. python-packages.md per-repo tables (fallback when a package is not in the index)

Also prints which indexed cheat-sheet paths (research/packages/python/*.md) are missing.

Output: sorted, LF, one requirement per line. Idempotent.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VENV_PY = ROOT / ".venv" / "Scripts" / "python.exe"
MD_REPORT = ROOT / "python-packages.md"
OUT = ROOT / "requirements.txt"

ROW_RE = re.compile(r"^\|\s*`?([A-Za-z0-9_.-]+)`?\s*\|\s*([^|]+?)\s*\|")
INDEX_RE = re.compile(r"^\|\s*`?([A-Za-z0-9_.-]+)`?\s*\|\s*([^|]+?)\s*\|\s*[^|]+\|\s*`?([^|`]+)`?\s*\|")


def _semver_key(spec: str) -> tuple:
    m = re.search(r"(\d+)(?:\.(\d+))?(?:\.(\d+))?", spec)
    if not m:
        return (0, 0, 0)
    return tuple(int(g or 0) for g in m.groups())


def installed_packages() -> dict[str, str]:
    """Return {pkg(lower): requirement} from uv pip freeze (==/editable pins)."""
    cmd = ["uv", "pip", "freeze", "--python", str(VENV_PY)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except (subprocess.TimeoutExpired, OSError) as exc:
        print(f"warning: uv pip freeze failed ({exc}); installed set empty", file=sys.stderr)
        return {}
    if out.returncode != 0:
        print(f"warning: uv pip freeze exit {out.returncode}: {out.stderr.strip()}", file=sys.stderr)
        return {}
    result: dict[str, str] = {}
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, sep, _ = line.partition("==")
        if sep:
            result[name.strip().lower()] = line
        elif line.startswith("-e ") or line.startswith("--editable"):
            # keep editable installs verbatim (git/file paths)
            nm = line.rsplit("/", 1)[-1].strip()
            if nm:
                result[nm.lower()] = line
    return result


def index_packages() -> tuple[dict[str, str], list[str]]:
    """Return ({pkg(lower): requirement}, missing_cheat_sheet_paths) from the index."""
    if not MD_REPORT.exists():
        print(f"warning: missing {MD_REPORT}; index empty", file=sys.stderr)
        return {}, []
    lines = MD_REPORT.read_text(encoding="utf-8", errors="replace").splitlines()
    in_index = False
    index: dict[str, str] = {}
    missing: list[str] = []
    for line in lines:
        if line.startswith("## Unique Package Index"):
            in_index = True
            continue
        if not in_index or not line.startswith("|"):
            continue
        m = INDEX_RE.match(line)
        if not m:
            continue
        name = m.group(1).strip()
        versions = [v.strip().strip("`").strip(",") for v in m.group(2).split("`,")]
        versions = [v for v in versions if v and v.startswith(("==", ">=", "<=", "~=", ">", "<"))]
        if not versions:
            continue
        spec = max(versions, key=_semver_key)
        index[name.lower()] = f"{name}{spec}"
        sheet = m.group(3).strip().strip("`")
        if sheet and not (ROOT / sheet).exists():
            missing.append(sheet)
    return index, missing


def main() -> int:
    freeze = installed_packages()
    index, missing = index_packages()
    union = dict(index)
    union.update(freeze)  # installed pins win
    lines = sorted(union.values())
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"requirements.txt: {len(lines)} packages "
          f"(installed={len(freeze)}, md-index={len(index)}, "
          f"md-only={len(set(index) - set(freeze))})")
    if missing:
        print(f"missing cheat-sheets: {len(missing)}")
        for p in missing[:10]:
            print(f"  - {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())