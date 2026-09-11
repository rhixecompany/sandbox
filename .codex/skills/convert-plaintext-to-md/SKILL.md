---
name: convert-plaintext-to-md
title: "Convert Plaintext to Markdown"
description: "Convert plain text files (.txt, .md fragments, notes) into properly formatted Markdown with headings, lists, links, and structure. Enforce DRY formatting rules and cross-reference to workspace templates."
version: 1.0.0
author: Alexa
license: MIT
tags:
  - conversion
  - markdown
  - formatting
---

# Convert Plaintext to Markdown

When working with unstructured text sources, convert them to clean Markdown matching workspace conventions (no H1 duplication per MEMORY.md rules; use headings only at level 2+ for sections).

## Workflow

1. Read source file with `read_file` or terminal.
2. Normalize line endings (`normalize_lf.py` available in workspace).
3. Apply heading structure using confirmed workspace rules.
4. Verify output with `markdownlint`.
5. Commit change; no `.bak` files.

## References

- `references/session-reporting.md` (for format examples)
- `references/preference-preferences.md` (for DRY/style rules)

Note: Not an external MCP server; workspace formatting tool.
