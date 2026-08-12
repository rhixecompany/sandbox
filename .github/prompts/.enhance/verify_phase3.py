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

def check_parity(text):
    """Fence parity per CommonMark: a bare closer is valid if its backtick
    length is >= the open fence's length (create-llms/tldr close 3-fences with
    ````-style 4-backtick closers). A line with a language tag opens a fence
    only when no fence is open, or when longer than the open fence; inside an
    open fence a shorter lang-tagged line (e.g. ```sql inside a 4-backtick
    fence) is content, not a fence."""
    lines = text.splitlines()
    stack = []
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(`{3,})(.*)$", line)
        if not m:
            continue
        n = len(m.group(1))
        rest = m.group(2).strip()
        if stack and not rest and n >= stack[-1][1]:
            stack.pop()  # bare closer long enough for the open fence
        elif rest and stack:
            continue  # lang-tagged line inside an open fence -> content
        elif rest:
            stack.append((i, n))  # opener with language tag
        elif not stack:
            stack.append((i, n))  # bare opener
        # else: bare line shorter than open fence -> content
    return stack  # leftover unclosed openers

for f in files:
    text = f.read_text(encoding="utf-8")
    leftover = check_parity(text)
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
    # `> /` artifact: blockquote line that is a bare path fragment (glue residue).
    # Allowlist = verified-legit patterns: usage examples in create-tldr and
    # `> //` code comments inside code fences (csharp-mstest, setup, swift).
    LEGIT_GT = (
        "> /create-tldr-page",
        "> //",
    )
    for i, line in enumerate(lines):
        if line.strip().startswith(LEGIT_GT):
            continue
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
