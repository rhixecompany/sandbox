#!/usr/bin/env python3
"""Score all .md files on AI-readiness (0-100)."""
import os
import re
import sys
import json
from datetime import datetime

TARGET_DIR = sys.argv[1] if len(sys.argv) > 1 else "."
OUTPUT_FILE = "docs/ai-readiness-report.md"


def score_file(filepath):
    """Score a single markdown file on AI-readiness."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception:
        return None

    total_lines = content.count("\n")
    score = 0
    fm_score = 0
    summary_score = 0
    lang_score = 0
    xref_score = 0
    struct_score = 0
    penalty = 0
    lines = content.split("\n")

    # Criterion 1: YAML frontmatter present (+20)
    if content.startswith("---"):
        fm_score = 20
        score += 20

    # Criterion 2: Summary paragraph in first 3 lines after H1 (+15)
    h1_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            h1_idx = i
            break
    if h1_idx is not None:
        after_h1 = lines[h1_idx + 1 : h1_idx + 4]
        summary_text = " ".join(after_h1).strip()
        if len(summary_text) >= 30 and any(c.isalpha() for c in summary_text):
            summary_score = 15
            score += 15

    # Criterion 3: Language-tagged code blocks (+10 each, max +30)
    lang_count = len(re.findall(r"^```[a-zA-Z]", content, re.MULTILINE))
    lang_score = min(lang_count * 10, 30)
    score += lang_score

    # Criterion 4: Relative cross-refs that resolve (+10 each, max +20)
    file_dir = os.path.dirname(filepath)
    xref_count = 0
    for match in re.finditer(r"\[.*?\]\((\.\.?/[^)]+)\)", content):
        link = match.group(1)
        # Skip anchors and external URLs
        if link.startswith("http"):
            continue
        if "#" in link:
            link = link.split("#")[0]
        target = os.path.normpath(os.path.join(file_dir, link))
        if os.path.isfile(target):
            xref_count += 1
    xref_score = min(xref_count * 10, 20)
    score += xref_score

    # Criterion 5: H2/H3 break every <200 lines (+15)
    header_count = len(re.findall(r"^## |^### ", content, re.MULTILINE))
    if total_lines > 0 and header_count > 0:
        lines_per_header = total_lines / header_count
        if lines_per_header < 200:
            struct_score = 15
            score += 15

    # Penalty: >500 lines with no H2/H3 (-20)
    if total_lines > 500 and header_count == 0:
        penalty = 20
        score -= 20

    score = max(0, score)

    if score >= 70:
        verdict = "AI-READY ✅"
    elif score >= 40:
        verdict = "NEEDS WORK ⚠️"
    else:
        verdict = "REWRITE ❌"

    rel_path = os.path.relpath(filepath, TARGET_DIR)

    return {
        "file": rel_path,
        "score": score,
        "fm": fm_score,
        "summary": summary_score,
        "lang": lang_score,
        "xref": xref_score,
        "struct": struct_score,
        "penalty": penalty,
        "verdict": verdict,
    }


def main():
    results = []
    excluded = {"node_modules", ".git", "__pycache__", ".hermes", "archive", "node_modules/"}

    for root, dirs, files in os.walk(TARGET_DIR):
        # Skip excluded directories at any depth
        dirs[:] = [d for d in dirs if d not in excluded and not any(e in root.split(os.sep) for e in excluded)]
        # Only score docs/ and Bash/docs/ — skip project dirs, node_modules, .git
        if "/projects/" in root or "\\projects\\" in root:
            continue
        if "/Bash/node_modules/" in root or "\\Bash\\node_modules\\" in root:
            continue
        for fname in files:
            if fname.endswith(".md"):
                fpath = os.path.join(root, fname)
                result = score_file(fpath)
                if result:
                    results.append(result)

    results.sort(key=lambda r: r["score"])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("title: AI-Readiness Report\n")
        f.write(f"description: Scoring of {len(results)} markdown files on AI-readiness metrics.\n")
        f.write("status: final\n")
        f.write("tags: [ai-readiness, documentation, quality]\n")
        f.write(f"generated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("---\n\n")
        f.write(f"# AI-Readiness Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n")
        f.write(f"**Scope**: `{TARGET_DIR}`  \n")
        f.write(f"**Files scored**: {len(results)}\n\n")
        f.write("| # | File | FM+20 | Sum+15 | Lang+30 | XRef+20 | Struct+15 | Pen | **Score** | Verdict |\n")
        f.write("|---|------|-------|--------|---------|---------|-----------|-----|-----------|--------|\n")

        for i, r in enumerate(results, 1):
            f.write(
                f"| {i} | {r['file']} | {r['fm']} | {r['summary']} | {r['lang']} | "
                f"{r['xref']} | {r['struct']} | -{r['penalty']} | **{r['score']}** | {r['verdict']} |\n"
            )

        # Summary stats
        ready = sum(1 for r in results if r["score"] >= 70)
        needs_work = sum(1 for r in results if 40 <= r["score"] < 70)
        rewrite = sum(1 for r in results if r["score"] < 40)
        avg_score = sum(r["score"] for r in results) / len(results) if results else 0

        f.write("\n## Summary\n\n")
        f.write("| Metric | Count |\n")
        f.write("|--------|-------|\n")
        f.write(f"| Total files scored | {len(results)} |\n")
        f.write(f"| Average score | {avg_score:.1f} |\n")
        f.write(f"| AI-ready (>=70) | {ready} |\n")
        f.write(f"| Needs work (40-69) | {needs_work} |\n")
        f.write(f"| Rewrite required (<40) | {rewrite} |\n\n")

        # Top issues
        f.write("## Top Issues\n\n")
        no_fm = sum(1 for r in results if r["fm"] == 0)
        no_summary = sum(1 for r in results if r["summary"] == 0)
        no_lang = sum(1 for r in results if r["lang"] == 0)
        no_xref = sum(1 for r in results if r["xref"] == 0)
        wall_of_text = sum(1 for r in results if r["struct"] == 0 and r["penalty"] > 0)

        f.write(f"| Issue | Files affected | Remediation |\n")
        f.write(f"|-------|---------------|-------------|\n")
        f.write(f"| Missing YAML frontmatter | {no_fm} | Add `---\\ntitle: ...\\ndescription: ...\\n---` |\n")
        f.write(f"| Missing summary paragraph | {no_summary} | Add 2-3 sentence summary after H1 |\n")
        f.write(f"| No language-tagged code blocks | {no_lang} | Use ` ```sh`, ` ```json` etc. |\n")
        f.write(f"| No resolvable cross-references | {no_xref} | Add internal links with relative paths |\n")
        f.write(f"| Wall-of-text (>500 lines, no headers) | {wall_of_text} | Break into sections with H2/H3 |\n")

    print(f"Report saved to {OUTPUT_FILE}")
    print(f"Files scored: {len(results)}")
    print(f"Average score: {avg_score:.1f}")
    print(f"AI-ready: {ready}")
    print(f"Needs work: {needs_work}")
    print(f"Rewrite: {rewrite}")


if __name__ == "__main__":
    main()
