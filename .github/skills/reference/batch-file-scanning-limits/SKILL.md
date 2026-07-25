---
name: batch-file-scanning-limits
title: "Batch File Scanning Limits"
description: "Use when scanning 100+ files in batch operations. Documents the execute_code 50-call limit and the os.walk workaround."
version: 1.0.0
author: OWL
license: MIT
tags: [batch, scanning, limits, tips, performance]
---

# Batch File Scanning Limits

## Problem

`execute_code` caps at **50 tool calls per script**. When scanning 600+ SKILL.md files via individual `read_file` calls, the limit is hit before the report can be written.

## Solution

Use `terminal()` with a single `python3 -c` invocation backed by Python stdlib `os.walk`:

```python
# BAD — hits 50-call limit before finishing
from hermes_tools import read_file
results = []
for path in all_600_paths:
    content = read_file(path)  # Each call counts against 50 limit
    results.append(process(content))

# GOOD — one terminal call, no limit issues
from hermes_tools import terminal
result = terminal("""python3 -c "
import os
for root, dirs, files in os.walk(skills_root):
    if 'SKILL.md' in files:
        path = os.path.join(root, 'SKILL.md')
        with open(path) as f:
            content = f.read()
        # process...
" """)
```

## When to Use

- Scanning 50+ files in a single execute_code script
- Any batch operation where tool call count may be a factor
- Generating aggregate reports from file metadata

## Pitfalls

- **MSYS path bleeding:** On Windows Git Bash, `/c/Users/...` paths passed to `python3` get mangled to `C:\c\Users\...`. Use native Windows paths with forward slashes: `"C:/Users/..."`
- **`write_file` inside execute_code also counts** toward the 50-call limit. If your batch reads 48 files then calls write_file, you're at 49/50 with no room for error handling. Build the output in memory, then `print()` it and use a single `terminal()` call to write the artifact.
- **Not a replacement for proper batching:** For truly large datasets (10K+ files), offload to a Python script saved via write_file and invoked via terminal, not inline python -c.
