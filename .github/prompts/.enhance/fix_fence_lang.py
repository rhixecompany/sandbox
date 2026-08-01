#!/usr/bin/env python3
"""
fix_fence_lang.py — Repair fence-open corruption introduced by pass 1's lazy
split_content regex.

Bug: `### Missing File```text[user]> ...``` was split into
  ```
  text[user]> ...
  ```
instead of
  ```text
  [user]> ...
  ```
The fence language (`text`, `php`, `bash`, ...) was swallowed into content.

Signature: a line that is exactly ``` (bare fence opener) followed by a line
starting with a short lowercase token immediately followed by `[`, `>`, or `:`
(e.g. `text[user]>`, `php#[McpResource`).

Fix: merge the language token back onto the opener: ```lang + rest.

Dry-run by default; --apply writes. LF output.
"""

import argparse
import re
import sys
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

# content line starting with a lowercase language token glued to [ > : or #
SIG = re.compile(r"^([a-z][a-z0-9+#.\-]{0,11})(\[|>|:|#)")


def fix_text(text: str) -> tuple[str, int]:
    changes = 0
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\r\n")
        # bare fence opener followed by a language-swallowed line?
        if line.strip() == "```" and i + 1 < len(lines):
            nxt = lines[i + 1].rstrip("\r\n")
            m = SIG.match(nxt.strip())
            if (
                m
                and len(m.group(1)) <= 12
                and not nxt.strip().startswith(("```", "~~~"))
                and nxt.strip() != "```"  # next line must NOT itself be a fence closer
            ):
                lang = m.group(1)
                # rebuild: opener with language + content minus the lang token
                out.append("```" + lang)
                out.append(nxt.strip()[len(lang) :])
                changes += 1
                i += 2
                continue
        out.append(line)
        i += 1

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
        raw = f.read_bytes()
        text = raw.decode("utf-8", errors="replace")
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
