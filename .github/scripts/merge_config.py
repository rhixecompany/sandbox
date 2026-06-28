#!/usr/bin/env python3
"""
Properly merge model block into root config.yaml.
Handles CRLF line endings. Saves .original backup first.
"""
import os
import shutil

CONFIG = "C:/Users/Alexa/AppData/Local/hermes/config.yaml"
BACKUP = CONFIG + ".original"

# Backup original
shutil.copy2(CONFIG, BACKUP)
print(f"Backed up to {BACKUP}")

with open(CONFIG, 'rb') as f:
    raw = f.read()

# Detect line ending
has_crlf = b'\r\n' in raw
newline = b'\r\n' if has_crlf else b'\n'

lines = raw.split(newline)
first_line = lines[0]

model_block = b"""model:
  api_mode: chat_completions
  base_url: https://opencode.ai/zen/v1
  default: deepseek-v4-flash-free
  provider: opencode-zen

""".replace(b'\n', newline)

# Insert after first line
merged = first_line + newline + model_block + newline.join(lines[1:])

# Add missing agent fields
# Root has: api_max_retries: 3\n  background_review: false
# Add: restart_drain_timeout, service_tier, task_completion_guidance, tool_use_enforcement
agent_insert = b"  api_max_retries: 3" + newline + b"""  restart_drain_timeout: 180
  service_tier: ''
  task_completion_guidance: true
  tool_use_enforcement: auto
""".replace(b'\n', newline) + b"  background_review: false"

merged = merged.replace(
    b"  api_max_retries: 3" + newline + b"  background_review: false",
    agent_insert,
    1
)

with open(CONFIG, 'wb') as f:
    f.write(merged)

print(f"Written {len(merged)} bytes to {CONFIG}")
print(f"CRLF: {has_crlf}")
print("\nFirst 6 lines:")
for i, line in enumerate(merged.split(newline)[:6]):
    print(f"  {i+1}: {line.decode('utf-8', errors='replace')}")
