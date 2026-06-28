#!/usr/bin/env python3
"""Trim RESEARCH_REPORT.md to 1-5KB - aggressive mode."""
import os, re

projects_dir = "C:\\Users\\Alexa\\Desktop\\SandBox\\projects"
reports = ["comicwise", "Django-Scrapy-Selenium", "rhixe_scans", 
           "rhixecompany-comics", "university-libary-jsm"]

max_per_section = {
    "project": 8, "similar": 4, "key": 10, "cheatsheets": 4,
    "best": 4, "common": 4, "performance": 3, "security": 3,
    "related": 4, "resources": 4
}

for name in reports:
    fpath = os.path.join(projects_dir, name, "RESEARCH_REPORT.md")
    if not os.path.exists(fpath):
        continue
    
    with open(fpath, "r", encoding="utf-8") as fh:
        content = fh.read()
    
    lines = content.split("\n")
    total_before = os.path.getsize(fpath)
    
    # Find all ## headings
    headings = []
    for i, line in enumerate(lines):
        if re.match(r'^## ', line):
            headings.append(i)
    
    if not headings:
        continue
    
    new_lines = []
    for idx, h_idx in enumerate(headings):
        nxt = headings[idx+1] if idx+1 < len(headings) else len(lines)
        
        new_lines.append(lines[h_idx])
        
        h_text = lines[h_idx].lower()
        max_n = 5
        for key, val in max_per_section.items():
            if key in h_text:
                max_n = val
                break
        
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
    
    status = "✅" if total_after <= 5120 else "❌"
    print(f"{name:40s} {total_before:>6}B -> {total_after:>6}B [{status}]")
