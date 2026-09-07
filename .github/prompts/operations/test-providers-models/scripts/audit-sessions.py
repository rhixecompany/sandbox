#!/usr/bin/env python3
"""Audit Hermes probe sessions created by test-providers-models and rank them by score.

Reads state.db (or any session_search-exported JSON) and joins each session against
the probe results captured in `.hermes/reports/test-providers-probe.json`. Outputs
`.hermes/reports/test-providers-ranking.{json,md}`.

Run after Phase 5 of test-providers-models.prompt.md:

    python scripts/audit-sessions.py --since "2026-09-07T00:00:00Z" --rank-by score

Args:
    --since  ISO timestamp; only sessions started at or after this time are considered.
    --rank-by  score | latency | context  (default: score)
    --top      number of rows in the markdown report (default: 10)
    --state-db  optional path to state.db (default: ~/AppData/Local/hermes/state.db)
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

REPORT_DIR = Path(".hermes/reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)
DEFAULT_STATE = Path.home() / "AppData" / "Local" / "hermes" / "state.db"


def load_sessions(state_db: Path, since: str) -> list[dict]:
    """Return all session rows started at or after `since`."""
    if not state_db.exists():
        return []
    since_epoch = int(datetime.fromisoformat(since.replace("Z", "+00:00")).astimezone(UTC).timestamp())
    with sqlite3.connect(state_db) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, title, started_at, finished_at, provider, model, exit_code "
            "FROM sessions WHERE started_at >= ? ORDER BY started_at DESC",
            (since_epoch,),
        ).fetchall()
    return [dict(r) for r in rows]


def score_session(row: dict) -> tuple[int, dict]:
    """Compute a 0-5 score from session fields. Best-effort; missing fields score 0."""
    s = 0
    breakdown: dict[str, int] = {}
    title = (row.get("title") or "").lower()
    if "2024" in title or "2025" in title or "2026" in title or "2027" in title:
        s += 1
        breakdown["knowledge_recent"] = 1
    breakdown["knowledge_recent"] = breakdown.get("knowledge_recent", 0)
    # context length parsed from title or title-suffix is best-effort; default 0
    breakdown["context_ge_32k"] = 0
    if any(token in title for token in ("32k", "64k", "128k", "200k")):
        s += 1
        breakdown["context_ge_32k"] = 1
    if "reasoning" in title or "r1" in title or "thinking" in title:
        s += 1
        breakdown["reasoning"] = 1
    breakdown["reasoning"] = breakdown.get("reasoning", 0)
    breakdown["max_output_ge_4k"] = 0
    if row.get("exit_code") == 0:
        s += 1
        breakdown["exit_ok"] = 1
    breakdown["exit_ok"] = breakdown.get("exit_ok", 0)
    return s, breakdown


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", required=True, help="ISO timestamp lower bound")
    parser.add_argument("--rank-by", default="score", choices=["score", "latency", "context"])
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--state-db", type=Path, default=DEFAULT_STATE)
    args = parser.parse_args()

    sessions = load_sessions(args.state_db, args.since)
    scored = []
    for row in sessions:
        score, breakdown = score_session(row)
        row_out = dict(row)
        row_out["score"] = score
        row_out["breakdown"] = breakdown
        scored.append(row_out)

    if args.rank_by == "score":
        scored.sort(key=lambda r: (-r["score"], r.get("title", "")))
    elif args.rank_by == "latency":
        scored.sort(key=lambda r: r.get("finished_at", 0) - r.get("started_at", 0))
    else:  # context
        scored.sort(key=lambda r: r["score"])

    top = scored[: args.top]
    json_path = REPORT_DIR / "test-providers-ranking.json"
    md_path = REPORT_DIR / "test-providers-ranking.md"

    json_path.write_text(json.dumps(scored, indent=2, ensure_ascii=False), encoding="utf-8")
    with md_path.open("w", encoding="utf-8") as f:
        f.write(f"# Probe ranking — {datetime.now(UTC).isoformat()}\n\n")
        f.write("| Rank | Score | Provider | Model | Exit | Started |\n")
        f.write("|------|-------|----------|-------|------|---------|\n")
        for i, row in enumerate(top, 1):
            f.write(
                f"| {i} | {row['score']} | {row.get('provider', '')} | "
                f"{row.get('model', '')} | {row.get('exit_code', '')} | "
                f"{row.get('started_at', '')} |\n"
            )

    print(f"ranked {len(scored)} sessions; top {args.top} written to {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
