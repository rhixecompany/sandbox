#!/usr/bin/env python3
"""Add the hooks registration block to config.yaml."""

import asyncio
import sys


async def main():
    config_path = sys.argv[1]

    loop = asyncio.get_running_loop()
    content = await loop.run_in_executor(None, _read_file, config_path)

    # Find the hooks_auto_accept line and insert hooks block before it
    lines = content.split("\n")
    new_lines = []
    hooks_block = """hooks:
  on_session_start:
    - command: 'session-logger'
    - command: 'governance-audit'
  on_session_end:
    - command: 'session-logger'
    - command: 'session-auto-commit'
    - command: 'governance-audit'
  pre_llm_call:
    - command: 'session-logger'
    - command: 'governance-audit'
hooks_auto_accept: true"""

    inserted = False
    for _i, line in enumerate(lines):
        if line.strip() == "hooks_auto_accept: true" and not inserted:
            new_lines.append(hooks_block)
            inserted = True
        new_lines.append(line)

    if not inserted:
        print("ERROR: hooks_auto_accept line not found", file=sys.stderr)
        sys.exit(1)

    await loop.run_in_executor(None, _write_file, config_path, "\n".join(new_lines))

    print("Added hooks registration block")


def _read_file(path):
    with open(path) as f:
        return f.read()


def _write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    asyncio.run(main())
