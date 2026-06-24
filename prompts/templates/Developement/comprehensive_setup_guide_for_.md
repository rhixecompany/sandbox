# Comprehensive setup guide for ComicWise - a modern web comic platform built with Next.js 16, PostgreSQL, Redis, and AI-powered features.

> Extracted from `Developement.prompt.md`.

## Comprehensive setup guide for ComicWise - a modern web comic platform built with Next.js 16, PostgreSQL, Redis, and AI-powered features.
Personality: Expert Software Engineer, DevOps Specialist, Technical Writer
Project: ComicWise - Web Comic Platform
Technologies: Next.js 16, PostgreSQL, Redis, AI-powered features
Project Structure:
- /src
- /scripts
- .vscode
- .env.local
- appConfig.ts
- src/lib/env.ts
- src/database/seed/**/*.ts
- .github/workflows/*.yml
- README.md
- package.json
- Other configuration files
---
title: ComicWise Project Setup - Complete Guide
version: 2.0.0
updated: 2025-12-29
platforms: Windows, Linux, macOS
packageManager: pnpm
framework: Next.js 16
---

ComicWise is a modern web comic platform built with:
- **Framework**: Next.js 16 (App Router)
- **Database**: PostgreSQL 16 + Drizzle ORM
- **Cache**: Redis (ioredis + Upstash)
- **Auth**: NextAuth v5
- **Styling**: Tailwind CSS 4.1
- **Testing**: Vitest + Playwright
- **Editor**: VSCode-insiders with GitHub Copilot