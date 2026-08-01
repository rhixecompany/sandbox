"""Fence-aware check: find files with unbalanced triple-backtick fences.

Treats only lines that START with ``` as fence markers (inline single/double
backticks don't count). 4-backtick escaped fences are handled by the regex.
"""

import re
import sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else ".github/prompts")
flagged = []
for f in sorted(p.rglob("*")):
    if f.suffix != ".md" and not f.name.endswith(".prompt.md"):
        continue
    text = f.read_text(encoding="utf-8", errors="replace")
    depth = 0
    for line in text.splitlines():
        stripped = line.strip()
        m = re.match(r"^(```+)", stripped)
        if m and len(m.group(1)) == 3:
            depth += 1
    if depth % 2 != 0:
        flagged.append(str(f.relative_to(p)))
print("TRUE unbalanced (fence-aware):", len(flagged))
for x in flagged[:30]:
    print(" ", x)
