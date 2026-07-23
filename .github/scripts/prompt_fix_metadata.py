#!/usr/bin/env python3
"""Fix prompt metadata: remove duplicate external metadata blocks, then inject a single metadata block inside the first frontmatter."""
import asyncio
from pathlib import Path
import re

ROOT = Path("prompts")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\s*\n---\s*\n", re.S)
METADATA_BLOCK_RE = re.compile(r"^metadata:\s*\n(?:[ \t]+.*\n?)+\n?", re.M)
CLEANUP_COUNT = 0
UPDATED_COUNT = 0
REMAINING = 0


def cleanup_external_metadata(path: Path, text: str) -> str:
    global CLEANUP_COUNT
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text
    after = text[match.end():]
    metas = METADATA_BLOCK_RE.findall("\n" + after)
    if len(metas) <= 1:
        return text
    cleaned = after
    for i, m in enumerate(metas):
        if i == 0:
            continue
        cleaned = cleaned.replace("\n" + m, "", 1)
    CLEANUP_COUNT += 1
    return text[: match.end()] + cleaned


def inject_metadata(path: Path, text: str) -> str:
    global UPDATED_COUNT
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text
    if "metadata:" in match.group(1):
        return text
    slug = path.stem.replace(" ", "-").replace("_", "-").lower()
    block = "\nmetadata:\n  hermes:\n    related_skills: []\n    tags:\n    - {}\n".format(slug)
    insertion = match.group(0) + block
    rest = text[match.end():]
    UPDATED_COUNT += 1
    return insertion + rest


async def main():
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix != ".md" or "templates" in p.parts or "_shared" in p.parts or p.parent.name == "templates":
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if not text.startswith("---"):
            continue
        text = cleanup_external_metadata(p, text)
        text = inject_metadata(p, text)
        p.write_text(text, encoding="utf-8")

    print(f"cleaned_duplicates={CLEANUP_COUNT}")
    print(f"injected_metadata={UPDATED_COUNT}")

    for p in sorted(ROOT.rglob("*.md")):
        if "templates" in p.parts or "_shared" in p.parts or p.parent.name == "templates":
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        m = FRONTMATTER_RE.match(txt)
        if not m:
            continue
        if "metadata:" not in m.group(1):
            REMAINING += 1
    print(f"remaining={REMAINING}")


if __name__ == '__main__':
    asyncio.run(main())
