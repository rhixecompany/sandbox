#!/usr/bin/env python3
"""post-exec-state-log — State modification logging hook.

Logs file writes, config changes, and tool invocations to the session
history JSONL queue for durability and audit trail.

Usage:
    post-exec-state-log.py <event_type> <payload_json>

Events:
    file_write   {"path": "...", "size": N, "action": "create|modify"}
    config_set   {"key": "...", "value": "..."}
    tool_call    {"tool": "...", "args": {...}, "result": "ok|fail"}
"""

from __future__ import annotations

import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path

from _pathutil import resolve_path

HOOKS_DIR = resolve_path(__file__).parent
HERMES_HOME = Path(os.environ.get("HERMES_HOME", "") or Path.home() / "AppData" / "Local" / "hermes")
LOG_DIR = HERMES_HOME / "logs" / "hermes"
LOG_FILE = LOG_DIR / "exec-state.jsonl"


def ensure_dir() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def log_entry(event_type: str, payload: dict) -> None:
    ensure_dir()
    record = {
        "ts": datetime.now(UTC).isoformat(),
        "event": event_type,
        "payload": payload,
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record, default=str) + "\n")
    # Mirror to stderr for immediate visibility
    print(f"[STATE] {event_type}: {json.dumps(payload)}", file=sys.stderr, flush=True)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: post-exec-state-log.py <event_type> [payload_json]", file=sys.stderr)
        sys.exit(1)

    event_type = sys.argv[1]
    payload = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    log_entry(event_type, payload)


if __name__ == "__main__":
    main()
