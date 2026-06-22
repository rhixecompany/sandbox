# Notes & Considerations

> Extracted from `plan-phase1ComprehensiveValidation.prompt.md`.

## Notes & Considerations

### Phase 1

- TypeScript error is a **blocker** — fix first
- Test failures likely due to mock setup or assertion mismatches — analyze before fixing
- Auto-fix will resolve ~10 lint errors; ~20 require manual attention
- Some warnings may be acceptable with documentation (e.g., intentional console.logs)

### Phase 2

- ESLint config is a **leverage point** for code quality — worth investing time
- Hybrid approach: use reference config as template but apply selectively
- `perfectionist` and `unicorn` are nice-to-have; focus on critical plugins first
- Security plugin is **important** for catching vulnerabilities early

### Phase 3

- Linear order ensures no dependency issues
- Seeding system ✅ provides 274 test comics, so features can use real-like data
- Start with User Profile to establish patterns (DAL, actions, components)
- Comics Listing is critical path; chapter reader depends on it
- Bookmarks completes the core loop; advanced features are post-MVP

### General

- Commit frequently (after each task, not just phase end)
- Quality gate must pass before moving to next phase
- Documentation in `.github/copilot-instructions.md` should be updated
- No breaking changes to existing APIs or database schema without migration

---
