"""Fast inventory of prompt files for prompt-management Phase 1."""
from __future__ import annotations
import asyncio

from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROMPTS = REPO / "prompts"
DOCS = REPO / "docs"
INDEX = DOCS / "prompt-inventory.md"


async def main() -> int:
    DOCS.mkdir(exist_ok=True)
    prompt_files = sorted(PROMPTS.glob("*.prompt.md"))
    rows = []
    for path in prompt_files:
        rows.append(path.name)
    lines = [
        "# Prompt Inventory",
        "",
        f"- Prompts directory: `prompts/`",
        f"- Prompt count: {len(rows)}",
        f"- Last updated: (auto-generated)",
        "",
        "| Path | Name | Title | Version | Tags |",
        "| --- | --- | --- | --- | --- |",
    ]
    for name in rows:
        lines.append(f"| `prompts/{name}` | | | | |")
    lines += ["", "---", ""]
    INDEX.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
