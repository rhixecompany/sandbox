#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Master Project Setup & Optimization Script (Interactive Orchestrator)
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * This script orchestrates all unified scripts for complete project management:
 *
 * Unified Scripts (executed via this orchestrator):
 * - Health Checks: Database, Redis, Environment, MCP servers
 * - Database Operations: Truncate, Setup, Autofix, Report, Verify
 * - Performance Optimization: Analysis, SEO, Performance
 * - Code Refactoring: Types, Imports, DAL verification
 * - Development Setup: Dependencies, Environment, Extensions, Cleanup
 *
 * Documentation (standalone):
 * - Documentation generation
 * - README creation
 * - GitHub prompts generation
 * - GitHub workflows setup
 *
 * Usage:
 *   pnpm master                 # Interactive menu
 *   pnpm master --task=health  # Run health checks
 *   pnpm master --task=db      # Run database operations
 *   pnpm master --task=optimize # Run performance optimization
 *   pnpm master --task=refactor # Run code refactoring
 *   pnpm master --task=setup   # Run development setup
 *   pnpm master --task=all     # Run all tasks
 */

import { execSync } from "node:child_process";
import fs from "node:fs/promises";
import path from "node:path";

import chalk from "chalk";
import inquirer from "inquirer";
import ora from "ora";

// ═══════════════════════════════════════════════════════════════════════════
// CONFIGURATION
// ═══════════════════════════════════════════════════════════════════════════

const ROOT_DIR = process.cwd();
const DOCS_DIR = path.join(ROOT_DIR, "docs");
const GITHUB_DIR = path.join(ROOT_DIR, ".github");
const PROMPTS_DIR = path.join(GITHUB_DIR, "prompts");

const taskArg = process.argv.find((arg) => arg.startsWith("--task="));
const specificTask = taskArg?.split("=")[1];

