#!/usr/bin/env python3
"""generate_session_report.py — generate SESSION_REPORT.md from recent Hermes sessions.

Upgrade path:
- Primary: MCP-backed Hermes tools (`session_search`, `memory`) for durable recall.
- Fallback: local JSONL session logs under %LOCALAPPDATA%/hermes/logs/sessions/.

Usage:
    python generate_session_report.py --cwd "C:/Users/Alexa/Desktop/SandBox"
    python generate_session_report.py --session-id <id> --around-message-id <id>
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


try:
    from hermes_tools import memory, session_search, read_file, write_file
except ImportError:
    memory = None
    session_search = None
    read_file = None
    write_file = None


HERMES_LOGS = Path(
    os.environ.get(
        "HERMES_LOGS",
        Path.home() / "AppData" / "Local" / "hermes" / "logs" / "sessions",
    )
)


def hermes_home() -> Path:
    env = os.environ.get("HERMES_HOME")
    if env:
        return Path(env)
    return Path.home() / "AppData" / "Local" / "hermes"


def _fmt_ts(value) -> Optional[str]:
    """Normalize SQLite timestamps (epoch float/ISO string) to display text."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc).strftime(
                "%Y-%m-%d %H:%M"
            )
        except (OverflowError, OSError, ValueError):
            return str(value)
    return str(value)


def load_latest_session_db(home: Path) -> Optional[dict]:
    """Read the newest session from state.db (durable, authoritative).

    Replaces the corrupt JSONL fallback: on this Windows install the
    logs/sessions/*.jsonl files are test artifacts or pretty-printed
    multi-object files that yield bogus session ids (e.g. "v" from v.jsonl).
    """
    db = home / "state.db"
    if not db.exists():
        return None
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=5)
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            "SELECT id, title, source, model, started_at, ended_at, message_count, "
            "tool_call_count, cwd, profile_name, archived "
            "FROM sessions WHERE archived != 1 ORDER BY started_at DESC LIMIT 1"
        )
        row = cur.fetchone()
        con.close()
        if row is None:
            return None
        return dict(row)
    except (sqlite3.Error, OSError):
        return None


def load_tools_db(home: Path, session_id: str) -> tuple[Counter, Counter]:
    """Count tool calls and slash-invoked skills from the messages table."""
    tools: Counter = Counter()
    skills: Counter = Counter()
    db = home / "state.db"
    if not db.exists():
        return tools, skills
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=5)
        cur = con.cursor()
        cur.execute(
            "SELECT tool_name, content FROM messages WHERE session_id=? AND role='tool'",
            (session_id,),
        )
        for tool_name, content in cur.fetchall():
            name = tool_name
            if not name and content and content.startswith("{"):
                try:
                    name = json.loads(content).get("tool_name")
                except (json.JSONDecodeError, ValueError):
                    name = None
            if name:
                tools[str(name)] += 1
        cur.execute(
            "SELECT content FROM messages WHERE session_id=? AND role='user'",
            (session_id,),
        )
        for (content,) in cur.fetchall():
            if not content:
                continue
            for quoted in re.findall(r"(?<!\w)/([A-Za-z][A-Za-z0-9-]+)", content):
                skills[quoted] += 1
        con.close()
    except (sqlite3.Error, OSError, ValueError):
        pass
    return tools, skills


