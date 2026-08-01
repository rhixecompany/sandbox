#!/usr/bin/env python3
"""session-auto-commit — async hook entrypoint.

Automatically commits session changes at on_session_end.
Replaces legacy auto-commit.sh for the deprecated session_end event.

Upgrade path:
- Primary durable store: Hermes logs JSONL under C:/Users/Alexa/AppData/Local/hermes/logs/hermes
- MCP mirror: optional write-through to mcp-memory for durable cross-session recall
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

_HOOK_DIR = Path(__file__).resolve().parent
_LIB_DIR = _HOOK_DIR.parent
if str(_LIB_DIR) not in sys.path:
    sys.path.insert(0, str(_LIB_DIR))

from lib import (  # noqa: E402  (sys.path bootstrap above is required)
    is_skipped,
    json_get,
    log_debug,
    log_error,
    log_info,
    now_iso,
    read_payload,
    run_git,
    skip_context,
    write_jsonl,
)

_HOOK_PREFIX = "session-auto-commit"
_HOOK_FALLBACK_NAME = "session_auto_commit"
_ERRORS_JSONL = Path("C:/Users/Alexa/AppData/Local/hermes/logs/hermes/session-auto-commit-errors.jsonl")
_SKIPS_JSONL = Path("C:/Users/Alexa/AppData/Local/hermes/logs/hermes/session-auto-commit-skips.jsonl")
_MCP_MEMORY = None
try:
    from hermes_tools import memory as _mcp_memory  # type: ignore[import-untyped]

    _MCP_MEMORY = _mcp_memory
except Exception:
    _MCP_MEMORY = None


def _should_mirror() -> bool:
    return _MCP_MEMORY is not None


async def _memory_upsert_auto_commit(session_id: str, payload: dict) -> None:
    if not _should_mirror():
        return
    try:
        await asyncio.to_thread(
            _MCP_MEMORY,
            observations=[
                {
                    "entityName": session_id,
                    "contents": [
                        "session_event=auto_commit",
                        f"profile={payload.get('profile', 'default')}",
                        f"working_dir={payload.get('working_dir', '')}",
                        f"status={payload.get('status', 'unknown')}",
                        f"timestamp={payload.get('timestamp', now_iso())}",
                    ],
                }
            ],
        )
    except Exception as exc:
        log_debug(f"session-auto-commit: mcp memory mirror skipped: {exc}")


async def _log_error_record(session_id: str, raw_event: str, message: str) -> None:
    await write_jsonl(
        _ERRORS_JSONL,
        {
            "event": "error",
            "session_id": session_id,
            "raw_event": raw_event,
            "error": message,
            "timestamp": now_iso(),
        },
    )


async def _log_skip(session_id: str, skip_var: str) -> None:
    await write_jsonl(
        _SKIPS_JSONL,
        {
            "event": "skipped",
            "session_id": session_id,
            "skip_var": skip_var,
            "timestamp": now_iso(),
        },
    )


async def _repo_root_for(cwd: Path | None) -> Path | None:
    candidates: list[tuple[Path | None, bool]] = [
        (cwd, True),
        (Path("C:/Users/Alexa/Desktop/SandBox"), False),
        (Path("C:/Users/Alexa/AppData/Local/hermes"), False),
    ]

    for path, required in candidates:
        if path is None:
            continue
        rc, out, _ = await run_git("rev-parse", "--show-toplevel", cwd=path)
        if rc == 0 and out.strip():
            return Path(out.strip())

        if required:
            git_dir = path / ".git"
            if git_dir.exists():
                return path

    return None


async def _auto_commit(session_id: str, repo_root: Path, payload: dict) -> None:
    timestamp = now_iso()
    commit_msg = f"chore(session): auto-commit session {session_id} at {timestamp}"

    rc, _, stderr = await run_git("add", "-A", cwd=repo_root)
    if rc != 0:
        raise RuntimeError(f"git add failed: {stderr}")

    rc, _, stderr = await run_git("commit", "-m", commit_msg, cwd=repo_root)
    if rc != 0:
        raise RuntimeError(f"git commit failed: {stderr}")

    log_info(f"Auto-committed session {session_id}: {commit_msg}")
    await _memory_upsert_auto_commit(session_id, payload)


async def handle_session_end(payload: dict) -> None:
    if is_skipped(_HOOK_PREFIX, _HOOK_FALLBACK_NAME):
        await _log_skip(
            json_get(payload, "session_id", "unknown"),
            f"SKIP_{_HOOK_FALLBACK_NAME.upper()}",
        )
        log_info("session-auto-commit skipped")
        return

    session_id = json_get(payload, "session_id", "unknown")
    working_dir = json_get(payload, "working_dir", "")
    raw_event = payload.get("event", "")

    repo_root = await _repo_root_for(Path(working_dir) if working_dir else None)
    if repo_root is None:
        log_info(f"No git repository found for session {session_id}; skipping auto-commit")
        await write_jsonl(
            _SKIPS_JSONL,
            {
                "event": "skipped",
                "session_id": session_id,
                "reason": "no_repo",
                "working_dir": working_dir,
                "timestamp": now_iso(),
            },
        )
        return

    rc, out, stderr = await run_git("status", "--porcelain", cwd=repo_root)
    if rc != 0:
        log_error(f"git status failed for {repo_root}: {stderr}")
        await _log_error_record(session_id, raw_event, f"git status failed: {stderr}")
        sys.exit(1)

    if not out.strip():
        log_info(f"No changes to commit for session {session_id}")
        return

    await _auto_commit(session_id, repo_root, payload)


async def main() -> None:
    ctx = skip_context(_HOOK_PREFIX, _HOOK_FALLBACK_NAME)
    if ctx["skip"]:
        await _log_skip("unknown", ctx["skip_var"])
        log_info(f"{_HOOK_FALLBACK_NAME} skipped via {ctx['skip_var']}")
        return

    payload = read_payload()
    raw_event = payload.get("event", "")

    if raw_event != "on_session_end":
        log_error(f"session-auto-commit: expected on_session_end, got {raw_event or '<unset>'}")
        await _log_error_record(
            json_get(payload, "session_id", "unknown"),
            raw_event,
            f"unexpected_event:{raw_event or '<unset>'}",
        )
        sys.exit(1)

    try:
        await handle_session_end(payload)
    except Exception as exc:
        log_error(str(exc))
        await _log_error_record(
            json_get(payload, "session_id", "unknown"),
            raw_event,
            str(exc),
        )
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
