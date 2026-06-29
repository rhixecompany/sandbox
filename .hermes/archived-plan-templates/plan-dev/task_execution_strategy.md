# Task Execution Strategy

> Extracted from `plan-dev.prompt.md`.

## Task Execution Strategy

### Implementation Order

**PHASE 1 (BLOCKING):** Fix TypeScript errors → Everything else depends on this

**PHASE 2 (FOUNDATION):** Verify database, auth, dev environment

**PHASES 3-7 (FEATURES):** Implement features in order (User → Comics → Reader → Bookmarks → Admin)

**PHASE 8 (QUALITY):** Testing and performance optimization

**PHASE 9 (DEPLOYMENT):** Documentation and production deployment

### Systematic Approach

For each task:

1. **Create Zod schema** if new entity
2. **Create/update DAL** with proper eager loading
3. **Create server actions** with validation and error handling
4. **Build UI components** (server + client as needed)
5. **Add tests** hitting 80%+ coverage goal
6. **Manual testing** in dev environment
7. **Commit** with clear message linking to task

### Token Efficiency Tips

- **Parallel reads:** Read multiple files at once when planning
- **Batch edits:** Make multiple edits with single tool call
- **Focused prompts:** Ask for specific guidance, not broad reviews
- **Cache knowledge:** Reference files once, reuse understanding
- **Complete features:** Finish one before starting next
- **Avoid re-asks:** Plan implementation before requesting

---
