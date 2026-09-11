#!/usr/bin/env python3
"""Dedupe skills: keep best canonical copy, merge unique sections, quarantine rest.

Policy (user-approved): near-exact duplicates -> keep canonical (category-placed,
else richer) copy, enhance it by merging sections missing from deleted copies,
quarantine duplicates (recoverable), log everything. Re-run the analyzer after
this completes to verify zero remaining clusters.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
RESULTS = Path(__file__).resolve().parent.parent / "results"
ANALYSIS = RESULTS / "skills-dup-analysis-2026-09-11.json"
QUARANTINE = SKILLS / ".quarantine-2026-09-11"
LOG = RESULTS / "skills-deduped-2026-09-11.md"

HEADING_RE = re.compile(r"^#{1,3} .+$", re.M)


def section_map(text: str) -> dict[str, str]:
    """heading -> section text (heading to next heading, incl. body-only prefix '')."""
    lines = text.splitlines()
    sections: dict[str, list[str]] = {}
    cur = ""
    for ln in lines:
        if HEADING_RE.match(ln):
            cur = ln
            sections.setdefault(cur, [ln])
        else:
            sections.setdefault(cur, []).append(ln)
    return {k: "\n".join(v) for k, v in sections.items()}


def choose_keeper(copies: list) -> Path:
    """Category-placed copy wins (relative depth >= 3), then most lines."""
    return max(
        copies,
        key=lambda p: (len(p.relative_to(SKILLS).parts) >= 3, sum(1 for _ in p.open(encoding="utf-8", errors="replace"))),
    )


def main() -> int:
    data = json.loads(ANALYSIS.read_text(encoding="utf-8"))
    clusters = data["clusters"]
    QUARANTINE.mkdir(exist_ok=True)
    log_lines = [
        "# Skills Deduplication Log — 2026-09-11 (pass 2)",
        "",
        f"Scanned: {data['total_skills']} readable SKILL.md files | "
        f"clusters: {len(clusters)} | dup paths: {data['exact_duplicate_paths']}",
        "",
        "| Keeper | Deleted (quarantined) | Merge actions |",
        "|---|---|---|",
    ]
    deleted_total = 0
    skipped = 0
    for cluster in clusters:
        paths = [
            Path(SKILLS / p["path"]) for p in cluster["paths"]
        ]
        copies = [p for p in paths if p.exists()]
        if len(copies) < 2:
            continue
        keeper = choose_keeper(copies)
        keeper_text = keeper.read_text(encoding="utf-8", errors="replace")
        keeper_sections = section_map(keeper_text)
        merges: list[str] = []
        for dup in copies:
            if dup == keeper:
                continue
            try:
                dup_text = dup.read_text(encoding="utf-8", errors="replace")
            except OSError:
                skipped += 1
                continue
            for h, sec in section_map(dup_text).items():
                if h and h not in keeper_sections and not h.startswith("# Merged from duplicates"):
                    merges.append(sec)
            target = QUARANTINE / dup.relative_to(SKILLS).parent.name
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                shutil.rmtree(target)
            shutil.move(str(dup.parent), str(target))
            deleted_total += 1
        if merges:
            # insert merged sections before a References section, else append
            insert_before = None
            for i, ln in enumerate(keeper_text.splitlines()):
                if re.match(r"^#{1,2} References", ln):
                    insert_before = i
                    break
            if insert_before is not None:
                lines = keeper_text.splitlines()
                merged_blob = "\n\n".join(merges)
                lines.insert(insert_before, f"\n\n## Merged from duplicates\n\n{merged_blob}")
                keeper_text = "\n".join(lines)
            else:
                keeper_text = keeper_text.rstrip() + "\n\n## Merged from duplicates\n\n" + "\n\n".join(merges) + "\n"
            keeper.write_text(keeper_text, encoding="utf-8", newline="\n")
        log_lines.append(
            f"| {keeper.relative_to(SKILLS)} | {', '.join(str(p.relative_to(SKILLS)) for p in copies if p != keeper)} | {len(merges)} section(s) merged |"
        )
    LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8", newline="\n")
    print(f"clusters processed: {len(clusters)} | duplicates quarantined: {deleted_total}")
    print(f"log: {LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())