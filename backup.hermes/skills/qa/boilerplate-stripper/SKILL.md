---
name: boilerplate-stripper
title: Markdown Boilerplate Stripper
description: >
  Strip known template boilerplate from SKILL.md, .prompts.md, or any markdown
  file. Detects and removes empty generic sections left behind by template
  scaffolding. Run against a single file, a folder, or the entire skills library.
author: Alexa
tags: [cleanup, boilerplate, template, markdown, normalization, batch]
version: 1.0.0
---

# Markdown Boilerplate Stripper

Automatically strip known template boilerplate patterns from markdown files.
Works on SKILL.md, .prompts.md, or any markdown that accumulated scaffolding
garbage.

## When to Use

- A skill or prompt file has generic sections that add no value
- A file ends with template scaffolding: "Prerequisites and environment are properly configured", "Prepare before executing", "Phase 1: Preparation — Set up required environment..."
- You need to batch-clean an entire directory of markdown files
- You inherited imported/generated skills and want to normalize them

## When NOT to Use

- Content that happens to contain those words as legitimate prose
- Files where the generic sections ARE the content (thin scaffolding for new topics)

## How It Works

Uses a Python script (`scripts/strip-boilerplate.py`) that applies 6 regex
patterns to strip known boilerplate. Each pattern is conservative — it matches
the exact known template text and nothing else.

### Patterns Removed

| # | Section | What Matches |
|---|---------|-------------|
| 1 | `## Overview` | Self-referential "The X skill provides tools and workflows..." |
| 2 | `## Workflow` | Generic Phase 1–4 (Preparation → Execution → Verification → Completion) |
| 3 | `## When to Use` | "When you need to perform X operations or tasks" + 3 bullets |
| 4 | `## Best Practices` | 5 numbered generic rules starting with "Prepare before executing" |
| 5 | `## Verification Checklist` | 5 generic checkboxes with "Prerequisites and environment" |
| 6 | Stray path ref | Inline `, use skills\...\skill.md` fragments |

The patterns are embedded in `scripts/strip-boilerplate.py` as compiled
`re.Pattern` objects — easy to add more.

## Workflow

### Phase 1: Inventory

Scan the target folder for boilerplate:

```bash
python scripts/strip-boilerplate.py --dry-run --path ./skills
```

If `--path` is omitted, defaults to the Hermes skills directory
(`~/AppData/Local/hermes/skills/`).

### Phase 2: Review Dry-Run Output

The dry-run shows:
- How many files are affected
- Which patterns were found in each file
- Total number of boilerplate removals

Review before applying. If you see files that shouldn't be touched,
exclude them via `--exclude` (supports glob).

### Phase 3: Apply

```bash
# Apply to all affected files
python scripts/strip-boilerplate.py

# Apply to a specific folder
python scripts/strip-boilerplate.py --path ./docs

# Apply to a single file
python scripts/strip-boilerplate.py --path ./path/to/file.md

# Exclude specific files
python scripts/strip-boilerplate.py --exclude "node_modules/*" --exclude "*.bak"
```

### Phase 4: Verify

```bash
# Confirm zero remaining boilerplate
python scripts/strip-boilerplate.py --dry-run

# Spot-check a few cleaned files
tail -5 path/to/skill/SKILL.md
```

## CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--dry-run` | `False` | Report what would be removed without modifying files |
| `--path` | Hermes skills dir | Target file or folder. File = single file. Folder = recursive scan for `<glob>` |
| `--glob` | `*SKILL.md` | Glob pattern when path is a directory |
| `--exclude` | — | Glob patterns to exclude (repeatable) |

## Pitfalls

- **Custom Content**: If a skill has a legitimate `## Verification Checklist`
  section that happens to start with "Prerequisites and environment", the
  pattern will match. Always run `--dry-run` first and review.
- **False matches in code blocks**: The patterns match raw text — a code block
  showing "Prerequisites and environment" as an example will be matched.
  The script targets markdown sections, not fenced code blocks, so this is
  unlikely but possible with inline code.
- **Safe to re-run**: Already-cleaned files won't be affected — patterns only
  match exact text.

## Files

- `scripts/strip-boilerplate.py` — The cleanup engine (runs standalone)
- `references/boilerplate-patterns.md` — Reference listing all currently known
  patterns with examples

## Verification

After running:

```bash
# Verify: should show 0 affected
python scripts/strip-boilerplate.py --dry-run --path <target>

# Check no corrupt frontmatter
grep -rn "^---$" <target>/*/SKILL.md | wc -l
# Should be even number (open + close) per file
```

## Origin

This skill was extracted from a library-wide sweep that cleaned 144 SKILL.md
files across 196 scanned, removing 275 boilerplate sections and 7 stray path
references in a single batch.
