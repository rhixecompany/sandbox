#!/usr/bin/env python3
"""Invoke Hermes' installed end-capture module for the current real session.

Why: the capture implementation is owned by Hermes hooks; this wrapper keeps
invocation reproducible, local-only, and secret-safe without synthesizing IDs.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes"))
HOOKS = HERMES_HOME / "hooks"
sys.path.insert(0, str(HOOKS))

from session_end_capture import run_capture  # noqa: E402


session_id = os.environ.get("HERMES_SESSION_ID", "").strip()
if not session_id:
    raise SystemExit("HERMES_SESSION_ID is missing; refusing to synthesize a session ID")

result = run_capture(session_id, payload={"cwd": "C:/Users/Alexa/Desktop/SandBox"})
artifact = result.get("artifact")
if not artifact:
    raise SystemExit(f"end capture did not return an artifact: {result.get('capture_error', 'unknown error')}")
print(artifact)
