#!/usr/bin/env python3
"""Find duplicate skills on disk by frontmatter name + content similarity.

Read-only analysis. Outputs JSON to results/skills-dup-analysis-2026-09-11.json
and a human list to stdout. Never deletes anything.
"""
from __future__ import annotations

import difflib
import json
import pathlib
import re
import sys

SKILLS = pathlib.Path(__file__).resolve().parent.parent.parent / "AppData" / "Local" / "hermes" / "skills"
if not SKILLS.exists():
    SKILLS = pathlib.Path(r"C:\Users\Alexa\AppData\Local\hermes\skills")

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.S)
NAME_RE = re.compile(r"^name:\s*['\"]?([^'\"]+?)['\"]?\s*$", re.M)


def frontmatter_name(text: str) -> str | None:
    m = FM_RE.search(text)
    if not m:
        return None
    nm = NAME_RE.search(m.group(1))
    return nm.group(1).strip() if nm else None


def norm(name: str) -> str:
    return name.strip().lower().replace("_", "-").replace(" ", "-")


def walk_skills() -> list[dict]:
    out = []
    for sk in sorted(SKILLS.rglob("SKILL.md")):
        if any(".quarantine" in p for p in sk.parts):
            continue
        try:
            text = sk.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        name = frontmatter_name(text) or sk.parent.name
        rel = sk.relative_to(SKILLS)
        is_category = len(rel.parts) >= 3  # skills/<category>/<name>/SKILL.md
        out.append(
            {
                "path": str(rel),
                "name": name,
                "norm": norm(name),
                "lines": text.count("\n") + 1,
                "version": re.search(r"^version:\s*(\S+)", text, re.M).group(1) if re.search(r"^version:\s*(\S+)", text, re.M) else "",
                "category": rel.parts[0] if is_category else "",
                "in_category": is_category,
                "body": text,
            }
        )
    return out


def main() -> int:
    skills = walk_skills()
    by_norm: dict[str, list[dict]] = {}
    for s in skills:
        by_norm.setdefault(s["norm"], []).append(s)

    exact = {k: v for k, v in by_norm.items() if len(v) > 1}
    # near-exact: different names, one in category, body similarity >= 0.9
    near: list[tuple[dict, dict, float]] = []
    for i, a in enumerate(skills):
        for b in skills[i + 1 :]:
            if a["norm"] == b["norm"] or a["in_category"] == b["in_category"]:
                continue
            if a["name"] == b["name"]:
                continue
            la, lb = len(a["body"]), len(b["body"])
            if la == 0 or lb == 0 or max(la, lb) / min(la, lb) > 1.15:
                continue  # length gate: near-dups have near-equal bodies
            if a["norm"][:8] != b["norm"][:8]:
                continue  # name-prefix gate: candidates must share prefix
            ratio = difflib.SequenceMatcher(None, a["body"], b["body"]).ratio()
            if ratio >= 0.9:
                near.append((a, b, round(ratio, 3)))

    out = {
        "total_skills": len(skills),
        "exact_duplicate_clusters": len(exact),
        "exact_duplicate_paths": sum(len(v) for v in exact.values()),
        "near_duplicate_pairs": len(near),
        "clusters": [
            {
                "name": k,
                "paths": [
                    {"path": v["path"], "lines": v["lines"], "version": v["version"], "in_category": v["in_category"]}
                    for v in vals
                ],
            }
            for k, vals in sorted(exact.items())
        ],
        "near_pairs": [
            {"a": a["path"], "b": b["path"], "similarity": r, "name_a": a["name"], "name_b": b["name"]}
            for a, b, r in sorted(near, key=lambda t: -t[2])
        ],
    }
    outfile = pathlib.Path(__file__).resolve().parent.parent / "results" / "skills-dup-analysis-2026-09-11.json"
    outfile.parent.mkdir(exist_ok=True)
    outfile.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"total skills: {len(skills)}")
    print(f"exact duplicate clusters: {len(exact)} ({sum(len(v) for v in exact.values())} paths)")
    print(f"near duplicate pairs: {len(near)}")
    print("\n=== EXACT CLUSTERS ===")
    for k, vals in sorted(exact.items()):
        cat = [v["path"] for v in vals if v["in_category"]]
        flat = [v["path"] for v in vals if not v["in_category"]]
        print(f"\n{k}:")
        for v in vals:
            print(f"  {v['path']} ({v['lines']}L v{v['version']})")
        print(f"  -> category: {cat or 'NONE'} | flat: {flat}")
    print("\n=== NEAR PAIRS (>=0.9) ===")
    for a, b, r in sorted(near, key=lambda t: -t[2])[:40]:
        print(f"  {r:.3f} {a['path']}  <->  {b['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())