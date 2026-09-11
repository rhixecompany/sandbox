#!/usr/bin/env python3
"""Fix OpenCode .agent.md frontmatter: convert deprecated `tools` ARRAY to OBJECT.

OpenCode >=1.18 schema: `tools` must be an object (tool -> true/false);
array form fails validation ("Expected object | undefined, got [...]").
Each entry becomes `tool: true` (= allow), preserving the original intent.
Uses yaml round-trip only on the frontmatter; body is untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

AGENTS = Path(__file__).resolve().parent.parent / ".opencode" / "agents"

FM_RE = re.compile(r"^(---\r?\n)(.*?)(\r?\n---)(\r?\n.*)$", re.S)


def main() -> int:
    if not AGENTS.is_dir():
        print(f"no agents dir: {AGENTS}")
        return 2
    fixed = 0
    for md in sorted(AGENTS.glob("*.agent.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        m = FM_RE.match(text)
        if not m:
            print(f"skip (no frontmatter): {md.name}")
            continue
        try:
            fm = yaml.safe_load(m.group(2))
        except yaml.YAMLError as e:
            print(f"skip (yaml error): {md.name}: {e}")
            continue
        if not isinstance(fm, dict) or "tools" not in fm:
            continue
        tools = fm["tools"]
        if isinstance(tools, list):
            fm["tools"] = {t: True for t in tools}
            new_fm = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
            new_text = "---\n" + new_fm + "\n---\n" + m.group(4).lstrip("\r\n") + "\n"
            md.write_text(new_text, encoding="utf-8", newline="\n")
            fixed += 1
            print(f"fixed {len(tools)} tool(s): {md.name}")
    print(f"total fixed: {fixed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())