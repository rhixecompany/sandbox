---
name: technology-stack-blueprint-generator-generated
description: Generated prompt section for technology-stack-blueprint-generator workflow
version: 2.0.0
tags: [template, generated, technology-stack]
---

# Technology Stack Blueprint Generator — Generated Instructions

## Execution Checklist

### Phase 1: Project Discovery

- [ ] Scan `projects/` for all directories containing build manifests
- [ ] Build inventory: project name, path, manifest type(s)
- [ ] Output: JSON array of discovered projects

### Phase 2: Per-Project Analysis

For each project:

- [ ] Read all manifest files (package.json, requirements.txt, pyproject.toml, Cargo.toml, go.mod, pom.xml, build.gradle.kts, composer.json, Package.swift, *.csproj, Gemfile)
- [ ] Parse dependencies with versions
- [ ] Detect frameworks from dependency names
- [ ] Read tooling configs (.editorconfig, eslint.config.mjs, .ruff.toml, pyrightconfig.json, .prettierrc, etc.)
- [ ] Read CI/CD workflows (.github/workflows/*.yml)
- [ ] Read .env.example if present
- [ ] Detect architecture (check for backend/, frontend/, apps/, packages/ subdirectories)

### Phase 3: Per-Project Generation

For each project:

- [ ] Write `projects/<project-name>/TECHNOLOGY_STACK.md`
- [ ] Verify file exists and has >50 lines
- [ ] Validate Markdown syntax

### Phase 4: Master Blueprint Generation

- [ ] Write `Technology_Stack_Blueprint.md` at workspace root
- [ ] Include cross-project technology matrix
- [ ] Include shared tooling summary
- [ ] Include dependency alignment analysis
- [ ] Include consolidation recommendations

## Required Sections Per TECHNOLOGY_STACK.md

```markdown
# 🏗 Technology Stack Blueprint - <Project Name>

**Project Path:** `projects/<project-name>`
**Generated:** <ISO date>
**Status:** <Active|Maintenance|Archive|Consolidation Target>

---

## Technology Stack Overview

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Language | <e.g., TypeScript> | <e.g., 5.9> | Primary language |
| Runtime | <e.g., Bun> | <e.g., 1.3.14> | Execution runtime |
| Framework | <e.g., Next.js> | <e.g., 16.2.4> | Application framework |
| Package Manager | <e.g., bun> | <e.g., 1.3.14> | Dependency manager |
| Database | <e.g., PostgreSQL> | <e.g., 16> | Primary database |
| ORM | <e.g., Drizzle> | <e.g., 0.44> | Data access layer |
| Auth | <e.g., NextAuth> | <e.g., v5 beta> | Authentication |
| Styling | <e.g., Tailwind> | <e.g., v4> | CSS framework |

---

## Dependencies

### Production Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| <name> | <version> | <description> |

### Development Dependencies
| Package | Version | Purpose |
|---------|---------|---------|

---

## Coding Conventions

| Convention | Setting | Source |
|------------|---------|--------|
| Indent | 2 spaces | .editorconfig |
| Quotes | Single | eslint.config.mjs |
| Line Length | 120 | .ruff.toml / .prettierrc |
| Type Checking | Strict | tsconfig.json / pyrightconfig.json |

---

## Commands

| Task | Command |
|------|---------|
| Install | `bun install` / `pip install -r requirements.txt` |
| Dev | `bun run dev` / `python manage.py runserver` |
| Build | `bun run build` / `cargo build --release` |
| Test | `bun test` / `pytest` |
| Lint | `bun run lint` / `ruff check` |
| Format | `bun run format` / `ruff format` |
| Type Check | `tsc --noEmit` / `pyright` |

---

## Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| DATABASE_URL | Yes | PostgreSQL connection string | - |
| NEXT_PUBLIC_... | No | Client-side config | - |

---

## Architecture Notes

- Pattern: <Monolith / Dual-Stack / Microservices / Library>
- Notable: <Any special characteristics>

---

## Related Projects

- <Cross-references to related projects in workspace>
```

## Required Sections for Master Blueprint

```markdown
# 🏗 Technology Stack Blueprint — <Workspace Name>

**Workspace:** `<absolute path>`
**Generated:** <ISO date>

---

## 1. Technology Inventory (Cross-Project)

| Language | Version(s) | Projects | Count |
|----------|-----------|----------|-------|
| TypeScript | 5.x, 6.0 | Banking, comicwise, ... | N |
| Python | 3.11, 3.12 | rhixecompany-comics, ecom, ... | N |

## 2. Runtime & Package Manager Matrix

| Runtime | Version | Package Manager | Projects |
|---------|---------|-----------------|----------|
| Bun | 1.3.14 | bun | Banking, Bash, Resume_maker |
| Node.js | 18+ | npm/pnpm | xamehi, selenium_webdriver |

## 3. Framework Adoption

| Framework | Version | Projects |
|-----------|---------|----------|
| Next.js | 16.2.4 | Banking |
| Next.js | 15.x | comicwise, rhixe_scans, university-libary-jsm |
| Django | 5.x | rhixecompany-comics, cookiecutter... |
| Django | 3.1 | ecom (legacy) |

## 4. Shared Tooling Configurations

| Tool | Config File | Scope |
|------|-------------|-------|
| TypeScript | tsconfig.json (root) | Workspace defaults |
| ESLint | eslint.config.mjs (root) | Workspace rules |
| Prettier | .prettierrc (root) | Workspace formatting |
| Ruff | .ruff.toml (root) | Python lint/format |
| Pyright | pyrightconfig.json (root) | Python type checking |

## 5. Dependency Alignment Analysis

- **Aligned**: Projects using same major versions
- **Diverged**: Projects on different major versions (list)
- **Recommendations**: Upgrade paths

## 6. Architectural Patterns

| Pattern | Projects | Notes |
|---------|----------|-------|
| Next.js App Router | Banking, comicwise, rhixe_scans, university-libary-jsm | React 19 Server Components |
| Dual-Stack (Django + Next.js) | rhixecompany-comics | Backend + Frontend separation |
| Legacy Dual-Stack | xamehi, xamehi.tv, ecom | Consolidation targets |
| MCP Server (STDIO) | mcp-servers/* (10 langs) | Reference implementations |
| MCP Server (HTTP) | mcp-servers/copilot-studio | Power Platform integration |

## 7. Consolidation Targets

| Project | Reason | Target |
|---------|--------|--------|
| Django-Scrapy-Selenium | Scraping moved to rhixecompany-comics | Archive |
| ecom | Django 3.1 EOL, Python 3.10 EOL Oct 2026 | Upgrade to Django 5.x |
| xamehi | 3-service legacy architecture | Consolidate |
| xamehi.tv | React 17, Material-UI v5 | Modernize |
| Python-projects (partial) | 18 beginner scripts | Archive subset |

---

*Generated by Hermes Agent — Technology Stack Blueprint Generator*
```

## Quality Gates

- [ ] Every project with a manifest has TECHNOLOGY_STACK.md
- [ ] All version numbers trace to source files (no invented versions)
- [ ] No secrets/credentials in output
- [ ] Valid Markdown syntax
- [ ] Master blueprint references all per-project files
- [ ] Consolidation targets match actual project status
