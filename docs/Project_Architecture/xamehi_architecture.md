# xamehi Architecture

**Generated:** 2026-07-28  
**Project Type:** Full-Stack (React + Django)  
**Architecture Pattern:** React frontend + Django REST backend

## Overview

Multi-purpose full-stack application with React frontend and Django REST API backend.

## Technology Stack

React, Node.js, Django, Python, DRF

## Source Layout

src/, xamehi/

## Architecture Diagram

```mermaid
graph TD
    subgraph "xamehi"
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

- **React frontend + Django REST backend**
- Version control: Shared monorepo git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./xamehi_folders.md)
- [Technology Stack](./xamehi_techstack.md)
