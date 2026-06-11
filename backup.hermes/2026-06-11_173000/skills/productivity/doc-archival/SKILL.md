---
name: doc-archival
description: "Fetch documentation from authoritative URLs and save as structured, formatted markdown files with consistent layout, cross-references, and an index catalog."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [documentation, markdown, archival, web-extract, index]
    related_skills: [llm-wiki]
---

# Doc Archival

Fetch documentation from authoritative URLs and save as structured, formatted markdown files with consistent layout, cross-references, and an index catalog.

## When This Skill Activates

Use this skill when the user:
- Asks to fetch, download, or archive documentation from URLs
- Wants to save web documentation as local markdown files
- Asks to create a docs folder structure from online sources
- Wants to build a local mirror/reference of external documentation
- Says "save this as markdown", "archive these docs", "fetch and format"

## Core Workflow

### Phase 1: Fetch

1. **Batch-fetch all URLs** using `web_extract(urls=[...])` — up to 5 URLs per call
2. **For truncated pages** (LLM summarization timeout), use `browser_navigate(url)` then `browser_console(expression="document.querySelector('article').innerText")` to get full content
3. **Store content** in memory or temp files — don't write final files until you have all content

### Phase 2: Structure

Create a directory structure that mirrors the source URL paths:

```
docs/
├── INDEX.md                    (master index — always create this)
├── section/
│   ├── topic/
│   │   └── index.md            (always use index.md, never topic.md)
│   └── other-topic/
│       └── index.md
```

**Rules:**
- Always use `index.md` as the filename (not the page title)
- Create subdirectories that reflect the source URL path structure
- Group related pages under common parent directories

### Phase 3: Write Files

Each markdown file follows this exact template:

```markdown
# <Page Title>

> **Source:** [<title>](<full-url>)

## Overview

<2-3 sentence summary from source>

---

## <Section 1>

<Content with code blocks, tables, lists as appropriate>

---

## <Section 2>

<More content>

---

## See Also

- [<Related Page Title>](<relative-or-external-url>)
- [<Another Page>](<url>)
```

**Formatting rules:**
- H1 title on line 1
- Source URL blockquote on lines 2-3
- `## Overview` as first section
- `---` horizontal rules between major sections
- Code blocks MUST have language identifiers (```bash, ```yaml, ```python, ```markdown, ```json)
- Tables for structured comparisons
- `## See Also` as the last section with 3-10 relevant links
- Use external URLs for See Also links (not relative paths) unless files are in the same directory tree

### Phase 4: Create Index

The `INDEX.md` at the root MUST contain:

```markdown
# <Project> Documentation

> **Source:** <base-url>
> **Generated:** YYYY-MM-DD
> **Pages:** N

---

## Index

### <Category 1>

| #  | Page    | Description    | Path                    |
|----|---------|----------------|-------------------------|
| 01 | **X**   | Brief desc     | `path/to/index.md`      |

### <Category 2>

...

---

## Source URLs

| Page    | URL          |
|---------|--------------|
| X       | https://...  |

---

## Directory Structure

```
<tree of all files>
```

---

## See Also

- <relative links to all indexed pages>
```

### Phase 5: Verify

After writing all files, run a verification pass:

1. **Existence check** — all expected files exist and are > 1 KB
2. **Structure check** — all files have H1, source URL, `## See Also`, ≥3 H2 sections
3. **Content check** — no obvious truncation, code blocks are complete
4. **Fix issues** — patch any files that fail checks
5. **Final validation** — re-read all files and confirm pass

## Pitfalls

- **web_extract truncation:** Large pages get LLM-summarized and truncated. Always check if content was truncated. If the returned content has `[... summary truncated ...]` or seems incomplete, use `browser_navigate` + `browser_console` to get the full text from `document.querySelector('article').innerText`.
- **Patch corruption:** When using `patch()` on files with code blocks, the fuzzy matcher can corrupt the file if the old_string matches inside a code block. If a patch produces a bad diff, rewrite the entire file with `write_file` instead of patching.
- **INDEX.md code blocks:** The directory tree code block in INDEX.md is especially vulnerable to patch corruption. Prefer `write_file` over `patch` for INDEX.md.
- **Missing See Also:** Always add a `## See Also` section to every file. This is the most commonly missed requirement.
- **Inconsistent naming:** Always use `index.md` as the filename, never the page title as the filename.

## Verification Script

Use this Python snippet (via `execute_code`) to verify all files:

```python
import os, re

base_dir = "<docs-base-dir>"
expected_files = [...]  # list of relative paths

all_pass = True
for f in expected_files:
    full_path = os.path.join(base_dir, f)
    with open(full_path, 'r', encoding='utf-8') as fh:
        lines = fh.readlines()
        content = ''.join(lines)
    
    has_h1 = lines[0].strip().startswith('# ')
    has_source = 'hermes-agent.nousresearch.com' in ''.join(lines[:5]) or 'Source:' in ''.join(lines[:5])
    has_see_also = '## See Also' in content
    h2_count = sum(1 for l in lines if l.strip().startswith('## '))
    
    passed = has_h1 and has_source and has_see_also and h2_count >= 3
    status = "PASS" if passed else "FAIL"
    if not passed:
        all_pass = False
    print(f"  [{status}] {f:55s} {len(lines):>4} lines  H2s={h2_count}")
```
