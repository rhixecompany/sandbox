# xamehi.tv/frontend Architecture

**Generated:** 2026-07-28  
**Project Type:** React/Bun (Frontend)  
**Architecture Pattern:** React frontend for video platform

## Overview

React frontend for the xamehi.tv video streaming platform.

## Technology Stack

React, Bun

## Source Layout

src/

## Architecture Diagram

```mermaid
graph TD
    subgraph "xamehi.tv/frontend"
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

- **React frontend for video platform**
- Version control: Shared xamehi.tv git

## Cross-Cutting Concerns

- **Linting/Formatting:** Aligned with workspace root configs (ESLint, Prettier, Ruff)
- **Documentation:** AGENTS.md + standard doc files per project convention
- **Dependencies:** Managed via project-specific package manager

## Related Documents

- [Folder Structure](./xamehi.tv-frontend_folders.md)
- [Technology Stack](./xamehi.tv-frontend_techstack.md)
