#!/usr/bin/env python3
"""Final trim pass for remaining oversized reports."""
import os, re

fpath = "C:\\Users\\Alexa\\Desktop\\SandBox\\projects\\university-libary-jsm\\RESEARCH_REPORT.md"

with open(fpath, "r", encoding="utf-8") as fh:
    content = fh.read()
lines = content.split("\n")
total_before = os.path.getsize(fpath)

headings = [i for i, l in enumerate(lines) if re.match(r'^## ', l)]

max_per = {"project":6, "similar":3, "key":8, "cheatsheets":3, "best":3,
           "common":3, "performance":2, "security":2, "related":3, "resources":3}

new_lines = []
for idx, h_idx in enumerate(headings):
    nxt = headings[idx+1] if idx+1 < len(headings) else len(lines)
    new_lines.append(lines[h_idx])
    h_text = lines[h_idx].lower()
    max_n = next((v for k,v in max_per.items() if k in h_text), 3)
    added = 0
    for cl in range(h_idx+1, nxt):
        s = lines[cl].strip()
        if not s or s == "---": continue
        if added >= max_n: break
        new_lines.append(lines[cl])
        added += 1
    new_lines.append("")

new_content = "\n".join(new_lines)
total_after = len(new_content.encode("utf-8"))
with open(fpath, "w", encoding="utf-8") as fh:
    fh.write(new_content)
status = "✅" if total_after <= 5120 else "❌"
print(f"university-libary-jsm: {total_before}B -> {total_after}B [{status}]")
