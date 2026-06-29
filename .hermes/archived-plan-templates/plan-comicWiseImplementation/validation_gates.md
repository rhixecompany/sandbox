# Validation Gates

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Validation Gates

### After Phase 3:

```bash
pnpm type-check    # Must be 0 errors
pnpm lint:fix      # Auto-fix
```

### After Phase 6:

```bash
pnpm type-check    # DAL types validated
pnpm test          # Run unit tests
```

### After Phase 9A:

```bash
pnpm type-check    # Store types validated
pnpm lint:fix
```

### After Phase 10:

```bash
pnpm type-check
pnpm build --debug-prerender   # Static generation verified
```

### After Phase 11:

```bash
pnpm test           # Vitest unit tests pass
pnpm test:e2e       # Playwright E2E pass
pnpm build          # Final build green
```

---
