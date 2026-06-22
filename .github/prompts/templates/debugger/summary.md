# Summary

> Extracted from `debugger.prompt.md`.

## Summary

This guide provides:

✅ **Quick Reference** - Common patterns at a glance ✅ **Complete Database Context** - All 25+ tables explained ✅ **Architecture Patterns** - DAL, validation, actions, components ✅ **Implementation Workflow** - 10-step process for new features ✅ **Feature Phases** - Organized roadmap for development ✅ **Quality Gates** - Checklists and validation commands

Use this guide to understand the system, implement new features, and maintain code quality.

---

**Version:** 1.0.0 | **Updated:** March 1, 2026 | **Framework:** Next.js 16 | **ORM:** Drizzle | **Database:** PostgreSQL` go ahead and implement all phase and tasks start by creating all missing files

read and understand all `docs/*.md`,`docs/*.json`,`.github/prompts/*.prompt.md`, the project files, `.references/comicwise/**/**/*.ts`,`.references/comicwise/**/**/*.tsx`,`.references/comicwise/**/**/*.mts`,`.references/comicwise/**/**/*.mjs`,`.references/comicr/**/**/*.ts`,`.references/comicr/**/**/*.tsx`,`.references/comicr/**/**/*.mts`,`.references/comicr/**/**/*.mjs` then intelligent merge all files using next best practices, dry practices, markdown format, into `docs/dev.content.md` include all code samples then create or update `.github/prompts/setup-enhanced.prompt.md` as a complete enhanced github copilot prompt which uses `docs/dev.content.md` for context and ensure to avoid `Sorry, you have been rate-limited. Please wait a moment before trying again. Learn More Server Error: Sorry, you have exceeded your Copilot token usage. Please review our Terms of Service. Error Code: rate_limited` issues by create or update and running a script to automate any tasks and sub tasks then output `.github/prompts/setup-enhanced.prompt.md` and output an enhanced prompt for running `.github/prompts/setup-enhanced.prompt.md` in copilot cli with personas and completing all steps, phase, task, sub task by creating a todos for steps, phase, tasks and sub tasks then implement all steps, phase, tasks and sub tasks in batch and ensure not to stop until all steps, phase, tasks and sub tasks are completed

As Debugger persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, review the seeding system for improvements and modify the seeding system to read and validate @src\data\comic.json then filter all type,author,artist,genre and pass them to the type,author,artist,genre seeder execute pnpm seed:validate && pnpm seed:all --image-strategy=local --batch-size=500 fix all issues .

As Debugger persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, execute pnpm validate and batch fix all warnings, errors and issues

/plan /create-prompt /create-implementation-plan "As Reviewer persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, Read and understand all `.references/comicwise/scripts/**/*.ps1`,`.references/comicwise/scripts/**/*.sh`,`.references/comicwise/scripts/**/*.ts`,`.references/comicwise/scripts/**/*.js`,`.references/comicr/scripts/**/*.ps1`,`.references/comicr/scripts/**/*.sh`,`.references/comicr/scripts/**/*.ts`,`.references/comicr/scripts/**/*.js`,`src/scripts/**/*.ts` files.

Take this steps before implementing:

- Start by search for improvements that can be made to all `src/scripts/**/*.ts` files
- Then Remove Redundancy from `.references/comicwise/scripts/**/*.ps1`,`.references/comicwise/scripts/**/*.sh`,`.references/comicwise/scripts/**/*.ts`,`.references/comicwise/scripts/**/*.js`,`.references/comicr/scripts/**/*.ps1`,`.references/comicr/scripts/**/*.sh`,`.references/comicr/scripts/**/*.ts`,`.references/comicr/scripts/**/*.js` and output a list of files to a markdown file then read the markdown and triage then output all files to be created or updated with all code samples into a mardown file at `docs/refactor-context.md`. ensure to enfore all typesript files live in `src/scripts` and all powershell and bash scripts live in the root directory ensure all files have dry-run enables, comprehensive and consise logging and enforce dry practices and next.js best practices.
- intelligently group and categorize all files in `docs/refactor-context.md` with valid code samples.
- generate or update all files in `docs/refactor-context.md` with valid code samples.
- modify package.json to include all typescript files in `src/scripts`,bash and powershell scripts in the root directory"

/plan /create-prompt /create-implementation-plan "As Reviewer persona, Review `src/scripts/seed/**/*.ts` files. Create a User seeder to handle all user operations. Create a Comic Image seeder to handle all comic image operations. Create a Chapter Image seeder to handle all chapter image operations. Identify warnings,errors,issues and batch fix them. Think Of any improvements that can be made and implement all of them"

/plan /create-prompt /create-implementation-plan "create a bash and powershell scripts in the root directory that runs pnpm type-check 2>&1 | Tee-Object -FilePath type-check.txt && pnpm lint:fix 2>&1 | Tee-Object -FilePath lint-fixed.txt && pnpm test --run 2>&1 | Tee-Object -FilePath test-report.txt pnpm build:debug 2>&1 | Tee-Object -FilePath build-report.txt comprehensive and consise logging"

/plan /create-prompt /create-implementation-plan "that uses the Debugger Persona Reviews type-check.txt, lint-fixed.txt, test-report.txt, build-report.txt files and triaged all warnings,errors and issues, then implement batch-fixes"

/plan /create-prompt /create-implementation-plan "Audit and Review all `.vscode/*.json` files then "Fetch docs on `.vscode/*.json` files and read them if found then generate or update all `.vscode/*.json` files for this project enforce consistency, correctness, use next best practices and dry practices." /plan /create-prompt /create-implementation-plan "Read docs/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/app/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/components/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/scripts/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "List all Phase Tasks And Micro-Tasks then Create a detailed Plan for all Phase Tasks And Micro-Tasks with built-in checkpoints and recovery points and code samples with diff and file references"
