# Quality Gates & Validation

> Extracted from `debugger.prompt.md`.

## Quality Gates & Validation

### Pre-Implementation Checklist

- [ ] Feature requirements are clear and documented
- [ ] Database schema is designed and validated
- [ ] Cascade delete implications understood
- [ ] N+1 query risks identified and mitigated
- [ ] Similar patterns found in codebase
- [ ] Task broken down into 1-2 week sprints

---

### Development Commands

```bash
# Type check all code
pnpm run type-check

# Lint and auto-fix
pnpm run lint:fix

# Run unit tests
pnpm test

# Run E2E tests
pnpm run test:ui

# Full build validation
pnpm run build --debug-prerender

# Generate database types
pnpm db:generate

# Push schema to database
pnpm db:push

# Open database GUI
pnpm db:studio
```

---

### Code Quality Gates

Before delivering implementation, verify:

✅ **TypeScript:** `pnpm run type-check` → 0 errors ✅ **Linting:** `pnpm run lint:fix` → 0 errors ✅ **Tests:** `pnpm test` → All pass, 80%+ coverage ✅ **Build:** `pnpm run build --debug-prerender` → No errors ✅ **Security:** Zod validation, auth checks present ✅ **Performance:** Database indexes present, queries optimized ✅ **Accessibility:** ARIA labels, semantic HTML ✅ **Documentation:** Complex logic commented

---

### Code Review Standards

#### Type Safety

- Verify proper TypeScript usage and type definitions
- No `any` types anywhere

#### Performance

- Check for performance implications and optimization opportunities
- Verify database indexes on WHERE/JOIN columns
- No N+1 query patterns

#### Security

- Review for security vulnerabilities and best practices
- Zod validation on all user inputs
- Auth checks on mutations

#### Testing

- Ensure adequate test coverage for new features
- Unit tests for utilities and logic
- E2E tests for critical user flows

#### Documentation

- Verify code is properly documented
- Complex logic has comments
- Components have prop documentation

---
