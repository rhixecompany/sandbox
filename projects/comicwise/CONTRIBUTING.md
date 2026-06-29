# ComicWise — Contributing Guide

## Getting Started

```bash
git clone <repo-url>
cd comicbook
pnpm install
cp .env.local.example .env.local
pnpm db:push
pnpm dev
```

## Before You Submit

Run the full validation suite:

```bash
pnpm validate
```

This runs: format check → type check → lint strict → import check → health check → tests.

## Pull Request Process

1. **Branch from `main`**: `git checkout -b feature/my-feature`
2. **Make changes** following project conventions
3. **Run all quality gates**:
   ```bash
   pnpm lint:strict && pnpm triage && pnpm type-check && pnpm test && pnpm build
   ```
4. **Write tests** for new features
5. **Update documentation** for user-facing changes
6. **Open a PR** against `main`

## Commit Convention

We use conventional commits:

```
feat: add chapter bookmarking
fix: resolve reader progress not saving
docs: update setup guide for Neon
chore: upgrade Drizzle ORM to 0.45.1
test: add comic DAL unit tests
refactor: consolidate auth middleware
style: fix indentation in proxy.ts
perf: optimize image loading with lazy loading
```

## Code Standards

- **TypeScript**: Strict mode, zero `any` types (ESLint enforced)
- **ESLint**: Zero warnings required in CI
- **React**: Server Components first, React Compiler auto-memoization
- **Database**: Drizzle ORM with eager loading (no N+1)
- **Mutations**: Server Actions only, no API routes
- **Validation**: Zod schemas on all input boundaries
- **Formatting**: Prettier with tailwindcss plugin

## What We Look For

- ✅ Type safety (no `any`, proper generics)
- ✅ Performance (no N+1 queries, proper image optimization)
- ✅ Accessibility (ARIA labels, keyboard navigation)
- ✅ Testing (unit tests for DAL/actions, E2E for critical flows)
- ✅ Documentation (updated for user-facing changes)

## Testing

```bash
pnpm test          # Vitest unit tests
pnpm test:ui       # Playwright E2E tests
```

New features should include:

- Unit tests for DAL methods
- Server Action tests
- Component tests where applicable
- E2E tests for critical user flows

## Questions?

Open a [GitHub Issue](https://github.com/comicwise/comicwise/issues) or start a [Discussion](https://github.com/comicwise/comicwise/discussions).
