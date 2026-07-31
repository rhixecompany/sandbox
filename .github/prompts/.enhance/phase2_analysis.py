#!/usr/bin/env python3
"""Phase 2: ANALYSIS — detect exact duplicates, frontmatter patterns, semantic overlaps, template candidates.

Deliverables (written to .copilot/session-state/):
- duplicate-clusters.json        exact duplicates grouped by SHA256 of normalized body
- semantic-overlap-flags.json    name/title similarity clusters (manual review)
- template-candidates.json       repeated section patterns suggesting templates
- analysis-manifest.json         combined machine-readable findings
- analysis-manifest.md           human-readable report
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PROMPTS_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / ".copilot" / "session-state"
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)

HEADING_RE = re.compile(r"^#{1,6}\s+.*$", re.MULTILINE)
SECTION_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def split_fm(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    raw = m.group(1)
    data: dict = {}
    for line in raw.splitlines():
        line = line.rstrip()
        if not line or line.startswith(("#", " ", "\t")) or ":" not in line:
            continue
        key, _, val = line.partition(":")
        data[key.strip()] = val.strip().strip("'\"")
    return data, text[m.end():]


def normalize_body(body: str) -> str:
    """Normalize for exact-duplicate detection: strip whitespace variance."""
    return re.sub(r"\s+", " ", body).strip().lower()


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9_\-]{3,}", text.lower()))


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in PROMPTS_DIR.rglob("*") if p.is_file() and (p.suffix == ".md" or p.name.endswith(".prompt.md")))

    records = []
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = split_fm(text)
        rel = str(p.relative_to(PROMPTS_DIR)).replace("\\", "/")
        records.append({
            "path": rel,
            "fm": fm,
            "body": body,
            "norm": normalize_body(body),
            "name": (fm.get("name") or p.stem).lower(),
            "title": (fm.get("title") or p.stem).lower(),
            "tags": [t.strip().lower() for t in re.split(r"[,\s]+", fm.get("tags", "")) if t.strip()],
        })

    # 1) Exact duplicates by normalized body hash
    by_hash: dict[str, list[str]] = defaultdict(list)
    for r in records:
        h = hashlib.sha256(r["norm"].encode("utf-8")).hexdigest()
        by_hash[h].append(r["path"])
    dup_clusters = [{"hash": h, "count": len(paths), "files": paths}
                    for h, paths in by_hash.items() if len(paths) > 1]
    dup_clusters.sort(key=lambda c: -c["count"])

    # 2) Frontmatter patterns
    fm_fields = Counter()
    tag_counter: Counter[str] = Counter()
    name_prefix = Counter()
    for r in records:
        for k in r["fm"]:
            fm_fields[k] += 1
        for t in r["tags"]:
            tag_counter[t] += 1
        stem = r["name"].split("-")[0] if r["name"] else "?"
        name_prefix[stem] += 1

    # 3) Semantic overlaps via jaccard on name+title+tags tokens
    overlap_clusters: list[dict] = []
    used: set[int] = set()
    for i in range(len(records)):
        if i in used:
            continue
        group = [records[i]]
        for j in range(i + 1, len(records)):
            if j in used:
                continue
            a = tokenize(records[i]["name"] + " " + records[i]["title"])
            b = tokenize(records[j]["name"] + " " + records[j]["title"])
            score = jaccard(a, b)
            if score >= 0.6:
                group.append(records[j])
        if len(group) > 1:
            used.update(id(r) for r in group[1:])
            overlap_clusters.append({
                "score_basis": "name+title token jaccard >= 0.6",
                "files": [r["path"] for r in group],
            })

    # 4) Template candidates: repeated section headings
    section_counter: Counter[str] = Counter()
    for r in records:
        for m in SECTION_RE.finditer(r["body"]):
            h = m.group(1).strip().lower()
            if 3 <= len(h) <= 60:
                section_counter[h] += 1
    template_candidates = [
        {"section": heading, "occurrences": count}
        for heading, count in section_counter.most_common(30) if count >= 5
    ]

    manifest = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "scope": str(PROMPTS_DIR),
        "total_prompts": len(records),
        "exact_duplicate_clusters": len(dup_clusters),
        "exact_duplicate_files": sum(c["count"] for c in dup_clusters),
        "semantic_overlap_clusters": len(overlap_clusters),
        "frontmatter_field_counts": dict(fm_fields),
        "top_tags": tag_counter.most_common(20),
        "top_name_prefixes": name_prefix.most_common(20),
        "template_candidate_sections": template_candidates,
    }

    (OUT_DIR / "duplicate-clusters.json").write_text(json.dumps({"generated": manifest["generated"], "clusters": dup_clusters}, indent=2), encoding="utf-8")
    (OUT_DIR / "semantic-overlap-flags.json").write_text(json.dumps({"generated": manifest["generated"], "clusters": overlap_clusters}, indent=2), encoding="utf-8")
    (OUT_DIR / "template-candidates.json").write_text(json.dumps({"generated": manifest["generated"], "candidates": template_candidates}, indent=2), encoding="utf-8")
    (OUT_DIR / "analysis-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    md = f"""# Prompt Library Analysis Manifest

> Generated: {manifest['generated']} | Scope: `.github/prompts/` (717 files)

## Executive Summary

- **Exact duplicate clusters:** {manifest['exact_duplicate_clusters']} ({manifest['exact_duplicate_files']} files)
- **Semantic overlap clusters (manual review):** {manifest['semantic_overlap_clusters']}
- **Template candidate sections:** {len(template_candidates)} shared headings repeated ≥5×
- **Frontmatter fields observed:** {', '.join(k for k in fm_fields)}

## Exact Duplicates

"""
    if dup_clusters:
        for c in dup_clusters[:20]:
            md += f"- **{c['count']}×** `{c['files'][0]}`" + (f" (also: {', '.join(c['files'][1:4])})" if len(c['files']) > 1 else "") + "\n"
    else:
        md += "(none found)\n"

    md += "\n## Semantic Overlap Flags (GATE 1 — manual review required)\n\n"
    if overlap_clusters:
        for c in overlap_clusters[:20]:
            md += "- " + " | ".join(f"`{f}`" for f in c["files"]) + "\n"
    else:
        md += "(none flagged)\n"

    md += "\n## Template Candidates (repeated sections)\n\n| Section | Occurrences |\n|---------|-------------|\n"
    for t in template_candidates:
        md += f"| `{t['section']}` | {t['occurrences']} |\n"

    md += "\n## Top Tags\n\n"
    md += "\n".join(f"- `{t}` ({n})" for t, n in tag_counter.most_common(15)) + "\n"

    md += "\n## Top Name Prefixes\n\n"
    md += "\n".join(f"- `{p}` ({n})" for p, n in name_prefix.most_common(15)) + "\n"
    (OUT_DIR / "analysis-manifest.md").write_text(md, encoding="utf-8")

    print(json.dumps({
        "total_prompts": len(records),
        "exact_duplicate_clusters": len(dup_clusters),
        "exact_duplicate_files": sum(c["count"] for c in dup_clusters),
        "semantic_overlap_clusters": len(overlap_clusters),
        "template_candidates": len(template_candidates),
        "output_dir": str(OUT_DIR),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
