#!/usr/bin/env python3
"""Score all .md files on AI-readiness (0-100).

Usage:
    python scripts/score-docs.py <target_directory>

Scoring criteria:
  - YAML frontmatter present (+20)
  - Summary paragraph after H1 heading (+15)
  - Language-tagged code blocks (+10 each, max +30)
  - Resolvable relative cross-references (+10 each, max +20)
  - Section header density: H2/H3 every <200 lines (+15)
  - Penalty: >500 lines with no H2/H3 headers (-20)
"""
import os
import re
import sys
from datetime import datetime

TARGET_DIR = sys.argv[1] if len(sys.argv) > 1 else "."
OUTPUT_FILE = os.path.join(TARGET_DIR, "docs/ai-readiness-report.md")


def score_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception:
        return None

    total_lines = content.count("\n")
    score = 0
    fm_score = summary_score = lang_score = xref_score = struct_score = penalty = 0
    lines = content.split("\n")

    # Criterion 1: YAML frontmatter (+20)
    if content.startswith("---"):
        fm_score = 20
        score += 20

    # Criterion 2: Summary after H1 (+15)
    h1_idx = next((i for i, line in enumerate(lines) if line.startswith("# ") and not line.startswith("## ")), None)
    if h1_idx is not None:
        after_h1 = " ".join(lines[h1_idx + 1 : h1_idx + 4]).strip()
        if len(after_h1) >= 30 and any(c.isalpha() for c in after_h1):
            summary_score = 15
            score += 15

    # Criterion 3: Language-tagged code blocks (+30 max)
    lang_count = len(re.findall(r"^```[a-zA-Z]", content, re.MULTILINE))
    lang_score = min(lang_count * 10, 30)
    score += lang_score

    # Criterion 4: Resolvable cross-refs (+20 max)
    file_dir = os.path.dirname(filepath)
    xref_count = 0
    for match in re.finditer(r"\[.*?\]\((\.\.?/[^)]+)\)", content):
        link = match.group(1).split("#")[0]
        if not link.startswith("http") and os.path.isfile(os.path.normpath(os.path.join(file_dir, link))):
            xref_count += 1
    xref_score = min(xref_count * 10, 20)
    score += xref_score

    # Criterion 5: Header density (+15)
    header_count = len(re.findall(r"^## |^### ", content, re.MULTILINE))
    if total_lines > 0 and header_count > 0:
        if total_lines / header_count < 200:
            struct_score = 15
            score += 15

    # Penalty: wall of text (-20)
    if total_lines > 500 and header_count == 0:
        penalty = 20
        score -= 20

    score = max(0, score)
    verdict = "AI-READY \u2705" if score >= 70 else "NEEDS WORK \u26a0\ufe0f" if score >= 40 else "REWRITE \u274c"
    return {"file": os.path.relpath(filepath, TARGET_DIR), "score": score, "fm": fm_score,
            "summary": summary_score, "lang": lang_score, "xref": xref_score,
            "struct": struct_score, "penalty": penalty, "verdict": verdict}


def main():
    results = []
    excluded = {"node_modules", ".git", "__pycache__", ".hermes", "archive"}
    exclusions = excluded | set()

    for root, dirs, files in os.walk(TARGET_DIR):
        dirs[:] = [d for d in dirs if d not in exclusions and not any(e in root.split(os.sep) for e in exclusions)]
        for fname in files:
            if fname.endswith(".md"):
                r = score_file(os.path.join(root, fname))
                if r:
                    results.append(r)

    results.sort(key=lambda r: r["score"])
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("---\ntitle: AI-Readiness Report\ndescription: Scoring of %d markdown files on AI-readiness metrics.\n" % len(results))
        f.write("status: final\ntags: [ai-readiness, documentation, quality]\ngenerated: %s\n---\n\n" % datetime.now().strftime('%Y-%m-%d'))
        f.write("# AI-Readiness Report\n\n**Files scored**: %d\n\n" % len(results))
        f.write("| # | File | FM+20 | Sum+15 | Lang+30 | XRef+20 | Struct+15 | Pen | **Score** | Verdict |\n")
        f.write("|---|------|-------|--------|---------|---------|-----------|-----|-----------|--------|\n")
        for i, r in enumerate(results, 1):
            f.write("| %d | %s | %d | %d | %d | %d | %d | -%d | **%d** | %s |\n" % (
                i, r['file'], r['fm'], r['summary'], r['lang'], r['xref'], r['struct'], r['penalty'], r['score'], r['verdict']))

        ready = sum(1 for r in results if r["score"] >= 70)
        needs = sum(1 for r in results if 40 <= r["score"] < 70)
        rewrite = sum(1 for r in results if r["score"] < 40)
        avg = sum(r["score"] for r in results) / len(results) if results else 0

        f.write("\n## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total | %d |\n| Average | %.1f |\n| AI-ready (>=70) | %d |\n| Needs work (40-69) | %d |\n| Rewrite (<40) | %d |\n" % (len(results), avg, ready, needs, rewrite))

        no_fm = sum(1 for r in results if r["fm"] == 0)
        no_sum = sum(1 for r in results if r["summary"] == 0)
        no_lang = sum(1 for r in results if r["lang"] == 0)
        no_xref = sum(1 for r in results if r["xref"] == 0)
        wall = sum(1 for r in results if r["struct"] == 0 and r["penalty"] > 0)

        f.write("\n## Issues\n\n| Issue | Affected | Fix |\n|-------|----------|-----|\n")
        f.write("| Missing frontmatter | %d | Add `---\\ntitle: ...\\n---` |\n" % no_fm)
        f.write("| Missing summary | %d | 2-3 sentences after H1 |\n" % no_sum)
        f.write("| No lang-tagged code | %d | Use ```sh, ```json etc. |\n" % no_lang)
        f.write("| No cross-refs | %d | Relative-path internal links |\n" % no_xref)
        f.write("| Wall-of-text | %d | Break with H2/H3 |\n" % wall)

    print("Report: %s\nScored: %d | Avg: %.1f | Ready: %d | Needs: %d | Rewrite: %d" % (
        OUTPUT_FILE, len(results), avg, ready, needs, rewrite))


if __name__ == "__main__":
    main()
