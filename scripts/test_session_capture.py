#!/usr/bin/env python3
"""Regression test for Hermes session start/end capture modules."""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
from pathlib import Path


HOOKS = Path(r"C:/Users/Alexa/AppData/Local/hermes/hooks")


def create_fixture(home: Path, session_id: str) -> None:
    database = home / "state.db"
    connection = sqlite3.connect(database)
    connection.execute(
        "CREATE TABLE sessions ("
        "id TEXT, source TEXT, user_id TEXT, model TEXT, started_at TEXT, ended_at TEXT, "
        "end_reason TEXT, message_count INTEGER, tool_call_count INTEGER, api_call_count INTEGER, "
        "input_tokens INTEGER, output_tokens INTEGER, estimated_cost_usd REAL, cwd TEXT, "
        "profile_name TEXT, git_branch TEXT, git_repo_root TEXT, display_name TEXT, "
        "last_activity_description TEXT)"
    )
    connection.execute(
        "CREATE TABLE messages ("
        "role TEXT, content TEXT, tool_calls TEXT, tool_name TEXT, finish_reason TEXT, "
        "effect_disposition TEXT, id INTEGER, session_id TEXT)"
    )
    connection.execute(
        "INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (session_id, "tui", "alexa", "test-model", "2026-09-05T08:00:00Z", None, None, 3, 1, 1, 0, 0, 0.0, str(home), "ops", "", "", "capture test", ""),
    )
    connection.executemany(
        "INSERT INTO messages VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            ("user", "/using-superpowers token=do-not-persist-this", None, None, None, None, 1, session_id),
            ("assistant", "", json.dumps([{"function": {"name": "filesystem_read"}}]), None, "tool_calls", None, 2, session_id),
            ("tool", "ok", None, "filesystem_read", None, "normal", 3, session_id),
        ],
    )
    connection.commit()
    connection.close()


def main() -> int:
    session_id = "capture-test-20260905"
    with tempfile.TemporaryDirectory(prefix="hermes-capture-test-") as temp:
        home = Path(temp)
        logs = home / "logs"
        os.environ["HERMES_HOME"] = str(home)
        os.environ["HERMES_LOGS_DIR"] = str(logs)
        os.environ["HERMES_CAPTURE_MIRROR_MEMORY"] = "0"
        sys.path.insert(0, str(HOOKS))
        import session_end_capture  # noqa: PLC0415
        import session_start_capture  # noqa: PLC0415

        create_fixture(home, session_id)
        start = session_start_capture.run_capture(
            session_id,
            {"cwd": str(home), "profile": "ops", "extra": {"model": "test-model"}},
            "2026-09-05T08:00:00Z",
        )
        end = session_end_capture.run_capture(
            session_id,
            {"cwd": str(home), "duration_seconds": "4", "turns": "1"},
            "2026-09-05T08:00:04Z",
        )
        assert "artifact" in start, start
        assert "artifact" in end, end
        start_data = json.loads(Path(start["artifact"]).read_text(encoding="utf-8"))
        end_data = json.loads(Path(end["artifact"]).read_text(encoding="utf-8"))
        assert start_data["event"] == "session_start_capture"
        assert start_data["environment"]["profile"] == "ops"
        assert end_data["event"] == "session_end_capture"
        assert end_data["duration_seconds"] == 4
        assert end_data["tools"]["filesystem_read"] == 2
        assert end_data["skills"]["using-superpowers"] == 1
        assert "token=[REDACTED]" in end_data["prompts"]["first_user_message"]
        assert "do-not-persist-this" not in json.dumps(end_data)
        invalid = session_end_capture.run_capture("../invalid", {}, "2026-09-05T08:00:04Z")
        assert invalid.get("capture_error") == "ValueError", invalid
    print("session capture regression: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
