#!/usr/bin/env python3
"""fix_fence_glue.py — repair code-fence and heading glue in spring-boot + rust prompts.

Handles:
  1. `- text```shellCMD``` ` -> bullet, blank line, proper fenced block
  2. collapsed shell line continuations (backslash-space) -> backslash + newline + indent
  3. duplicate `## Unzip the downloaded file` block in kotlin variant
  4. rust-mcp-server-generator mangled `## Running the Generated Server` section

Dry-run default; `--apply` writes.
"""
import re
import sys
from pathlib import Path

P = Path(__file__).resolve().parent.parent  # .github/prompts
DRY = "--apply" not in sys.argv

FENCE_RE = re.compile(r"(- [^\n]*?)```shell([\s\S]*?)```")
CONT_RE = re.compile(r"\\ +(?=-)")


def fix_spring_boot(text):
    def repl(m):
        bullet = m.group(1).strip()
        cmd = m.group(2).strip()
        cmd = CONT_RE.sub("\\\n  ", cmd)
        return f"{bullet}\n\n```shell\n{cmd}\n```"
    return FENCE_RE.sub(repl, text)


def fix_kotlin_dup(text):
    head, sep, tail = text.partition("## Remove the downloaded zip file")
    if not sep:
        return text
    tail = re.sub(
        r"## Unzip the downloaded file\n\n- Run following command in terminal to unzip the downloaded file\n\n```shell\nunzip[^\n]*\n```\n\n?",
        "", tail, count=1,
    )
    return head + sep + tail


RUST_OLD = "## Running the Generated ServerAfter generation:```bashcd"
RUST_NEW = (
    "## Running the Generated Server\n\nAfter generation:\n\n```bash\n"
    "cd {project-name}\n"
    "cargo build\n"
    "cargo test\n"
    "cargo run\n"
    "```\n\n"
    "For Claude Desktop integration:\n\n```json\n"
    "{\n"
    '  "mcpServers": {\n'
    '    "{project-name}": {\n'
    '      "command": "path/to/{project-name}/target/release/{project-name}",\n'
    '      "args": []\n'
    "    }\n"
    "  }\n"
    "}\n"
    "```\n\n"
    "Now generate the complete project based on the user's requirements!"
)


def fix_rust(text):
    if RUST_OLD in text:
        return text.replace(RUST_OLD, RUST_NEW)
    return text


def main():
    targets = {
        "create-spring-boot-java-project.prompt.md": [fix_spring_boot],
        "create-spring-boot-kotlin-project.prompt.md": [fix_spring_boot, fix_kotlin_dup],
        "rust-mcp-server-generator.prompt.md": [fix_rust],
    }
    print(f"=== Fence/Heading Glue Fixer ===\nMode: {'DRY' if DRY else 'APPLY'}\n")
    for name, fixers in targets.items():
        pf = P / name
        text = pf.read_text(encoding="utf-8")
        for fn in fixers:
            text = fn(text)
        new_text = text
        if new_text != pf.read_text(encoding="utf-8"):
            print(f"  {name}: CHANGED")
            if not DRY:
                pf.write_text(new_text, encoding="utf-8")
        else:
            print(f"  {name}: no change")
    print(f"\n{'DRY RUN. Run with --apply to execute.' if DRY else 'APPLY COMPLETE.'}")


if __name__ == "__main__":
    main()
