# GitHub Copilot Instructions — rhixe_scans

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
   - **TypeScript** (strict) — check `tsconfig.json`
   - **React 19** — check `package.json`
   - **Node.js** — check `package.json` engine requirements

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Next.js 15** with App Router and Turbopack — check `next.config.ts`
   - **Prisma ORM 6** — check `prisma/schema.prisma`
   - **NextAuth v5** with Prisma adapter
   - **Tailwind CSS 3** — check `tailwind.config.ts` and `postcss.config.mjs`

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **Stripe** (`@stripe/react-stripe-js`) for payments
   - **PayPal** (`@paypal/react-paypal-js`) for payments
   - **UploadThing** for file uploads
   - **Resend** + React Email for email
   - **WebSocket** (`ws`) for realtime
   - **Jest** with ts-jest for testing
   - **Radix UI** primitives (shadcn/ui style)
   - **@dnd-kit** for drag-and-drop
   - **@tanstack/react-table** for data tables
   - **recharts** for charts

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines for comic reading platform
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: PascalCase for components, camelCase for utilities/hooks, kebab-case for pages
   - **Component structure**: shadcn/ui conventions with Radix UI primitives
   - **Forms**: React Hook Form + Zod validation
   - **Database**: Prisma schema-driven, migrations via Prisma Migrate
   - **Authentication**: NextAuth v5 for session management
   - **Payments**: Stripe/PayPal integration patterns
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Use TypeScript strict mode throughout
- Use `cn()` utility with tailwind-merge and class-variance-authority for styling
- Validate all user inputs with Zod schemas
- Use React Hook Form for form handling

## Documentation Requirements

- Follow the exact documentation format found in the codebase
- Match the style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for usage examples

## Testing Approach

- Match the exact structure and style of existing tests
- **Unit tests**: Jest with ts-jest
- Follow existing patterns for test organization

## Technology-Specific Guidelines

### TypeScript
- Strict mode TypeScript as configured
- ESLint with Next.js config
- Use TypeScript path aliases as defined in `tsconfig.json`

### Next.js 15 (App Router)
- Use App Router conventions (page.tsx, layout.tsx, loading.tsx, error.tsx)
- Server Components by default; Client Components only when needed
- Turbopack for development
- Image optimization via Next.js Image

### Database (Prisma)
- Schema managed via `prisma/schema.prisma`
- Use Prisma Client for all database operations
- Migrations via Prisma Migrate

### Auth (NextAuth v5)
- NextAuth v5 for session management
- Prisma adapter for database-backed sessions
- Use `auth()` helper for protected routes

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Never commit `.env` files — use environment variables
- Rate limiting via Upstash Ratelimit (if configured)

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Full-featured web application for reading comics online
- PostgreSQL via Prisma for data storage
- Stripe/PayPal for payment processing
- UploadThing for comic file uploads
- WebSocket support for realtime features
- Deploy via Vercel (recommended) or Docker
