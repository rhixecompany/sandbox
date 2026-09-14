#!/usr/bin/env python3
"""session_start_capture.py — full session-start capture for Hermes.

Runs at on_session_start (invoked by the session-logger hook after the
lifecycle record is written). Produces the *start-of-session* artifact that
complements session_end_capture.py:

1. Reads the authoritative session row from state.db (the runtime creates
   the row before firing the hook; every field degrades if it is missing).
2. Captures the git baseline of the working directory: branch, HEAD sha,
   repo root, and the dirty-file list *at start time*. This is the diff
   anchor the end capture's changelog is measured against.
3. Captures the environment snapshot: profile, user, model, provider,
   platform, hostname, OS, python runtime, working dir, command, Hermes
   home, and hook version.
4. Writes logs/sessions/<session_id>.start.json — one JSON artifact that
   generate_session_report.py can read deterministically to report where
   the previous session started from (branch/commit/dirty state) instead
   of only where it ended.
5. Mirrors a compact summary to MCP memory for cross-session recall.

The module is self-contained (no lib.py import) so it can be tested
standalone and fails soft: every subsystem degrades gracefully and the
hook pipeline stays green.
"""

from __future__ import annotations

import asyncio
import json
import os
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

_HERMES_HOME = Path(
    os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes")
)
_LOG_DIR = _HERMES_HOME / "logs" / "sessions"
_DB_PATH = _HERMES_HOME / "state.db"
_HOOK_VERSION = "1.5.0"
_MAX_DIRTY_FILES = 30


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


def run_git(cwd: str, args: list[str], timeout: int = 10) -> tuple[int, str]:
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


# -------------------------------------------------------------- baseline

def capture_git_baseline(cwd: str) -> dict:
    """Git state of the working dir at session start.

    The dirty-file list is the diff anchor for the end capture's changelog:
    files already dirty before the session are excluded from 'changed during
    session' analysis. Every field degrades to ''/0/[] when cwd is not a repo.
    """
    if not cwd or not Path(cwd).exists():
        return {
            "branch": "",
            "sha": "",
            "sha_full": "",
            "repo_root": "",
            "dirty_count": 0,
            "dirty_files": [],
        }
    code, branch = run_git(cwd, ["branch", "--show-current"])
    code2, sha_short = run_git(cwd, ["rev-parse", "--short", "HEAD"])
    code3, sha_full = run_git(cwd, ["rev-parse", "HEAD"])
    code4, root = run_git(cwd, ["rev-parse", "--show-toplevel"])
    code5, status = run_git(cwd, ["status", "--porcelain"])
    dirty_lines = [
        line.strip()
        for line in status.splitlines()
        if line.strip() and len(line) >= 4
    ] if code5 == 0 else []
    return {
        "branch": branch.strip() if code == 0 and branch.strip() else "",
        "sha": sha_short.strip() if code2 == 0 and sha_short.strip() else "",
        "sha_full": sha_full.strip() if code3 == 0 and sha_full.strip() else "",
        "repo_root": root.strip() if code4 == 0 and root.strip() else "",
        "dirty_count": len(dirty_lines),
        "dirty_files": dirty_lines[:_MAX_DIRTY_FILES],
    }


def capture_environment(payload: dict, row: dict, start_iso: str) -> dict:
    """Environment snapshot merged from wire payload + config + host.

    The runtime's on_session_start stdin carries only session_id, cwd, and
    extra.{model,platform} — profile/user/provider are resolved locally, the
    same way hook.py's handle_on_session_start resolves them, so the artifact
    and the lifecycle record always agree.
    """
    model_cfg = {"model": "unknown", "provider": "unknown"}
    try:
        import yaml as _yaml  # type: ignore[import-untyped]

        cfg = _yaml.safe_load((_HERMES_HOME / "config.yaml").read_text(encoding="utf-8"))
        model = cfg.get("model") or {}
        model_cfg = {
            "model": str(model.get("default") or "unknown"),
            "provider": str(model.get("provider") or "unknown"),
        }
    except Exception:
        pass

    def _profile() -> str:
        for key in ("HERMES_PROFILE", "HERMES_PROFILE_NAME", "PROFILE_NAME"):
            if os.environ.get(key):
                return os.environ[key]
        try:
            import yaml as _yaml  # type: ignore[import-untyped]

            cfg = _yaml.safe_load((_HERMES_HOME / "config.yaml").read_text(encoding="utf-8"))
            if isinstance(cfg, dict):
                for probe in ("active_profile", "profile", "profiles"):
                    val = cfg.get(probe)
                    if isinstance(val, str) and val:
                        return val
        except Exception:
            pass
        return "default"

    def _user() -> str:
        for key in ("USERNAME", "USER", "LOGNAME"):
            if os.environ.get(key):
                return os.environ[key]
        try:
            import getpass

            return getpass.getuser()
        except Exception:
            return "unknown"

    try:
        import platform as _platform
        hostname = _platform.node() or "unknown"
        os_name = f"{_platform.system()} {_platform.release()}".strip() or "unknown"
        python_ver = _platform.python_version() or "unknown"
    except Exception:
        hostname, os_name, python_ver = "unknown", "unknown", "unknown"

    cwd = json_get(payload, "cwd") or json_get(payload, "working_dir") or row.get("cwd", "")
    return {
        "session_id": json_get(payload, "session_id", "unknown"),
        "started_at": start_iso,
        "profile": json_get(payload, "profile", "") or _profile(),
        "user": json_get(payload, "user", "") or _user(),
        "model": json_get(payload, "extra.model") or json_get(payload, "model") or model_cfg["model"],
        "provider": json_get(payload, "extra.provider") or json_get(payload, "provider") or model_cfg["provider"],
        "platform": json_get(payload, "extra.platform") or json_get(payload, "platform") or "",
        "hostname": hostname,
        "os": os_name,
        "python": python_ver,
        "working_dir": cwd,
        "command": json_get(payload, "command", ""),
        "hermes_home": str(_HERMES_HOME),
        "hook_version": _HOOK_VERSION,
    }


