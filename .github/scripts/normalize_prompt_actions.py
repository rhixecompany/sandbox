#!/usr/bin/env python3
"""Normalize prompt actions section."""

import asyncio
import re
from pathlib import Path

root = Path(r"C:\Users\Alexa\Desktop\SandBox")
prompts_dir = root / "prompts"
actions_text = """\n## Actions\n\n- Follow the prompt workflow as specified.\n- Produce the requested deliverable(s) in the exact structure requested.\n- Validate output against acceptance criteria before finishing.\n"""


async def main():
    count = 0
    for path in sorted(prompts_dir.glob("*.prompt.md")):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if "## Actions" in text:
            continue
        if text.startswith("---"):
            m = re.match(r"^---\n.*?\n---\n", text, re.S)
            new_text = m.group(0) + "\n" + actions_text + text[m.end() :] if m else actions_text + text
        else:
            new_text = actions_text + text
        path.write_text(new_text, encoding="utf-8")
        count += 1
    print("NORMALIZED", count)


if __name__ == "__main__":
    asyncio.run(main())
