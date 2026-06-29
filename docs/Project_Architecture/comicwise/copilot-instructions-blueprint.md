# GitHub Copilot Instructions — comicwise

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our **Layered (Monolithic)** architectural style and established boundaries
5. **Code Quality**: Prioritize **maintainability, security, and performance** in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - **TypeScript** (strict mode) — examine `tsconfig.json`
   - **Node.js** — check `engines` in `package.json`
   - **Package manager**: pnpm (`pnpm@9.12.3`)

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Next.js 15** with App Router — check `next.config.ts`
   - **Prisma ORM** — check schema in `prisma/schema.prisma`
   - **NextAuth.js** for authentication
   - **Stripe** for payment subscriptions

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **PostgreSQL** via Prisma
   - **Tailwind CSS** — check `tailwind.config.ts` and `postcss.config.mjs`
   - **Drizzle ORM** (if present in codebase)
   - **shadcn/ui** components (if configured via `components.json`)

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines for comic streaming platform
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: camelCase for utilities/hooks, PascalCase for components, kebab-case for pages
   - **Code organization**: API routes in `src/app/api/`, components in `src/components/`
   - **Database**: Prisma schema-driven, migrations via Prisma Migrate
   - **Authentication**: NextAuth.js session management
   - **Payments**: Stripe subscription lifecycle via webhooks
   - **Image optimization**: Next.js Image component for comic assets
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Follow established naming conventions from the codebase
- Use TypeScript strict mode throughout
- Ensure proper error handling in API routes and server actions
- Optimize images for digital comic delivery

## Documentation Requirements

- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior
- Use the same format for parameter descriptions as existing code

## Testing Approach

- Match the exact structure and style of existing tests
- Follow existing testing patterns (Playwright, Vitest)
- Mirror source directory structure in test files
- Use existing test utilities and fixtures

## Technology-Specific Guidelines

### TypeScript
- Use strict mode TypeScript as configured
- Follow established type patterns from existing codebase
- Use path aliases as defined in `tsconfig.json`

### Next.js 15 (App Router)
- Use App Router conventions (page.tsx, layout.tsx)
- Server Components by default; Client Components only when needed
- API routes under `src/app/api/`

### Database (Prisma)
- Manage schema via `prisma/schema.prisma`
- Use Prisma Client for all database operations
- Follow existing migration patterns (`prisma migrate`)

### Payments (Stripe)
- Use Stripe webhooks for subscription lifecycle events
- Follow existing patterns for checkout session creation
- Store Stripe customer IDs and subscription status

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Use `.env.local` for secrets — never commit sensitive data
- Use `pnpm` for package management

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Digital comic storefront with subscription management
- Use Next.js Image optimization for comic assets
- Stripe webhooks for subscription lifecycle events
- Node 18+ required
