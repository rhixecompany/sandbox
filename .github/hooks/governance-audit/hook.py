#!/usr/bin/env python3
"""governance-audit — async hook entrypoint.

Handles on_session_start, on_session_end, and pre_llm_call events for
governance and compliance auditing. Replaces legacy audit-session-start.sh,
audit-session-end.sh, and audit-prompt.sh.

Upgrade path:
- Primary durable store: Hermes logs JSONL under C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance
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
    json_get,
    log_debug,
    log_error,
    log_info,
    normalize_event,
    now_iso,
    read_payload,
    skip_context,
    write_jsonl,
)

_HOOK_PREFIX = "governance-audit"
_HOOK_FALLBACK_NAME = "governance_audit"
_CURRENT_LOG_DIR = Path("C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance")
_DEPRECATED_LOG_DIR = Path("C:/Users/Alexa/AppData/Local/hermes/logs/audit")
_ERRORS_JSONL = Path("C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance-audit-errors.jsonl")
_SKIPS_JSONL = Path("C:/Users/Alexa/AppData/Local/hermes/logs/hermes/governance-audit-skips.jsonl")
_MCP_MEMORY = None
try:
    from hermes_tools import memory as _mcp_memory  # type: ignore[import-untyped]

    _MCP_MEMORY = _mcp_memory
except Exception:
    _MCP_MEMORY = None


def _should_mirror() -> bool:
    return _MCP_MEMORY is not None


async def _memory_upsert_governance(session_id: str, payload: dict) -> None:
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
                        f"session_event_status={payload.get('status', 'unknown')}",
                        f"timestamp={payload.get('timestamp', now_iso())}",
                    ],
                }
            ],
        )
    except Exception as exc:
        log_debug(f"governance-audit: mcp memory mirror skipped: {exc}")


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


async def _ensure_log_file(path: Path) -> None:
    await asyncio.to_thread(path.parent.mkdir, parents=True, exist_ok=True)
    if not path.exists():
        await asyncio.to_thread(path.write_text, "", encoding="utf-8")


def _log_paths(session_id: str) -> tuple[Path, Path | None]:
    current = _CURRENT_LOG_DIR / f"{session_id}.jsonl"
    deprecated = _DEPRECATED_LOG_DIR / f"{session_id}.jsonl"
    return current, deprecated if deprecated.parent.exists() or session_id != "unknown" else None


async def handle_on_session_start(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    profile = json_get(payload, "profile", "default")
    user = json_get(payload, "user", "unknown")
    model = json_get(payload, "model", "unknown")

    record: dict = {
        "event": "session_start",
        "session_id": session_id,
        "timestamp": timestamp,
        "profile": profile,
        "user": user,
        "model": model,
        "checks": ["prompt_injection", "secret_leak", "policy_compliance"],
    }

    current, deprecated = _log_paths(session_id)
    await _ensure_log_file(current)
    await write_jsonl(current, record)
    if deprecated is not None:
        await _ensure_log_file(deprecated)
        await write_jsonl(deprecated, record)
    await _memory_upsert_governance(session_id, payload)
    log_info(f"Governance audit session start logged: {session_id}")


async def handle_on_session_end(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    duration_ms = json_get(payload, "duration_ms", "0")
    turns = json_get(payload, "turns", "0")
    tokens_in = json_get(payload, "tokens_in", "0")
    tokens_out = json_get(payload, "tokens_out", "0")
    status = json_get(payload, "status", "unknown")

    record: dict = {
        "event": "session_end",
        "session_id": session_id,
        "timestamp": timestamp,
        "duration_ms": int(duration_ms) if str(duration_ms).isdigit() else 0,
        "turns": int(turns) if str(turns).isdigit() else 0,
        "tokens_in": int(tokens_in) if str(tokens_in).isdigit() else 0,
        "tokens_out": int(tokens_out) if str(tokens_out).isdigit() else 0,
        "status": status,
        "checks": ["prompt_injection", "secret_leak", "policy_compliance"],
    }

    current, deprecated = _log_paths(session_id)
    await _ensure_log_file(current)
    await write_jsonl(current, record)
    if deprecated is not None:
        await _ensure_log_file(deprecated)
        await write_jsonl(deprecated, record)
    await _memory_upsert_governance(session_id, payload)
    log_info(f"Governance audit session end logged: {session_id} ({duration_ms}ms, {turns} turns)")


async def handle_pre_llm_call(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    model = json_get(payload, "model", "unknown")
    provider = json_get(payload, "provider", "unknown")
    prompt_length = json_get(payload, "prompt_length", "0")
    system_prompt_length = json_get(payload, "system_prompt_length", "0")
    user_message = json_get(payload, "user_message", "")
    event_type = json_get(payload, "event", "pre_llm_call")

    record: dict = {
        "event": event_type,
        "session_id": session_id,
        "timestamp": timestamp,
        "model": model,
        "provider": provider,
        "prompt_length": int(prompt_length) if str(prompt_length).isdigit() else 0,
        "system_prompt_length": int(system_prompt_length) if str(system_prompt_length).isdigit() else 0,
        "user_message": user_message,
        "checks": ["prompt_injection", "secret_leak", "policy_compliance"],
    }

    current, deprecated = _log_paths(session_id)
    await _ensure_log_file(current)
    await write_jsonl(current, record)
    if deprecated is not None:
        await _ensure_log_file(deprecated)
        await write_jsonl(deprecated, record)
    await _memory_upsert_governance(session_id, payload)
    log_info(f"Governance audit prompt logged: {session_id} -> {model} ({prompt_length} chars)")


_EVENT_HANDLERS = {
    "on_session_start": handle_on_session_start,
    "on_session_end": handle_on_session_end,
    "pre_llm_call": handle_pre_llm_call,
}


async def main() -> None:
    ctx = skip_context(_HOOK_PREFIX, _HOOK_FALLBACK_NAME)
    if ctx["skip"]:
        log_info(f"{_HOOK_FALLBACK_NAME} skipped via {ctx['skip_var']}")
        await _log_skip("unknown", ctx["skip_var"])
        return

    payload = read_payload()
    raw_event = payload.get("event", "")
    event = normalize_event(raw_event)

    log_debug(
        f"governance-audit event={raw_event!r} normalized={event} session_id={json_get(payload, 'session_id', 'unknown')}"
    )
    handler = _EVENT_HANDLERS.get(event)
    if handler is None:
        log_error(f"Unknown event: {raw_event or '<unset>'}")
        await _log_error_record(
            json_get(payload, "session_id", "unknown"),
            raw_event,
            f"unknown_event:{raw_event or '<unset>'}",
        )
        sys.exit(1)

    try:
        await handler(payload)
    except FileNotFoundError as exc:
        session_id = json_get(payload, "session_id", "unknown")
        log_error(f"Governance audit logging failed for {session_id}: missing log file: {exc}")
        await _log_error_record(session_id, raw_event, f"missing_log_file:{exc}")
        sys.exit(1)
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
