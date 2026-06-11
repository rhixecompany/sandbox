---
description: 🚀 ComicWise - Complete Project Setup & Scaffolding Guide
agent: Next.js Expert
model: GPT-5 mini (copilot)
tools: [vscode, execute, read, agent, edit, search, web, 'github/*', 'github/*', 'io.github.upstash/context7/*', 'io.github.vercel/next-devtools-mcp/*', 'neondatabase/mcp-server-neon/*', vscode.mermaid-chat-features/renderMermaidDiagram, cweijan.vscode-postgresql-client2/dbclient-getDatabases, cweijan.vscode-postgresql-client2/dbclient-getTables, cweijan.vscode-postgresql-client2/dbclient-executeQuery, github.vscode-pull-request-github/issue_fetch, github.vscode-pull-request-github/suggest-fix, github.vscode-pull-request-github/searchSyntax, github.vscode-pull-request-github/doSearch, github.vscode-pull-request-github/renderIssues, github.vscode-pull-request-github/activePullRequest, github.vscode-pull-request-github/openPullRequest, ms-azuretools.vscode-azureresourcegroups/azureActivityLog, ms-azuretools.vscode-containers/containerToolsConfig, ms-windows-ai-studio.windows-ai-studio/aitk_get_ai_model_guidance, ms-windows-ai-studio.windows-ai-studio/aitk_get_agent_model_code_sample, ms-windows-ai-studio.windows-ai-studio/aitk_get_tracing_code_gen_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_get_evaluation_code_gen_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_convert_declarative_agent_to_code, ms-windows-ai-studio.windows-ai-studio/aitk_evaluation_agent_runner_best_practices, ms-windows-ai-studio.windows-ai-studio/aitk_evaluation_planner, ms-windows-ai-studio.windows-ai-studio/aitk_get_custom_evaluator_guidance, ms-windows-ai-studio.windows-ai-studio/check_panel_open, ms-windows-ai-studio.windows-ai-studio/get_table_schema, ms-windows-ai-studio.windows-ai-studio/data_analysis_best_practice, ms-windows-ai-studio.windows-ai-studio/read_rows, ms-windows-ai-studio.windows-ai-studio/read_cell, ms-windows-ai-studio.windows-ai-studio/export_panel_data, ms-windows-ai-studio.windows-ai-studio/get_trend_data, ms-windows-ai-studio.windows-ai-studio/aitk_list_foundry_models, ms-windows-ai-studio.windows-ai-studio/aitk_agent_as_server, ms-windows-ai-studio.windows-ai-studio/aitk_add_agent_debug, ms-windows-ai-studio.windows-ai-studio/aitk_gen_windows_ml_web_demo, prisma.prisma/prisma-migrate-status, prisma.prisma/prisma-migrate-dev, prisma.prisma/prisma-migrate-reset, prisma.prisma/prisma-studio, prisma.prisma/prisma-platform-login, prisma.prisma/prisma-postgres-create-database, todo]
---

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
## Prerequisites

1. Node.js 20+
2. pnpm 9+
3. PostgreSQL 16+
4. Redis 7+ (optional)

## **Comprehensive setup guide for ComicWise - a modern web comic platform built with Next.js 16, PostgreSQL, Redis, and AI-powered features.**

Read And understand the following files before proceeding with the tasks and also to get context on how the project is structured and works:
- `**/*.ts` ,
- `**/*.tsx`,
- `**/*.mjs`,
- `**/*.json`,
- `**/*.mts`,
- `**/*.json`,
- `**/*.md`,
- `**/*.txt`,
-  `**/*.yml`,
-   `**/*.ps1`,
- `**/*.sh`,
- `**/*/Dockerfile`,
- `src/**`,
- `scripts/**`
Complete all Tasks
## Tasks:
1 - Setup the project by installing all dependencies using pnpm, setting up the database, and configuring any necessary environment variables at `.env.local`, importing it at `src/lib/env.ts` use `src/lib/env.ts` to Optimize `appConfig.ts` (ensure all environment variables are properly set and configured for development and production environments update all usage of this file across the project).
2 - Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of `src/database/seed/**/*.ts`  to be faster (ensure all data from `users.json`, `comics.json`, `comicsdata1.json`, `comicsdata2.json`, `chapters.json`, `chaptersdata1.json`, `chaptersdata2.json` are validated using zod schemas and  then inserted into the database an onConflictDoUpdate of the inserted data with all its  chapters images, comics images, genres, inserted into the database an onConflictDoUpdate of the inserted data make sure no image is being downloaded twice by only downloading the image file if the file does not exists in the file system, using  `src/services/imageService.ts`,   save the comic images at `/comics/${comic.slug}` set `/placeholder-comic.jpg` as the default fallback image, if a user image isnt available, save the comic images at `/comics/${comic.slug}/chapters/${chapter.chapterId}` ,set `/shadcn.jpg` as the default fallback image  if a user image isnt available, use nextjs@latest best practices and dry practices, ensure it has a comprehensive logging with clear, concise descriptions,  and update all usage of this files across the project).
3 - Run pnpm  db:seed and get a list of all errors and warnings then batch fix all its errors and warnings.
4 - Create, Optimize and Validate all comprehensive configurations listed below if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of the following files use nextjs@latest best practices and dry practices. Ensure all configurations are optimized for performance, security, and scalability, and update all usage of these files across the project:

