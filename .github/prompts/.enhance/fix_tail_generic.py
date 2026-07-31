#!/usr/bin/env python3
"""
fix_tail_generic.py — Final generic glue rules that are provably safe:

  1. Bracket glue: `## Heading[Instruction]` (no space before `[`) →
     `## Heading` + `[Instruction]`. Head must be a plausible heading:
     no `[`, `**`, `{` inside; ends with word char; not a styled heading.
  2. Bold glue: `## Heading**Bold content**` → `## Heading` + `**Bold content**`.
     Head must contain no `**` and must be short-ish (<= 70 chars).

Template placeholders with a space (`## 💰 Cost Optimization: [Brief Title]`)
are untouched. Fence-aware. Dry-run default; --apply writes. LF output.
"""
import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

BRACKET = re.compile(r"^(#{2,4}) ([^#\n]{3,70}?)\[")
BOLD = re.compile(r"^(#{2,4}) ([^#\n]{3,70}?)\*\*")


def plausible_head(head: str) -> bool:
    h = head.strip()
    if not h or len(h) > 70:
        return False
    if any(ch in h for ch in ("[", "]", "**", "{", "}")):
        return False
    if re.search(r"[a-z][A-Z]", h):  # camelCase inside head — not a heading
        return False
    if h.endswith((":", "-", "|", ">")):
        return False
    return True


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    out = []
    in_fence = False
    for raw_line in text.split("\n"):
        line = raw_line.rstrip("\r\n")
        fm = line.count("```") + line.count("~~~")
        if in_fence:
            if fm % 2 == 1:
                in_fence = False
            out.append(line)
            continue
        if fm % 2 == 1:
            in_fence = True
            out.append(line)
            continue
        if not line.startswith(("## ", "### ", "#### ")):
            out.append(line)
            continue

        applied = False
        # bracket glue
        m = BRACKET.match(line)
        if m and plausible_head(m.group(2)) and not m.group(2).endswith(" "):
            head = (m.group(1) + " " + m.group(2)).strip()
            content = "[" + line[m.end():]  # keep the [ marker
            if content:
                out.extend([head, "", content])
                changes += 1
                applied = True
        if not applied:
            # bold glue
            m = BOLD.match(line)
            if m and plausible_head(m.group(2)) and not m.group(2).endswith(" "):
                head = (m.group(1) + " " + m.group(2)).strip()
                content = "**" + line[m.end():]  # keep the ** marker
                if content:
                    out.extend([head, "", content])
                    changes += 1
                    applied = True
        if not applied:
            out.append(line)
    new_text = "\n".join(out)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    new_text = new_text.replace("\r\n", "\n").replace("\r", "\n")
    return new_text, changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--file", help="Process only this filename substring")
    args = ap.parse_args()

    files = sorted(PROMPTS_DIR.glob("*.prompt.md")) + sorted(PROMPTS_DIR.glob("templates/**/*.md"))
    total_files = 0
    total_changes = 0
    for f in files:
        if args.file and args.file not in f.name:
            continue
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        new_text, changes = fix_text(text)
        if changes:
            total_files += 1
            total_changes += changes
            if args.apply:
                f.write_text(new_text, encoding="utf-8", newline="")
                print(f"FIXED {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
            else:
                print(f"WOULD FIX {f.relative_to(PROMPTS_DIR).as_posix()}: {changes}")
    print(f"\n{total_files} files, {total_changes} fixes ({'APPLIED' if args.apply else 'DRY-RUN'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
