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
    git_snapshot,
    json_get,
    load_model_config,
    log_debug,
    log_error,
    log_info,
    normalize_event,
    now_iso,
    platform_snapshot,
    read_payload,
    resolve_profile,
    resolve_user,
    skip_context,
    write_jsonl,
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


def _resolve_start_ctx(payload: dict) -> dict:
    """Merge wire payload + resolved environment/identity into one context dict.

    The runtime's on_session_start stdin is:
        {"hook_event_name":"on_session_start","session_id":"...","cwd":"...",
         "extra":{"model":"...","platform":"..."}}
    User/profile/model are never top-level fields — resolve them locally.
    """
    working_dir = json_get(payload, "cwd") or json_get(payload, "working_dir") or ""
    model_cfg = load_model_config()
    model = json_get(payload, "extra.model") or json_get(payload, "model") or model_cfg["model"]
    platform = json_get(payload, "extra.platform") or json_get(payload, "platform") or ""
    snapshot = platform_snapshot()
    return {
        "session_id": json_get(payload, "session_id", "unknown"),
        "profile": json_get(payload, "profile", "") or resolve_profile(),
        "user": json_get(payload, "user", "") or resolve_user(),
        "model": model,
        "provider": json_get(payload, "extra.provider") or json_get(payload, "provider") or model_cfg["provider"],
        "platform": platform,
        "working_dir": working_dir,
        "hostname": snapshot["hostname"],
        "os": snapshot["os"],
        "python": snapshot["python"],
        "command": json_get(payload, "command", ""),
    }


async def handle_on_session_start(payload: dict) -> None:
    ctx = _resolve_start_ctx(payload)
    timestamp = json_get(payload, "timestamp", now_iso())

    record: dict = {
        "event": "session_start",
        "session_id": ctx["session_id"],
        "timestamp": timestamp,
        "profile": ctx["profile"],
        "user": ctx["user"],
        "model": ctx["model"],
        "provider": ctx["provider"],
        "platform": ctx["platform"],
        "working_dir": ctx["working_dir"],
        "hostname": ctx["hostname"],
        "os": ctx["os"],
        "python": ctx["python"],
        "command": ctx["command"],
    }

    if ctx["working_dir"]:
        try:
            record.update(await git_snapshot(ctx["working_dir"]))
        except Exception as exc:
            log_debug(f"session-logger: git snapshot skipped: {exc}")

    log_file = _LOG_DIR / f"{ctx['session_id']}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(ctx["session_id"], record)
        log_info(f"Session start captured: {ctx['session_id']} ({ctx['model']}@{ctx['provider']})")
    except FileNotFoundError:
        record.setdefault("diagnostics", []).append(f"missing_log_file:{log_file}")
        log_error(f"Session start failed for {ctx['session_id']}: missing log file at {log_file}")


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
    model_cfg = load_model_config()
    model = json_get(payload, "extra.model") or json_get(payload, "model") or model_cfg["model"]
    provider = json_get(payload, "extra.provider") or json_get(payload, "provider") or model_cfg["provider"]
    platform = json_get(payload, "extra.platform") or json_get(payload, "platform") or ""
    user_message = json_get(payload, "extra.user_message") or ""
    working_dir = json_get(payload, "cwd") or json_get(payload, "working_dir") or ""
    event_type = json_get(payload, "event", "pre_llm_call")
    is_first_turn = str(json_get(payload, "extra.is_first_turn", "false")).lower() in ("1", "true", "yes")
    summary = (user_message[:220] + "…") if len(user_message) > 220 else user_message

    record: dict = {
        "event": event_type,
        "session_id": session_id,
        "timestamp": timestamp,
        "model": model,
        "provider": provider,
        "platform": platform,
        "working_dir": working_dir,
        "prompt_length": len(user_message),
        "prompt_summary": summary,
        "is_first_turn": is_first_turn,
    }

    log_file = _LOG_DIR / f"{session_id}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(session_id, record)
        log_info(f"LLM call captured: {session_id} -> {model} ({len(user_message)} chars)")
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
    # Hermes serializes the event as hook_event_name; accept both spellings.
    if not payload.get("event"):
        payload["event"] = payload.get("hook_event_name", "")
    raw_event = payload.get("event", "")
    event = normalize_event(raw_event)

    log_debug(
        f"session-logger event={raw_event!r} normalized={event} session_id={json_get(payload, 'session_id', 'unknown')}"
    )
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
