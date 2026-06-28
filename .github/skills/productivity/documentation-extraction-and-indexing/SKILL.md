---
name: documentation-extraction-and-indexing
title: Documentation Extraction and Indexing
description: Extract full content from web documentation sources, save as structured markdown with consistent formatting, and create a searchable index catalog. Handles paginated/batch extraction, truncation workarounds, and verification.
version: 1.0.0
author: Hermes Assistant
license: MIT
tags: [documentation, extraction, indexing, web-extract, cataloging, verification]
---

# Documentation Extraction and Indexing

## When to Use

- Extracting documentation from multiple URLs (official docs, GitHub repos, tutorials)
- Building a local knowledge base from web sources
- Creating searchable indexes for extracted content
- Need full content without truncation (web_extract caps at ~5000 chars/page)
- Verifying extraction completeness across batches

## Trigger Conditions

- Task involves "extract docs from X URLs" or "build documentation catalog"
- User provides a list of URLs or a source document with URL list
- Output needs to be Markdown files + index for later reference

## Procedure

### Phase 1: URL Discovery & Planning
1. Read source document (e.g., `sample.prompt.md`) to get URL list
2. Group URLs by domain/source for batching
3. Plan batches of 5 URLs (web_extract limit)
4. Create output directory structure: `docs/<source>/`

### Phase 2: Batch Extraction (web_extract)
```python
# web_extract accepts max 5 URLs per call
batches = [urls[i:i+5] for i in range(0, len(urls), 5)]
for batch in batches:
    results = web_extract(batch)
    for r in results['results']:
        # Save with source header
        fname = sanitize_url(r['url'])
        write_file(path=f"docs/{source}/{fname}.md", 
                   content=f"# Source: {r['url']}\n\n{r['content']}")
```

**Critical:** Check `len(content)` for each result. If < 3000 chars on a known-large page, flag as potentially truncated.

### Phase 3: Browser Fallback for Truncated Pages
If web_extract truncates (returns summary instead of full content):
1. Use `browser_navigate(url)` 
2. Extract via `browser_console("document.querySelector('article').innerText")`
3. Save full content to same path

### Phase 4: Index Creation
Create `docs/<source>/index.md` with:
- Catalog table: #, File, Source URL, Status, Size
- Topic clusters grouping
- Verification commands
- Next-phase references

### Phase 5: Verification
```bash
ls docs/<source>/*.md | wc -l  # Count matches expected
head -3 docs/<source>/*.md     # All have "# Source: <URL>"
grep -r "truncated" docs/<source>/  # Should be empty
```

## File Naming Convention

```
docs/<source>/<sanitized-url>.md
```

Sanitization: replace non-alphanumeric with `_`, keep `.md` extension.

Example: `https://hermes-agent.nousresearch.com/docs/user-guide/features/skills` 
→ `hermes-agent.nousresearch.com_docs_user-guide_features_skills.md`

## Markdown File Structure

```markdown
# Source: <original-url>

<Full extracted content, no summarization>

---

*Extracted: <date> via web_extract (or browser fallback)*
```

## Pitfalls

| Pitfall | Detection | Fix |
|---------|-----------|-----|
| web_extract truncates large pages | Content length < 3000 on known-large page | Use browser fallback (navigate + console) |
| Batch size exceeded | web_extract error | Split into 5-URL batches |
| Filename collisions | Two URLs sanitize to same name | Add domain prefix or path hash |
| Missing source header | File doesn't start with "# Source:" | Re-write with header |
| Incomplete extraction | Count mismatch vs URL list | Re-run failed URLs individually |

## Verification Checklist

- [ ] All URLs from source list have corresponding `.md` files
- [ ] Each file has `# Source: <URL>` header
- [ ] No file shows truncation markers ("... [truncated]")
- [ ] Index.md catalogs every file with URL, status, size
- [ ] Verification commands pass

## Related Skills

- `web-research-pipeline` — broader research workflow
- `documentation-writer` — authoring new documentation
- `hermes-agent` — Hermes-specific CLI operations

## References

- `references/web-extract-batch-pattern.md` — Python batch extraction template
- `references/browser-fallback-pattern.md` — Console extraction for truncated pages
- `references/index-template.md` — Index.md structure template