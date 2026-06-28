# Fix Plan: Prompts Enhancement

## Priority Order

1. **High: Missing tags (150 files)** — Bulk-add `tags: []` via Python sweep
2. **Medium: Missing description (1 file)** — Add `description` to Initial.prompt.md
3. **Low: H1 body start (11 files)** — Add `# ` heading where missing
4. **Low: Double fence false positives** — No action needed (horizontal rules, not bugs)

## Execution Strategy

- Use `execute_code` for bulk tags fix (150 files, same missing-field pattern)
- Use individual `patch` for the 1 missing description
- Use batch for h1 fixes if needed
