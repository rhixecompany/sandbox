--- C:\Users\Alexa\Desktop\SandBox\patches\0001-chore-session-auto-commit-session-20260815_155304_ab.patch.Name ---
From e93bc3337c0314702268b421baf30552c6894b28 Mon Sep 17 00:00:00 2001
From: rhixecompany <rhixecompany@gmail.com>
Date: Sat, 15 Aug 2026 16:44:32 +0100
Subject: [PATCH] chore(session): auto-commit session 20260815_155304_ab36b9 at
 2026-08-15T15:44:31Z

---

.github/hooks/generate_session_report.py | 155 +++++++++++++++++++++++
.github/hooks/session_end_capture.py | 23 +++-
SESSION_REPORT.md | 117 ++++++-----------
3 files changed, 212 insertions(+), 83 deletions(-)
create mode 100644 .github/hooks/generate_session_report.py

diff --git a/.github/hooks/generate_session_report.py b/.github/hooks/generate_session_report.py
new file mode 100644
index 00000000..a87c0c15
--- /dev/null
+++ b/.github/hooks/generate_session_report.py
@@ -0,0 +1,155 @@ +
+#!/usr/bin/env python3
+"""generate_session_report.py — Generates a human-readable SESSION_REPORT.md from session end capture artifacts. +
+Consumes the JSON artifact produced by session_end_capture.py and produces a
+markdown report, intended to be consumed at the start of the next session.
+""" +
+from **future** import annotations +
+import json
+import os
+import sys
+from datetime import datetime, timezone
+from pathlib import Path
+from typing import Any +
+# Resolve paths
+_HOOK_DIR = Path(**file**).resolve().parent
+_HERMES_HOME = Path(

- os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes")
  +)
  +_LOG_DIR = _HERMES_HOME / "logs" / "sessions"
  +_REPORT_PATH = Path("C:/Users/Alexa/Desktop/SandBox/SESSION_REPORT.md")
-

+# --- Helpers ---
+def _fmt_ts(iso_timestamp: str) -> str:

- if not iso_timestamp:
-        return ""
- try:
-        dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
-        return dt.strftime("%Y-%m-%d %H:%M:%S")
- except ValueError:
-        return iso_timestamp
-

+def _truncate_list(items: list[str], limit: int = 5) -> list[str]:

- return items[:limit] + [f"[+{len(items) - limit} more]"] if len(items) > limit else items
-

+# --- Report Generation ---
+def generate_report_content(capture_data: dict) -> str:

- session_info = capture_data.get("session", {})
- tools = capture_data.get("tools", {})
- skills = capture_data.get("skills", {})
- prompts = capture_data.get("prompts", {})
- errors = capture_data.get("errors", {})
- changelog = capture_data.get("changelog", [])
-
- report_lines = []
- report_lines.append("# SESSION_REPORT.md")
- report_lines.append("")
- report_lines.append(f"> Generated: {capture_data.get('captured_at', '')} | cwd: `{session_info.get('cwd', '')}`")
- report_lines.append("")
- report_lines.append("## Last Session Summary")
- report_lines.append("")
- report_lines.append("| Field | Value |")
- report_lines.append("| ---------- | --------------------------------- |")
- report_lines.append(f"| Session ID | {capture_data.get('session_id', '')} |")
- report_lines.append(f"| Title | {session_info.get('title', prompts.get('first_user_message', ''))} |")
- report_lines.append(f"| When | {_fmt_ts(session_info.get('started_at', ''))} |")
- report_lines.append(f"| Model | {session_info.get('model', '')} |")
- report_lines.append(f"| Source | {session_info.get('source', '')} |")
- report_lines.append(f"| Status | {capture_data.get('status', 'unknown')} |")
- dur = capture_data.get('duration_seconds')
- dur_str = f"{dur}s" if dur is not None else "N/A"
- turns = capture_data.get('turns')
- turns_str = str(turns) if turns is not None else "N/A"
- report_lines.append(f"| Duration | {dur_str} |")
- report_lines.append(f"| Turns | {turns_str} |")
- report_lines.append("")
-
- if tools:
-        report_lines.append("## Tools Used")
-        report_lines.append("")
-        report_lines.append("| Tool | Calls | Purpose |")
-        report_lines.append("| --- | --- | --- |")
-        for tool, count in tools.items():
-            report_lines.append(f"| {tool} | {count} | |")
-        report_lines.append("")
-
- if skills:
-        report_lines.append("## Skills Loaded")
