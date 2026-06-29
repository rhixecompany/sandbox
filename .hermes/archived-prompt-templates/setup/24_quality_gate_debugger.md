# 24. Quality Gate Debugger

> Extracted from `setup.prompt.md`.

## 24. Quality Gate Debugger

When debugging and fixing errors/warnings/deprecations, follow this workflow:

### Phase 1: Run Validation Scripts

```powershell
# Windows / PowerShell
pnpm type-check    # TypeScript errors
pnpm lint:fix      # ESLint errors/warnings
pnpm test          # Vitest unit tests
pnpm build         # Production build
```

### Phase 2: Document Issues

For each issue found, document in `docs/proposedFixes.MD` and `docs/proposedFixes.json`:

- File path and line number
- Error code and severity
- Root cause analysis
- Before/after code snippets
- Fix rationale and references

### Phase 3: Batch Fixes

Apply fixes in this order (highest impact first):

1. Import resolution errors
2. Type errors
3. Build errors
4. Test failures
5. Lint warnings

### Phase 4: Verify

Rerun all validation scripts until all gates pass with zero errors/warnings.

### Key Debugging Patterns

| Pattern | Problem | Solution |
| --- | --- | --- |
| `new Date()` in Server Component | `NEXT_PRERENDER_CURRENT_TIME` | Use `useCurrentYear()` hook |
| `toHaveText()` without argument | Playwright 1.58+ requires arg | Use `toBeVisible()` instead |
| `try { ... } catch { throw err }` | Useless try/catch | Remove try/catch wrapper |
| Duplicate export | `TS2300` error | Use `export type { X }` for types |
| `isolatedModules` type re-export | `TS1205` error | Separate type exports from value exports |

### Documentation Requirements

Every significant fix must be recorded in both:

1. `docs/proposedFixes.MD` - human readable format
2. `docs/proposedFixes.json` - structured JSON with keys: file, line, issue, fix, before, after, rationale, references
