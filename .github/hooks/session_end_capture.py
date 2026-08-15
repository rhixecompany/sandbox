#!/usr/bin/env python3
"""session_end_capture.py — full session-end capture for Hermes.

Runs at on_session_end (invoked by the session-logger hook after the
lifecycle record is written). Produces the *complete* end-of-session
artifact that session-audit-report consumes at the next session start:

1. Reads the authoritative session row + messages from state.db
   (the durable store; logs/sessions/*.jsonl are lifecycle-only and
   historically corrupt on this install).
2. Counts tools (messages.tool_name on role='tool' rows, supplemented by
   assistant tool_calls JSON), slash-invoked skills (user messages).
3. Captures the git changelog: commits since session start + uncommitted
   working-tree files at end time.
4. Captures error signals (finish_reason, effect_disposition, error tool
   names) and user prompt summaries.
5. Writes logs/sessions/<session_id>.end.json — one JSON artifact that
   generate_session_report.py can read deterministically instead of
   heuristically re-counting tools/skills from raw messages.
6. Mirrors a compact summary to MCP memory for cross-session recall.

The module is self-contained (no lib.py import) so it can be tested
standalone and fails soft: every subsystem degrades gracefully.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import sqlite3
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_HERMES_HOME = Path(
    os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes")
)
_LOG_DIR = _HERMES_HOME / "logs" / "sessions"
_DB_PATH = _HERMES_HOME / "state.db"

# Slash-token matcher: captures /skill-name style invocations. The trailing
# lookahead rejects anything followed by a word char, underscore, dot, or
# slash — killing Windows/MSYS path segments (/c/Users, /tmp/x, /foo.py,
# /generate_session_report.py) that get quoted inside user messages. Content
# is CR-normalized first because stored messages use CRLF line endings, which
# would otherwise truncate the last char of each match.
_SKILL_RE = re.compile(r"(?<!\w)/([A-Za-z][A-Za-z0-9-]+)(?![A-Za-z0-9_./])")
# Directory-ish tokens that appear in quoted paths and are never skills.
_SKILL_STOPLIST = {
    "desktop", "users", "usr", "user", "home", "tmp", "temp", "hooks",
    "scripts", "appdata", "local", "hermes", "sandbox", "github", "prompts",
    "plans", "dev", "devops", "sys", "system", "windows", "program", "files",
    "data", "logs", "sessions", "state", "db", "branch", "skill", "heredoc",
    "t3", "t4", "skills-debug", "c", "d", "e", "etc",
    "opt", "var", "bin", "lib", "src", "test", "tests", "node_modules",
    "venv", ".venv",
}
_PROMPT_SUMMARY_LIMIT = 220
_MAX_PROMPTS = 8


# ---------------------------------------------------------------- helpers

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def json_get(data: dict, key: str, default: str = "") -> str:
    """Dot-path getter (e.g. 'extra.model'); returns default on any miss."""
    cur: Any = data
    for part in key.split("."):
        if not isinstance(cur, dict):
            return default
        cur = cur.get(part)
        if cur is None:
            return default
    return cur if isinstance(cur, str) else str(cur) if isinstance(cur, (int, float)) else default


def _fmt_ts(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except (OverflowError, OSError, ValueError):
            return str(value)
    return str(value)


def _truncate(text: str, limit: int = _PROMPT_SUMMARY_LIMIT) -> str:
    text = (text or "").strip().replace("\r", " ").replace("\n", " ")
    if len(text) > limit:
        return text[:limit] + "…"
    return text


def run_git(cwd: str, args: list[str], timeout: int = 15) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return 1, ""


# ------------------------------------------------------------- db readers

def _connect_ro() -> Optional[sqlite3.Connection]:
    if not _DB_PATH.exists():
        return None
    try:
        return sqlite3.connect(f"file:{_DB_PATH}?mode=ro", uri=True, timeout=5)
    except (sqlite3.Error, OSError):
        return None


def load_session_row(con: sqlite3.Connection, session_id: str) -> dict:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        "SELECT id, title, source, user_id, model, started_at, ended_at, "
        "end_reason, message_count, tool_call_count, input_tokens, output_tokens, "
        "cwd, profile_name, git_branch, git_repo_root, api_call_count, "
        "estimated_cost_usd, display_name, last_activity_description "
        "FROM sessions WHERE id=?",
        (session_id,),
    )
    row = cur.fetchone()
    return dict(row) if row else {}


def count_tools(con: sqlite3.Connection, session_id: str) -> Counter:
    """Count tool invocations.

    Primary signal: messages.tool_name on role='tool' rows (one row per
    executed call, already how generate_session_report.py counts).
    Supplement: assistant tool_calls JSON names not already present
    (calls that never produced a result row).
    """
    tools: Counter = Counter()
    cur = con.cursor()
    cur.execute(
        "SELECT tool_name FROM messages WHERE session_id=? AND role='tool'",
        (session_id,),
    )
    for (name,) in cur.fetchall():
        if name:
            tools[str(name)] += 1
    cur.execute(
        "SELECT tool_calls FROM messages WHERE session_id=? AND role='assistant' "
        "AND tool_calls IS NOT NULL AND tool_calls != ''",
        (session_id,),
    )
    for (calls_json,) in cur.fetchall():
        try:
            calls = json.loads(calls_json)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(calls, list):
            continue
        for call in calls:
            if not isinstance(call, dict):
                continue
            fn = call.get("function") or {}
            name = fn.get("name") if isinstance(fn, dict) else None
            if name and name not in tools:
                tools[str(name)] += 1
    return tools


def count_skills(con: sqlite3.Connection, session_id: str) -> Counter:
    """Slash-invoked skills from user messages (e.g. /executing-plans)."""
    skills: Counter = Counter()
    cur = con.cursor()
    cur.execute(
        "SELECT content FROM messages WHERE session_id=? AND role='user' "
        "AND content IS NOT NULL",
        (session_id,),
    )
    for (content,) in cur.fetchall():
        for quoted in _SKILL_RE.findall(content.replace("\r", "")):
            if quoted.lower() not in _SKILL_STOPLIST:
                skills[quoted] += 1
    return skills


def capture_prompts(con: sqlite3.Connection, session_id: str) -> dict:
    """First user message (title-ish), count, and summaries."""
    cur = con.cursor()
    cur.execute(
        "SELECT content FROM messages WHERE session_id=? AND role='user' "
        "AND content IS NOT NULL ORDER BY id",
        (session_id,),
    )
    rows = [r[0] for r in cur.fetchall()]
    first = _truncate(rows[0]) if rows else ""
    summaries = [_truncate(r) for r in rows[:_MAX_PROMPTS]]
    return {
        "first_user_message": first,
        "user_turn_count": len(rows),
        "prompt_summaries": summaries,
    }


def capture_errors(con: sqlite3.Connection, session_id: str) -> dict:
    """Error signals from the message store (never fabricated)."""
    cur = con.cursor()
    cur.execute(
        "SELECT finish_reason, COUNT(*) FROM messages WHERE session_id=? "
        "AND role='assistant' AND finish_reason IS NOT NULL GROUP BY finish_reason",
        (session_id,),
    )
    finish_reasons = {str(r[0]): r[1] for r in cur.fetchall()}
    cur.execute(
        "SELECT tool_name, COUNT(*) FROM messages WHERE session_id=? AND role='tool' "
        "AND (effect_disposition IN ('error','failed') OR tool_name LIKE '%error%') "
        "GROUP BY tool_name",
        (session_id,),
    )
    error_tools = {str(r[0]): r[1] for r in cur.fetchall()}
    return {"finish_reasons": finish_reasons, "error_tools": error_tools}


# ------------------------------------------------------------- changelog

def capture_changelog(cwd: str, started_at: Any) -> list[dict]:
    """Files touched during the session.

    Committed files: git log --since=<session start> --name-only.
    Uncommitted files: git status --porcelain at end time.
    Both degrade to [] when cwd is not a repo. Actions stay factual:
    'committed' vs 'uncommitted' — no inference about content.
    """
    if not cwd or not Path(cwd).exists():
        return []
    start_iso = _fmt_ts(started_at) or ""
    changelog: list[dict] = []
    if start_iso:
        code, out = run_git(cwd, ["log", f"--since={start_iso}", "--name-only", "--format="])
        if code == 0:
            seen: set[str] = set()
            for line in out.splitlines():
                line = line.strip()
                if line and line not in seen:
                    seen.add(line)
                    changelog.append({"path": line, "action": "committed"})
    code, out = run_git(cwd, ["status", "--porcelain"])
    if code == 0:
        for line in out.splitlines():
            if len(line) < 4:
                continue
            path = line[3:].strip()
            if path:
                changelog.append({"path": path, "action": "uncommitted"})
    return changelog


# ------------------------------------------------------------- artifact

def _resolve_status(payload: dict) -> str:
    """Collapse the wire's end-state fields into a small status vocabulary,
    matching session-logger's resolve_end_status semantics so the lifecycle
    record and the end-capture artifact agree.
    """
    raw = (
        json_get(payload, "status")
        or json_get(payload, "extra.status")
        or json_get(payload, "extra.turn_exit_reason")
        or ""
    ).strip()
    lowered = raw.lower().replace("_", " ").replace("(", " ").replace(")", " ")
    if not lowered:
        if json_get(payload, "extra.failed", "0") not in ("", "0", "false"):
            return "failed"
        if json_get(payload, "extra.interrupted", "0") not in ("", "0", "false"):
            return "interrupted"
        if json_get(payload, "extra.completed", "0") not in ("", "0", "false"):
            return "completed"
        return "unknown"
    if "finish reason=stop" in lowered:
        return "completed"
    if "finish reason=length" in lowered:
        return "truncated"
    if lowered.startswith("text response") or lowered.startswith("tool call"):
        return "completed"
    if any(token in lowered for token in ("interrupt", "cancel", "abort")):
        return "interrupted"
    if any(token in lowered for token in ("error", "fail", "exception")):
        return "failed"
    for token in ("completed", "complete", "success", "succeeded"):
        if token in lowered:
            return "completed"
    return raw


def build_capture(session_id: str, payload: dict, end_iso: str) -> dict:
    con = _connect_ro()
    if con is None:
        return {"session_id": session_id, "capture_error": "state.db unavailable"}
    try:
        row = load_session_row(con, session_id)
        tools = count_tools(con, session_id)
        skills = count_skills(con, session_id)
        prompts = capture_prompts(con, session_id)
        errors = capture_errors(con, session_id)
    finally:
        con.close()

    cwd = json_get(payload, "cwd") or json_get(payload, "working_dir") or row.get("cwd", "")
    started_at = row.get("started_at")
    ended_at = row.get("ended_at")
    changelog = capture_changelog(cwd, started_at)

    status = _resolve_status(payload)
    
    # Compute duration from session row timestamps (epoch floats)
    duration_seconds = None
    if started_at is not None and ended_at is not None:
        try:
            duration_seconds = int(float(ended_at) - float(started_at))
        except (ValueError, TypeError):
            pass
    
    # Compute turns from message count / 2 (rough estimate: user+assistant pairs)
    turns = None
    msg_count = row.get("message_count")
    if msg_count is not None and isinstance(msg_count, int):
        turns = max(1, msg_count // 2)

    return {
        "event": "session_end_capture",
        "session_id": session_id,
        "captured_at": end_iso,
        "status": status,
        "duration_seconds": duration_seconds,
        "turns": turns,
        "session": {
            "title": row.get("title") or prompts["first_user_message"] or "",
            "source": row.get("source", ""),
            "user_id": row.get("user_id", ""),
            "model": row.get("model", ""),
            "started_at": _fmt_ts(started_at),
            "ended_at": _fmt_ts(ended_at) or end_iso,
            "end_reason": row.get("end_reason", ""),
            "message_count": row.get("message_count"),
            "tool_call_count": row.get("tool_call_count"),
            "api_call_count": row.get("api_call_count"),
            "input_tokens": row.get("input_tokens"),
            "output_tokens": row.get("output_tokens"),
            "estimated_cost_usd": row.get("estimated_cost_usd"),
            "cwd": cwd,
            "profile_name": row.get("profile_name", ""),
            "git_branch": row.get("git_branch", ""),
            "git_repo_root": row.get("git_repo_root", ""),
            "display_name": row.get("display_name", ""),
            "last_activity_description": row.get("last_activity_description", ""),
        },
        "tools": dict(tools.most_common()),
        "skills": dict(skills.most_common()),
        "prompts": prompts,
        "errors": errors,
        "changelog": changelog,
    }


def write_capture(capture: dict) -> Optional[Path]:
    try:
        _LOG_DIR.mkdir(parents=True, exist_ok=True)
    except OSError:
        return None
    out = _LOG_DIR / f"{capture['session_id']}.end.json"
    try:
        out.write_text(json.dumps(capture, indent=2, ensure_ascii=False), encoding="utf-8")
        return out
    except OSError:
        return None


# ------------------------------------------------------------- memory

async def mirror_memory(capture: dict) -> None:
    """Compact mirror to MCP memory (best-effort, never fatal)."""
    try:
        from hermes_tools import memory as _mcp_memory  # type: ignore[import-untyped]
    except Exception:
        return
    try:
        sid = capture["session_id"]
        tools_n = len(capture.get("tools", {}))
        skills_n = len(capture.get("skills", {}))
        files_n = len(capture.get("changelog", []))
        await asyncio.to_thread(
            _mcp_memory,
            observations=[
                {
                    "entityName": sid,
                    "contents": [
                        "event=session_end_capture",
                        f"title={capture['session']['title']}",
                        f"model={capture['session']['model']}",
                        f"status={capture.get('status', 'unknown')}",
                        f"tools={tools_n} kinds",
                        f"skills={skills_n} slash-invocations",
                        f"files_changed={files_n}",
                        f"captured_at={capture['captured_at']}",
                    ],
                }
            ],
        )
    except Exception:
        pass


# ------------------------------------------------------------- entry

def run_capture(session_id: str, payload: dict | None = None, end_iso: str = "") -> dict:
    """Synchronous entrypoint used by the session-logger hook.

    Never raises: returns the capture dict on success, or a minimal
    diagnostic dict on failure so the hook pipeline stays green.
    """
    payload = payload or {}
    end_iso = end_iso or now_iso()
    try:
        capture = build_capture(session_id, payload, end_iso)
        out = write_capture(capture)
        if out:
            capture["artifact"] = str(out)
        return capture
    except Exception as exc:  # noqa: BLE001 - hook must never crash the session
        return {
            "event": "session_end_capture",
            "session_id": session_id,
            "captured_at": end_iso,
            "capture_error": str(exc),
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Capture a session's end state to .end.json")
    parser.add_argument("--session-id", required=True, help="Session ID to capture")
    parser.add_argument("--end-iso", default="", help="End timestamp ISO (default: now)")
    args = parser.parse_args()
    result = run_capture(args.session_id, {}, args.end_iso)
    print(json.dumps(result, indent=2, ensure_ascii=False))
