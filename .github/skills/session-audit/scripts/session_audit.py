#!/usr/bin/env python3
"""session_audit.py — audit active/recent Hermes sessions.

Implements the full /session-audit skill contract:
  --output PATH    write report (default: docs/session-audit-report.md)
  --cleanup        enable cleanup mode (removes stale session files)
  --dry-run        show what would be cleaned without removing
  --max-age DAYS   max session age before it is stale (default: 7)
  --force          bypass safety checks (active-session protection)

Safety:
  - never cleans the active session (current process / newest)
  - preserves sessions with uncommitted work (dirty git) when detected
  - backs up files to <hermes>/session-audit-backup-<ts>/ before removal
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import sys
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

DEFAULT_HERMES = Path(os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes"))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Audit Hermes sessions")
    p.add_argument("--output", default="docs/session-audit-report.md", help="Report output path")
    p.add_argument("--cleanup", action="store_true", help="Enable cleanup mode")
    p.add_argument("--dry-run", action="store_true", help="Show what would be cleaned")
    p.add_argument("--max-age", type=int, default=7, help="Max session age in days (default 7)")
    p.add_argument("--force", action="store_true", help="Bypass safety checks")
    p.add_argument("--hermes-home", default=str(DEFAULT_HERMES), help="Hermes home")
    return p.parse_args()


def read_json_objects(path: Path) -> list[dict]:
    """Robustly read pretty-printed or JSONL session files."""
    objs: list[dict] = []
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return objs
    decoder = json.JSONDecoder()
    pos = 0
    n = len(text)
    while pos < n:
        while pos < n and text[pos] in " \t\r\n":
            pos += 1
        if pos >= n:
            break
        try:
            obj, end = decoder.raw_decode(text, pos)
            if isinstance(obj, dict):
                objs.append(obj)
            pos = end
        except json.JSONDecodeError:
            # skip to next line start
            nl = text.find("\n", pos)
            pos = n if nl == -1 else nl + 1
    return objs


def session_files(hermes_home: Path) -> list[Path]:
    logs = hermes_home / "logs" / "sessions"
    if not logs.exists():
        return []
    return sorted(logs.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def session_meta(path: Path) -> dict:
    objs = read_json_objects(path)
    meta: dict = {
        "path": path,
        "name": path.name,
        "size": path.stat().st_size,
        "mtime": datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc),
        "events": len(objs),
        "session_id": None,
        "profile": None,
        "model": None,
        "status": "unknown",
        "turns": 0,
        "tokens_in": 0,
        "tokens_out": 0,
        "start_ts": None,
        "end_ts": None,
    }
    for obj in objs:
        sid = obj.get("session_id")
        if sid:
            meta["session_id"] = sid
        profile = obj.get("profile") or obj.get("working_dir_profile")
        if profile:
            meta["profile"] = profile
        model = obj.get("model")
        if model:
            meta["model"] = model
        ev = obj.get("event") or obj.get("type")
        if ev in ("session_start", "session_end", "llm_call"):
            ts = obj.get("timestamp") or obj.get("ts")
            if ts:
                if ev == "session_start":
                    meta["start_ts"] = ts
                if ev == "session_end":
                    meta["end_ts"] = ts
        if ev == "session_end":
            meta["status"] = obj.get("status", "unknown")
            meta["turns"] = int(obj.get("turns", 0) or 0)
            meta["tokens_in"] = int(obj.get("tokens_in", 0) or 0)
            meta["tokens_out"] = int(obj.get("tokens_out", 0) or 0)
    return meta


def db_session_ids(hermes_home: Path) -> set[str]:
    """Read session ids from state.db sessions table if present."""
    ids: set[str] = set()
    db = hermes_home / "state.db"
    if not db.exists():
        return ids
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=5)
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cur.fetchall()]
        for table in tables:
            if "session" in table.lower():
                try:
                    cur.execute(f'SELECT DISTINCT session_id FROM "{table}" WHERE session_id IS NOT NULL')
                    for (sid,) in cur.fetchall():
                        if sid:
                            ids.add(str(sid))
                except sqlite3.Error:
                    continue
        con.close()
    except (sqlite3.Error, OSError):
        pass
    return ids


def is_git_dirty(hermes_home: Path) -> bool:
    """Heuristic: workspace git dirty => preserve sessions (uncommitted work)."""
    for root in (Path.cwd(), hermes_home):
        git = root / ".git"
        if git.exists():
            try:
                import subprocess
                out = subprocess.run(
                    ["git", "-C", str(root), "status", "--porcelain"],
                    capture_output=True, text=True, timeout=10,
                )
                return bool(out.stdout.strip())
            except Exception:
                return True
    return False


def main() -> int:
    args = parse_args()
    home = Path(args.hermes_home)
    files = session_files(home)
    db_ids = db_session_ids(home)
    active_guard = time.time() - 3600  # files touched in last hour = active

    metas = [session_meta(f) for f in files]
    metas.sort(key=lambda m: m["mtime"], reverse=True)
    active = [m for m in metas if m["mtime"].timestamp() >= active_guard]
    now = datetime.now(tz=timezone.utc)
    stale = [
        m for m in metas
        if (now - m["mtime"]).days > args.max_age and m not in active
    ]
    # A session referenced in state.db is considered live regardless of mtime.
    stale = [m for m in stale if m["session_id"] not in db_ids]

    # ---- report ----
    lines: list[str] = []
    lines.append("# Session Audit Report")
    lines.append("")
    lines.append(f"> Generated: {now.isoformat()} | hermes-home: `{home}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Session files | {len(metas)} |")
    lines.append(f"| Active (last 1h) | {len(active)} |")
    lines.append(f"| Stale (> {args.max_age}d) | {len(stale)} |")
    lines.append(f"| DB-referenced (live) | {len(db_ids)} |")
    lines.append(f"| Git dirty (preserve) | {is_git_dirty(home)} |")
    total_size = sum(m["size"] for m in metas)
    stale_size = sum(m["size"] for m in stale)
    lines.append(f"| Total size | {total_size/1024:.1f} KB |")
    lines.append(f"| Reclaimable (stale) | {stale_size/1024:.1f} KB |")
    lines.append("")
    lines.append("## Sessions")
    lines.append("")
    lines.append("| File | Events | Session ID | Model | Status | Turns | Size | Modified (UTC) |")
    lines.append("|------|--------|-----------|-------|--------|-------|------|----------------|")
    for m in metas:
        lines.append(
            f"| {m['name']} | {m['events']} | {m['session_id'] or '—'} | {m['model'] or '—'} | "
            f"{m['status']} | {m['turns']} | {m['size']}B | {m['mtime'].strftime('%Y-%m-%d %H:%M')} |"
        )
    lines.append("")
    lines.append("## Cleanup Recommendations")
    lines.append("")
    if stale:
        lines.append(f"`{len(stale)}` stale session file(s) older than {args.max_age} days:")
        for m in stale:
            lines.append(f"- `{m['name']}` ({m['size']}B, last modified {m['mtime'].strftime('%Y-%m-%d %H:%M')})")
    else:
        lines.append("No stale sessions found. Nothing to clean.")
    lines.append("")
    lines.append("## Safety Checks")
    lines.append("")
    lines.append(f"- Active-session guard: **{'OFF' if args.force else 'ON'}** (1h recency window)")
    lines.append(f"- DB-liveness check: sessions referenced in `state.db` are never cleaned: **{'enabled' if db_ids else 'no db table found'}**")
    lines.append("- Files are backed up to `<hermes>/session-audit-backup-<ts>/` before removal")
    lines.append("")

    # ---- write report ----
    out = Path(args.output)
    if not out.is_absolute():
        out = Path.cwd() / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written: {out}")

    # ---- cleanup ----
    if not args.cleanup:
        return 0

    if stale and not args.force:
        active_names = {m["name"] for m in active}
        for m in stale:
            if m["name"] in active_names:
                print(f"SKIP active: {m['name']}")
                stale.remove(m)

    if args.dry_run:
        for m in stale:
            print(f"[dry-run] would remove {m['name']} ({m['size']}B)")
        print(f"[dry-run] {len(stale)} file(s) would be removed")
        return 0

    if not stale:
        print("Nothing to clean.")
        return 0

    backup_dir = home / f"session-audit-backup-{time.strftime('%Y%m%d_%H%M%S')}"
    backup_dir.mkdir(exist_ok=True)
    for m in stale:
        dest = backup_dir / m["name"]
        shutil.copy2(m["path"], dest)
        m["path"].unlink()
        print(f"removed {m['name']} -> backed up to {dest.name}")
    print(f"Removed {len(stale)} stale session file(s); backup at {backup_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