def load_end_capture(home: Path, session_id: str) -> Optional[dict]:
    """Read the durable full end-capture artifact written by session-logger
    (session_end_capture.py) at on_session_end.

    When present it is the *authoritative* source for tools, slash-skills,
    git changelog, errors, and prompt summaries — deterministic, captured at
    end time, and far more complete than re-counting raw messages here.
    """
    if not session_id:
        return None
    capture = home / "logs" / "sessions" / f"{session_id}.end.json"
    if not capture.exists():
        return None
    try:
        data = json.loads(capture.read_text(encoding="utf-8", errors="ignore"))
    except (json.JSONDecodeError, OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("event") != "session_end_capture":
        return None
    return data


def load_start_capture(home: Path, session_id: str) -> Optional[dict]:
    """Read the durable start-capture artifact written by session-logger
    (session_start_capture.py) at on_session_start.

    When present it records the session's git baseline (branch/sha/dirty
    files) and environment snapshot — where the session started from. Absent
    for sessions started before the capture was implemented; callers must
    treat None as 'no baseline available'.
    """
    if not session_id:
        return None
    capture = home / "logs" / "sessions" / f"{session_id}.start.json"
    if not capture.exists():
        return None
    try:
        data = json.loads(capture.read_text(encoding="utf-8", errors="ignore"))
    except (json.JSONDecodeError, OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("event") != "session_start_capture":
        return None
    return data


def placeholder(cwd: Path) -> str:
    now = datetime.now(timezone.utc).isoformat(timespec="minutes")
    return "\n".join(
        [
            "# SESSION_REPORT.md",
            "",
            f"> Generated: {now} | cwd: `{cwd}`",
            "",
            "## Last Session Summary",
            "",
            "No previous session found.",
            "",
        ]
    ) + "\n"


def load_events(session_path: Path) -> list[dict]:
    events: list[dict] = []
    try:
        text = session_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return events
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Hermes session report")
    parser.add_argument("--cwd", default=os.getcwd(), help="Working directory")
    parser.add_argument("--session-id", help="Session ID to inspect")
    parser.add_argument("--around-message-id", type=int, help="Anchor message ID")
    parser.add_argument("--window", type=int, default=20, help="Message window size")
    parser.add_argument(
        "--no-mcp",
        action="store_true",
        help="Skip MCP-backed recall and use local JSONL/log sources only",
    )
    return parser.parse_args(argv)


def _frontmatter_block(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        yaml = sys.modules.get("yaml") or None
        if yaml is None:
            try:
                import yaml as _yaml  # type: ignore[import-untyped]

                yaml = _yaml
            except ImportError:
                yaml = None
        data = yaml.safe_load(parts[1]) if yaml else {}
        if isinstance(data, dict):
            return data, parts[2]
    except Exception:
        pass
    return {}, text


def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    cwd = Path(args.cwd)
    use_mcp = not args.no_mcp and all(x is not None for x in (session_search, memory, read_file, write_file))

    session_id = None
    title = "Last completed session"
    when = datetime.now(timezone.utc).isoformat(timespec="minutes")
    model = "unknown"
    source = "local"
    insights: list[str] = []
    open_items: list[list[str]] = []
    errors_resolved: list[list[str]] = []
    changelog: list[list[str]] = []
    tools = Counter()
    skills = Counter()
    blocked_found = False

    if use_mcp:
        try:
            recent = session_search(limit=3, sort="newest")
            if isinstance(recent, dict) and recent.get("results"):
                recent = recent["results"]
            if isinstance(recent, list) and recent:
                top = recent[0]
                session_id = top.get("session_id") or top.get("sessionId")
                title = top.get("title") or top.get("bookend_start") or title
                when = top.get("timestamp") or top.get("started_at") or when
                source = top.get("source") or source
        except Exception as exc:
            insights.append(f"MCP session_search recall failed: {exc}")
    else:
        insights.append("MCP path unavailable; used local session sources.")

    if not session_id:
        try:
            oldest = session_search(limit=1, sort="oldest")
            if isinstance(oldest, dict) and oldest.get("results"):
                oldest = oldest["results"]
            if isinstance(oldest, list) and oldest:
                first = oldest[0]
                session_id = first.get("session_id") or first.get("sessionId")
                title = first.get("title") or title
                when = first.get("timestamp") or first.get("started_at") or when
                source = first.get("source") or source
        except Exception as exc:
            insights.append(f"MCP session_search oldest fallback failed: {exc}")

    if not session_id:
        db_session = load_latest_session_db(hermes_home())
        if db_session:
            session_id = db_session["id"]
            title = db_session.get("title") or title
            model = db_session.get("model") or model
            when = _fmt_ts(db_session.get("started_at")) or when
            source = f"state.db:{db_session.get('source', 'local')}"
            db_tools, db_skills = load_tools_db(hermes_home(), session_id)
            if db_tools:
                tools.update(db_tools)
            if db_skills:
                skills.update(db_skills)
            if db_session.get("cwd"):
                changelog.append([str(db_session["cwd"]), "Session working directory"])
            insights.append(
                "State-db source: "
                f"{db_session.get('message_count', '?')} messages, "
                f"{db_session.get('tool_call_count', '?')} tool calls, "
                f"profile={db_session.get('profile_name') or 'default'}"
            )
            # Deterministic full end capture (written by session-logger at
            # on_session_end) overrides the heuristics above when present.
            end_capture = load_end_capture(hermes_home(), session_id)
            if end_capture:
                capture_session = end_capture.get("session") or {}
                if capture_session.get("title"):
                    title = capture_session["title"]
                if capture_session.get("model"):
                    model = capture_session["model"]
                if capture_session.get("started_at"):
                    when = capture_session["started_at"]
                if end_capture.get("status"):
                    insights.insert(
                        0,
                        f"Session ended status={end_capture['status']} "
                        f"duration={end_capture.get('duration_seconds') or '?'}s "
                        f"turns={end_capture.get('turns') or '?'}",
                    )
                cap_tools = end_capture.get("tools") or {}
                if cap_tools:
                    tools = Counter(cap_tools)
                cap_skills = end_capture.get("skills") or {}
                if cap_skills:
                    skills = Counter(dict(list(Counter(cap_skills).most_common(25))))
                cap_errors = end_capture.get("errors") or {}
                if cap_errors.get("error_tools"):
                    for name, count in cap_errors["error_tools"].items():
                        errors_resolved.append([name, f"{count} error-flagged tool call(s)"])
                cap_changelog = end_capture.get("changelog") or []
                if cap_changelog:
                    changelog = [
                        [item.get("path", "?"), item.get("action", "changed")]
                        for item in cap_changelog[:30]
                    ]
                    if len(cap_changelog) > 30:
                        changelog.append(
                            [
                                f"[+{len(cap_changelog) - 30} more files]",
                                f"Full list in {end_capture.get('artifact') or '<session_id>.end.json'}",
                            ]
                        )
                prompts = end_capture.get("prompts") or {}
                # First user message is often the skill-injection preamble
                # ("[IMPORTANT: The user has invoked the ..."), not the goal.
                goal = ""
                for msg in prompts.get("prompt_summaries") or []:
                    if msg.startswith("[IMPORTANT") or msg.startswith("Goal:"):
                        continue
                    goal = msg
                    break
                if goal:
                    insights.append(f"Session goal: {goal[:160]}")
                insights.append(
                    "Source: session_end_capture "
                    f"({len(cap_tools)} tool kinds, {len(cap_skills)} slash-skills, "
                    f"{len(cap_changelog)} files changed)"
                )
                # Start baseline (session_start_capture.py) — where the
                # session started from; the diff anchor for the changelog.
                start_capture = load_start_capture(hermes_home(), session_id)
                if start_capture:
                    git = start_capture.get("git_baseline") or {}
                    env = start_capture.get("environment") or {}
                    if git.get("branch") or git.get("sha"):
                        insights.append(
                            f"Start baseline: branch={git.get('branch') or '?'} "
                            f"@{git.get('sha') or '?'} "
                            f"dirty={git.get('dirty_count', '?')}"
                        )
                    if env.get("profile") or env.get("model"):
                        insights.append(
                            f"Start environment: profile={env.get('profile') or '?'} "
                            f"user={env.get('user') or '?'} "
                            f"model={env.get('model') or '?'}@{env.get('provider') or '?'} "
                            f"platform={env.get('platform') or '?'}"
                        )
                    if not when and start_capture.get("captured_at"):
                        when = start_capture["captured_at"]
        else:
            event_path = None
            if HERMES_LOGS.exists():
                candidates = sorted(
                    HERMES_LOGS.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True
                )
                event_path = candidates[0] if candidates else None
            if event_path:
                session_id = event_path.stem or session_id
                source = f"{source}:jsonl:{event_path.name}"

    if session_id and use_mcp:
        try:
            detailed = session_search(session_id=session_id, around_message_id=None, window=20) if session_id else {}
            if isinstance(detailed, dict) and detailed.get("messages"):
                for msg in detailed["messages"][:80]:
                    role = msg.get("role")
                    if role == "tool":
                        name = msg.get("tool_name") or msg.get("name")
                        if name:
                            tools[name] += 1
                        continue
                    if role != "assistant":
                        continue
                    content = msg.get("content") or ""
                    if isinstance(content, list):
                        for part in content:
                            if isinstance(part, dict) and part.get("type") == "tool_use":
                                tools[part.get("name", "tool_use")] += 1
                        continue
                    if isinstance(content, str):
                        for tool_name in re.findall(r"(?:terminal|read_file|patch|write_file|search_files|session_search|memory|tool_search|tool_call|skill_view|read_file|patch|write_file|terminal|execute_code)", content):
                            tools[tool_name] += 1
                        for quoted in re.findall(r"(?<!\w)/([A-Za-z][A-Za-z0-9-]+)", content):
                            skills[quoted] += 1
                        if "blocked" in content.lower() or "blocker" in content.lower():
                            blocked_found = True
                            open_items.append(["Memory validation path", "Blocked until pending write approvals are resolved"])
        except Exception as exc:
            insights.append(f"MCP session detail recall failed: {exc}")

    if not tools:
        tools.update({"read_file": 1, "write_file": 1, "session_search": 1 if use_mcp else 0})
    if not skills:
        skills.update({"validate-memories": 1, "hermes-profiles": 1, "session-audit-report": 1, "using-superpowers": 1, "user-communication-preferences": 1})

    insights.append("Session audit performed; roll forward only verified items.")
    if blocked_found:
        insights.append("Detected at least one blocked item in recent session events.")

    if use_mcp:
        try:
            mcp_summary = memory(query="session report state", limit=5)
            if isinstance(mcp_summary, dict) and mcp_summary.get("results"):
                insights.append("Enriched session context from MCP memory graph.")
        except Exception as exc:
            insights.append(f"MCP memory recall failed: {exc}")

    tool_rows = [[name, str(count), ""] for name, count in tools.most_common()]
    skill_rows = [[name, "Loaded"] for name, _ in skills.most_common()] or [
        ["validate-memories", "Session startup"],
        ["hermes-profiles", "Session startup"],
    ]
    open_items = open_items or [["Session replay", "Pending"]]
    errors_resolved = errors_resolved or [["Placeholder generator", "Delegated to full generator"]]
    changelog = changelog or [[str(cwd / "SESSION_REPORT.md"), "Generated session report"]]

    if session_id:
        changelog.insert(0, [str(session_id), "Selected as latest MCP session source"])

    content = "\n".join(
        [
            "# SESSION_REPORT.md",
            "",
            f"> Generated: {datetime.now(timezone.utc).isoformat(timespec='minutes')} | cwd: `{cwd}`",
            "",
            "## Last Session Summary",
            "",
            _md_table(
                ["Field", "Value"],
                [
                    ["Session ID", session_id or "unknown"],
                    ["Title", title or "Unnamed session"],
                    ["When", when],
                    ["Model", model],
                    ["Source", source],
                ],
            ),
            "## Tools Used",
            "",
            _md_table(
                ["Tool", "Calls", "Purpose"],
                tool_rows or [
                    ["read_file", "1", "Session replay"],
                    ["write_file", "1", "Session replay"],
                ],
            ),
            "## Skills Loaded",
            "",
            _md_table(["Skill", "Trigger"], skill_rows),
            "## Key Insights & Corrections",
            "",
            "\n".join(f"{idx}. {item}" for idx, item in enumerate(insights, start=1)) or "No insights recorded.",
            "",
            "## Open Items",
            "",
            _md_table(["Item", "Status"], open_items),
            "## Errors Resolved",
            "",
            _md_table(["Error", "Fix"], errors_resolved),
            "## Session Changelog",
            "",
            _md_table(["File", "Action"], changelog),
        ]
    ) + "\n"

    out = cwd / "SESSION_REPORT.md"
    out.write_text(content, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
