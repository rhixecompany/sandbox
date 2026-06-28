#!/usr/bin/env python3
"""Trim Banking report which has '## Project: Banking' format."""
import os, re

fpath = "C:\\Users\\Alexa\\Desktop\\SandBox\\projects\\Banking\\RESEARCH_REPORT.md"

with open(fpath, "r", encoding="utf-8") as fh:
    content = fh.read()
lines = content.split("\n")
total_before = os.path.getsize(fpath)

# Find all ## headings (any format)
headings = [i for i, l in enumerate(lines) if l.startswith("## ")]
print(f"Found {len(headings)} headings")

# Keep: header lines before first heading + 2-4 lines per section
new_lines = lines[:headings[0]] if headings else []
if new_lines and new_lines[-1].strip():
    new_lines.append("")

for idx, h_idx in enumerate(headings):
    nxt = headings[idx+1] if idx+1 < len(headings) else len(lines)
    new_lines.append(lines[h_idx])
    h_text = lines[h_idx].lower()
    
    # Count lines in this section
    section_lines = [l for l in lines[h_idx+1:nxt] if l.strip() and l.strip() != "---"]
    
    # Determine max lines based on section type
    max_n = 4  # default
    for key, val in {"project":8, "similar":4, "key":10, "cheatsheets":4, 
                     "best":4, "common":4, "performance":3, "security":3,
                     "related":3, "resources":4}.items():
        if key in h_text:
            max_n = val
            break
    
    for cl in range(h_idx+1, nxt):
        s = lines[cl].strip()
        if not s or s == "---":
            continue
        if len(new_lines) - (len(new_lines) - len(section_lines)) > max_n:
            # Count lines added since heading
            count_since_heading = sum(1 for l in new_lines if l.strip() and l.strip() != "---" and not l.startswith("## "))
        # Simpler approach: just count
        pass
    
    added = 0
    for cl in range(h_idx+1, nxt):
        s = lines[cl].strip()
        if not s or s == "---":
            continue
        if added >= max_n:
            break
        new_lines.append(lines[cl])
        added += 1
    
    new_lines.append("")

new_content = "\n".join(new_lines)
total_after = len(new_content.encode("utf-8"))

with open(fpath, "w", encoding="utf-8") as fh:
    fh.write(new_content)

print(f"{total_before}B -> {total_after}B {'✅' if total_after <= 5120 else '❌'}")