- `.vscode/mcp.json`
- `.vscode/extensions.json`
- `.vscode/launch.json` (include all scripts in package.json)
- `.vscode/tasks.json` (include all scripts in package.json)
- `.vscode/settings.json`(include all recommended settings for nextjs development, typescript, eslint, prettier, tailwindcss, and any other relevant extensions, ensure it is optimized for performance and best practices, include all recommended settings for nextjs development, typescript, eslint, prettier, tailwindcss, and any other relevant extensions, ensure it is optimized for performance and best practices, and update all usage of this file across the project, include all recommended settings for .prettierrc.ts, eslint.config.ts, tsconfig.json).

5 - Create, Optimize and Validate a custom typescript at `drizzle.config.ts` to Setup and Configure Drizzle ORM with PostgreSQL including connection settings, migrations, and schema definitions ensure the configuration is optimized for performance and scalability.
6 - Create, Optimize and Validate a comprehensive @.github/workflows/*.yml files for ci, automating the testing, building, and deployment of the project.
7 - Create, Optimize and Validate a script to Analyze the project for performance bottlenecks, security vulnerabilities, and code quality issues generate a report with findings and suggestions for improvements.
8 - Create, Optimize and Validate a script to Generate comprehensive documentation for the project including setup instructions, usage guidelines, and API references ensure the documentation is clear, concise, and easy to navigate.
9 - Create, Optimize and Validate all testing for the project including unit tests, integration tests, and end-to-end tests ensure tests are well-structured and provide adequate coverage for critical components.
10 - Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of  `scripts/projectCleanup2026.ts` to Perform a cleanup of the project,Delete all  duplicate or unused zod schemas in src,scripts, Delete all  duplicate or unused components,functions, types, interfaces and classes in src,scripts, Delete unused,duplicate,empty folders, blank files in src,scripts, Delete all backup files, Uninstall all dependency not being used by src,scripts from package.json with pnpm, verify and Run if no issues found `scripts/projectCleanup2026.ts`.
12 - Create, Optimize and Validate a comprehensive README.md for the project that includes setup instructions, usage guidelines, contribution instructions, and any other relevant information.
13 - Create, Optimize and Validate a CONTRIBUTING.md file that outlines the contribution guidelines for the project including code style, testing requirements, and the pull request process.
14 - Create, Optimize and Validate a CODE_OF_CONDUCT.md file that establishes the code of conduct for contributors to the project, including expectations for behavior and consequences for violations.
15 - Create, Optimize and Validate a SECURITY.md file that outlines the security practices for the project including how to report vulnerabilities and the process for handling security issues.
16 - Create, Optimize and Validate a LICENSE file that specifies the licensing terms for the project.
17 - Create, Optimize and Validate a .editorconfig file that defines the coding styles and formatting rules for the project to ensure consistency across different editors and IDEs.
18 - Create, Optimize and Validate a .gitignore file that specifies which files and directories should be ignored by Git to prevent unnecessary files from being committed.
19 - Create, Optimize and Validate a .prettierignore file that specifies which files and directories should be ignored by Prettier to prevent unnecessary formatting.
20 - Create, Optimize and Validate a .prettierrc.ts file that defines the Prettier configuration for the project to ensure consistent code formatting across the codebase.
21 - Performance Optimization Implement caching and query optimization
22 - Testing Suite Achieve 80%+ code coverage with unit and E2E tests
23 - CI/CD Pipeline Automate testing and deployment
24 - Docker & Deployment -ready containerization
25 - Documentation Complete project documentation
27 - Enhanced Admin Features Analytics, filtering, file manager, multi-step forms
28 - User Profile Customization Avatars, bios, social links
29 - Social Features Comments, ratings, favorites, reading lists
30 - Mobile Responsiveness & PWA Ensure mobile-friendly design and PWA capabilities
31 - Accessibility Compliance WCAG 2.1 AA standards
32 - Security Enhancements OWASP Top 10 protections
33 - Analytics & Monitoring Integrate tools like Google Analytics and Sentry
34 - Internationalization (i18n) Multi-language support
35 - AI-Powered Features Integrate AI for recommendations, tagging, and content moderation
36 - Community & Support Features Forums, FAQs, support ticketing
37 - Regular Maintenance & Updates Keep dependencies and documentation up to date
38 - User Onboarding & Tutorials Guided tours and tutorials for new users
38 - Feedback Mechanism In-app feedback and surveys
39 - Scalability Planning Database indexing, load balancing, horizontal scaling
40 - Legal & Compliance Privacy policy, terms of service, GDPR compliance


Lastly After completing all tasks, respond with "All tasks have been completed successfully." and provide a summary of the changes made without including any code snippets. Then Output a structured report of your recommendations for this project including any potential improvements, optimizations, or future features that could be implemented to enhance the project further.
