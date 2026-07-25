# Scrape-Artifact Remediation Pattern

**Source session:** 2026-06-29 — awesome-hermes-agent scrape duplicate cleanup
**Files involved:** 6 markdown files (README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, preamble.md, skills-&-plugins.md, core-overview.md)

## What This Covers

Fixing quality defects introduced by scraping/content-extraction tools — duplicated sections, cut-off sentences, merged entries, and trailing separator artifacts in markdown files.

## Common Defect Patterns

| Pattern | Example | Fix Strategy |
|---------|---------|-------------|
| **Exact duplicate block** | "Community Skills" appears twice, copied verbatim at the end of the file | Delete the second occurrence via `patch` with exact text match |
| **Trailing duplicate sections** | "Repository Suggestions 2" and "Code of Conduct 2" repeat the same content from above | Same — delete the second occurrence. The section heading is unique enough to match on |
| **Duplicated paragraph (standard text)** | The "Attribution" paragraph in CODE_OF_CONDUCT.md appears twice | `replace_all=true` for both, but must restore one copy after. Safer: match the duplicated block precisely and remove it, leaving the original |
| **Line-level duplication** | A single metadata line repeated with formatting differences | Match the entire duplicated pair and replace with a single clean copy |
| **Text corruption** | Cut-off sentence merges two list entries (e.g., super-hermes line and litprog-skill description smashed together) | Match the corrupt text exactly — it's unique by definition |
| **Extraneous formatting** | Extra `---` separator lines left behind after content was extracted | Simple `old_string` match for `---\n\n---` |

## Workflow

### Phase 1: Inventory

Read all files in the target directory. Build a map of each file's structure. Look for:
- Repeated section headings at the end of files (copied verbatim)
- Unusual line breaks mid-sentence
- Content that references the same passage twice
- Trailing content that duplicates something that came before

### Phase 2: Fix (Surgical Removal)

For each defect:

1. **Read the full file** with `read_file(path)` to get exact line content
2. **Identify unique matching text** — the section heading for duplicates, the corrupt sentence for corruption
3. **Use `patch(mode='replace', path, old_string, new_string='')`** to delete the duplicate block. Empty `new_string` deletes the matched text
4. **For `replace_all=true` text removal**: verify both copies were removed, then restore one copy. If you used replace_all, you'll need a follow-up `patch` or `write_file` call to put one copy back

### Phase 3: Verify

Re-read each fixed file's affected region. Check:
- The duplicate is gone
- The original content survived
- No formatting breaks (respect blank lines between sections)
- The file ends cleanly

### Phase 4: Update Documentation

If a catalog, inventory, or status document existed before the fixes, update it to:
- Note which files were fixed and what the defect was
- Update file sizes (they'll be smaller after removal)
- Change 'Has defect' status entries to 'Fixed'

## Pitfalls

- **`replace_all=true` removes everything**. If the same text appears in two places (duplicate + original), `replace_all=true` deletes both. Always verify the file state after and restore if needed.
- **Blank lines matter**. Removing a section header but leaving a blank line gap creates visual whitespace. Include the trailing newline in your match.
- **Corruption may span list boundaries**. A cut-off sentence in one list entry often merges into the next. Include both entries in your `old_string` to clean up cleanly.
- **Don't use file index.md for navigation index content as a fix target**. It's the source of truth for the docs structure — fix content files, not the index.

## When to Use This Pattern

- Scraped/archived web content has been downloaded as markdown
- AI-generated content has repeated sections or truncated sentences
- Imported documentation shows signs of tool-chain artifacts
- Any markdown file set where you see section headings repeated at the bottom
