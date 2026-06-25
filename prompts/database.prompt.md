---
toolsets:
  - vscode
  - execute
  - read
  - agent
  - edit
  - search
  - web
  - github/*
  - context7/*
  - modelcontextprotocol-servers-sequentialthinking/*
  - next-devtools/*
  - nextjs-docs-mcp/*
  - sentry/*
  - shadcn/*
  - github/*
  - io.github.chromedevtools/chrome-devtools-mcp/*
  - io.github.upstash/context7/*
  - playwright/*
  - vscode.mermaid-chat-features/renderMermaidDiagram
  - github.vscode-pull-request-github/issue_fetch
  - github.vscode-pull-request-github/suggest-fix
  - github.vscode-pull-request-github/searchSyntax
  - github.vscode-pull-request-github/doSearch
  - github.vscode-pull-request-github/renderIssues
  - github.vscode-pull-request-github/activePullRequest
  - github.vscode-pull-request-github/openPullRequest
  - ms-azuretools.vscode-containers/containerToolsConfig
  - prisma.prisma/prisma-migrate-status
  - prisma.prisma/prisma-migrate-dev
  - prisma.prisma/prisma-migrate-reset
  - prisma.prisma/prisma-studio
  - prisma.prisma/prisma-platform-login
  - prisma.prisma/prisma-postgres-create-database
  - todo
license: MIT
author: Hermes Agent
version: 1.0.0
title: Database Schema Guide for ComicWise
name: database
description: "Database schema knowledge base for ComicWise - use for any database-related tasks"
---


# Database Schema Guide for ComicWise

This prompt provides comprehensive database knowledge for implementing features, fixing bugs, and optimizing queries in ComicWise.

## Quick Reference

**📖 Full Context Map:** See [docs/database-context-map.md](./database-context-map.md) for:

- Complete entity relationship overview
- All 50+ tables with purposes and constraints
- Cascade delete scenarios
- N+1 query problems and solutions
- Query pattern examples
- Performance considerations
- AI-optimized schema reference

## How to Use This Prompt

1. **When implementing a feature:** Read the context map section for the tables involved
2. **When debugging a query issue:** Check "N+1 Query Problems & Solutions"
3. **When working with relationships:** Review "Critical Relationships Explained"
4. **When deleting records:** Study "Cascade Delete Scenarios"
5. **For performance optimization:** See "Performance Considerations"

## Key Tables at a Glance

| Table | Purpose | Key Relationship |
| --- | --- | --- |
| `user` | User accounts | Cascades to: account, session, bookmark, comment, rating, readingProgress |
| `comic` | Comic entries | Cascades to: chapter, comicImage, comicToGenre, bookmark, rating, readingProgress |
| `chapter` | Comic chapters | Cascades to: chapterImage, readingProgress, comment |
| `bookmark` | User's reading list | Composite key (userId, comicId) for idempotent upserts |
| `readingProgress` | Reading position tracking | Tracks: comic, chapter, page, scroll position, completion |
| `comment` | Chapter discussions | Threaded replies via parentId |
| `notification` | User alerts | Can link to comic or chapter |

## Common Patterns

> ### Get Comic with All Details
> const comic = await db.query.comic.findFirst({

> **Full content:** `templates/database/common_patterns.md`

## Critical Rules

⚠️ **Always use Drizzle `with()`** for relationships - never loop and query individually  
⚠️ **Never forget cascade deletes** - deleting a comic cascades 3+ levels deep  
⚠️ **Always check if soft-delete exists** - some tables have `deletedAt` columns  
⚠️ **Use composite keys for upserts** - (userId, comicId) enables idempotent operations  
⚠️ **Filter deleted users** - WHERE clause should exclude `deletedAt IS NOT NULL`

## When You Need More Details

For deep dives into specific topics, reference the context map:

- **Schema Details:** Section "Detailed Entity Reference"
- **Relationship Mechanics:** Section "Critical Relationships Explained"
- **Cascade Behavior:** Section "Cascade Delete Scenarios"
- **Query Performance:** Section "N+1 Query Problems & Solutions" + "Query Patterns & Examples"
- **Optimization:** Section "Performance Considerations"
- **AI Reference:** Section "AI-Optimized Schema Reference"

---

**Last Updated:** March 1, 2026 | **Database:** PostgreSQL | **ORM:** Drizzle


## Template References

Templates in `templates/database/`:
- `common_patterns.md`
