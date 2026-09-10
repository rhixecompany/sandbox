#!/usr/bin/env python3
"""Inventory default-profile Hermes sessions for a fixed WAT date window.

Why: session_search is authoritative for conversation recall, while this script
provides a reproducible on-disk metadata inventory without printing secrets.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

WAT = timezone(timedelta(hours=1))


def epoch(date_text: str) -> float:
    return datetime.strptime(date_text, "%Y-%m-%d").replace(tzinfo=WAT).timestamp()


def candidate_databases(hermes_home: Path) -> list[Path]:
    """Return only the current default profile database.

    Why: profile databases are isolated; scanning them would violate the
    requested default-profile session scope.
    """
    state_db = hermes_home / "state.db"
    return [state_db] if state_db.is_file() else []


def coerce_timestamp(value: Any) -> float | None:
    """Normalize SQLite numeric or ISO timestamps to epoch seconds."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        numeric = float(value)
        return numeric / 1000 if numeric > 10_000_000_000 else numeric
    text = str(value).strip()
    if not text:
        return None
    try:
        numeric = float(text)
        return numeric / 1000 if numeric > 10_000_000_000 else numeric
    except ValueError:
        pass
    normalized = text.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.timestamp()


def redact_excerpt(text: str, limit: int = 900) -> str:
    """Remove obvious credentials before persisting message evidence."""
    import re

    redacted = re.sub(r"(?i)(bearer\s+|sk-|tvly-|hch-|napi_)[A-Za-z0-9._:-]+", r"\1<REDACTED>", text)
    redacted = re.sub(r"(?i)(api[_ -]?key|token|password|secret)\s*[:=]\s*[^\s,;]+", r"\1=<REDACTED>", redacted)
    return " ".join(redacted.split())[:limit]


def evidence_for_sessions(conn: sqlite3.Connection, sessions: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Collect bounded, redacted goal/task evidence from default-profile messages."""
    if not sessions or "messages" not in {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}: 
        return {}
    columns = table_schema(conn, "messages")
    required = {"session_id", "role", "content"}
    if not required.issubset(columns):
        return {}
    selected = [c for c in ["session_id", "role", "content", "timestamp"] if c in columns]
    patterns = ("goal", "subgoal", "spec", "plan", "prompt", "phase", "task", "action", "run-all-goals")
    evidence: dict[str, list[dict[str, Any]]] = {str(s["session_id"]): [] for s in sessions}
    placeholders = ",".join("?" for _ in sessions)
    query = f'SELECT {", ".join(selected)} FROM messages WHERE session_id IN ({placeholders}) ORDER BY id'
    for row in conn.execute(query, [str(s["session_id"]) for s in sessions]):
        item = dict(zip(selected, row))
        content = str(item.get("content") or "")
        if not any(pattern in content.lower() for pattern in patterns):
            continue
        session_id = str(item["session_id"])
        bucket = evidence.setdefault(session_id, [])
        if len(bucket) >= 12:
            continue
        bucket.append({
            "role": item.get("role"),
            "timestamp": item.get("timestamp"),
            "excerpt": redact_excerpt(content),
        })
    return evidence


def table_schema(conn: sqlite3.Connection, table: str) -> list[str]:
    return [row[1] for row in conn.execute(f'PRAGMA table_info("{table}")')]


def find_session_rows(conn: sqlite3.Connection, table: str, columns: list[str], start: float, end: float) -> list[dict[str, Any]]:
    """Read session rows and filter timestamps in Python across schema versions."""
    if table == "sessions" and "id" in columns:
        id_column = "id"
    elif "session_id" in columns:
        id_column = "session_id"
    else:
        return []
    time_columns = [
        c for c in ("started_at", "created_at", "timestamp", "last_activity_at", "updated_at", "start_time")
        if c in columns
    ]
    if not time_columns:
        return []
    selected = [
        c for c in (
            id_column,
            "title",
            "source",
            "model",
            "provider",
            "profile_name",
            "started_at",
            "ended_at",
            "last_activity_at",
            "message_count",
            "tool_call_count",
            "cwd",
            "git_branch",
            "git_repo_root",
        )
        if c in columns
    ]
    try:
        raw_rows = conn.execute(f'SELECT {", ".join(selected)} FROM "{table}"').fetchall()
    except sqlite3.Error:
        return []
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        item = dict(zip(selected, raw))
        timestamp_value = None
        matched_time_column = None
        for time_column in time_columns:
            timestamp_value = coerce_timestamp(item.get(time_column))
            if timestamp_value is not None:
                matched_time_column = time_column
                break
        if timestamp_value is None or not (start <= timestamp_value < end):
            continue
        item["session_id"] = item.pop(id_column)
        item["matched_time_column"] = matched_time_column
        item["matched_epoch"] = timestamp_value
        rows.append(item)
    return rows


def inspect_database(path: Path, start: float, end: float) -> dict[str, Any]:
    result: dict[str, Any] = {"path": str(path), "tables": {}, "sessions": []}
    try:
        conn = sqlite3.connect(str(path), uri=False)
    except sqlite3.Error as exc:
        result["error"] = str(exc)
        return result
    try:
        try:
            tables = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        except sqlite3.Error as exc:
            result["error"] = str(exc)
            return result
        for table in tables:
            columns = table_schema(conn, table)
            result["tables"][table] = columns
            result["sessions"].extend(find_session_rows(conn, table, columns, start, end))
    finally:
        conn.close()
    return result


def dedupe_sessions(databases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for database in databases:
        for session in database.get("sessions", []):
            key = str(session.get("session_id", ""))
            if not key:
                continue
            session = dict(session)
            session["database"] = database["path"]
            unique.setdefault(key, session)
    return sorted(unique.values(), key=lambda item: (item.get("started_at") or item.get("created_at") or 0, item["session_id"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hermes-home", default="C:/Users/Alexa/AppData/Local/hermes")
    parser.add_argument("--start", default="2026-09-06")
    parser.add_argument("--end", default="2026-09-11", help="exclusive end date in WAT")
    parser.add_argument("--output", default=".hermes/plans/run-all-goals-five-day-session-corpus.json")
    args = parser.parse_args()

    home = Path(args.hermes_home)
    start = epoch(args.start)
    end = epoch(args.end)
    dbs = [inspect_database(path, start, end) for path in candidate_databases(home)]
    sessions = dedupe_sessions(dbs)
    if dbs and sessions:
        try:
            conn = sqlite3.connect(dbs[0]["path"])
            evidence = evidence_for_sessions(conn, sessions)
            conn.close()
            for session in sessions:
                session["evidence"] = evidence.get(str(session["session_id"]), [])
        except sqlite3.Error as exc:
            output_evidence_error = str(exc)
        else:
            output_evidence_error = None
    else:
        output_evidence_error = None
    output = {
        "window": {"start_wat": args.start, "end_wat_exclusive": args.end, "start_epoch": start, "end_epoch": end},
        "hermes_home": str(home),
        "databases": dbs,
        "sessions": sessions,
        "session_count": len(sessions),
        "evidence_error": output_evidence_error,
        "notes": [
            "Metadata inventory only; message content is recalled through session_search.",
            "Cron sessions are retained in the raw inventory and should be filtered only if the user excludes them.",
        ],
    }
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output_path), "databases": len(dbs), "sessions": len(sessions), "session_ids": [s["session_id"] for s in sessions]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
