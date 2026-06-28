#!/usr/bin/env python3
"""Generate periodic inventory report of docs/ and research/ directories.

Usage:
    python3 ~/AppData/Local/hermes/scripts/docs-inventory-report.py [--output <path>]

Outputs markdown report with file counts, sizes, and per-subdirectory breakdown.
"""

import os
import sys
import subprocess
from datetime import datetime

DOCS_DIR = os.path.expanduser("~/Desktop/SandBox/docs")
RESEARCH_DIR = os.path.expanduser("~/Desktop/SandBox/research")
OUTPUT_DIR = os.path.expanduser("~/.hermes/plans/inventory")

def count_files(base_dir, glob_pattern="*.md"):
    """Count files by extension in a directory tree."""
    counts = {}
    total = 0
    total_size = 0
    
    if not os.path.isdir(base_dir):
        return counts, total, total_size
    
    for entry in os.listdir(base_dir):
        subpath = os.path.join(base_dir, entry)
        if os.path.isdir(subpath):
            file_count = 0
            dir_size = 0
            for root, dirs, files in os.walk(subpath):
                for f in files:
                    if f.endswith('.md'):
                        fp = os.path.join(root, f)
                        file_count += 1
                        dir_size += os.path.getsize(fp)
            counts[entry] = {"files": file_count, "size": dir_size}
            total += file_count
            total_size += dir_size
    
    return counts, total, total_size

def format_size(bytes_val):
    """Format bytes to human-readable size."""
    for unit in ['B', 'K', 'M']:
        if bytes_val < 1024:
            return f"{bytes_val}{unit}"
        bytes_val /= 1024
    return f"{bytes_val:.1f}M"

def generate_report():
    """Generate markdown inventory report. Returns (report_text, docs_total, research_total)."""
    docs_counts, docs_total, docs_size = count_files(DOCS_DIR)
    research_counts, research_total, research_size = count_files(RESEARCH_DIR)
    
    lines = [
        f"# Docs & Research Inventory Report",
        f"",
        f"> Generated: {datetime.now().isoformat()}",
        f"",
        f"## Summary",
        f"| Area | Files | Size |",
        f"|------|-------|------|",
        f"| docs/ | {docs_total} | {format_size(docs_size)} |",
        f"| research/ | {research_total} | {format_size(research_size)} |",
        f"| **Total** | **{docs_total + research_total}** | **{format_size(docs_size + research_size)}** |",
        f"",
        f"## docs/ Breakdown",
        f"| Subdirectory | Files | Size |",
        f"|-------------|-------|------|",
    ]
    
    for name, info in sorted(docs_counts.items(), key=lambda x: -x[1]["files"]):
        if info["files"] > 0:
            lines.append(f"| {name} | {info['files']} | {format_size(info['size'])} |")
    
    lines.extend([
        f"",
        f"## research/ Breakdown",
        f"| Subdirectory | Files | Size |",
        f"|-------------|-------|------|",
    ])
    
    for name, info in sorted(research_counts.items(), key=lambda x: -x[1]["files"]):
        if info["files"] > 0:
            lines.append(f"| {name} | {info['files']} | {format_size(info['size'])} |")
    
    lines.extend([
        f"",
        f"## Notes",
        f"- Auto-generated artifacts (skills-reports, skills-audit individual files): 459 deleted on 2026-06-22",
        f"- Only hand-authored content and aggregate index.md remain",
        f"- Run `ls docs/skills-reports/` and `ls docs/skills-audit/` to verify no regrowth",
    ])
    
    return "\n".join(lines), docs_total, research_total

def main():
    report, docs_total, research_total = generate_report()
    
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out_path = sys.argv[idx + 1]
        else:
            out_path = os.path.join(OUTPUT_DIR, "docs-inventory-report.md")
    else:
        out_path = os.path.join(OUTPUT_DIR, "docs-inventory-report.md")
    
    dir_path = os.path.dirname(out_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)
    
    print(f"Report written to: {out_path}")
    print(f"Total data rows: {docs_total + research_total} files documented")

if __name__ == "__main__":
    main()