# ------------------------------------------------------------- artifact

def build_capture(session_id: str, payload: dict, start_iso: str) -> dict:
    con = _connect_ro()
    row: dict = {}
    if con is not None:
        try:
            row = load_session_row(con, session_id)
        finally:
            con.close()

    cwd = json_get(payload, "cwd") or json_get(payload, "working_dir") or row.get("cwd", "")
    git = capture_git_baseline(cwd)
    env = capture_environment(payload, row, start_iso)

    return {
        "event": "session_start_capture",
        "session_id": session_id,
        "captured_at": start_iso,
        "session": {
            "title": row.get("title") or "",
            "source": row.get("source") or env["platform"],
            "user_id": row.get("user_id", ""),
            "model": row.get("model") or env["model"],
            "started_at": _fmt_ts(row.get("started_at")) or start_iso,
            "ended_at": _fmt_ts(row.get("ended_at")),
            "message_count": row.get("message_count"),
            "tool_call_count": row.get("tool_call_count"),
            "api_call_count": row.get("api_call_count"),
            "input_tokens": row.get("input_tokens"),
            "output_tokens": row.get("output_tokens"),
            "estimated_cost_usd": row.get("estimated_cost_usd"),
            "cwd": cwd,
            "profile_name": row.get("profile_name") or env["profile"],
            "git_branch": row.get("git_branch") or git["branch"],
            "git_repo_root": row.get("git_repo_root") or git["repo_root"],
        },
        "git_baseline": git,
        "environment": env,
    }


def write_capture(capture: dict) -> Optional[Path]:
    try:
        _LOG_DIR.mkdir(parents=True, exist_ok=True)
    except OSError:
        return None
    out = _LOG_DIR / f"{capture['session_id']}.start.json"
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
        git = capture.get("git_baseline", {})
        env = capture.get("environment", {})
        await asyncio.to_thread(
            _mcp_memory,
            observations=[
                {
                    "entityName": sid,
                    "contents": [
                        "event=session_start_capture",
                        f"title={capture['session']['title']}",
                        f"model={capture['session']['model']}",
                        f"branch={git.get('branch') or ''}",
                        f"sha={git.get('sha') or ''}",
                        f"dirty={git.get('dirty_count', 0)}",
                        f"profile={env.get('profile') or ''}",
                        f"captured_at={capture['captured_at']}",
                    ],
                }
            ],
        )
    except Exception:
        pass


# ------------------------------------------------------------- entry

def run_capture(session_id: str, payload: dict | None = None, start_iso: str = "") -> dict:
    """Synchronous entrypoint used by the session-logger hook.

    Never raises: returns the capture dict on success, or a minimal
    diagnostic dict on failure so the hook pipeline stays green.
    """
    payload = payload or {}
    start_iso = start_iso or now_iso()
    try:
        capture = build_capture(session_id, payload, start_iso)
        out = write_capture(capture)
        if out:
            capture["artifact"] = str(out)
        return capture
    except Exception as exc:  # noqa: BLE001 - hook must never crash the session
        return {
            "event": "session_start_capture",
            "session_id": session_id,
            "captured_at": start_iso,
            "capture_error": str(exc),
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Capture a session's start state to .start.json")
    parser.add_argument("--session-id", required=True, help="Session ID to capture")
    parser.add_argument("--start-iso", default="", help="Start timestamp ISO (default: now)")
    args = parser.parse_args()
    result = run_capture(args.session_id, {}, args.start_iso)
    print(json.dumps(result, indent=2, ensure_ascii=False))
