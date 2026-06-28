# Conversion Patterns & Edge Cases

## Heading Detection Patterns

| Source Pattern | Markdown | Confidence | Notes |
|----------------|----------|------------|-------|
| `ALL CAPS LINE` (standalone) | `## All Caps Line` | High | Must be isolated line, not in paragraph |
| `Title Case Line` + `=====` | `## Title Case Line` | High | Setext underline (any length >= 3) |
| `Title Case Line` + `-----` | `### Title Case Line` | High | Setext H2 underline |
| `# ` prefix | `# Title` | High | ATX style, preserve level |
| `1. ` / `2. ` at line start | `1. Item` | High | Numbered list, not heading |
| `### ` prefix in middle of text | Keep as-is | Medium | Could be intentional literal |

**False Positive Guards:**
- ALL CAPS inside paragraph → NOT a heading
- ALL CAPS acronyms (API, JSON, HTTP) → NOT headings
- Lines ending with `:` followed by indented content → could be definition list, not heading

## List Detection Patterns

| Source Pattern | Markdown | Notes |
|----------------|----------|-------|
| `1. ` / `2. ` / `3. ` | `1. Item` | Preserve numbering |
| `- ` / `* ` / `+ ` | `- Item` | Normalize to `-` |
| Indented `    - ` | `    - Item` | Nested list (4 spaces) |
| `a) ` / `b) ` / `i) ` | `a) Item` | Alpha/roman lists |

**Edge Cases:**
- Hard-wrapped list items: detect continuation by indent alignment
- Mixed list types in same parent → normalize to consistent style

## Code Block Detection

| Indicator | Action |
|-----------|--------|
| 4+ space indent on consecutive lines | Wrap in ``` fence |
| Tab indent on consecutive lines | Wrap in ``` fence |
| Triple backticks present | Preserve, add language if missing |
| `file/path/name` inline | Wrap in backticks |
| Monospace-like: `command --flag` | Wrap in backticks |

**Language Inference Heuristics:**
- `npm`, `yarn`, `node`, `package.json` → `bash` or `shell`
- `import`, `export`, `function`, `const` → `javascript` / `typescript`
- `def `, `class `, `import ` → `python`
- `SELECT`, `FROM`, `WHERE` → `sql`
- `docker`, `kubectl`, `helm` → `bash`

## Emphasis Conversion

| Source | Markdown | Priority |
|--------|----------|----------|
| `**text**` | `**text**` | Preserve |
| `__text__` | `**text**` | Normalize |
| `*text*` | `*text*` | Preserve |
| `_text_` | `*text*` | Normalize |
| `ALL CAPS WORD` (isolated) | `**WORD**` | Context-dependent |

**Guard:** Don't convert ALL CAPS in:
- Acronyms (API, URL, HTTP, JSON, XML, YAML, CLI, GUI, IDE)
- File extensions (.MD, .TXT, .JSON, .YAML)
- Environment variables (PATH, HOME, CONFIG_DIR)
- Command flags (--HELP, --VERSION)

## Link & Reference Conversion

| Source | Markdown |
|--------|----------|
| `http://...` / `https://...` | `[url](url)` or preserve if already linked |
| `file/path/name` (detected) | `` `file/path/name` `` |
| `see Section 3` | `[see Section 3](#section-3)` |
| `[ref]` / `[1]` | `[ref](#ref)` if target identifiable |

## Table Detection

| Source Pattern | Action |
|----------------|--------|
| `| col1 | col2 |` with `|---|---|` | Preserve as Markdown table |
| Aligned columns with spaces | Convert to pipe table |
| TSV-like tabs | Convert to pipe table |

## Frontmatter Template

```yaml
---
title: Document Title
description: Brief one-line description
date: YYYY-MM-DD
tags: [tag1, tag2]
---
```

Use when: converting documentation, README, specs, or any file >200 words.