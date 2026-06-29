# GitHub Copilot Instructions — Banking

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Layered** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, security, and testability** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **TypeScript** (strict mode) — examine `tsconfig.json` for compiler options
   - **Bun** runtime (check `bunfig.toml` and `bun.lock`)
   - Node.js compatibility (verify through `package.json` engine requirements)

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Next.js 16** with App Router — check `next.config.ts` for configuration
   - **React 19** — verify through `package.json` dependencies
   - **shadcn/ui** components — respect `components.json` configuration
   - **Drizzle ORM** — check `drizzle.config.ts` for schema and migration settings

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **PostgreSQL** via drizzle-orm
   - **Plaid** integrations for bank connections
   - **Dwolla** for ACH transfers
   - **NextAuth.js** for authentication
   - **Zustand** for client state management
   - **Zod** for validation schemas
   - **Playwright** for E2E testing
   - **Vitest** for unit testing

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: `dot.camelCase` for server actions, `PascalCase` for components, `camelCase` for utils/hooks, `snake_case` for database tables
   - **Code organization**: Server Actions in `src/actions/`, components in `src/components/`, DAL in `src/dal/`, database schema in `src/database/`
   - **Error handling**: Use `{ error, ok }` pattern with Zod validation at all entry points
   - **Database access**: Constructor-based DAL classes with type-safe queries
   - **Server Actions**: "use server" directive with Zod input validation, returning `{ error, ok }`
   - **Environment variables**: Access via `lib/env.ts`, never inline secrets
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow established naming conventions (`dot.camelCase` for server actions, `PascalCase` for components)
- Use Zod for runtime validation at every action entry point
- Implement idempotency for financial transactions
- Use soft-delete patterns for user data (never hard delete)
- Encrypt sensitive data at rest using `lib/utils` encryption functions

## Documentation Requirements

- Match the exact documentation format found in the codebase
- Follow existing patterns for non-obvious behavior
- Document parameters, returns, and exceptions in the same style as existing code
- Match class-level and function-level documentation style

## Testing Approach

- Match the exact structure and style of existing tests
- **Unit tests**: Vitest for isolated component/function testing
- **E2E tests**: Playwright for end-to-end browser tests
- Follow existing patterns for test organization (mirror source structure)
- Use existing test utilities and fixtures

## Technology-Specific Guidelines

### TypeScript
- Use strict mode TypeScript as configured in `tsconfig.json`
- Follow established type patterns from existing codebase
- Use `@/` path aliases for imports
- Define types in `src/types/` directory

### Next.js 16 (App Router)
- Use App Router conventions (page.tsx, layout.tsx, loading.tsx, error.tsx)
- Server Components by default; Client Components only when needed
- Server Actions for all mutations with "use server" directive
- API routes under `src/app/api/`

### Database (Drizzle ORM + PostgreSQL)
- Define schemas in `src/database/schema.ts`
- Use DAL pattern (constructor-based classes in `src/dal/`)
- Promote all database operations through DAL layer
- Use Drizzle Kit for migrations (`db:generate`, `db:migrate`)

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns (Zod validation + `{ error, ok }` return)
- Follow the same approach to testing as seen in the codebase
- Use environment variables for all secrets via `lib/env.ts`
- Use the same approach to configuration as seen in the codebase

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Banking/fintech application: prioritize security, idempotency, and data integrity
- Plaid integration: follow existing patterns for link token creation and token exchange
- Dwolla integration: follow existing patterns for customer creation and ACH transfers
- Never commit secrets — use `.env.local` and access via `lib/env.ts`
