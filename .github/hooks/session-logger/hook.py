#!/usr/bin/env python3
"""session-logger — async hook entrypoint.

Handles on_session_start, on_session_end, and pre_llm_call events.
Replaces legacy log-session-start.sh, log-session-end.sh, and log-prompt.sh.

Upgrade path:
- Primary durable store: Hermes logs JSONL under C:/Users/Alexa/AppData/Local/hermes/logs/sessions
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

from lib import (
    is_skipped,
    json_get,
    log_debug,
    log_error,
    log_info,
    now_iso,
    read_payload,
    skip_context,
    write_jsonl,
    normalize_event,
    read_jsonl,
)

_LOG_DIR = Path("C:/Users/Alexa/AppData/Local/hermes/logs/sessions")
_HOOK_PREFIX = "session-logger"
_HOOK_FALLBACK_NAME = "session_logger"
_MCP_MEMORY = None
try:
    from hermes_tools import memory as _mcp_memory  # type: ignore[import-untyped]

    _MCP_MEMORY = _mcp_memory
except Exception:
    _MCP_MEMORY = None


def _should_mirror() -> bool:
    return _MCP_MEMORY is not None


async def _memory_upsert_session(session_id: str, payload: dict) -> None:
    if not _should_mirror():
        return
    try:
        await asyncio.to_thread(
            _MCP_MEMORY,
            observations=[
                {
                    "entityName": session_id,
                    "contents": [
                        f"session_event={payload.get('event') or payload.get('event_type') or 'unknown'}",
                        f"profile={payload.get('profile', 'default')}",
                        f"model={payload.get('model', 'unknown')}",
                        f"provider={payload.get('provider', 'unknown')}",
                        f"working_dir={payload.get('working_dir', '')}",
                        f"status={payload.get('status', 'unknown')}",
                        f"timestamp={payload.get('timestamp', now_iso())}",
                    ],
                }
            ],
        )
    except Exception as exc:
        log_debug(f"session-logger: mcp memory mirror skipped: {exc}")


async def handle_on_session_start(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    profile = json_get(payload, "profile", "default")
    user = json_get(payload, "user", "unknown")
    model = json_get(payload, "model", "unknown")
    working_dir = json_get(payload, "working_dir", "")
    command = json_get(payload, "command", "")

    record: dict = {
        "event": "session_start",
        "session_id": session_id,
        "timestamp": timestamp,
        "profile": profile,
        "user": user,
        "model": model,
        "working_dir": working_dir,
        "command": command,
    }

    log_file = _LOG_DIR / f"{session_id}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(session_id, record)
        log_info(f"Session start logged: {session_id}")
    except FileNotFoundError:
        record.setdefault("diagnostics", []).append(f"missing_log_file:{log_file}")
        log_error(f"Session start failed for {session_id}: missing log file at {log_file}")


async def handle_on_session_end(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    duration_ms = json_get(payload, "duration_ms", "0")
    turns = json_get(payload, "turns", "0")
    tokens_in = json_get(payload, "tokens_in", "0")
    tokens_out = json_get(payload, "tokens_out", "0")
    status = json_get(payload, "status", "unknown")
    working_dir = json_get(payload, "working_dir", "")
    exit_code = json_get(payload, "exit_code", "")
    duration_seconds = json_get(payload, "duration_seconds", "")

    record: dict = {
        "event": "session_end",
        "session_id": session_id,
        "timestamp": timestamp,
        "duration_ms": int(duration_ms) if str(duration_ms).isdigit() else 0,
        "duration_seconds": int(duration_seconds) if str(duration_seconds).isdigit() else 0,
        "turns": int(turns) if str(turns).isdigit() else 0,
        "tokens_in": int(tokens_in) if str(tokens_in).isdigit() else 0,
        "tokens_out": int(tokens_out) if str(tokens_out).isdigit() else 0,
        "status": status,
        "working_dir": working_dir,
        "exit_code": int(exit_code) if str(exit_code).lstrip("-").isdigit() else 0,
    }

    log_file = _LOG_DIR / f"{session_id}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(session_id, record)
        log_info(f"Session end logged: {session_id} ({duration_ms}ms, {turns} turns)")
    except FileNotFoundError:
        record.setdefault("diagnostics", []).append(f"missing_log_file:{log_file}")
        log_error(f"Session end failed for {session_id}: missing log file at {log_file}")


async def handle_pre_llm_call(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    model = json_get(payload, "model", "unknown")
    provider = json_get(payload, "provider", "unknown")
    prompt_length = json_get(payload, "prompt_length", "0")
    system_prompt_length = json_get(payload, "system_prompt_length", "0")
    tools_count = json_get(payload, "tools_count", "0")
    event_type = json_get(payload, "event", "pre_llm_call")
    prompt_summary = json_get(payload, "prompt_summary", "")
    session_end = json_get(payload, "session_end", "")

    record: dict = {
        "event": event_type,
        "session_id": session_id,
        "timestamp": timestamp,
        "model": model,
        "provider": provider,
        "prompt_length": int(prompt_length) if str(prompt_length).isdigit() else 0,
        "system_prompt_length": int(system_prompt_length) if str(system_prompt_length).isdigit() else 0,
        "tools_count": int(tools_count) if str(tools_count).isdigit() else 0,
        "prompt_summary": prompt_summary,
        "session_end": session_end,
    }

    log_file = _LOG_DIR / f"{session_id}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(session_id, record)
        log_info(f"LLM call logged: {session_id} -> {model} ({prompt_length} chars)")
    except FileNotFoundError:
        record.setdefault("diagnostics", []).append(f"missing_log_file:{log_file}")
        log_error(f"LLM call logging failed for {session_id}: missing log file at {log_file}")


_EVENT_HANDLERS = {
    "on_session_start": handle_on_session_start,
    "on_session_end": handle_on_session_end,
    "pre_llm_call": handle_pre_llm_call,
}


async def main() -> None:
    ctx = skip_context(_HOOK_PREFIX, _HOOK_FALLBACK_NAME)
    if ctx["skip"]:
        log_info(f"Session logger skipped via {ctx['skip_var']}")
        record = {
            "event": "skipped",
            "hook": ctx["hook_name"],
            "skip_var": ctx["skip_var"],
            "timestamp": ctx["timestamp"],
        }
        await write_jsonl(_LOG_DIR / "skips.jsonl", record)
        sys.exit(0)

    payload = read_payload()
    raw_event = payload.get("event", "")
    event = normalize_event(raw_event)

    log_debug(f"session-logger event={raw_event!r} normalized={event} session_id={json_get(payload, 'session_id', 'unknown')}")
    handler = _EVENT_HANDLERS.get(event)
    if handler is None:
        log_error(f"Unknown event: {raw_event or '<unset>'}")
        record = {
            "event": "error",
            "hook": ctx["hook_name"],
            "error": "unknown_event",
            "raw_event": raw_event,
            "session_id": json_get(payload, "session_id", "unknown"),
            "timestamp": now_iso(),
        }
        await write_jsonl(_LOG_DIR / "errors.jsonl", record)
        sys.exit(1)

    await handler(payload)


if __name__ == "__main__":
    asyncio.run(main())
