# GitHub Copilot Instructions — university-libary-jsm

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
   - **TypeScript 5** (strict mode) — check `tsconfig.json`
   - **React 19** — check `package.json`
   - **Node.js** — check engine requirements in `package.json`

2. **Framework Versions**: Identify the exact versions of all frameworks
   - **Next.js 15** with Turbopack — check `next.config.ts`
   - **Drizzle ORM** — check `drizzle.config.ts`
   - **NextAuth v5** (beta) with Upstash Redis
   - **Tailwind CSS 4** — check configuration

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - **Neon PostgreSQL** (`@neondatabase/serverless`) — serverless Postgres
   - **ImageKit** for image uploads
   - **Upstash Workflow + QStash** for async job processing
   - **React Email + Nodemailer** for email
   - **Zod 4** with react-hook-form for validation
   - **shadcn/ui** with Radix UI primitives
   - **@dnd-kit** for drag-and-drop
   - **@tanstack/react-table** for data tables
   - **recharts** for charts
   - **lucide-react** for icons

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines for library management
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - **Naming conventions**: PascalCase for components, camelCase for utilities/hooks, dot notation for actions
   - **Component structure**: shadcn/ui conventions with Radix UI primitives
   - **Database**: Drizzle ORM with Zod schema validation
   - **Server Actions**: Next.js Server Actions for mutations, Zod for input validation
   - **Styling**: Tailwind CSS 4 with `cn()` utility, tailwind-merge, CVA
   - **Auth**: NextAuth v5 with `auth()` helper for protected routes
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

- Write self-documenting code with clear naming
- Use TypeScript strict mode throughout
- Use `cn()` utility with tailwind-merge and class-variance-authority for styling
- Validate all server action inputs with Zod schemas
- Use React Hook Form for form handling with Zod resolvers

## Documentation Requirements

- Follow the exact documentation format found in the codebase
- Match the style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for usage examples

## Testing Approach

- Match the exact structure and style of existing tests
- **TypeScript validation**: `npx tsc --noEmit`
- **Linting**: `npm run lint` (ESLint 9 with Next.js config)
- **Format checking**: `npm run format:check` (Prettier)

## Technology-Specific Guidelines

### TypeScript
- Strict mode as configured
- ESLint 9 with Next.js config + Prettier + plugins for drizzle, zod, jsx-a11y
- Use TypeScript path aliases

### Next.js 15 (App Router)
- App Router conventions (page.tsx, layout.tsx, loading.tsx, error.tsx)
- Server Components by default; Client Components only when needed
- Server Actions for all mutations with Zod validation
- Turbopack for development

### Database (Drizzle ORM + Neon)
- Schema in `database/schema.ts`
- Use Drizzle Kit for migrations (`db:push`, `db:generate`, `db:migrate`)
- Zod schema validation for type safety
- Neon serverless PostgreSQL via `@neondatabase/serverless`

### Auth (NextAuth v5)
- NextAuth v5 for session management
- Use `auth()` helper for protected routes
- Rate limiting via Upstash Ratelimit

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Never commit `.env` files or secrets
- Rate limiting in API routes via Upstash Ratelimit

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- University Library Management System (BookWise)
- Full-stack application for managing library book requests, user accounts, and administrative workflows
- Neon PostgreSQL with Drizzle ORM for data storage
- ImageKit for image uploads
- Upstash Workflow + QStash for async job processing
- React Email for email templates
- Deploy on Vercel with Neon PostgreSQL and Upstash Redis
