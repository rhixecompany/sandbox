#!/usr/bin/env python3
"""Summarize the five-day default-profile session corpus without secrets."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

WAT = timezone(timedelta(hours=1))


def date_wat(value: Any) -> str:
    if isinstance(value, (int, float)):
        seconds = value / 1000 if value > 10_000_000_000 else value
        return datetime.fromtimestamp(seconds, tz=WAT).date().isoformat()
    text = str(value or "")
    if not text:
        return "unknown"
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(WAT).date().isoformat()
    except ValueError:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default=".hermes/plans/run-all-goals-five-day-session-corpus.json")
    parser.add_argument("output", nargs="?", default=".hermes/plans/run-all-goals-five-day-session-summary.json")
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    sessions = data.get("sessions", [])
    by_day: Counter[str] = Counter()
    by_source: Counter[str] = Counter()
    by_model: Counter[str] = Counter()
    titles: Counter[str] = Counter()
    evidence_count = 0
    evidence_by_keyword: Counter[str] = Counter()
    sessions_with_evidence: list[dict[str, Any]] = []
    keywords = ("goal", "subgoal", "spec", "plan", "prompt", "phase", "task", "action", "run-all-goals")
    for session in sessions:
        timestamp = session.get("started_at") or session.get("matched_epoch") or session.get("created_at")
        by_day[date_wat(timestamp)] += 1
        by_source[str(session.get("source") or "unknown")] += 1
        by_model[str(session.get("model") or "unknown")] += 1
        title = str(session.get("title") or "(untitled)").replace("\n", " ")[:180]
        titles[title] += 1
        evidence = session.get("evidence") or []
        if evidence:
            evidence_count += len(evidence)
            sessions_with_evidence.append({
                "session_id": session.get("session_id"),
                "date_wat": date_wat(timestamp),
                "source": session.get("source"),
                "title": title,
                "evidence": evidence,
            })
            for item in evidence:
                excerpt = str(item.get("excerpt") or "").lower()
                for keyword in keywords:
                    if keyword in excerpt:
                        evidence_by_keyword[keyword] += 1
    summary = {
        "window": data.get("window"),
        "scope": "default profile root state.db; all session sources including cron",
        "database_count": len(data.get("databases", [])),
        "session_count": len(sessions),
        "sessions_with_evidence": len(sessions_with_evidence),
        "evidence_excerpt_count": evidence_count,
        "by_day_wat": dict(sorted(by_day.items())),
        "by_source": dict(sorted(by_source.items())),
        "by_model": dict(sorted(by_model.items())),
        "evidence_by_keyword": dict(sorted(evidence_by_keyword.items())),
        "top_titles": [{"title": title, "count": count} for title, count in titles.most_common(40)],
        "sessions_with_evidence": sessions_with_evidence,
    }
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output_path),
        "session_count": summary["session_count"],
        "sessions_with_evidence": summary["sessions_with_evidence"],
        "evidence_excerpt_count": summary["evidence_excerpt_count"],
        "by_day_wat": summary["by_day_wat"],
        "by_source": summary["by_source"],
        "evidence_by_keyword": summary["evidence_by_keyword"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