interface SetupTask {
  description: string;
  execute(): Promise<void>;
  name: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// TASK FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

async function generateDocumentation(): Promise<void> {
  const spinner = ora("Generating comprehensive documentation...").start();

  try {
    // Ensure docs directory exists
    await fs.mkdir(DOCS_DIR, { recursive: true });

    // Generate API documentation
    const apiDocs = `# ComicWise API Documentation

## Overview

ComicWise provides a comprehensive RESTful API and Server Actions for managing comics, chapters, users, and more.

## Base URL

\`\`\`
Development: http://localhost:3000
Production: https://your-domain.com
\`\`\`

## Authentication

All authenticated endpoints require a valid session token.

\`\`\`typescript
// Using NextAuth session
import { auth } from "@/lib/auth";

const session = await auth();
\`\`\`

## Endpoints

### Comics

#### GET /api/comics
Get all comics with pagination.

**Query Parameters:**
- \`page\`: Page number (default: 1)
- \`limit\`: Items per page (default: 20)
- \`search\`: Search query
- \`genre\`: Filter by genre
- \`status\`: Filter by status

#### GET /api/comics/[slug]
Get a single comic by slug.

#### POST /api/comics
Create a new comic (Admin only).

### Chapters

#### GET /api/comics/[slug]/chapters
Get all chapters for a comic.

#### GET /api/comics/[slug]/chapters/[number]
Get a specific chapter.

### Users

#### GET /api/users/me
Get current user profile.

#### PATCH /api/users/me
Update current user profile.

## Server Actions

ComicWise uses Next.js Server Actions for mutations.

\`\`\`typescript
import { createComic } from "@/lib/actions/comics";

const result = await createComic(formData);
\`\`\`

## Rate Limiting

API endpoints are rate-limited to prevent abuse:
- Anonymous: 10 requests/minute
- Authenticated: 100 requests/minute
- Admin: Unlimited

## Error Handling

All API responses follow a consistent error format:

\`\`\`json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "details": {}
}
\`\`\`

## Code Examples

### Fetching Comics

\`\`\`typescript
const response = await fetch("/api/comics?page=1&limit=20");
const { comics, totalPages } = await response.json();
\`\`\`

### Creating a Comic (Server Action)

\`\`\`typescript
"use server";

import { createComic } from "@/lib/actions/comics";

export async function handleCreateComic(formData: FormData) {
  const result = await createComic(formData);
  return result;
}
\`\`\`

---

*Last updated: ${new Date().toISOString()}*
`;

    await fs.writeFile(path.join(DOCS_DIR, "API.md"), apiDocs);

    // Generate setup guide
    const setupGuide = `# ComicWise Setup Guide

## Prerequisites

- Node.js 20+ 
- pnpm 9+
- PostgreSQL 16+
- Redis 7+ (optional but recommended)

## Quick Start

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd comicwise
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pnpm install
   \`\`\`

3. **Setup environment variables**
   \`\`\`bash
   cp .env.example .env.local
   # Edit .env.local with your values
   \`\`\`

4. **Setup database**
   \`\`\`bash
   pnpm db:push
   pnpm db:seed
   \`\`\`

5. **Run development server**
   \`\`\`bash
   pnpm dev
   \`\`\`

## Environment Variables

See \`.env.example\` for all available environment variables.

### Required Variables

- \`DATABASE_URL\`: PostgreSQL connection string
- \`AUTH_SECRET\`: Secret for NextAuth (generate with \`openssl rand -base64 32\`)

### Optional Variables

- \`REDIS_URL\`: Redis connection string
- \`IMAGEKIT_*\`: ImageKit CDN credentials
- \`CLOUDINARY_*\`: Cloudinary credentials

## Development

### Available Scripts

- \`pnpm dev\`: Start development server
- \`pnpm build\`: Build for production
- \`pnpm start\`: Start production server
- \`pnpm lint\`: Run ESLint
- \`pnpm type-check\`: Run TypeScript compiler
- \`pnpm test\`: Run tests

### Database Commands

- \`pnpm db:push\`: Push schema changes to database
- \`pnpm db:seed\`: Seed database with sample data
- \`pnpm db:studio\`: Open Drizzle Studio
- \`pnpm db:reset\`: Reset and reseed database

## Production Deployment

### Vercel (Recommended)

1. Push to GitHub
2. Import repository in Vercel
3. Configure environment variables
4. Deploy

### Docker

1. Build image: \`docker compose build\`
2. Run containers: \`docker compose up -d\`

## Troubleshooting

### Common Issues

**Database connection failed**
- Ensure PostgreSQL is running
- Check DATABASE_URL is correct

**Module not found**
- Run \`pnpm install\`
- Clear cache: \`pnpm clean && pnpm install\`

**TypeScript errors**
- Run \`pnpm type-check\` to see all errors
- Update \`tsconfig.json\` if needed

---

*Last updated: ${new Date().toISOString()}*
`;

    await fs.writeFile(path.join(DOCS_DIR, "SETUP.md"), setupGuide);

    spinner.succeed(chalk.green("✓ Documentation generated"));
  } catch (error) {
    spinner.fail(chalk.red(`✗ Documentation generation failed: ${error}`));
  }
}

async function generateREADME(): Promise<void> {
  const spinner = ora("Generating comprehensive README...").start();

  try {
    const readme = `# 🎨 ComicWise

> A modern, high-performance web comic platform built with Next.js 16, PostgreSQL, and Redis.

[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)](https://www.typescriptlang.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

## ✨ Features

- 📚 **Comic Management**: Complete CRUD operations for comics and chapters
- 🔐 **Authentication**: NextAuth v5 with multiple providers (Google, GitHub)
- 🎨 **Modern UI**: Tailwind CSS 4.1 with dark mode support
- ⚡ **Performance**: Optimized with Redis caching and ISR
- 🔍 **Search**: Full-text search with PostgreSQL
- 📱 **Responsive**: Mobile-first design
- 🛠️ **Developer Experience**: TypeScript, ESLint, Prettier
- 🐳 **Docker**: Ready for containerized deployment
- 📊 **Analytics**: Sentry error tracking and monitoring

## 🚀 Quick Start

### Prerequisites

- Node.js 20+
- pnpm 9+
- PostgreSQL 16+
- Redis 7+ (optional)

### Installation

\`\`\`bash
# Clone repository
git clone <repository-url>
cd comicwise

# Install dependencies
pnpm install

# Setup environment
cp .env.example .env.local
# Edit .env.local with your credentials

# Setup database
pnpm db:push
pnpm db:seed

# Start development server
pnpm dev
\`\`\`

Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📖 Documentation

- [Setup Guide](./docs/SETUP.md)
- [API Documentation](./docs/API.md)
- [Contributing Guide](./docs/CONTRIBUTING.md)

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4.1
- **UI Components**: Radix UI
- **State Management**: Zustand, Jotai
- **Forms**: React Hook Form + Zod

### Backend
- **Database**: PostgreSQL 16
- **ORM**: Drizzle ORM
- **Cache**: Redis (ioredis + Upstash)
- **Authentication**: NextAuth v5
- **Validation**: Zod

### DevOps
- **Package Manager**: pnpm
- **Linting**: ESLint 9
- **Formatting**: Prettier 3
- **Testing**: Vitest + Playwright
- **CI/CD**: GitHub Actions
- **Deployment**: Vercel / Docker

## 📦 Project Structure

\`\`\`
comicwise/
├── src/
│   ├── app/              # Next.js app directory
│   ├── components/       # React components
│   ├── lib/              # Utility functions
│   ├── database/         # Database schema & queries
│   ├── services/         # Business logic
│   └── types/            # TypeScript types
├── public/               # Static assets
├── scripts/              # Utility scripts
├── docs/                 # Documentation
└── tests/                # Test files
\`\`\`

## 🧪 Testing

\`\`\`bash
# Run unit tests
pnpm test:unit

# Run e2e tests  
pnpm test

# Run with coverage
pnpm test:unit:coverage
\`\`\`

## 🐳 Docker

\`\`\`bash
# Development
docker compose up -d

# Production
docker compose -f docker-compose.yml up -d
\`\`\`

## 📝 Available Scripts

| Command | Description |
|---------|-------------|
| \`pnpm dev\` | Start development server |
| \`pnpm build\` | Build for production |
| \`pnpm start\` | Start production server |
| \`pnpm lint\` | Run ESLint |
| \`pnpm format\` | Format code with Prettier |
| \`pnpm type-check\` | Check TypeScript types |
| \`pnpm test\` | Run all tests |
| \`pnpm db:push\` | Push database schema |
| \`pnpm db:seed\` | Seed database |
| \`pnpm db:studio\` | Open Drizzle Studio |

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](./docs/CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Drizzle ORM](https://orm.drizzle.team/)
- [Radix UI](https://www.radix-ui.com/)

---

**Made with ❤️ by the ComicWise Team**

*Last updated: ${new Date().toISOString()}*
`;

    await fs.writeFile(path.join(ROOT_DIR, "README.md"), readme);

    spinner.succeed(chalk.green("✓ README generated"));
  } catch (error) {
    spinner.fail(chalk.red(`✗ README generation failed: ${error}`));
  }
}

async function generateGitHubPrompts(): Promise<void> {
  const spinner = ora("Generating GitHub Copilot prompts...").start();

  try {
    // Ensure prompts directory exists
    await fs.mkdir(PROMPTS_DIR, { recursive: true });

    const setupPrompt = `---
title: ComicWise Complete Setup
description: Complete setup guide for ComicWise project
tags: [setup, nextjs, postgresql, redis]
---

# ComicWise - Complete Project Setup

## Project Overview

ComicWise is a modern web comic platform built with:
- **Framework**: Next.js 16 (App Router)
- **Database**: PostgreSQL 16 + Drizzle ORM
- **Cache**: Redis (ioredis + Upstash)
- **Auth**: NextAuth v5
- **Styling**: Tailwind CSS 4.1
- **Testing**: Vitest + Playwright

## Prerequisites

1. Node.js 20+
2. pnpm 9+
3. PostgreSQL 16+
4. Redis 7+ (optional)

## Quick Setup

\`\`\`bash
# Install dependencies
pnpm install

# Setup environment
cp .env.example .env.local

# Setup database
pnpm db:push
pnpm db:seed

# Run development server
pnpm dev
\`\`\`

## Environment Variables

Required variables in \`.env.local\`:

\`\`\`env
DATABASE_URL="postgresql://user:password@localhost:5432/comicwise"
AUTH_SECRET="<generate-with-openssl-rand-base64-32>"
NEXT_PUBLIC_APP_URL="http://localhost:3000"
\`\`\`

## Project Structure

- \`src/app\` - Next.js app router pages
- \`src/components\` - Reusable React components
- \`src/database\` - Database schema and queries
- \`src/lib\` - Utility functions and helpers
- \`src/services\` - Business logic layer

## Development Workflow

1. Create feature branch
2. Make changes
3. Run tests: \`pnpm test\`
4. Run linter: \`pnpm lint\`
5. Commit and push
6. Create pull request

## Common Commands

\`\`\`bash
pnpm dev              # Start dev server
pnpm build            # Build for production
pnpm lint             # Run ESLint
pnpm type-check       # Check TypeScript
pnpm test:unit        # Run unit tests
pnpm test             # Run e2e tests
pnpm db:studio        # Open Drizzle Studio
\`\`\`

## Deployment

### Vercel
1. Push to GitHub
2. Import in Vercel
3. Set environment variables
4. Deploy

### Docker
\`\`\`bash
docker compose up -d
\`\`\`

## Resources

- [Next.js Docs](https://nextjs.org/docs)
- [Drizzle ORM](https://orm.drizzle.team)
- [Tailwind CSS](https://tailwindcss.com)

---

*Generated: ${new Date().toISOString()}*
`;

    await fs.writeFile(path.join(PROMPTS_DIR, "Setup.prompt.md"), setupPrompt);

    spinner.succeed(chalk.green("✓ GitHub prompts generated"));
  } catch (error) {
    spinner.fail(chalk.red(`✗ Prompt generation failed: ${error}`));
  }
}

async function setupGitHubWorkflows(): Promise<void> {
  const spinner = ora("Setting up GitHub Actions workflows...").start();

  try {
    const workflowsDir = path.join(GITHUB_DIR, "workflows");
    await fs.mkdir(workflowsDir, { recursive: true });

    const ciWorkflow = `name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint

  type-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm type-check

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm test:unit:run

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v2
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
`;

    await fs.writeFile(path.join(workflowsDir, "ci.yml"), ciWorkflow);

    spinner.succeed(chalk.green("✓ GitHub workflows created"));
  } catch (error) {
    spinner.fail(chalk.red(`✗ Workflow creation failed: ${error}`));
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// UNIFIED SCRIPT ORCHESTRATION
// ═══════════════════════════════════════════════════════════════════════════

function runUnifiedScript(scriptPath: string, args: string[] = []): void {
  const cmd = `tsx ${scriptPath} ${args.join(" ")}`;
  execSync(cmd, { stdio: "inherit" });
}

async function runHealthChecks(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running Health Checks...\n"));
  runUnifiedScript("src/scripts/unified-project-health.ts", ["--all"]);
}

async function runDbOperations(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running Database Operations...\n"));
  const { dbTask } = await inquirer.prompt([
    {
      type: "list",
      name: "dbTask",
      message: "Select database operation:",
      choices: [
        { name: "Truncate seeded tables", value: "truncate" },
        { name: "Setup Drizzle migrations", value: "setup" },
        { name: "Report missing fields", value: "report" },
        { name: "Verify seed storage", value: "verify" },
        { name: "All operations", value: "all" },
      ],
    },
  ]);
  runUnifiedScript("src/scripts/unified-db-operations.ts", [`--${dbTask}`]);
}

async function runOptimizations(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running Performance Optimizations...\n"));
  const { optimizeTask } = await inquirer.prompt([
    {
      type: "list",
      name: "optimizeTask",
      message: "Select optimization task:",
      choices: [
        { name: "Analyze project metrics", value: "analysis" },
        { name: "SEO optimization", value: "seo" },
        { name: "Performance optimization", value: "performance" },
        { name: "All optimizations", value: "all" },
      ],
    },
  ]);
  runUnifiedScript("src/scripts/unified-performance-ops.ts", [`--${optimizeTask}`]);
}

async function runRefactoring(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running Code Refactoring...\n"));
  const { refactorTask } = await inquirer.prompt([
    {
      type: "list",
      name: "refactorTask",
      message: "Select refactoring task:",
      choices: [
        { name: "Fix 'any' type annotations", value: "types" },
        { name: "Replace relative imports", value: "imports" },
        { name: "Verify DAL compliance", value: "dal-verify" },
        { name: "All refactoring", value: "all" },
      ],
    },
  ]);
  runUnifiedScript("src/scripts/unified-schema-refactor.ts", [`--${refactorTask}`]);
}

async function runDevSetup(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running Development Setup...\n"));
  const { setupTask } = await inquirer.prompt([
    {
      type: "list",
      name: "setupTask",
      message: "Select setup task:",
      choices: [
        { name: "Install dependencies", value: "deps" },
        { name: "Setup environment", value: "env" },
        { name: "Install VS Code extensions", value: "extensions" },
        { name: "Validate environment", value: "validate-env" },
        { name: "Project cleanup", value: "cleanup" },
        { name: "All setup tasks", value: "all" },
      ],
    },
  ]);
  runUnifiedScript("src/scripts/unified-dev-setup.ts", [`--${setupTask}`]);
}

async function runAllTasks(): Promise<void> {
  console.log(chalk.cyan("\n▶ Running ALL tasks...\n"));

  const spinner = ora("Running all setup tasks...").start();

  try {
    await runHealthChecks();
    await runDbOperations();
    await runOptimizations();
    await runRefactoring();
    await runDevSetup();
    await generateDocumentation();
    await generateREADME();
    await generateGitHubPrompts();
    await setupGitHubWorkflows();

    spinner.succeed(chalk.green("✓ All tasks completed"));
  } catch (error) {
    spinner.fail(chalk.red(`✗ Error running tasks: ${error}`));
  }
}

async function showInteractiveMenu(): Promise<string[]> {
  const { tasks } = await inquirer.prompt([
    {
      type: "checkbox",
      name: "tasks",
      message: "Select tasks to run (space to select, enter to confirm):",
      choices: [
        { name: "Health Checks (DB, Redis, Env)", value: "health", checked: true },
        { name: "Database Operations", value: "db" },
        { name: "Performance Optimization", value: "optimize" },
        { name: "Code Refactoring", value: "refactor" },
        { name: "Development Setup", value: "setup" },
        { name: "Generate Documentation", value: "docs" },
        { name: "Generate README", value: "readme" },
        { name: "Generate GitHub Prompts", value: "prompts" },
        { name: "Setup GitHub Workflows", value: "workflows" },
        { name: "Run ALL tasks", value: "all" },
      ],
    },
  ]);

  return tasks as string[];
}

// ═══════════════════════════════════════════════════════════════════════════
// TASK REGISTRY
// ═══════════════════════════════════════════════════════════════════════════

const tasks: SetupTask[] = [
  {
    name: "health",
    description: "Run health checks (DB, Redis, Env, MCP)",
    execute: runHealthChecks,
  },
  {
    name: "db",
    description: "Run database operations",
    execute: runDbOperations,
  },
  {
    name: "optimize",
    description: "Run performance optimizations",
    execute: runOptimizations,
  },
  {
    name: "refactor",
    description: "Run code refactoring",
    execute: runRefactoring,
  },
  {
    name: "setup",
    description: "Run development setup",
    execute: runDevSetup,
  },
  {
    name: "all",
    description: "Run all tasks",
    execute: runAllTasks,
  },
  {
    name: "docs",
    description: "Generate comprehensive documentation",
    execute: generateDocumentation,
  },
  {
    name: "readme",
    description: "Generate comprehensive README.md",
    execute: generateREADME,
  },
  {
    name: "prompts",
    description: "Generate GitHub Copilot prompts",
    execute: generateGitHubPrompts,
  },
  {
    name: "workflows",
    description: "Setup GitHub Actions workflows",
    execute: setupGitHubWorkflows,
  },
];

// ═══════════════════════════════════════════════════════════════════════════
// MAIN EXECUTION
// ═══════════════════════════════════════════════════════════════════════════

async function main() {
  console.log(chalk.bold.cyan("\n═══════════════════════════════════════════════════════"));
  console.log(chalk.bold.cyan("   ComicWise Master Setup"));
  console.log(chalk.bold.cyan("═══════════════════════════════════════════════════════\n"));

  let tasksToRun: SetupTask[] = [];

  if (specificTask) {
    const task = tasks.find((t) => t.name === specificTask);
    if (task) {
      tasksToRun = [task];
      console.log(chalk.white(`Running specific task: ${task.description}\n`));
    } else {
      console.log(chalk.red(`✗ Task '${specificTask}' not found\n`));
      console.log(chalk.white("Available tasks:"));
      for (const t of tasks) console.log(`  - ${t.name}: ${t.description}`);
      process.exit(1);
    }
  } else {
    const selected = await showInteractiveMenu();

    if (selected.includes("all")) {
      tasksToRun = tasks;
    } else {
      tasksToRun = tasks.filter((t) => selected.includes(t.name));
    }
  }

  for (const task of tasksToRun) {
    console.log(chalk.cyan(`\n▶ Running: ${task.description}`));
    await task.execute();
  }

  console.log(chalk.bold.cyan("\n═══════════════════════════════════════════════════════"));
  console.log(chalk.bold.cyan("   Setup Complete"));
  console.log(chalk.bold.cyan("═══════════════════════════════════════════════════════\n"));

  console.log(chalk.green("✓ All tasks completed successfully\n"));
}

main().catch((error) => {
  console.error(chalk.red(`\n✗ Setup failed: ${error}\n`));
  process.exit(1);
});
