# 17. Testing

> Extracted from `setup.prompt.md`.

## 17. Testing

### Unit Tests (Vitest)

```bash
pnpm test                        # Run all
pnpm test -- --watch             # Watch mode
```

- Files: `src/**/*.test.{ts,tsx}`
- Environment: `jsdom` with setup at `src/tests/setup-env.ts`
- Mock external deps (database, auth)
- Test behavior, not implementation details
- Use `describe` / `it` blocks

### Testing Conventions (from `.github/instructions/testing.instructions.md`)

- **Accessibility:** Include accessibility checks in component tests
- **Test config:** Use `.env.test` for test-specific configuration
- **Cleanup:** Tests must clean up after themselves (no state leakage between tests)
- **Auth mocking:** Mock auth for unit tests; use real auth for E2E
- **Assertions:** Use Vitest built-in assertions (not external assertion libraries)
- **Naming:** Test files mirror source files: `my-feature.ts` → `my-feature.test.ts`

### E2E Tests (Playwright)

```bash
pnpm test:ui                     # Run E2E tests
pnpm test:ui:codegen             # Test code generator
```

- Page Object pattern
- Fixtures for test data
- Cross-browser testing

### Pre-PR Checklist

```bash
pnpm type-check          # 0 TypeScript errors
pnpm lint:fix            # 0 ESLint errors
pnpm test                # All unit tests pass
pnpm build               # Clean production build
```

---
