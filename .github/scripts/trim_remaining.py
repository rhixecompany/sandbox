#!/usr/bin/env python3
"""Trim remaining oversized reports."""
import os

reports = {
    "ecom": 10145, "profile": 10078, "Python-projects": 10655,
    "selenium_webdriver": 10248, "xamehi.tv": 10612, "xamehi": 9420,
    "youtube-downloader": 11102
}

max_per = {"project":6, "similar":3, "key":8, "cheatsheets":3, "best":3,
           "common":3, "performance":2, "security":2, "related":3, "resources":3,
           "findings":8, "cheat":3}

for name in reports:
    fpath = f"C:\\Users\\Alexa\\Desktop\\SandBox\\projects\\{name}\\RESEARCH_REPORT.md"
    if not os.path.exists(fpath):
        print(f"{name}: NOT FOUND")
        continue
    
    with open(fpath, "r", encoding="utf-8") as fh:
        content = fh.read()
    lines = content.split("\n")
    total_before = len(content.encode("utf-8"))
    
    # Find ## headings
    headings = [i for i, l in enumerate(lines) if l.startswith("## ")]
    if not headings:
        print(f"{name}: no headings")
        continue
    
    new_lines = lines[:headings[0]]
    if new_lines and new_lines[-1].strip():
        new_lines.append("")
    
    for idx, h_idx in enumerate(headings):
        nxt = headings[idx+1] if idx+1 < len(headings) else len(lines)
        new_lines.append(lines[h_idx])
        
        h_text = lines[h_idx].lower()
        max_n = 3
        for key, val in max_per.items():
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
    print(f"{name:25s} {total_before:>6}B -> {total_after:>6}B [{status}]")
