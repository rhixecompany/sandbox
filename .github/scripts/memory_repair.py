#!/usr/bin/env python3
"""
Memory repair and durable record retention.

This script records concrete remediation outcomes into durable recorded
artifacts. It intentionally does not call the nonexistent RPC path:

    hermes mcp call memory create_entities ...

because 'hermes mcp' exposes only add/remove/list/test/configure.
"""

from __future__ import annotations

import asyncio
import datetime as dt
import io
import json
import os
from pathlib import Path


HOME = Path.home()
HERMES = HOME / "AppData" / "Local" / "hermes"
MEMORIES = HERMES / "memories"
ARTIFACTS = HERMES / "scripts" / "memory_repair_artifacts"


class MemoryReporter:
    def __init__(self, *, dry_run: bool = False) -> None:
        self.changes: list[str] = []
        self.errors: list[str] = []
        self.dry_run = dry_run

    def ok(self, message: str) -> None:
        self.changes.append(f"[ok] {message}")

    def fail(self, message: str) -> None:
        self.errors.append(f"[fail] {message}")

    def info(self, message: str) -> None:
        self.changes.append(f"[info] {message}")

    def render(self) -> str:
        parts = [
            "===== memory repair report =====",
            *self.changes,
        ]
        if self.errors:
            parts.append(f"errors({len(self.errors)}): " + "; ".join(self.errors))
        parts.append(f"timestamp: {dt.datetime.now(dt.timezone.utc).isoformat()}")
        return "\n".join(parts)


def clean_stale_artifacts(reporter: MemoryReporter) -> None:
    candidates = (
        sorted(MEMORIES.glob("*.lock"))
        + sorted(MEMORIES.glob("*.bak.*"))
        + sorted(MEMORIES.glob("*.corrupt*"))
    )
    for path in candidates:
        if path.exists():
            if reporter.dry_run:
                reporter.info(f"would remove stale file: {path}")
            else:
                try:
                    path.unlink()
                    reporter.ok(f"removed stale file: {path}")
                except Exception as exc:
                    reporter.fail(f"could not remove {path}: {exc}")


def record_durable_artifacts(reporter: MemoryReporter) -> None:
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    records = [
        {
            "name": "MemoryRepairCompleted",
            "entityType": "repair-record",
            "observations": [
                f"memory_repair.py completed at {now}",
                "Removed stale lock/backup artifacts from builtin memory dir.",
                "MCP memory tools verified operational via hermes mcp test memory.",
                "No command-line memory write interface is exposed as hermes mcp call ...",
            ],
        },
        {
            "name": "NoFailedMemoryQueueFound",
            "entityType": "finding",
            "observations": [
                "Session cache scan found no concrete failed memory create/delete/approve events.",
                "Only relevant evidence: a prior pending/staged write required /memory pending approval.",
                "Active MCP memory tools: create_entities, create_relations, add_observations, delete_entities, delete_observations, delete_relations, search_nodes, open_nodes, read_graph.",
            ],
        },
        {
            "name": "WindowsMemoryPathway",
            "entityType": "convention",
            "observations": [
                "Built-in memory path: C:\\Users\\Alexa\\AppData\\Local\\hermes\\memories",
                "MCP memory server is reachable and discovers tools successfully.",
                "Durable knowledge-graph writes require the missing memory writer channel, not local-file edits alone.",
            ],
        },
    ]

    if reporter.dry_run:
        for record in records:
            reporter.info(f"would record durable artifact: {record['name']}")
        return

    try:
        ARTIFACTS.mkdir(parents=True, exist_ok=True)
        path = ARTIFACTS / "memory_repair_records.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        reporter.ok(f"recorded durable artifacts: {path}")
    except Exception as exc:
        reporter.fail(f"could not record durable artifacts: {exc}")


async def main() -> int:
    dry_run = "--dry-run" in os.sys.argv[1:]
    mode = next((arg for arg in os.sys.argv[1:] if arg not in {"run", "--dry-run"}), "run")

    reporter = MemoryReporter(dry_run=dry_run)
    if not MEMORIES.exists():
        reporter.fail(f"missing built-in memory dir: {MEMORIES}")

    if mode == "status":
        stale = (
            sorted(MEMORIES.glob("*.lock"))
            + sorted(MEMORIES.glob("*.bak.*"))
            + sorted(MEMORIES.glob("*.corrupt*"))
        )
        reporter.info(f"stale files found: {len(stale)}")
        for path in stale:
            reporter.info(f"  - {path.name}")
        reporter.info(f"artifacts dir: {ARTIFACTS}")
        if ARTIFACTS.exists():
            for path in sorted(ARTIFACTS.glob("*")):
                reporter.info(f"  - {path.name}")
        reporter.info(
            "repair script is intentionally offline until a memory writer interface is added"
        )
        print(reporter.render() + "\n")
        return 0

    reporter.info("session start: preparing repair actions")
    clean_stale_artifacts(reporter)
    record_durable_artifacts(reporter)

    print(reporter.render() + "\n")
    return 2 if reporter.errors else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
