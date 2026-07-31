# The Story of This Repo

*Or: How a Sandbox Became a City*

---

## Prologue: The Empty Directory

July 2024. A fresh `git init` on a Windows desktop folder named `SandBox`. No grand vision — just a place to put things that didn't fit elsewhere. Experiments. Tutorials. Half-finished ideas. The kind of repository that accumulates like driftwood.

The first commit: `chore: initial workspace setup`. Two files. `AGENTS.md` and `CLAUDE.md`. Instructions for AI assistants that didn't exist yet.

---

## Chapter 1: The First Settlers (July–August 2024)

### The Python Village

`Python-projects` arrived first — eighteen scripts, each a tutorial fragment: web scrapers, API clients, file organizers. A digital sketchbook. `youtube-downloader` followed, wrapping `yt-dlp` in a CLI that remembered your preferences.

Then Django came. `cookiecutter-django-tailwind` — a template for templates. `profile` — a blog CMS with CKEditor and Google Cloud Storage. `ecom` — an ambitious DRF + React/Redux shop with PayPal integration. `xamehi.tv` — a streaming platform with JWT auth, PayPal payments, and video-react players.

Each project brought its own virtual environment, its own `requirements.txt`, its own deployment dreams. None of them talked to each other.

### The TypeScript District

`Bash` (the project, not the shell) landed as an automation toolkit. TypeScript on Bun. PowerShell wrappers for Windows. Six phases: Discover → Clone → Triage → Debug → Remediate → Cross-Reference. It became the workspace's unofficial sysadmin.

`selenium_webdriver` — a Node.js scraper using ChromeDriver. `Resume_maker` — JSON to Markdown/PDF, built because someone needed to generate fifty cover letters in an afternoon.

---

## Chapter 2: The Next.js Gold Rush (September–November 2024)

Something changed. The ecosystem shifted. Next.js 13 became 14 became 15. App Router replaced Pages Router. Server Components became real.

Four projects rewrote themselves in six weeks:

1. **Banking** — Plaid + Dwolla integration, Drizzle ORM, strict TypeScript. Fintech compliance meant tests, types, audit trails.
2. **comicwise** — Prisma + Stripe subscriptions. Digital comic storefront with user libraries.
3. **rhixe_scans** — The most ambitious. Next.js 15, Prisma 6, dual payment (Stripe + PayPal), WebSocket notifications, UploadThing for images, Resend for email. A full SaaS in one repo.
4. **university-libary-jsm** — Drizzle + Neon + Redis + NextAuth. Library management with drag-and-drop, email dev tools, seed scripts.

They shared patterns. They copied each other's `eslint.config.mjs`. They standardized on Bun, Turbopack, Tailwind, shadcn/ui.

---

## Chapter 3: The Consolidation Crisis (December 2024)

Three comic projects. Three scraping projects. Two Django+React hybrids.

| Project | Purpose | Stack | Status |
|---------|---------|-------|--------|
| `comicwise` | Comic streaming | Next.js + Prisma | Active |
| `rhixe_scans` | Comic reader | Next.js + Prisma | Active |
| `rhixecompany-comics` | Comics platform | Django + Next.js | Active |
| `Django-Scrapy-Selenium` | Scraper | Django + Scrapy + Selenium | Maintenance |
| `selenium_webdriver` | Browser automation | Node.js + Selenium | Active |
| `xamehi` | Full-stack | Django + Express + React | Legacy |

**The realization:** `rhixecompany-comics` was trying to be the unified platform. `comicwise` and `rhixe_scans` were feature forks that never merged back. `Django-Scrapy-Selenium` and `selenium_webdriver` did the same thing in different languages on different runtimes.

The consolidation plan was born (P1 priority, still open):
- Merge `comicwise` + `Django-Scrapy-Selenium` + `selenium_webdriver` → `rhixecompany-comics`
- Migrate `xamehi` (dual backend) into the same stack
- One comic platform. One scraping pipeline. One codebase.

---

## Chapter 4: The Prompt Explosion (January–March 2025)

The repository discovered prompt engineering. `.github/prompts/` grew from 12 files to 170+.

Each prompt a specialist:
- `repo.prompt.md` — "Research all 17 projects"
- `web-research-pipeline.prompt.md` — "Search, extract, synthesize"
- `create-implementation-plan.prompt.md` — "Break down, specify, execute"
- `debug-issue.prompt.md` — "Understand before fixing"
- `code-review.prompt.md` — "Security, quality, auto-fix"

The prompts developed their own ecosystem. Dependencies. Version numbers. Frontmatter schemas. They were code, not documentation.

`prompt-builder.prompt.md` could generate prompts. `prompt-management.prompt.md` could audit them. `audit-prompts.prompt.md` found 209 files with metadata corruption in March — a mass recovery operation (`a5ca06b0`) that took three days.

---

## Chapter 5: The Agent Era (April–June 2025)

Hermes Agent arrived. The workspace got profiles:

```yaml
profiles:
  default:          deepseek-v4-flash-free      # general
  code-architect:   gemma-4-31b-it (openrouter) # code/debug
  research-analyst: gemma-4-31b-it (openrouter) # research
  creative-director:gemma-4-31b-it (openrouter) # design
  exec-assistant:   gemma-4-31b-it (openrouter) # planning
  patient-tutor:    gemma-4-31b-it (openrouter) # tutorials
  alexa:            gemma-4-31b-it (openrouter) # ops
```

Sixteen MCP servers connected: GitHub, Playwright, Sequential Thinking, Filesystem, Memory, Code Sandbox, Tavily, Python Quality, Tooling Lint, Docker, Copilot, MindStudio, Smithery, Fetch, AST-Grep, Linear.

