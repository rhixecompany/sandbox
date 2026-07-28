# xamehi.tv Architecture

**Generated:** 2026-07-28  
**Project Type:** Python/Django (Backend)  
**Architecture Pattern:** Django + Video streaming backend

## Overview

Video platform backend with Django admin, video management, and player integration.

## Technology Stack

Django, Python, Gunicorn, SQLite

## Source Layout

player/, video/, templates/

## Architecture Diagram

```mermaid
graph TD
    subgraph "xamehi.tv"
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

- **Django + Video streaming backend**
- Version control: Shared monorepo git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./xamehi.tv_folders.md)
- [Technology Stack](./xamehi.tv_techstack.md)
