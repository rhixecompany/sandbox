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
    duration_seconds_between,
    git_snapshot,
    json_get,
    load_model_config,
    log_debug,
    log_error,
    log_info,
    normalize_event,
    now_iso,
    platform_snapshot,
    read_jsonl,
    read_payload,
    resolve_end_status,
    resolve_profile,
    resolve_user,
    skip_context,
    write_jsonl,
)

import session_end_capture  # noqa: E402  (hooks dir on sys.path via _LIB_DIR above)
import session_start_capture  # noqa: E402  (hooks dir on sys.path via _LIB_DIR above)

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
        # Full start capture: session row + git baseline + environment
        # from state.db/payload -> <session_id>.start.json, consumed by
        # session-audit-report as the diff anchor for the end changelog.
        try:
            capture = await asyncio.to_thread(
                session_start_capture.run_capture, ctx["session_id"], payload, timestamp
            )
            artifact = capture.get("artifact") or capture.get("capture_error") or "?"
            log_info(f"Session start capture written: {ctx['session_id']} -> {artifact}")
        except Exception as exc:  # noqa: BLE001 - capture must never break the hook
            log_debug(f"session-logger: full start capture skipped: {exc}")
    except FileNotFoundError:
        record.setdefault("diagnostics", []).append(f"missing_log_file:{log_file}")
        log_error(f"Session start failed for {ctx['session_id']}: missing log file at {log_file}")


async def handle_on_session_end(payload: dict) -> None:
    session_id = json_get(payload, "session_id", "unknown")
    timestamp = json_get(payload, "timestamp", now_iso())
    working_dir = json_get(payload, "cwd") or json_get(payload, "working_dir") or ""
    model_cfg = load_model_config()
    model = json_get(payload, "extra.model") or json_get(payload, "model") or model_cfg["model"]
    platform = json_get(payload, "extra.platform") or json_get(payload, "platform") or ""
    snapshot = platform_snapshot()
    status = resolve_end_status(payload)

    # The runtime never sends duration/turns/tokens on on_session_end (verified
    # wire shape: extra.{completed,failed,interrupted,turn_exit_reason}). Derive
    # what we can from the accumulated session JSONL — the start record gives
    # duration, each pre_llm_call row is a turn — and treat any future wire
    # fields as explicit overrides.
    history = await read_jsonl(_LOG_DIR / f"{session_id}.jsonl")
    start_ts = next(
        (rec.get("timestamp", "") for rec in history if rec.get("event") == "session_start"),
        "",
    )
    derived_duration = duration_seconds_between(start_ts, timestamp) if start_ts else 0
    derived_turns = sum(1 for rec in history if rec.get("event") == "pre_llm_call")

    duration_ms_raw = json_get(payload, "duration_ms", "")
    duration_sec_raw = json_get(payload, "duration_seconds", "")
    turns_raw = json_get(payload, "turns", "")
    tokens_in_raw = json_get(payload, "tokens_in", "")
    tokens_out_raw = json_get(payload, "tokens_out", "")
    exit_code_raw = json_get(payload, "exit_code", "")

    record: dict = {
        "event": "session_end",
        "session_id": session_id,
        "timestamp": timestamp,
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
        "status": status,
        "duration_ms": int(duration_ms_raw) if duration_ms_raw.lstrip("-").isdigit() else derived_duration * 1000,
        "duration_seconds": int(duration_sec_raw) if duration_sec_raw.lstrip("-").isdigit() else derived_duration,
        "turns": int(turns_raw) if turns_raw.isdigit() else derived_turns,
        "tokens_in": int(tokens_in_raw) if tokens_in_raw.isdigit() else 0,
        "tokens_out": int(tokens_out_raw) if tokens_out_raw.isdigit() else 0,
        "exit_code": int(exit_code_raw) if exit_code_raw.lstrip("-").isdigit() else (1 if status == "failed" else 0),
    }

    if working_dir:
        try:
            record.update(await git_snapshot(working_dir))
        except Exception as exc:
            log_debug(f"session-logger: git snapshot skipped: {exc}")

    log_file = _LOG_DIR / f"{session_id}.jsonl"
    try:
        await write_jsonl(log_file, record)
        await _memory_upsert_session(session_id, record)
        log_info(
            f"Session end captured: {session_id} status={status} "
            f"duration={record['duration_seconds']}s turns={record['turns']}"
        )
        # Full end capture: tools/skills/changelog/errors/prompts from
        # state.db -> <session_id>.end.json, consumed by session-audit-report.
        # The wire never carries duration/turns, so the derived values are
        # passed through explicitly (they are already in the lifecycle record).
        try:
            capture_payload = dict(payload)
            capture_payload["duration_seconds"] = str(record["duration_seconds"])
            capture_payload["turns"] = str(record["turns"])
            capture = await asyncio.to_thread(
                session_end_capture.run_capture, session_id, capture_payload, timestamp
            )
            artifact = capture.get("artifact") or capture.get("capture_error") or "?"
            log_info(f"Session end capture written: {session_id} -> {artifact}")
        except Exception as exc:  # noqa: BLE001 - capture must never break the hook
            log_debug(f"session-logger: full end capture skipped: {exc}")
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

    # Guard: hermes hooks doctor and manual harness fires use synthetic ids
    # ("test-session", "unknown", "e2e-*"). Never write per-session JSONL under
    # a fake id — that pollutes the session log store and report generation.
    session_id = json_get(payload, "session_id", "unknown")
    if not session_id or session_id == "unknown" or session_id.startswith(("test", "e2e-")):
        log_info(f"Session logger skipped for synthetic session id {session_id!r}")
        await write_jsonl(
            _LOG_DIR / "skips.jsonl",
            {
                "event": "skipped",
                "hook": ctx["hook_name"],
                "reason": "synthetic_session_id",
                "session_id": session_id,
                "timestamp": now_iso(),
            },
        )
        sys.exit(0)

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
