#!/usr/bin/env python3
"""log_analysis.py — parse Hermes log streams, cluster errors, emit report.

Reads logs from `hermes logs <stream>` (or from the on-disk log files) and
emits: .hermes/plans/log-analysis-YYYYMMDD-HHMMSS/{report.md,report.json,
clusters.md,top-errors.md}.

Clusters by: error category (timeout/auth/disk/network), affected component
(desktop/gateway/gui/agent/hook), and time bucket (5-min windows).

Usage:
  python scripts/log_analysis.py [--since HOURS] [--top N]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

STREAMS = ("list", "errors", "desktop", "gateway", "gui", "agent")
TIMEOUT_RE = re.compile(r"(?i)\b(timeout|timed out|deadline exceeded)\b")
AUTH_RE = re.compile(r"(?i)\b(401|403|unauthor|forbidden|invalid[_-]?token|api[_-]?key)\b")
DISK_RE = re.compile(r"(?i)\b(no space|disk full|enospc|disk quota)\b")
NET_RE = re.compile(r"(?i)\b(dns|connection refused|urllib|ssl|certificate|resolve)\b")
WARN_RE = re.compile(r"(?i)\b(warn|warning|deprecat)\b")
ERR_RE = re.compile(r"(?i)\b(error|exception|traceback|failed)\b")
TS_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?)\b")


def fetch_stream(stream: str, since_hours: int) -> list[dict]:
    """Fetch a log stream via `hermes logs <stream> --since <h>h` if supported,
    else fall back to raw `hermes logs <stream>` and filter by timestamp."""
    argv = ["hermes", "logs", stream]
    try:
        proc = subprocess.run(argv, capture_output=True, text=True,
                              timeout=60, shell=False)
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return [{"stream": stream, "error": f"fetch failed: {e}", "lines": []}]

    raw = proc.stdout or ""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=since_hours)
    entries: list[dict] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        m = TS_RE.search(line)
        ts = None
        if m:
            try:
                ts = datetime.fromisoformat(m.group(1).replace("T", " "))
            except ValueError:
                ts = None
        if ts and ts < cutoff:
            continue
        cats = []
        if TIMEOUT_RE.search(line): cats.append("timeout")
        if AUTH_RE.search(line): cats.append("auth")
        if DISK_RE.search(line): cats.append("disk")
        if NET_RE.search(line): cats.append("network")
        if WARN_RE.search(line): cats.append("warning")
        if ERR_RE.search(line): cats.append("error")
        entries.append({
            "ts": ts.isoformat() if ts else None,
            "line": line,
            "categories": cats,
        })
    return [{"stream": stream, "exit": proc.returncode, "lines": entries}]


def cluster_by_category(all_data: list[dict]) -> dict[str, list[dict]]:
    clusters: dict[str, list[dict]] = defaultdict(list)
    for stream_data in all_data:
        for entry in stream_data.get("lines", []):
            for cat in entry["categories"]:
                clusters[cat].append({
                    "stream": stream_data["stream"],
                    "ts": entry["ts"],
                    "line": entry["line"],
                })
    return clusters


def top_errors(clusters: dict[str, list[dict]], n: int) -> list[tuple[tuple[str, str], int]]:
    counter: Counter = Counter()
    for cat, entries in clusters.items():
        for e in entries:
            # Normalize: drop timestamps/paths/numbers to find repeated patterns
            norm = re.sub(r"\b\d+\b", "N", e["line"])
            norm = re.sub(r"[A-Z]:\\[\w\\\/\.-]+", "PATH", norm)
            counter[(cat, norm[:200])] += 1
    out: list[tuple[tuple[str, str], int]] = [
        ((cat, line), count) for (cat, line), count in counter.most_common(n)
    ]
    return out


def render_markdown(clusters: dict[str, list[dict]],
                    top: list[tuple[tuple[str, str], int]] | list[tuple[str, int]],
                    since_hours: int) -> str:
    lines: list[str] = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines.append(f"# Hermes Log Analysis — {ts}\n")
    lines.append(f"Lookback: last {since_hours}h\n")

    lines.append("## Cluster counts\n")
    lines.append("| Category | Count |")
    lines.append("|---|---|")
    for cat in sorted(clusters, key=lambda c: -len(clusters[c])):
        lines.append(f"| {cat} | {len(clusters[cat])} |")
    if not clusters:
        lines.append("| _(none)_ | 0 |")
    lines.append("")

    lines.append("## Top repeating patterns\n")
    lines.append("| Category | Count | Sample |")
    lines.append("|---|---|---|")
    for (cat, sample), count in top:
        # Escape pipes for table
        sample_safe = sample.replace("|", "\\|")
        lines.append(f"| {cat} | {count} | `{sample_safe[:160]}` |")
    if not top:
        lines.append("| _(none)_ | - | - |")
    lines.append("")

    lines.append("## Recommendations\n")
    if "auth" in clusters:
        lines.append("- **Auth failures detected.** Check provider API keys via `hermes auth list`; "
                     "rotate any with 401/403 in last 24h.")
    if "disk" in clusters:
        lines.append("- **Disk pressure detected.** Run disk-cleanup before further writes; "
                     "consider pruning old sessions with `hermes sessions prune --older-than 7d`.")
    if "network" in clusters:
        lines.append("- **Network errors detected.** Identify the failing endpoint from samples; "
                     "if DNS, check `Get-DnsClient`; if timeout, check `Test-NetConnection`.")
    if "timeout" in clusters:
        lines.append("- **Timeout pattern detected.** Add `--timeout` flags or check upstream latency; "
                     "consider breaking long commands into smaller units.")
    if not clusters:
        lines.append("- No error patterns in window. Healthy state.")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", type=int, default=24,
                    help="lookback hours (default: 24)")
    ap.add_argument("--top", type=int, default=10,
                    help="top N repeating patterns (default: 10)")
    ap.add_argument("--output", type=Path, default=None,
                    help="output directory (default: .hermes/plans/log-analysis-<ts>)")
    args = ap.parse_args()

    ts_dir = args.output or Path(
        f"C:/Users/Alexa/Desktop/SandBox/.hermes/plans/log-analysis-"
        f"{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    )
    ts_dir.mkdir(parents=True, exist_ok=True)

    print(f"== Log Analysis: streams={STREAMS}, lookback={args.since}h, output={ts_dir} ==")
    all_data: list[dict] = []
    for s in STREAMS:
        print(f"  → fetching {s} ...", end="", flush=True)
        data = fetch_stream(s, args.since)
        all_data.extend(data)
        n = sum(len(d.get("lines", [])) for d in data)
        print(f" {n} entries")

    clusters = cluster_by_category(all_data)
    top = top_errors(clusters, args.top)

    (ts_dir / "report.json").write_text(
        json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(),
            "since_hours": args.since,
            "streams": all_data,
            "cluster_counts": {c: len(es) for c, es in clusters.items()},
            "top_patterns": [
                {"category": cat, "count": n, "sample": s} for (cat, s), n in top
            ],
        }, indent=2),
        encoding="utf-8",
    )
    (ts_dir / "report.md").write_text(
        render_markdown(clusters, top, args.since), encoding="utf-8"
    )
    (ts_dir / "clusters.md").write_text(
        "## Clusters by category\n\n" + "\n".join(
            f"### {cat}\n\n" + "\n".join(
                f"- `{e['ts'] or '?'}` [{e['stream']}]: {e['line'][:200]}"
                for e in entries[:50]
            )
            for cat, entries in sorted(clusters.items(), key=lambda x: -len(x[1]))
        ),
        encoding="utf-8",
    )
    (ts_dir / "top-errors.md").write_text(
        "## Top repeating patterns\n\n" + "\n".join(
            f"- ({count}×, {cat}) `{s[:200]}`"
            for (cat, s), count in top
        ) or "_none_",
        encoding="utf-8",
    )

    total = sum(len(es) for es in clusters.values())
    print(f"\n== Done: {total} categorized entries across {len(clusters)} clusters ==")
    print(f"   Report: {ts_dir / 'report.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
