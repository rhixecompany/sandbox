---
name: convert-plaintext-to-md
title: "Convert Plaintext to Markdown"
description: "Use when converting plain text files, notes, or unstructured content into well-formatted Markdown. Use during documentation migration, note cleanup, or content standardization."
version: 1.1.0
author: "Hermes Agent"
license: MIT
tags: [markdown, conversion, documentation, formatting]
metadata:
  hermes:
    tags: [imported]
    related_skills:
      - writing-clearly-and-concisely
      - documentation-writer
      - enhance-markdown
---

# Convert Plaintext to Markdown

## Overview

Convert plain text files, notes, or unstructured content into well-formatted Markdown with proper headings, lists, code blocks, and structure. This skill provides a systematic approach to text-to-markdown conversion.

## When to Use

- Converting legacy text files or notes to Markdown
- Migrating documentation from plain text to structured format
- Standardizing unstructured content across a project
- Cleaning up AI-generated or copy-pasted text
- Preparing content for static site generators or documentation systems

## When NOT to Use

- Converting between markup formats (HTML→MD, etc.) — use pandoc directly
- Writing new documentation from scratch — use documentation-writer
- Formatting already-structured Markdown — use enhance-markdown

## Workflow

### Phase 1: Analyze Source Content

**Entry check:** If `analysis-{basename}.json` exists → skip to Phase 2.

1. Read the source text file
2. Identify structural elements:
   - Section headers (ALL CAPS, underlined text, numbered sections)
   - Lists (numbered items, bullet points, indented blocks)
   - Code or technical content (indented blocks, monospace, file paths)
   - Emphasis (CAPS for bold, _underscores_ for italic)
   - Links and references (URLs, file paths)
3. Write analysis artifact → `analysis-{basename}.json` with:
   ```json
   {
     "headings": [...],
     "lists": [...],
     "code_blocks": [...],
     "emphasis": [...],
     "links": [...],
     "tables": [...]
   }
   ```

**Error handling:** If file not found → abort with clear error. If empty file → warn and continue (output minimal markdown). If read permission denied → abort.

### Phase 2: Convert Structure

**Entry check:** If `converted-{basename}.md` exists → skip to Phase 3.

Apply Markdown formatting:

| Source Pattern | Markdown Equivalent |
|----------------|-------------------|
| `SECTION HEADING` (ALL CAPS) | `## Section Heading` |
| `Section Heading` followed by `=====` | `## Section Heading` |
| `1. Item` / `2. Item` | `1. Item` (numbered list) |
| `- Item` or `* Item` | `- Item` (bullet list) |
| Indented code block | ` ```language ... ``` ` |
| `file/path/name` | `` `file/path/name` `` |
| `**bold**` or ALL CAPS emphasis | `**bold**` |
| `_italic_` or emphasis | `*italic*` |
| `http://url` | `[text](http://url)` |

**Reference:** See `references/conversion-patterns.md` for detailed patterns and edge cases.
**Reference:** See `references/heading-hierarchy.md` for hierarchy validation rules.
**Reference:** See `references/code-block-detection.md` for code block detection and language tagging.

**Error handling:** If analysis artifact missing → re-run Phase 1. If conversion produces empty output → warn and preserve original as fallback.

### Phase 3: Add Markdown Enhancements

**Entry check:** If `enhanced-{basename}.md` exists → skip to Phase 4.

1. Add YAML frontmatter if the file is documentation:
   ```yaml
   ---
   title: Document Title
   description: Brief description
   date: YYYY-MM-DD
   ---
   ```
2. Add table of contents for files >500 words
3. Convert any tables to Markdown table format
4. Add language tags to all code blocks
5. Ensure consistent heading hierarchy (no skipped levels) — see `references/heading-hierarchy.md`

**Error handling:** If heading hierarchy validation fails → apply auto-fix (demote/insert) and log. If frontmatter YAML invalid → fix common issues (unquoted colons, trailing spaces).

### Phase 4: Verify Output

**Entry check:** If `verify-{basename}.json` exists → report existing results.

1. Check that all original content is preserved
2. Verify heading hierarchy is logical (H1 → H2 → H3, no skips)
3. Ensure code blocks have language tags
4. Check that links are properly formatted
5. Validate YAML frontmatter if present
6. Write verification report → `verify-{basename}.json`

**Reference:** See `references/verification-patterns.md` for automated check implementations.

**Error handling:** If verification fails → report specific errors with line numbers. Do not silently pass.

## Platform Detection & Fallback

- **Windows (PowerShell/CMD):** Use `type` for reading, `>` for writing. Path separators `\`.
- **Unix/Linux/macOS (bash/zsh):** Use `cat` for reading, `>` for writing. Path separators `/`.
- **Cross-platform (Node/Python):** Prefer `fs.readFileSync` / `open()` — works everywhere.
- **Fallback:** If platform detection fails, assume POSIX and warn.

## Verification Checklist

- [ ] All source content preserved in conversion
- [ ] Heading hierarchy is logical (no skipped levels)
- [ ] Code blocks have language tags
- [ ] Lists are properly formatted
- [ ] Links are clickable Markdown links
- [ ] YAML frontmatter present (for documentation files)
- [ ] No orphaned formatting artifacts
- [ ] Entry checks work (artifacts skip completed phases)
- [ ] Error handling covers file-not-found, empty, permission denied
- [ ] Platform fallback documented

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-clearly-and-concisely` | Improve prose during conversion |
| `documentation-writer` | Full documentation creation |
| `enhance-markdown` | Post-conversion formatting polish |

## Example Conversion

**Before (plain text):**
```
PROJECT OVERVIEW

This project is a web application for managing tasks.

FEATURES
1. User authentication
2. Task creation and editing
3. Team collaboration

SETUP
Run npm install to install dependencies.
Then run npm start to start the server.
```

**After (Markdown):**
```markdown
# Project Overview

This project is a web application for managing tasks.

## Features

1. User authentication
2. Task creation and editing
3. Team collaboration

## Setup

Run `npm install` to install dependencies.
Then run `npm start` to start the server.
```

## Pitfalls

- **Over-formatting:** Not every ALL CAPS word is a heading — use context
- **Lost content:** Always diff the output against the source to ensure nothing was dropped
- **Inconsistent heading hierarchy:** Establish heading levels before converting
- **Code detection:** Not every indented block is code — check context before adding code fences
- **Missing entry checks:** Without resumability artifacts, re-running duplicates work
- **Silent failures:** Always verify output; never assume conversion succeeded
- **`write_file` stream timeout on large output:** When Phase 3 enhancements produce a large `.md` frontmatter + structure (5+ KB), the `write_file` `content` argument can exceed the ~8K token stream limit and time out. **Fix:** Keep `content` under ~8K tokens per `write_file` call. If a write times out, retry with shorter content or split the write (frontmatter first, then body via `patch`). Never repeat the identical large payload unchanged.

## References

- `references/conversion-patterns.md` — Detailed pattern table, edge cases, false positive guards
- `references/heading-hierarchy.md` — Hierarchy validation rules, auto-fix strategies
- `references/code-block-detection.md` — Detection rules, language inference heuristics
- `references/verification-patterns.md` — Automated verification check implementations