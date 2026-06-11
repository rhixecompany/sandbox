# ComicWise — Testing Guide

## Test Framework

| Layer | Tool | Scope |
|-------|------|-------|
| Unit Tests | Vitest 4.1 | DAL, actions, utils, schemas |
| Component Tests | Vitest + Testing Library | React component rendering |
| E2E Tests | Playwright 1.58 | Full user flows |

## Running Tests

```bash
pnpm test              # Unit tests (Vitest, jsdom)
pnpm test:ui           # E2E tests (Playwright)
pnpm test:ui:codegen   # Interactive test recorder
pnpm test:ui:report    # Show Playwright report
```

## Test Structure

```
tests/
├── unit/
│   ├── dal/               # DAL method tests
│   ├── actions/           # Server Action tests
│   ├── schemas/           # Zod schema validation tests
│   └── utils/             # Utility function tests
├── components/            # Component render tests
└── e2e/
    ├── auth.spec.ts       # Login, signup, logout
    ├── comics.spec.ts     # Browse, filter, search
    ├── reader.spec.ts     # Chapter reader, navigation
    ├── bookmarks.spec.ts  # Add/remove bookmarks
    ├── ratings.spec.ts    # Rate comics
    └── admin.spec.ts      # Admin operations
```

## What to Test

### DAL Methods
- CRUD operations for each of the 27 tables
- Relation eager loading via `.with()`
- Edge cases: not found returns `null`, empty results
- Filter, sort, pagination parameters

### Server Actions
- Zod validation rejection (every schema)
- Authorization checks (unauthenticated users)
- Successful operation paths
- Error handling for database failures
- ActionResult return type correctness

### Zod Schemas
- Valid input cases
- Invalid input rejection
- Edge cases (empty strings, special characters, Unicode)

### Components
- Render with data
- Render empty/loading states
- Interactive elements (forms, buttons, modals)
- Responsive behavior

### E2E Flows
- User registration and login (credentials + OAuth)
- Comic browsing with filters
- Chapter reading with progress tracking
- Bookmark management
- Rating and comments
- Admin CRUD operations
- Notification display

## Coverage Requirements

- Minimum 80% coverage for DAL and actions
- 100% coverage for Zod schemas
- E2E coverage for all critical user paths

## CI Integration

```yaml
# GitHub Actions
- name: Unit Tests
  run: pnpm test

- name: E2E Tests
  run: pnpm test:ui
```
