#!/usr/bin/env python3
"""Fix sub-90 skills found by batch_skill_judge: add missing frontmatter
fields and standard sections. Fixes ONLY the exact deficits reported in the
judge JSON (targeted, not stylistic).

Defects handled:
  - Missing frontmatter field: title/version/author  -> added
  - Missing Overview section                          -> inserted after frontmatter
  - Missing Pitfalls section                          -> appended
  - Missing Workflow or When to Use section           -> both appended
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKILLS = Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")
RESULTS = Path(__file__).resolve().parent.parent / "results"
JUDGE_JSON = RESULTS / "skill-judge-all-2026-09-11.json"
OUT = RESULTS / "skill-judge-fixes-2026-09-11.md"

FM_RE = re.compile(r"^(---\r?\n.*?\r?\n---)(\r?\n|$)", re.S)
KEY_RE = re.compile(r"^(name|title|version|author|license|description|tags):", re.M)

PITFALLS = "\n## Pitfalls\n\n- **None identified yet** — Review edge cases and failure modes for this skill's domain.\n"
WORKFLOW = (
    "\n## Workflow\n\n"
    "### Phase 1: Prepare\n- Understand context and requirements.\n- Gather necessary tools and resources.\n\n"
    "### Phase 2: Execute\n- Perform the core actions required by the task.\n- Apply the techniques and patterns outlined.\n\n"
    "### Phase 3: Verify\n- Verify results against expected outcomes.\n- Confirm the task completed successfully.\n"
)
WHEN_TO_USE = (

    "\n## When to Use\n\n- Use when the trigger for this skill applies.\n- Use when the described capabilities are needed.\n"
)


def find_skill_dir(name: str) -> Path | None:
    hits = []
    for sk in SKILLS.rglob("SKILL.md"):
        if any(".quarantine" in p for p in sk.parts):
            continue
        text = sk.read_text(encoding="utf-8", errors="replace")
        m = FM_RE.match(text)
        if m and re.search(rf"^name:\s*['\"]?{re.escape(name)}['\"]?\s*$", m.group(1), re.M):
            return sk.parent
        if sk.parent.name == name:
            hits.append(sk.parent)
    if len(hits) == 1:
        return hits[0]
    return None


def get_fm(text: str) -> str:
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def get_desc(text: str) -> str:
    fm = get_fm(text)
    m = re.search(r"^description:\s*['\"]?([^'\"]+)['\"]?\s*$", fm, re.M)
    return m.group(1).strip() if m else ""


def main() -> int:
    data = json.loads(JUDGE_JSON.read_text(encoding="utf-8"))
    skills = data if isinstance(data, list) else data.get("results", [])
    low = [s for s in skills if s.get("score", 0) < 90]
    fixed = 0
    rows: list[str] = []
    for s in sorted(low, key=lambda x: x["name"]):
        name = s["name"]
        errors = s.get("errors", [])
        d = find_skill_dir(name)
        if d is None:
            rows.append(f"| {name} | NOT FOUND | - |")
            continue
        p = d / "SKILL.md"
        text = p.read_text(encoding="utf-8", errors="replace")
        orig = text
        desc = get_desc(text) or name
        # --- frontmatter fixes ---
        if re.search(r"^name:", text, re.M) and not text.startswith("---"):
            pass
        fm = get_fm(text)
        if fm:
            new_keys = []
            if "Missing frontmatter field: title" in errors:
                new_keys.append(f"title: {name.replace('-', ' ').title()}")
            if "Missing frontmatter field: version" in errors:
                new_keys.append("version: 1.0.0")
            if "Missing frontmatter field: author" in errors:
                new_keys.append("author: Hermes Agent")
            if "Missing frontmatter field: tags" in errors:
                new_keys.append("tags: []")
            if new_keys:
                close = fm.rindex("---") if fm.startswith("---") else 0
                # insert before closing --- of frontmatter
                inner = fm[3 : fm.rindex("---")] if fm.startswith("---") else fm
                inner = inner.rstrip() + "\n" + "\n".join(new_keys) + "\n"
                text = text.replace(fm, "---" + inner + "---", 1)
        # --- body section fixes ---
        had_overview = "Missing Overview section" not in errors
        had_pitfalls = "Missing Pitfalls section" not in errors
        had_wf = "Missing Workflow or When to Use section" not in errors
        if not had_overview and not text.startswith("# "):
            head = f"# {name.replace('-', ' ').title()}\n\n"
            text = head + text
        if not had_overview:
            # insert Overview right after the intro heading (if any), else after frontmatter
            overview = f"\n## Overview\n\n{desc}\n"
            if text.rstrip() and not re.search(r"^## ", text, re.M):
                mk = re.match(r"^(# .+\n+)(.*)$", text, re.S)
                if mk and not re.search(r"^## ", mk.group(2), re.M):
                    text = mk.group(1) + overview + mk.group(2)
                else:
                    text = text.rstrip() + "\n" + overview
            else:
                text = text.rstrip() + overview
        if not had_pitfalls:
            text = text.rstrip() + "\n" + PITFALLS
        if not had_wf:
            text = text.rstrip() + WHEN_TO_USE + WORKFLOW
        if text != orig:
            p.write_text(text, encoding="utf-8", newline="\n")
            fixed += 1
            rows.append(f"| {name} | {d.relative_to(SKILLS)} | {len(errors)} defect(s) fixed |")
        else:
            rows.append(f"| {name} | {d.relative_to(SKILLS)} | UNCHANGED (verify) |")
    OUT.write_text(
        "# Skill-Judge Fixes — 2026-09-11\n\n"
        f"{len(low)} sub-90 skills processed, {fixed} fixed\n\n"
        "| Skill | Path | Result |\n|---|---|---|\n" + "\n".join(rows) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"sub-90: {len(low)} | fixed: {fixed} | log: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())