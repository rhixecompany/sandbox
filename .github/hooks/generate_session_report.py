
#!/usr/bin/env python3
"""generate_session_report.py — Generates a human-readable SESSION_REPORT.md from session end capture artifacts.

Consumes the JSON artifact produced by session_end_capture.py and produces a
markdown report, intended to be consumed at the start of the next session.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Resolve paths
_HOOK_DIR = Path(__file__).resolve().parent
_HERMES_HOME = Path(
    os.environ.get("HERMES_HOME", "C:/Users/Alexa/AppData/Local/hermes")
)
_LOG_DIR = _HERMES_HOME / "logs" / "sessions"
_REPORT_PATH = Path("C:/Users/Alexa/Desktop/SandBox/SESSION_REPORT.md")

# --- Helpers ---
def _fmt_ts(iso_timestamp: str) -> str:
    if not iso_timestamp:
        return ""
    try:
        dt = datetime.fromisoformat(iso_timestamp.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return iso_timestamp

def _truncate_list(items: list[str], limit: int = 5) -> list[str]:
    return items[:limit] + [f"[+{len(items) - limit} more]"] if len(items) > limit else items

# --- Report Generation ---
def generate_report_content(capture_data: dict) -> str:
    session_info = capture_data.get("session", {})
    tools = capture_data.get("tools", {})
    skills = capture_data.get("skills", {})
    prompts = capture_data.get("prompts", {})
    errors = capture_data.get("errors", {})
    changelog = capture_data.get("changelog", [])

    report_lines = []
    report_lines.append("# SESSION_REPORT.md")
    report_lines.append("")
    report_lines.append(f"> Generated: {capture_data.get('captured_at', '')} | cwd: `{session_info.get('cwd', '')}`")
    report_lines.append("")
    report_lines.append("## Last Session Summary")
    report_lines.append("")
    report_lines.append("| Field      | Value                             |")
    report_lines.append("| ---------- | --------------------------------- |")
    report_lines.append(f"| Session ID | {capture_data.get('session_id', '')}            |")
    report_lines.append(f"| Title      | {session_info.get('title', prompts.get('first_user_message', ''))} |")
    report_lines.append(f"| When       | {_fmt_ts(session_info.get('started_at', ''))}               |")
    report_lines.append(f"| Model      | {session_info.get('model', '')}            |")
    report_lines.append(f"| Source     | {session_info.get('source', '')}                      |")
    report_lines.append(f"| Status     | {capture_data.get('status', 'unknown')} |")
    dur = capture_data.get('duration_seconds')
    dur_str = f"{dur}s" if dur is not None else "N/A"
    turns = capture_data.get('turns')
    turns_str = str(turns) if turns is not None else "N/A"
    report_lines.append(f"| Duration   | {dur_str} |")
    report_lines.append(f"| Turns      | {turns_str} |")
    report_lines.append("")

    if tools:
        report_lines.append("## Tools Used")
        report_lines.append("")
        report_lines.append("| Tool | Calls | Purpose |")
        report_lines.append("| --- | --- | --- |")
        for tool, count in tools.items():
            report_lines.append(f"| {tool} | {count} | |")
        report_lines.append("")

    if skills:
        report_lines.append("## Skills Loaded")
        report_lines.append("")
        report_lines.append("| Skill | Trigger |")
        report_lines.append("| --- | --- |")
        for skill, count in skills.items():
            report_lines.append(f"| {skill} | Loaded ({count} times) |")
        report_lines.append("")

    report_lines.append("## Key Insights & Corrections")
    report_lines.append("")
    # Placeholder for insights, will be filled by agent or derived later
    report_lines.append("- Session audit performed; roll forward only verified items.")
    dur = capture_data.get('duration_seconds')
    dur_str = f"{dur}s" if dur is not None else "N/A"
    turns = capture_data.get('turns')
    turns_str = str(turns) if turns is not None else "N/A"
    report_lines.append(f"- Status: {capture_data.get('status', 'unknown')}, Duration: {dur_str}, Turns: {turns_str}")
    first_prompt = prompts.get("first_user_message", "")
    # Truncate first prompt to 220 chars
    if len(first_prompt) > 220:
        first_prompt = first_prompt[:220] + "…"
    report_lines.append(f'- First prompt: "{first_prompt}"')
    if errors.get('finish_reasons'):
        report_lines.append(f"- Finish reasons: {', '.join(f'{k}: {v}' for k, v in errors['finish_reasons'].items())}")
    if errors.get('error_tools'):
        report_lines.append(f"- Error tools: {', '.join(f'{k}: {v}' for k, v in errors['error_tools'].items())}")
    report_lines.append("")

    if changelog:
        report_lines.append("## Session Changelog")
        report_lines.append("")
        report_lines.append("| File | Action |")
        report_lines.append("| --- | --- |")
        display_changelog = changelog
        if len(changelog) > 10: # Only display first 10 for brevity in report
            display_changelog = changelog[:10]

        for entry in display_changelog:
            report_lines.append(f"| {entry.get('path', '')} | {entry.get('action', '')} |")
        
        if len(changelog) > 10:
            report_lines.append(f"| [+{len(changelog) - 10} more files] | Full list in <session_id>.end.json |")
        report_lines.append("")


    return "\n".join(report_lines)

# --- Entry Point ---
def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: generate_session_report.py <session_id>")
        sys.exit(1)

    session_id = sys.argv[1]
    capture_file = _LOG_DIR / f"{session_id}.end.json"

    if not capture_file.exists():
        print(f"Error: Session end capture file not found at {capture_file}")
        sys.exit(1)

    try:
        with open(capture_file, "r", encoding="utf-8") as f:
            capture_data = json.load(f)
        report_content = generate_report_content(capture_data)
        _REPORT_PATH.write_text(report_content, encoding="utf-8")
        print(f"SESSION_REPORT.md generated for session {session_id} at {_REPORT_PATH}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {capture_file}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
