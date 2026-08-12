#!/usr/bin/env python3
"""Phase 3 (Class C) verification sweep: fence parity, empty pairs, `> /` artifacts."""
import re
from pathlib import Path

root = Path.home() / "Desktop/SandBox/.github/prompts"
files = sorted(root.glob("*.md"))

parity_bad = []
empty_pairs = []
gt_artifacts = []

def fence_lines(text):
    return [(i, m.group(1), m.group(2))
            for i, line in enumerate(text.splitlines(), 1)
            for m in [re.match(r"^\s*(`{3,})(.*)$", line)]
            if m]

def check_parity(text, name):
    """Count fence lines; a 4+ backtick fence is balanced only by same-length closer.
    A fence line with a language tag is ALWAYS an opener. A bare fence line closes
    an open fence of the same length, else it opens a new one."""
    lines = text.splitlines()
    stack = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(`{3,})(.*)$", line)
        if not m:
            continue
        n = len(m.group(1))
        rest = m.group(2).strip()
        if rest:
            stack.append((i, n))  # opener with language tag — never a closer
        elif stack and stack[-1][1] == n:
            stack.pop()  # bare closer for open fence of same length
        elif not stack:
            stack.append((i, n))  # bare opener
        # else: bare closer with mismatched length — ignore (content or stray)
    return stack  # leftover unclosed openers

for f in files:
    text = f.read_text(encoding="utf-8")
    leftover = check_parity(text, f.name)
    if leftover:
        parity_bad.append((f.name, leftover))
    # empty pairs: ``` immediately followed by ``` (same length, nothing between)
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if i + 1 < len(lines):
            m1 = re.match(r"^\s*(`{3,})(.*)$", line)
            m2 = re.match(r"^\s*(`{3,})\s*$", lines[i + 1])
            if m1 and m2 and len(m1.group(1)) == len(m2.group(1)) and m1.group(2).strip() == "":
                empty_pairs.append((f.name, i + 1))
    # `> /` artifact inside a fence: blockquote line that is a bare path
    for i, line in enumerate(lines):
        if re.match(r"^\s*>\s*/", line) and not line.strip().endswith(":"):
            gt_artifacts.append((f.name, i + 1, line.strip()[:60]))

print("PARITY-FAILING FILES:", len(parity_bad))
for name, leftover in parity_bad:
    print(f"  {name}: unclosed {leftover}")
print("EMPTY PAIRS:", len(empty_pairs))
for name, ln in empty_pairs[:10]:
    print(f"  {name}:{ln}")
print("GT_ARTIFACTS:", len(gt_artifacts))
for name, ln, s in gt_artifacts[:10]:
    print(f"  {name}:{ln}: {s}")
print("DONE")
