#!/usr/bin/env python3
"""Build a redacted Markdown report for the current and previous WAT day.

The database is opened read-only. This script inventories sessions by start time,
then extracts bounded, redacted evidence from user/assistant/tool messages. It is
intentionally deterministic: it does not call a model, mutate Hermes state, or
perform network access.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import Counter
from collections.abc import Iterable
from datetime import UTC, date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.9+ normally provides zoneinfo.
    ZoneInfo = None


WAT = ZoneInfo("Africa/Lagos") if ZoneInfo else timezone(timedelta(hours=1))
DEFAULT_DB = Path.home() / "AppData/Local/hermes/state.db"
DEFAULT_REPORT_DIR = Path(__file__).resolve().parents[1] / "results"
SECRET_PATTERNS = [
    (re.compile(r"(?i)(bearer\s+)[A-Za-z0-9._~+/=-]+"), r"\1[REDACTED]"),
    (
        re.compile(
            r"(?i)\b(sk-[A-Za-z0-9_-]{12,}|ghp_[A-Za-z0-9]{12,}|github_pat_[A-Za-z0-9_]{12,}|xox[baprs]-[A-Za-z0-9-]{12,}|AIza[A-Za-z0-9_-]{20,})\b"
        ),
        "[REDACTED]",
    ),
    (re.compile(r"(?is)-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----"), "[PRIVATE_KEY_REDACTED]"),
    (
        re.compile(
            r"(?im)\b([A-Z0-9][A-Z0-9_ -]*(?:API[_ -]?KEY|TOKEN|PASSWORD|SECRET|CREDENTIAL|PRIVATE[_ -]?KEY))\s*[:=]\s*([^\n]+)"
        ),
        r"\1=[REDACTED]",
    ),
    (
        re.compile(r"(?im)\b(authorization|x-api-key|api-key|access-token|refresh-token)\s*[:=]\s*([^\n]+)"),
        r"\1: [REDACTED]",
    ),
]
MEMORY_CONTEXT_RE = re.compile(r"(?is)<memory-context>.*?</memory-context>")

CATEGORY_PATTERNS: dict[str, tuple[re.Pattern[str], ...]] = {
    "plans": (
        re.compile(r"(?i)\bplans?\b"),
        re.compile(r"(?i)(?:\.hermes/)?plans?/"),
        re.compile(r"(?i)implementation plan"),
    ),
    "specs": (
        re.compile(r"(?i)\bspecs?\b"),
        re.compile(r"(?i)(?:\.hermes/)?specs?/"),
        re.compile(r"(?i)requirements specification"),
    ),
    "prompts": (
        re.compile(r"(?i)\bprompts?\b"),
        re.compile(r"(?i)\.prompt\.md\b"),
        re.compile(r"(?i)/[a-z0-9_-]+(?:/[a-z0-9_-]+)+"),
    ),
    "goals": (re.compile(r"(?i)\bgoal\b|##\s*goals?\b|goal\s*[:=]"),),
    "subgoals": (re.compile(r"(?i)\bsub[- ]?goals?\b|sg\d+(?:\.\d+)?"),),
    "session_report": (re.compile(r"(?i)session[_ -]?report|execution[-_ ]summary|\.end\.json|session[-_ ]capture"),),
}
ERROR_RE = re.compile(
    r"(?i)\b(?:error|errors|failed|failure|failures|traceback|exception|blocked|blocker|timeout|timed out|cannot|could not|unavailable|warning)\b"
)
QUESTION_RE = re.compile(r"\?")
CLARIFY_RE = re.compile(
    r"(?i)\b(?:clarif|which|should we|do you want|would you like|confirm|could you|can you specify|what should|how should)\b"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--date", type=lambda value: date.fromisoformat(value), help="Today date in WAT (YYYY-MM-DD).")
    parser.add_argument(
        "--output", type=Path, help="Report path; defaults to results/run-today-and-yesterday-report-<today>.md"
    )
    return parser.parse_args()


def wat_boundaries(today: date | None) -> tuple[datetime, datetime, date]:
    current = today or datetime.now(WAT).date()
    start = datetime.combine(current - timedelta(days=1), time.min, tzinfo=WAT)
    end = datetime.combine(current + timedelta(days=1), time.min, tzinfo=WAT)
    return start, end, current


def connect_read_only(path: Path) -> sqlite3.Connection:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"Session database not found: {resolved}")
    return sqlite3.connect(f"file:{resolved.as_posix()}?mode=ro", uri=True)


def iso_timestamp(value: float | None) -> str:
    if value is None:
        return "—"
    return datetime.fromtimestamp(value, UTC).astimezone(WAT).isoformat(timespec="seconds")


def redact(text: str | None) -> str:
    if not text:
        return ""
    result = MEMORY_CONTEXT_RE.sub("[MEMORY_CONTEXT_OMITTED]", str(text))
    for pattern, replacement in SECRET_PATTERNS:
        result = pattern.sub(replacement, result)
    return result.strip()


def direct_user_text(text: str | None) -> str:
    if not text:
        return ""
    result = str(text)
    if "<memory-context>" in result.lower():
        result = re.split(r"(?i)<memory-context>", result, maxsplit=1)[0]
    return redact(result).strip()


def excerpt(text: str | None, limit: int = 900) -> str:
    value = re.sub(r"\s+", " ", redact(text)).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def message_text(message: dict[str, Any]) -> str:
    if message["role"] == "user":
        return direct_user_text(message.get("content"))
    return redact(message.get("content"))


def matches_category(category: str, text: str) -> bool:
    return any(pattern.search(text) for pattern in CATEGORY_PATTERNS[category])


def category_excerpts(messages: list[dict[str, Any]], category: str, limit: int = 6) -> list[str]:
    selected: list[str] = []
    for message in messages:
        if message["role"] not in {"user", "assistant"}:
            continue
        text = message_text(message)
        if not text or not matches_category(category, text):
            continue
        selected.append(f"[{message['role']}] {excerpt(text)}")
        if len(selected) >= limit:
            break
    return selected


def error_excerpts(messages: list[dict[str, Any]], limit: int = 8) -> list[str]:
    selected: list[str] = []
    for message in messages:
        if message["role"] not in {"user", "assistant"}:
            continue
        text = message_text(message)
        if not text or not ERROR_RE.search(text):
            continue
        selected.append(f"[{message['role']}] {excerpt(text)}")
        if len(selected) >= limit:
            break
    return selected


def question_lines(text: str, limit: int = 8) -> list[str]:
    lines: list[str] = []
    for raw_line in redact(text).splitlines():
        line = raw_line.strip()
        if not line or len(line) > 500 or not QUESTION_RE.search(line):
            continue
        if line.startswith(("http://", "https://", "|")):
            continue
        lines.append(excerpt(line, 700))
        if len(lines) >= limit:
            break
    return lines


def clarifications(messages: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    questions: list[str] = []
    answers: list[str] = []
    for index, message in enumerate(messages):
        if message["role"] != "assistant":
            continue
        text = redact(message.get("content"))
        candidates = [line for line in question_lines(text) if CLARIFY_RE.search(line)]
        if not candidates:
            continue
        questions.extend(f"[assistant] {line}" for line in candidates[:3])
        for next_message in messages[index + 1 :]:
            if next_message["role"] == "user":
                answer = direct_user_text(next_message.get("content"))
                if answer:
                    answers.append(f"[user] {excerpt(answer)}")
                break
        if len(questions) >= 12:
            break
    return questions[:12], answers[:12]


def tool_names(messages: list[dict[str, Any]]) -> list[str]:
    names: Counter[str] = Counter()
    for message in messages:
        if message.get("tool_name"):
            names[str(message["tool_name"])] += 1
        raw_calls = message.get("tool_calls")
        if not raw_calls:
            continue
        try:
            calls = json.loads(raw_calls) if isinstance(raw_calls, str) else raw_calls
        except (TypeError, json.JSONDecodeError):
            calls = []
        if isinstance(calls, dict):
            calls = [calls]
        if not isinstance(calls, list):
            continue
        for call in calls:
            if not isinstance(call, dict):
                continue
            function = call.get("function") if isinstance(call.get("function"), dict) else call
            name = function.get("name") if isinstance(function, dict) else None
            if name:
                names[str(name)] += 1
    return [f"{name} ({count})" for name, count in sorted(names.items())]


def user_inputs(messages: list[dict[str, Any]], limit: int = 60) -> tuple[str, list[str]]:
    values = [direct_user_text(m.get("content")) for m in messages if m["role"] == "user"]
    values = [value for value in values if value]
    if not values:
        return "—", []
    return values[0], [excerpt(value, 1000) for value in values[:limit]]


def output_excerpts(messages: list[dict[str, Any]], limit: int = 6) -> list[str]:
    values = [excerpt(m.get("content"), 1400) for m in messages if m["role"] == "assistant" and m.get("content")]
    values = [value for value in values if value]
    if len(values) <= limit:
        return values
    head = limit // 2
    return [
        *values[:head],
        "[… middle assistant outputs omitted …]",
        *values[-(limit - head - 1) :],
    ]


def render_list(items: Iterable[str]) -> str:
    values = list(items)
    return "\n".join(f"- {value}" for value in values) if values else "- —"


def load_sessions(connection: sqlite3.Connection, start: datetime, end: datetime) -> list[dict[str, Any]]:
    columns = (
        "id, source, profile_name, title, started_at, ended_at, last_activity_at, "
        "message_count, tool_call_count, input_tokens, output_tokens, cache_read_tokens, "
        "cache_write_tokens, reasoning_tokens, estimated_cost_usd, actual_cost_usd, "
        "end_reason, cwd, git_branch"
    )
    rows = connection.execute(
        f"SELECT {columns} FROM sessions WHERE started_at >= ? AND started_at < ? ORDER BY started_at, id",
        (start.timestamp(), end.timestamp()),
    ).fetchall()
    keys = columns.replace(" ", "").split(",")
    return [dict(zip(keys, row, strict=True)) for row in rows]


def load_messages(connection: sqlite3.Connection, session_id: str) -> list[dict[str, Any]]:
    rows = connection.execute(
        """
        SELECT id, role, content, tool_name, tool_calls, timestamp, token_count
        FROM messages
        WHERE session_id = ? AND active = 1
        ORDER BY COALESCE(display_order, id), id
        """,
        (session_id,),
    ).fetchall()
    keys = ("id", "role", "content", "tool_name", "tool_calls", "timestamp", "token_count")
    return [dict(zip(keys, row, strict=True)) for row in rows]


def render_session(session: dict[str, Any], messages: list[dict[str, Any]], number: int) -> str:
    query, inputs = user_inputs(messages)
    clarifying_questions, clarifying_answers = clarifications(messages)
    categories = {category: category_excerpts(messages, category) for category in CATEGORY_PATTERNS}
    errors = error_excerpts(messages)
    outputs = output_excerpts(messages)
    role_counts = Counter(message["role"] for message in messages)
    tools = tool_names(messages)
    title = session.get("title") or "(untitled)"
    lines = [
        f"## {number}. {redact(title)}",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Session ID | `{session['id']}` |",
        f"| Source / profile | `{session.get('source') or '—'}` / `{session.get('profile_name') or '—'}` |",
        f"| Started (WAT) | {iso_timestamp(session.get('started_at'))} |",
        f"| Ended (WAT) | {iso_timestamp(session.get('ended_at'))} |",
        f"| Last activity (WAT) | {iso_timestamp(session.get('last_activity_at'))} |",
        f"| Message count | {session.get('message_count') or 0} (read back: {len(messages)}) |",
        f"| Tool-call count | {session.get('tool_call_count') or 0} |",
        f"| End reason | {redact(session.get('end_reason')) or '—'} |",
        "",
        "### Query",
        "",
        query or "—",
        "",
        "### User inputs",
        "",
        render_list(inputs),
        "",
        "### Plans",
        "",
        render_list(categories["plans"]),
        "",
        "### Specs",
        "",
        render_list(categories["specs"]),
        "",
        "### Prompts",
        "",
        render_list(categories["prompts"]),
        "",
        "### Goals",
        "",
        render_list(categories["goals"]),
        "",
        "### Subgoals",
        "",
        render_list(categories["subgoals"]),
        "",
        "### Tools",
        "",
        render_list(tools),
        "",
        "### Usage",
        "",
        f"- Roles read: {dict(sorted(role_counts.items()))}",
        f"- Input tokens: {session.get('input_tokens') if session.get('input_tokens') is not None else '—'}",
        f"- Output tokens: {session.get('output_tokens') if session.get('output_tokens') is not None else '—'}",
        f"- Cache read/write tokens: {session.get('cache_read_tokens') or 0} / {session.get('cache_write_tokens') or 0}",
        f"- Reasoning tokens: {session.get('reasoning_tokens') or 0}",
        f"- Estimated/actual cost USD: {session.get('estimated_cost_usd') if session.get('estimated_cost_usd') is not None else '—'} / {session.get('actual_cost_usd') if session.get('actual_cost_usd') is not None else '—'}",
        "",
        "### Clarifying questions",
        "",
        render_list(clarifying_questions),
        "",
        "### Clarifying-question answers",
        "",
        render_list(clarifying_answers),
        "",
        "### Session-report evidence",
        "",
        render_list(categories["session_report"]),
        "",
        "### Errors and warnings",
        "",
        render_list(errors),
        "",
        "### Assistant output excerpts",
        "",
        render_list(outputs),
        "",
    ]
    return "\n".join(lines)


def build_report(db: Path, output: Path, today: date | None) -> tuple[int, Path]:
    start, end, _ = wat_boundaries(today)
    connection = connect_read_only(db)
    try:
        sessions = load_sessions(connection, start, end)
        rendered: list[str] = []
        total_messages = 0
        empty_sessions = 0
        for number, session in enumerate(sessions, start=1):
            messages = load_messages(connection, session["id"])
            total_messages += len(messages)
            empty_sessions += not bool(messages)
            rendered.append(render_session(session, messages, number))
    finally:
        connection.close()

    output = output.expanduser()
    if not output.is_absolute():
        output = Path.cwd() / output
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(WAT).isoformat(timespec="seconds")
    frontmatter = [
        "---",
        "name: run-today-and-yesterday-session-report",
        'title: "Run Today and Yesterday — Session Report"',
        'description: "Redacted, read-only report of all default-profile sessions started in the current and previous WAT day."',
        "version: 1.0.0",
        "author: Alexa",
        "license: MIT",
        "tags: [report, sessions, recall, local-only, run-all-goals]",
        "status: generated",
        f"generated_at_wat: {generated}",
        f"window_start_wat: {start.isoformat(timespec='seconds')}",
        f"window_end_wat_exclusive: {end.isoformat(timespec='seconds')}",
        f"session_count: {len(sessions)}",
        f"message_count_read: {total_messages}",
        f"source_db: {db.expanduser().resolve().as_posix()}",
        "redaction: memory-context-and-secret-patterns-redacted",
        "---",
        "",
        "# Run Today and Yesterday — Session Report",
        "",
        f"Generated **{generated}** from the local default-profile session database.",
        "",
        "## Scope and method",
        "",
        f"- WAT window: **{start.isoformat(timespec='seconds')}** through **{end.isoformat(timespec='seconds')}** (exclusive end).",
        f"- Session selection: sessions whose `started_at` falls inside the WAT window; count **{len(sessions)}**.",
        f"- Messages read back: **{total_messages}** active messages across the selected sessions.",
        "- The reusable prompt must additionally recall each selected session with `session_search` before finalizing the report.",
        "- User, assistant, and tool evidence is bounded and redacted; `<memory-context>` blocks, credentials, tokens, bearer values, and private keys are omitted or replaced with `[REDACTED]`.",
        "- No model calls, network access, configuration writes, profile mutations, commits, or pushes are performed by this builder.",
        "",
        "## Coverage summary",
        "",
        "| Measure | Value |",
        "|---|---:|",
        f"| Sessions found | {len(sessions)} |",
        f"| Active messages read | {total_messages} |",
        f"| Sessions with a title | {sum(bool(s.get('title')) for s in sessions)} |",
        f"| Sessions with at least one tool call | {sum(bool(s.get('tool_call_count')) for s in sessions)} |",
        f"| Sessions without messages on read-back | {empty_sessions} |",
        "",
        "## Per-session outputs",
        "",
        *rendered,
    ]
    output.write_text("\n".join(frontmatter), encoding="utf-8", newline="\n")
    return len(sessions), output


def main() -> int:
    args = parse_args()
    today = args.date
    _, _, current = wat_boundaries(today)
    output = args.output or (DEFAULT_REPORT_DIR / f"run-today-and-yesterday-report-{current.isoformat()}.md")
    count, path = build_report(args.db, output, today)
    print(json.dumps({"status": "generated", "session_count": count, "report": str(path.resolve())}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