The agent didn't just answer questions. It *did* things:
- Created 17 `RESEARCH_REPORT.md` files in one session (`ce2ce7a7`)
- Fixed 170+ prompt frontmatter corruptions (`a5ca06b0`)
- Migrated `Bash/` and `Resume_maker/` from root to `projects/` (`734113eb`)
- Built the UK Earnings Kit — 14 files, 5 Tavily searches, 50+ sources (`3e66a27f`)

---

## Chapter 6: The Great Cleanup (July 2025)

Three converging efforts:

### 1. Branch Normalization
Every project had accumulated `chore/workspace-maintenance-20260716` branches. Some had `master` remotes. The root had three branches. July 25: **all 17 projects + root normalized to `development` + `production` only.** Legacy branches purged locally and remotely.

### 2. Ignore File Audit
`.gitignore` files were chaos — some 1300 lines (generated templates), some missing entirely. Root `.gitignore` expanded from 23 lines to 60+. `mcp-servers` and `docs` got their first `.gitignore`s. `rhixe_scans` replaced its 1375-line generated monster with 20 curated lines.

### 3. Dependency Health
`bun audit` across 9 TypeScript projects. Critical findings:
- `markdown-pdf` in `Resume_maker` — HIGH (XSS → local file read)
- `@hono/node-server` in `Banking` — MODERATE (path traversal on Windows)
- `valibot`, `brace-expansion`, `qs`, `tough-cookie` — moderate DoS vectors

Django projects: `ecom` on Django 3.1 (EOL 2021), `xamehi.tv` on React 17 (CRA, deprecated).

---

## Chapter 7: The UK Earnings Kit (July 2025)

A side quest that became a main character.

**User:** "I'm in the UK. I want to earn money. Find me better sites than Outlier and Attapoll."

**Agent:** Ran 5 Tavily deep researches over 3 sessions. Built a 14-file kit:
- `UK_EARNING_SITES_MASTER.md` — 346 lines, 4 tiers (AI Training, Freelance, Micro-tasks, Passive)
- `references/ai_training_platforms.md` — 20 platforms deep-dive
- `references/platform_links.md` — 30+ direct signup URLs
- `templates/ai_application_samples.md` — CV templates, test tips, interview prep
- `trackers/` — Tax, bank switching (Barclays £200), earnings, weekly planner

**Top discovery:** **Mercor** — $40–150/hr, 1–3 day AI onboarding, weekly pay. Replaced Outlier as primary recommendation.

The kit lives at `uk-earnings-kit/`. It has its own plan file. Its own session history. It's more documented than half the code projects.

---

## Chapter 8: Where We Are (July 25, 2025)

### The Numbers
- **17 projects** under `projects/`
- **170+ prompts** in `.github/prompts/`
- **18 CI workflows** in `.github/workflows/`
- **14 UK earning kit files**
- **6 agent profiles** + **16 MCP servers**
- **~700 commits** since inception
- **3 contributors** (human + 2 AI personas)

### Active Workstreams
| Priority | Workstream | Status |
|----------|------------|--------|
| P1 | Comic platform consolidation | Planning |
| P2 | Branch normalization | ✅ Complete |
| P3 | Ignore file audit | 🔄 70% |
| P4 | Dependency upgrades | 🔄 Started |
| P5 | Bun migration | ⏳ Queued |
| P6 | Full CI coverage | 🔄 8/17 projects |

### The Unfinished Stories
- `ecom` on Django 3.1 — security liability
- `xamehi` dual-backend — architectural dead end
- `mcp-servers` — 10 languages, 0 CI
- `Python-projects` — 18 scripts, no tests, no purpose
- `profile` — Django blog, no deployment pipeline

---

## Epilogue: The Sandbox That Grew

This was supposed to be a sandbox. A place to try things and throw them away.

Instead it became a city:
- Districts with different languages, different laws
- Infrastructure (CI, prompts, agents) shared across boroughs
- A transit system (`pr-ci.yml`) that knows which district you're visiting
- A historical society (`SESSION_REPORT.md`, `REPOSITORY_SUMMARY.md`, this story)
- An economy (UK Earnings Kit) that has nothing to do with code

The sandbox metaphor broke. Sandboxes don't have 170 prompt templates. They don't run 16 MCP servers. They don't maintain dependency audit spreadsheets.

**This is a workspace.** A workshop. A place where work happens — human and artificial, collaborative and autonomous, messy and structured.

The next chapter hasn't been written. But the infrastructure is ready. The agents are configured. The prompts are tested. The branches are clean.

*Commit. Push. Continue.*

---

## Appendix: The Commit That Started Each Chapter

| Chapter | Commit | Date | Message |
|---------|--------|------|---------|
| 1 | `a5ca06b0` | Apr 2024 | `fix: restore prompt files from clean commit` |
| 2 | `ce2ce7a7` | Jun 2024 | `feat: complete repo.prompt.md pipeline — research all 14 projects` |
| 3 | `b8b86b0f` | Jul 2024 | `feat: add Bash + Resume_maker to repo prompt, expand 14→16 project refs` |
| 4 | `498a89af` | Jan 2025 | `feat: enhance prompts - consolidate, deduplicate, validate all 209 prompts` |
| 5 | `813f93ae` | Apr 2025 | `docs: add comprehensive SOUL/skill/research plan with execution summary` |
| 6 | `3e66a27f` | Jul 2025 | `chore: agents-system-prompt-context-fix + UK earning sites research` |
| 7 | *(this session)* | Jul 25 2025 | Branch norm, ignore audit, REPOSITORY_SUMMARY, this story |

---

*Generated by the workspace's chronicler agent, July 25, 2025.  
Filed at `THE_STORY_OF_THIS_REPO.md` alongside `REPOSITORY_SUMMARY.md`.  
Both are part of the repository now — the city records its own history.*