# rhixecompany-comics/backend Architecture

**Generated:** 2026-07-28  
**Project Type:** Python/Django (Backend)  
**Architecture Pattern:** Django + Docker backend for comics platform

## Overview

Django REST API backend with Docker deployment for the rhixecompany-comics platform.

## Technology Stack

Django, Python, Docker Compose, PostgreSQL

## Source Layout

Standard Django app structure, Docker Compose

## Architecture Diagram

```mermaid
graph TD
    subgraph "rhixecompany-comics/backend"
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

- **Django + Docker backend for comics platform**
- Version control: Shared rhixecompany-comics git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./rhixecompany-comics-backend_folders.md)
- [Technology Stack](./rhixecompany-comics-backend_techstack.md)
