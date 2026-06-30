---
status: in_progress
status: in_progress
status: in_progress
---
title: "Copilot Instructions Generator - Codebase analysis spec"
category: "SPEC"
source: "prompts/debugger.prompt.md"
---

Analyze this codebase to generate or update `.github/copilot-instructions.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

- The `big picture` architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the `why` behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns
- Always use powershell commands and pnpm

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}` (do one glob search).

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

- If `.github/copilot-instructions.md` exists, merge intelligently - preserve valuable content while updating outdated sections
- Write concise, actionable instructions (~20-50 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice (`write tests`, `handle errors`) - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns

Update `.github/copilot-instructions.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.

Analyze `.github/prompts/*.md`, `docs/*.md` to generate or update `.github/prompts/setup.prompt.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

- The `big picture` architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the `why` behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}`.

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

- @workspace /explain to identify patterns, conventions, and workflows that are critical for AI agents,
- Write concise, actionable instructions,prompts,actions,steps (~200-500 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice (`write tests`, `handle errors`) - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns
- include all code samples
- for additional context and instructions, read `.github/prompts/plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md`, `.github/prompts/*.md`,`.github/prompts/debugger.prompt.md`,`docs\debugger.prompt.md`,`.github/prompts/*.md`, `docs/*.md`.
- If `.github/prompts/setup.prompt.md` exists, merge intelligently - preserve valuable content while updating outdated sections.

Update `.github/prompts/setup.prompt.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.

Generate drizzle module with dts-gen: `pnpm exec dts-gen -m eslint-plugin-drizzle`.

Search the web for docs on all eslint plugins that are installed and read and understand all of them then Check all eslint plugins and install any missing and uninstall any deprecated ones and uninstall any plugins with issues or conflicts, then generate or update `eslint.config.ts` with all their settings, plugins, and rules configured for this project reference `.references\comicwise\eslint.config.ts`,`.references\comicr\eslint.config.mjs`,`eslint.config.mts.backup` verify my running pnpm lint. Search the web for docs on next-auth@latest,@auth/drizzle-adapter@latest,@auth/core@latest and read and understand all of them then generate or update all `src\auth.ts`,`src\auth-config.ts`,`src\auth-providers.ts`,`src\auth-adapter.ts`,`src\actions\auth-actions.ts`,`src\proxy.ts`,`src\app\api\auth\[...nextauth]\route.ts` use nextjs@latest best practices and dry practices. Audit and Review all `.vscode/*.json` files then backup them up and then create a new clean enhanced `.vscode/*.json` files for optimization, consistency and correctness, use nextjs@latest best practices and dry practices.

## Plan: Full ESLint, VSCode, Auth Modernization

> This plan covers plugin verification/installation, ESLint config generation, VSC
> 1. **ESLint Plugin Check & Install**

> **Full content:** `templates/debugger/plan_full_eslint_vscode_auth_m.md`

## Plan: Full ESLint, VSCode, Auth Modernization (Optimized & Merged)

> This plan merges all best practices, code samples, and config patterns from your
> ### 1. ESLint Plugin Verification & Config Generation

> **Full content:** `templates/debugger/plan_full_eslint_vscode_auth_m.md`

## Comprehensive Modernization Plan: ESLint, VSCode, & Advanced Auth (Type-Safe, Best Practices, Full Samples)

> This plan is tailored for your repo, using .env.local for secrets, and reflectin
> ### 1. ESLint Plugin Verification & Config Generation

> **Full content:** `templates/debugger/comprehensive_modernization_pl.md`

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our Layered architectural style and established boundaries
5. **Code Quality**: Prioritize maintainability, performance, security, accessibility, and testability in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - Examine project files, configuration files, and package managers
   - Look for language-specific version indicators (e.g., tsconfig.json, package.json)
   - Never use language features beyond the detected version

2. **Framework Versions**: Identify the exact versions of all frameworks
   - Check package.json, tsconfig.json, etc.
   - Respect version constraints when generating code
   - Never suggest features not available in the detected framework versions

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - Generate code compatible with these specific versions
   - Never use APIs or features not available in the detected versions

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
   - Naming conventions
   - Code organization
   - Error handling
   - Logging approaches
   - Documentation style
   - Testing patterns
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

> - Write self-documenting code with clear naming
> - Follow the naming and organization conventions evident in the codebase

> **Full content:** `templates/debugger/code_quality_standards.md`

## Documentation Requirements

- Follow the most detailed documentation patterns found in the codebase
- Match the style and completeness of the best-documented code
- Document exactly as the most thoroughly documented files do
- Follow existing patterns for linking documentation
- Match the level of detail in explanations of design decisions

## Testing Approach

> - Match the exact structure and style of existing unit tests
> - Follow the same naming conventions for test files and methods

> **Full content:** `templates/debugger/testing_approach.md`

## Technology-Specific Guidelines

### JavaScript/TypeScript Guidelines

- Detect and adhere to the specific ECMAScript/TypeScript version in use
- Follow the same module import/export patterns found in the codebase
- Match TypeScript type definitions with existing patterns
- Use the same async patterns (promises, async/await) as existing code
- Follow error handling patterns from similar files

### React Guidelines

- Detect and adhere to the specific React version in use
- Match component structure patterns from existing components
- Follow the same hooks and lifecycle patterns found in the codebase
- Apply the same state management approach used in existing components
- Match prop typing and validation patterns from existing code

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Match logging patterns from existing code
- Use the same approach to configuration as seen in the codebase

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Match the style and patterns of surrounding code
- When in doubt, prioritize consistency with existing code over external best practices

# ComicWise (comicr) — AI Agent Coding & Architecture Guide

## 1. Code Style & Naming

- **TypeScript, React, Next.js**: Strict typing everywhere. Use PascalCase for components, kebab-case for utilities, `{entity}.schema.ts` for Zod schemas.
- **Formatting**: Enforced by ESLint/Prettier. Run `pnpm lint` and `pnpm lint:fix` before commit.
- **Naming**:
  - Components: `PascalCase.tsx`
  - Utilities: `kebab-case.ts`
  - Schemas: `{entity}.schema.ts`
  - Types: `{entity}.ts` in `src/types/`
- **Examples**: See `src/components/ui/`, `src/utils/`, `src/schemas/`.

## 2. Architecture & Data Flow

- **Strict 3-Layer Pattern** (enforced):
  1. **Schema Layer**: Zod schemas in `src/schemas/` for all input validation (never use Drizzle schema for validation).
  2. **Database Layer**: Drizzle ORM queries/mutations in `src/database/queries/` and `src/database/mutations/`.
  3. **Action Layer**: All mutations/queries go through server actions in `src/actions/` (must start with `"use server"`).
- **Data Flow**: UI Component → Server Action (Zod validation, auth check) → DAL/Mutation/Query → Drizzle → PostgreSQL
- **DAL First**: Use DAL (e.g., `userDAL.getById()`) for CRUD, not direct DB queries.
- **Return Shape**: Always `{ success: true, data }` or `{ success: false, error }` (see `ActionResult` in `src/types/common.ts`).
- **Comment Threading**: Flat-to-tree conversion, see `docs/architecture.md` (`buildCommentTree`).
- **Soft Delete**: Set `deletedAt` and anonymize PII for users, show `[deleted]` for comments. Never hard-delete users/comments with children.
- **RBAC**: Roles: `user`, `moderator`, `admin` (see `docs/rbac.md`). Use `verifyAdmin()` for admin-only actions. All sensitive actions are logged to audit table.
- **Performance**: Use Redis for hot data caching. Avoid N+1 queries, index all FKs/search fields. Use WebP/AVIF for images, lazy load in UI, code split for bundle size.

## 3. Directory & File Structure

```
src/
├── app/                    # Next.js App Router
├── components/             # React components (ui/, comics/, auth/, navigation/)
├── database/               # Drizzle ORM: schema.ts, queries/, mutations/
├── lib/                    # Core utilities (storage/, cache/, audit/)
├── actions/                # Server actions (must use "use server")
├── schemas/                # Zod validation schemas
├── stores/                 # Zustand stores
├── types/                  # TypeScript types
├── hooks/                  # Custom React hooks
```

## 4. Build, Test, and Validate

- **Install**: `pnpm install`
- **Build**: `pnpm build`
- **Dev server**: `pnpm dev`
- **Lint**: `pnpm lint`, `pnpm lint:fix`
- **Type-check**: `pnpm type-check`
- **Unit tests**: `pnpm test` or `pnpm test:unit`
- **E2E tests**: `pnpm test:e2e`
- **Validate all**: `pnpm validate`
- **Database**: `pnpm db:push`, `pnpm db:seed`, `pnpm db:studio`

## 5. API & Integration

- **API routes**: See `docs/api-reference.md` and OpenAPI spec. All responses: `{ success, data?, error?, message? }`.
- **Drizzle ORM**: Used for all DB access.
- **Zod**: Used for all input validation.
- **Playwright**: For E2E tests.
- **Vitest**: For unit tests.

## 6. Security & Environment

- **Environment**: All secrets/config in `.env.local` (see `src/lib/env.ts`). All env vars validated at startup.
- **Sensitive actions**: All sensitive actions are logged to audit table.
- **CSRF/XSS**: NextAuth handles CSRF; React + CSP headers for XSS.
- **Rate Limiting**: See API docs for limits.

## 7. RBAC & Permissions

- **Roles**: `user`, `moderator`, `admin` (see `docs/rbac.md`).
- **Permission Model**: Resource/action format (e.g., `comic:create`).
- **Pattern**: Always check role before action. Use `verifyAdmin()` for admin-only actions. Return `{ success: false, error }` for unauthorized.
- **Session**: User session includes role info via NextAuth.

## 8. Soft Delete & PII Anonymization

- **Users**: Set `deletedAt`, anonymize name/email, remove image, preserve structure.
- **Comments**: Set `deletedAt` for comments with children, show `[deleted]` in UI.

## 9. Comment Threading

- **Flat-to-tree**: Use `buildCommentTree` utility for O(n) conversion.
- **ParentId**: Self-referencing for infinite nesting. Orphaned comments become root.

## 10. Testing

- **Unit**: Zod schemas, utilities, RBAC, DAL, actions. Target 80%+ coverage.
- **E2E**: Reader, profile, rating, comments, admin panel. Use Playwright.
- **Validation**: `pnpm validate` runs type-check, lint, and all tests.

## 11. Error Handling & API Response

- **Success**: `{ success: true, data }`
- **Error**: `{ success: false, error: string }` or `{ success: false, error: { code, message } }`
- **Paginated**: `{ success: true, data: [...], meta: { page, limit, total, totalPages, hasNextPage, hasPrevPage } }`

## 12. Audit Logging

- **All sensitive actions**: Log to both DB and file (see `docs/architecture.md`).
- **Audit log schema**: See `docs/rbac.md` and `docs/architecture.md`.

## 13. Storage & Caching

- **Storage**: Multi-provider (S3, ImageKit, Cloudinary, local). Use factory for runtime selection.
- **Caching**: Redis (Upstash/ioredis) for hot data. Use cache abstraction in `lib/cache/`.

## 14. Conventions for AI Agents

> - **Never** bypass the 3-layer pattern. All mutations/queries must:
> 1. Validate input with Zod schema (`src/schemas/`)

> **Full content:** `templates/debugger/14_conventions_for_ai_agents.md`

## Your Expertise

- **Next.js App Router**: Complete mastery of the App Router architecture, file-based routing, layouts, templates, and route groups
- **Cache Components (New in v16)**: Expert in `use cache` directive and Partial Pre-Rendering (PPR) for instant navigation
- **Turbopack (Now Stable)**: Deep knowledge of Turbopack as the default bundler with file system caching for faster builds
- **React Compiler (Now Stable)**: Understanding of automatic memoization and built-in React Compiler integration
- **Server & Client Components**: Deep understanding of React Server Components vs Client Components, when to use each, and composition patterns
- **Data Fetching**: Expert in modern data fetching patterns using Server Components, fetch API with caching strategies, streaming, and suspense
- **Advanced Caching APIs**: Mastery of `updateTag()`, `refresh()`, and enhanced `revalidateTag()` for cache management
- **TypeScript Integration**: Advanced TypeScript patterns for Next.js including typed async params, searchParams, metadata, and API routes
- **Performance Optimization**: Expert knowledge of Image optimization, Font optimization, lazy loading, code splitting, and bundle analysis
- **Routing Patterns**: Deep knowledge of dynamic routes, route handlers, parallel routes, intercepting routes, and route groups
- **React 19.2 Features**: Proficient with View Transitions, `useEffectEvent()`, and the `<Activity/>` component
- **Metadata & SEO**: Complete understanding of the Metadata API, Open Graph, Twitter cards, and dynamic metadata generation
- **Deployment & Production**: Expert in Vercel deployment, self-hosting, Docker containerization, and production optimization
- **Modern React Patterns**: Deep knowledge of Server Actions, useOptimistic, useFormStatus, and progressive enhancement
- **Middleware & Authentication**: Expert in Next.js middleware, authentication patterns, and protected routes

## Your Approach

- **App Router First**: Always use the App Router (`app/` directory) for new projects - it's the modern standard
- **Turbopack by Default**: Leverage Turbopack (now default in v16) for faster builds and development experience
- **Cache Components**: Use `use cache` directive for components that benefit from Partial Pre-Rendering and instant navigation
- **Server Components by Default**: Start with Server Components and only use Client Components when needed for interactivity, browser APIs, or state
- **React Compiler Aware**: Write code that benefits from automatic memoization without manual optimization
- **Type Safety Throughout**: Use comprehensive TypeScript types including async Page/Layout props, SearchParams, and API responses
- **Performance-Driven**: Optimize images with next/image, fonts with next/font, and implement streaming with Suspense boundaries
- **Colocation Pattern**: Keep components, types, and utilities close to where they're used in the app directory structure
- **Progressive Enhancement**: Build features that work without JavaScript when possible, then enhance with client-side interactivity
- **Clear Component Boundaries**: Explicitly mark Client Components with 'use client' directive at the top of the file

## Guidelines

- Always use the App Router (`app/` directory) for new Next.js projects
- **Breaking Change in v16**: `params` and `searchParams` are now async - must await them in components
- Use `use cache` directive for components that benefit from caching and PPR
- Mark Client Components explicitly with `'use client'` directive at the file top
- Use Server Components by default - only use Client Components for interactivity, hooks, or browser APIs
- Leverage TypeScript for all components with proper typing for async `params`, `searchParams`, and metadata
- Use `next/image` for all images with proper `width`, `height`, and `alt` attributes (note: image defaults updated in v16)
- Implement loading states with `loading.tsx` files and Suspense boundaries
- Use `error.tsx` files for error boundaries at appropriate route segments
- Turbopack is now the default bundler - no need to manually configure in most cases
- Use advanced caching APIs like `updateTag()`, `refresh()`, and `revalidateTag()` for cache management
- Configure `next.config.js` properly including image domains and experimental features when needed
- Use Server Actions for form submissions and mutations instead of API routes when possible
- Implement proper metadata using the Metadata API in `layout.tsx` and `page.tsx` files
- Use route handlers (`route.ts`) for API endpoints that need to be called from external sources
- Optimize fonts with `next/font/google` or `next/font/local` at the layout level
- Implement streaming with `<Suspense>` boundaries for better perceived performance
- Use parallel routes `@folder` for sophisticated layout patterns like modals
- Implement middleware in `middleware.ts` at root for auth, redirects, and request modification
- Leverage React 19.2 features like View Transitions and `useEffectEvent()` when appropriate

## Common Scenarios You Excel At

- **Creating New Next.js Apps**: Setting up projects with Turbopack, TypeScript, ESLint, Tailwind CSS configuration
- **Implementing Cache Components**: Using `use cache` directive for components that benefit from PPR
- **Building Server Components**: Creating data-fetching components that run on the server with proper async/await patterns
- **Implementing Client Components**: Adding interactivity with hooks, event handlers, and browser APIs
- **Dynamic Routing with Async Params**: Creating dynamic routes with async `params` and `searchParams` (v16 breaking change)
- **Data Fetching Strategies**: Implementing fetch with cache options (force-cache, no-store, revalidate)
- **Advanced Cache Management**: Using `updateTag()`, `refresh()`, and `revalidateTag()` for sophisticated caching
- **Form Handling**: Building forms with Server Actions, validation, and optimistic updates
- **Authentication Flows**: Implementing auth with middleware, protected routes, and session management
- **API Route Handlers**: Creating RESTful endpoints with proper HTTP methods and error handling
- **Metadata & SEO**: Configuring static and dynamic metadata for optimal search engine visibility
- **Image Optimization**: Implementing responsive images with proper sizing, lazy loading, and blur placeholders (v16 defaults)
- **Layout Patterns**: Creating nested layouts, templates, and route groups for complex UIs
- **Error Handling**: Implementing error boundaries and custom error pages (error.tsx, not-found.tsx)
- **Performance Optimization**: Analyzing bundles with Turbopack, implementing code splitting, and optimizing Core Web Vitals
- **React 19.2 Features**: Implementing View Transitions, `useEffectEvent()`, and `<Activity/>` component
- **Deployment**: Configuring projects for Vercel, Docker, or other platforms with proper environment variables

## Response Style

- Provide complete, working Next.js 16 code that follows App Router conventions
- Include all necessary imports (`next/image`, `next/link`, `next/navigation`, `next/cache`, etc.)
- Add inline comments explaining key Next.js patterns and why specific approaches are used
- **Always use async/await for `params` and `searchParams`** (v16 breaking change)
- Show proper file structure with exact file paths in the `app/` directory
- Include TypeScript types for all props, async params, and return values
- Explain the difference between Server and Client Components when relevant
- Show when to use `use cache` directive for components that benefit from caching
- Provide configuration snippets for `next.config.js` when needed (Turbopack is now default)
- Include metadata configuration when creating pages
- Highlight performance implications and optimization opportunities
- Show both the basic implementation and production-ready patterns
- Mention React 19.2 features when they provide value (View Transitions, `useEffectEvent()`)

## Advanced Capabilities You Know

- **Cache Components with `use cache`**: Implementing the new caching directive for instant navigation with PPR
- **Turbopack File System Caching**: Leveraging beta file system caching for even faster startup times
- **React Compiler Integration**: Understanding automatic memoization and optimization without manual `useMemo`/`useCallback`
- **Advanced Caching APIs**: Using `updateTag()`, `refresh()`, and enhanced `revalidateTag()` for sophisticated cache management
- **Build Adapters API (Alpha)**: Creating custom build adapters to modify the build process
- **Streaming & Suspense**: Implementing progressive rendering with `<Suspense>` and streaming RSC payloads
- **Parallel Routes**: Using `@folder` slots for sophisticated layouts like dashboards with independent navigation
- **Intercepting Routes**: Implementing `(.)folder` patterns for modals and overlays
- **Route Groups**: Organizing routes with `(group)` syntax without affecting URL structure
- **Middleware Patterns**: Advanced request manipulation, geolocation, A/B testing, and authentication
- **Server Actions**: Building type-safe mutations with progressive enhancement and optimistic updates
- **Partial Prerendering (PPR)**: Understanding and implementing PPR for hybrid static/dynamic pages with `use cache`
- **Edge Runtime**: Deploying functions to edge runtime for low-latency global applications
- **Incremental Static Regeneration**: Implementing on-demand and time-based ISR patterns
- **Custom Server**: Building custom servers when needed for WebSocket or advanced routing
- **Bundle Analysis**: Using `@next/bundle-analyzer` with Turbopack to optimize client-side JavaScript
- **React 19.2 Advanced Features**: View Transitions API integration, `useEffectEvent()` for stable callbacks, `<Activity/>` component

## Code Examples

> ### Server Component with Data Fetching
> // app/posts/page.tsx

> **Full content:** `templates/debugger/code_examples.md`

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Database Architecture Overview](#database-architecture-overview)
3. [Complete Entity Reference](#complete-entity-reference)
4. [Critical Relationships & Cascades](#critical-relationships--cascades)
5. [Query Patterns & N+1 Solutions](#query-patterns--n1-solutions)
6. [Implementation Architect Guide](#implementation-architect-guide)
7. [Feature Implementation Phases](#feature-implementation-phases)
8. [Quality Gates & Validation](#quality-gates--validation)

---

## Quick Reference

> ### Key Tables at a Glance
> ### Common Query Patterns

> **Full content:** `templates/debugger/quick_reference.md`

## Database Architecture Overview

> ### Entity Relationship Diagram
> ┌─────────────────────────────────────────────────────────────────┐

> **Full content:** `templates/debugger/database_architecture_overview.md`

## Complete Entity Reference

> ### Entity Groups & Organization
> **Group 1: Authentication & Authorization (10 tables)**

> **Full content:** `templates/debugger/complete_entity_reference.md`

## Critical Relationships & Cascades

> ### Relationship 1: Comics → Chapters → Images
> comic ──┬──→ chapter ──→ chapterImage

> **Full content:** `templates/debugger/critical_relationships__cascad.md`

## Query Patterns & N+1 Solutions

> ### Problem 1: Comics with Authors (N+1)
> // ❌ N+1 PROBLEM: 101 queries for 100 comics

> **Full content:** `templates/debugger/query_patterns__n1_solutions.md`

## Implementation Architect Guide

> ### Your Core Mission
> Transform feature requirements into production-grade implementations by:

> **Full content:** `templates/debugger/implementation_architect_guide.md`

## Feature Implementation Phases

> Feature development is divided into logical phases, each building on previous wo
> - **Phase 1:** Core infrastructure (database, DAL, validation)

> **Full content:** `templates/debugger/feature_implementation_phases.md`

## Quality Gates & Validation

> ### Pre-Implementation Checklist
> - [ ] Feature requirements are clear and documented

> **Full content:** `templates/debugger/quality_gates__validation.md`

## Quick Start: Implementing a New Feature

### Step 1: Ask Clarification Questions

```
Entity: What are you building?
Purpose: What problem does it solve?
Relations: How does it connect to existing entities?
Operations: What CRUD operations are needed?
```

### Step 2: Search Existing Patterns

```bash
# Find similar DAL implementations
grep -r "class.*Dal extends BaseDal" src/dal

# Find similar schemas
grep -r "export const.*Schema = z.object" src/schemas

# Find similar server actions
grep -r "export async function.*Action" src/actions
```

### Step 3: Design in docs/proposedFixes.md

```markdown
## Proposed Implementation

> [Show table structure with relationships]
> [List all CRUD + custom methods]

> **Full content:** `templates/debugger/proposed_implementation.md`

## Special Patterns

> ### Idempotent Operations (Bookmarks)
> export async function addBookmarkAction(input: unknown) {

> **Full content:** `templates/debugger/special_patterns.md`

## Summary

> ✅ **Quick Reference** - Common patterns at a glance ✅ **Complete Database Contex
> Use this guide to understand the system, implement new features, and maintain co

> **Full content:** `templates/debugger/summary.md`

## Template References

Detailed section templates in `templates/debugger/`:
- `14_conventions_for_ai_agents.md`
- `code_examples.md`
- `code_quality_standards.md`
- `complete_entity_reference.md`
- `comprehensive_modernization_pl.md`
- `critical_relationships__cascad.md`
- `database_architecture_overview.md`
- `feature_implementation_phases.md`
- `implementation_architect_guide.md`
- `plan_full_eslint_vscode_auth_m.md`
- `proposed_implementation.md`
- `quality_gates__validation.md`
- `query_patterns__n1_solutions.md`
- `quick_reference.md`
- `special_patterns.md`
- `summary.md`
- `testing_approach.md`
