# comicwise Architecture

**Generated:** 2026-07-28  
**Project Type:** TypeScript/Bun (Next.js)  
**Architecture Pattern:** Next.js App Router with Server Actions + Admin Panel

## Overview

Comic reading platform with user-generated content, admin panel, ratings, bookmarks, and notifications.

## Technology Stack

Next.js, React, Bun, TypeScript, Tailwind CSS, shadcn/ui, Drizzle ORM, Playwright

## Source Layout

src/app/, src/components/, src/actions/, src/lib/

## Architecture Diagram

```mermaid
graph TD
    subgraph "comicwise"
        MAIN[Main Entry Point]
        SRC[Source Code]
        BUILD[Build System]
    end
    subgraph "Dependencies"
        DEPS[Package Dependencies]
        EXT[External Services]
    end
    MAIN --> SRC
    SRC --> BUILD
    BUILD --> DEPS
    SRC --> EXT
```

## Key Patterns

- **Next.js App Router with Server Actions + Admin Panel**
- Version control: Shared monorepo git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./comicwise_folders.md)
- [Technology Stack](./comicwise_techstack.md)
