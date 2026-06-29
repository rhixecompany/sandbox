# 10. 🔄 Anti-Rate-Limiting Strategy

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 10. 🔄 Anti-Rate-Limiting Strategy

When using this prompt with Copilot CLI, follow these practices to avoid token exhaustion:

### Chunked Execution

1. **Never paste full documentation files into a prompt** — reference by path
2. **Work in focused phases** — one feature/section at a time
3. **Use section numbers** — "Implement pattern from Section 23.2" instead of quoting code
4. **Batch related changes** — edit multiple files in one turn, not sequential turns

### Efficient Prompting

```bash
# ✅ Good: Reference by section
"Add reading progress tracking using the idempotent upsert pattern from docs/dev.content.md Section 23.2"

# ❌ Bad: Paste entire code blocks into prompt
"Here's the full schema... [500 lines] ... now implement this"

# ✅ Good: Focused task with persona
"As Implementer, add a DAL method for comic search following docs/dev.content.md Section 22.4"

# ❌ Bad: Open-ended request
"Implement all features for the entire application"
```

### Session Management

- **Start fresh sessions** for each phase (Foundation → Features → QA → Deploy)
- **Commit between phases** to save state and reduce context window
- **Use `pnpm type-check` after each batch** to catch issues early
- **Keep prompts under 500 words** — reference docs instead of quoting

---
