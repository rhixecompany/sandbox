#!/usr/bin/env python3
"""Add the hooks registration block to config.yaml."""

import sys
import yaml

config_path = sys.argv[1]

with open(config_path, 'r') as f:
    content = f.read()

# Find the hooks_auto_accept line and insert hooks block before it
lines = content.split('\n')
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
for i, line in enumerate(lines):
    if line.strip() == 'hooks_auto_accept: true' and not inserted:
        new_lines.append(hooks_block)
        inserted = True
    new_lines.append(line)

if not inserted:
    print("ERROR: hooks_auto_accept line not found", file=sys.stderr)
    sys.exit(1)

with open(config_path, 'w') as f:
    f.write('\n'.join(new_lines))

print("Added hooks registration block")