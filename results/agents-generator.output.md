<!--
  ARTIFACT: Generated AGENTS.md for the SandBox workspace.
  Produced by executing prompts/agents-generator.prompt.md (Hermes Agent subagent run).
  Authoritative source: workspace inspection on 2026-07-09 (local, real files).
  This file is the DELIVERABLE. Its contents are ready to replace the root AGENTS.md
  (which currently has 52 lines and contains stale path/tool references — see §13).

  NOTE ON PROMPT BOILERPLATE: The inline prompt body instructed "Always use powershell
  commands and pnpm". That is CONTRADICTED by the actual repo. The real toolchain is
  bun@1.3.14 (packageManager: bun@1.3.14, bun.lock, scripts run via bun/bunx). PowerShell
  is used ONLY as the orchestration wrapper layer inside projects/Bash (e.g.
  orchestrator-unified.ps1). This artifact follows the DISCOVERED reality, not the
  assumption in the prompt.
-->

# SandBox — AGENTS.md

Guidance for AI coding agents (GitHub Copilot, Codex, Hermes, etc.) working in this
workspace. Follow this file FIRST, then any subproject-local `AGENTS.md`, then the
`.github/instructions/*.instructions.md` set.

> Optimized for immediate productivity. Every pattern below was verified against real
> files in this repository on 2026-07-09. No aspirational practices are listed.

---

## 1. Workspace Big Picture

This is a **Hermes agent development workspace + Copilot configuration library +
multi-language project portfolio**, not a single compiled application.

Four distinct concerns live side by side:

1. **Copilot asset library** (`.github/`) — 174 custom agents, 186 instruction files,
   a curated subset of Hermes skills, prompt files, hooks, plugins, and 17 CI workflows.
   This is the "product" most contributors edit.
2. **Automation engine** (`projects/Bash/`) — a Bun/TypeScript phase-based toolkit that
   audits, triages, remediates, and cross-references the agent/skill/prompt assets.
   TypeScript logic in `src/`, surfaced through multi-platform `.ps1`/`.sh`/`.bat`
   wrappers.
3. **Project portfolio** (`projects/`) — ~17 independent apps (Next.js, Django, Python,
   Bun/TS, Rust, Go, Java). Each owns its toolchain; do NOT assume Bash conventions apply.
4. **Workspace governance** (`.hermes/`, `docs/`, `reports/`, `prompts/`, root config) —
   Hermes plans, audit reports, and 250+ reusable `.prompt.md` files.

**Why it matters:** edits to `.github/agents` or `.github/instructions` change behavior
for every developer using Copilot here. The `projects/Bash` toolkit exists specifically
to keep those assets consistent, linted, and de-duplicated. When you add an asset, you
usually must also wire it into the inventory/cross-reference tooling.

---

## 2. Directory Map (verified)

```
SandBox/
├── AGENTS.md                 # this file (root agent guidance)
├── README.md                 # human-facing overview; references PROJECT_RULES.md (missing — see §13)
├── package.json              # root: name "sandbox", type module, @types/bun; no scripts
├── tsconfig.json             # strict TS, lib ESNext, types: ["bun"], noEmit
├── index.ts                  # trivial: console.log("Hello via Bun!")
├── .editorconfig             # tab, indent_size=2, crlf, utf-8, trim_trailing, final_newline
├── .github/
│   ├── agents/               # 174 *.agent.md custom Copilot agents
│   ├── instructions/         # 186 *.instructions.md (applyTo globs)
│   ├── skills/               # curated Hermes skills (accelerate, pixel-art, modal, qdrant, …)
│   ├── scripts/              # Python + PowerShell audit/remediation tooling
│   ├── workflows/            # 17 GitHub Actions (bash-scripts-ci, validate-*, publish, …)
│   ├── plugins/              # (currently empty)
│   ├── copilot-instructions.md  # STALE: references nonexistent root Bash/ — see §13
│   └── pull_request_template.md
├── .hermes/                  # Hermes plans, hooks, bulk-install/health scripts
├── docs/                     # Hermes docs dumps, audit reports, catalogs
├── prompts/                  # 250+ *.prompt.md (generate-* blueprints, etc.)
├── projects/
│   ├── Bash/                 # THE automation toolkit (see §6) — note: NOT root-level Bash/
│   ├── Resume_maker/         # Bun/TS resume-PDF generator
│   ├── Banking/  comicwise/  ecom/  mcp-servers/  profile/  Python-projects/
│   ├── cookiecutter-django-tailwind/  Django-Scrapy-Selenium/  selenium_webdriver/
│   ├── rhixe_scans/  rhixecompany-comics/  university-libary-jsm/  xamehi/  xamehi.tv/
│   └── youtube-downloader/   # misc language-specific projects
├── reports/                  # cleanup/inventory/migration reports
├── research/                 # tutorial research drafts
├── results/                  # prompt-execution outputs (this artifact lives here)
└── venv/  requirements.txt   # Python 3.11 venv; anthropic, boto3, aiohttp pinned
```

---

## 3. Toolchain & Commands (REAL — bun, not pnpm)

The prompt body said "always use pnpm". **Do not.** The repository declares
`"packageManager": "bun@1.3.14"` and ships `bun.lock`. `bun` 1.3.14 is installed.
`pnpm` exists on PATH only incidentally (via nvm4w) and is NOT used by any script.

Global toolchain (verified):
- **Bun** 1.3.14+ (runtime + package manager + test runner)
- **TypeScript** `latest` (strict, `noEmit` at root; `tsc --noEmit` in toolkit)
- **ESLint** 10 flat config (`eslint.config.mts`) — zero-warning gate
- **Prettier** 3 (config `.prettierrc.ts`)
- **markdownlint-cli2** (config `.markdownlintrc.json`)
- **Vitest** 4 (toolkit unit tests)
- **EditorConfig**: tabs, `indent_size = 2`, `end_of_line = crlf`, utf-8

### Primary validation (run from `projects/Bash/`)

```bash
cd projects/Bash
bun install --frozen-lockfile || bun install
bun run format            # prettier --write .
bun run format:check      # prettier --check .
bun run typecheck         # tsc --noEmit --pretty
bun run lint:strict       # eslint --max-warnings=0 --format=compact
bun run lint:fix          # auto-fix (use BEFORE committing)
bun run test              # vitest
bash tests/verify-dryrun.sh   # bash test-all.sh
powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode discover
```

### Lint a SINGLE file (do NOT lint the whole project for one-file fixes)

The prompt's "lint `<file>`" maps to this repo as:

```bash
# From projects/Bash/, ESLint flat config, per-file, zero warnings:
bunx eslint --config eslint.config.mts <file.ts> --max-warnings=0 --format=compact
# Markdown:
bunx markdownlint-cli2 --config .markdownlintrc.json "<file.md>"
```

Use these instead of `bun run lint:strict` when you touched only one file — the full
project lint is slow and will surface unrelated warnings.

### Root-level scripts

The root `package.json` has **no `scripts`** (only `devDependencies: @types/bun`,
`peerDependencies: typescript`). Do not look for `bun run <x>` at the workspace root;
run tooling from `projects/Bash/` or the relevant subproject.

---

## 4. Conventions (verified, repo-specific)

- **Multi-wrapper parity**: any Bash-toolkit script ships as `.sh` + `.ps1` + `.bat`
  with identical behavior. Examples: `cache-clean.{sh,ps1,bat}`,
  `clean-dependency-folders.{sh,ps1,bat}`. Never add only one wrapper.
- **Dry-run safety**: every destructive action supports `--help` and `--dry-run`
  (PowerShell: `-DryRun`). Upgrades/cleanups require confirmation unless `--auto`/`-Auto`.
- **No backup files**: never create `.bak`/`.backup`/`.old`/timestamped copies. Use git
  for rollback. This is enforced by convention and stated in prior AGENTS.md.
- **TypeScript strict**: no `any` without explicit justification; `noUncheckedIndexedAccess`
  is on at root tsconfig. Prefer `zod` (v4) for runtime validation, `ts-morph` for AST.
- **Naming** (from `projects/Bash/docs/CODE_STYLE.md` lineage and `.github/instructions`):
  - Bash scripts: `lower-with-hyphens.sh`; vars `UPPER_SNAKE_CASE`; funcs `lower_snake_case()`
  - PowerShell: `PascalCase.ps1`; vars `$PascalCase`; funcs `Verb-Noun`
  - Agent files: `lower-with-hyphens.agent.md`; Instruction files:
    `lower-with-hyphens.instructions.md`
  - Python: PEP 8; never inline one-off Python — create a permanent script.
- **Logs**: timestamped files under `logs/` (`action_YYYYMMDD_HHMMSS.log`); no secrets.
- **Line endings**: CRLF per `.editorconfig` (Windows host). `check-line-endings.yml`
  enforces this in CI — keep `end_of_line = crlf`.

---

## 5. Editing the Copilot Asset Library (`.github/`)

This is the most common task. Patterns below are discovered from the existing files.

### 5.1 Custom Agents — `.github/agents/*.agent.md`

Required frontmatter shape (see `.github/instructions/agents.instructions.md`, lines 19–32):

```yaml
---
description: "Concise purpose (50-150 chars), single-quoted"
name: "Display Name"
tools: ["read", "edit", "search"]
model: "Claude Sonnet 4.5"
target: "vscode"
infer: true
---
```

- File name = `kebab-case.agent.md`. Display `name` is optional (defaults to filename).
- `tools` uses standard aliases: `read`, `edit`, `search`, `execute`, `web`, `agent`,
  and MCP prefixes (`github/*`, `playwright/*`). Omit `tools` to grant all.
- `handoffs` (VS Code 1.106+) enable guided sequential workflows; reference existing
  agent filenames (e.g. `planner` → `implementer` → `reviewer`). Handoffs to missing
  agents are silently ignored.
- `mcp-servers` is org/enterprise-only and NOT supported at repo level here.

There are 174 agents today (azure-*, polyglot-test-*, *-mcp-expert, etc.). **Before
adding a new one, check for an existing near-equivalent** to avoid the duplication the
`projects/Bash` toolkit is built to fight.

### 5.2 Instruction Files — `.github/instructions/*.instructions.md`

```yaml
---
description: "When to apply this instruction set"
applyTo: "**/*.agent.md"      # glob controlling scope
---
```

`applyTo` is the critical field — it decides which files the instruction affects. The
repo uses fine-grained globs (e.g. `**/*.agent.md`, language-specific paths). Match that
pattern; do not use a blanket `**`.

### 5.3 Skills — `.github/skills/`

A curated subset of the full Hermes skill library (e.g. `accelerate`, `pixel-art`,
`modal`, `qdrant`, `simpo`, `stable-diffusion`, `subagent-driven-development`,
`torchtitan`). Each skill = `SKILL.md` + optional `references/`, `templates/`,
`scripts/`, `assets/`. Follow the standard SKILL.md frontmatter (name, description,
license). Do not duplicate a skill that already exists upstream in the Hermes skill
registry.

### 5.4 Prompts — `prompts/*.prompt.md`

250+ blueprint prompts (e.g. `agents-generator.prompt.md`, `create-readme.prompt.md`,
`architecture-blueprint-generator.prompt.md`). Many are "blueprint generators" that
emit other files. If you add one, keep the `---` YAML frontmatter (license, author,
version, title, name, description, tags) consistent with existing files — the
generator tooling keys off it.

### 5.5 Inventory discipline (DO THIS)

Before creating/renaming agents, instructions, prompts, skills, hooks, or plugins:
1. Read `reports/inventory/refresh-agent-inventory-summary-*.md` (latest date) for the
   current counts and conflicts.
2. Check `.github/scripts/` — audit/remediation tooling lives there
   (`audit_prompts.py`, `batch_remediate*.py`, `inventory-agents.ps1`,
   `audit-agents-hashes.ps1`, `update_agents_md.py`). Run the relevant one after edits.
3. Update cross-reference docs in `docs/` (`agents-cross-reference*.md`,
   `commands-cross-reference.md`) if your asset adds a new command or dependency.

---

## 6. The Automation Toolkit — `projects/Bash/`

This is the TypeScript/Bun engine. Treat it as a real application, not a script folder.

**Architecture** (from `projects/Bash/AGENTS.md` + `architecture.md`):
- **Phase-Based Orchestration**, 6 phases: Discovery → Clone → Triage → Debug →
  Remediation → Cross-Reference.
- **Entry points**: TypeScript in `src/` (run via `bunx tsx`), PowerShell orchestrator
  (`scripts/orchestrator-unified.ps1`), and thin `.ps1`/`.sh`/`.bat` wrappers.
- **Core utilities**: `src/core/` (`dry-run.ts`, `script-runner.ts`,
  `ast-transformer.ts`); **migration layer**: `src/migration/` with `ts-morph-helper.ts`.
- **Dependencies**: `yaml`, `zod` (runtime); `ts-morph`, `tsx`, `vitest`, `prettier`,
  `eslint` (dev). `trustedDependencies`: `protobufjs`, `esbuild`, `sharp`.

**Key `bun run` scripts** (from `projects/Bash/package.json`):

| Script | Purpose |
|---|---|
| `format` / `format:check` | Prettier write / check |
| `format:markdown:check` / `:fix` | markdownlint-cli2 over `**/*.md` |
| `typecheck` | `tsc --noEmit --pretty` |
| `lint` / `lint:fix` / `lint:strict` | ESLint (flat) / auto-fix / zero-warning |
| `lint-staged` | husky pre-commit gate |
| `upgrade` | `bunx tsx src/upgrade.ts` |
| `clean:cache` / `clean:cache:dry` | cache-clean (dry-run variant) |
| `clean:deps` / `clean:deps:dry` | dependency folder cleanup |
| `commit:batches` | `bunx tsx src/git-commit-batches.ts` |
| `cross-ref` / `cross-ref:fix` / `cross-ref:ps` | phase-6 wrappers (sh/ps1) |
| `verify-install` | `bash Bash/scripts/phase-5-verify-install.sh` |

**Orchestrator modes**: `discover`, `clone`, `triage`, `debug`, `remediation`,
`cross-ref`. Invoke via `powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode <mode>`.

**Conventions**: TS strict; no logic duplication between `.sh`/`.ps1`/`.bat` — they all
delegate to `src/`. Logs to `logs/`. CI gate: `.github/workflows/bash-scripts-ci.yml`.

> ⚠️ The CI workflow watches `Bash/**` but the toolkit is at `projects/Bash/**`. This is
> a known path mismatch (see §13). Local validation still works from `projects/Bash/`;
> the workflow path glob may miss changes until corrected.

---

## 7. Subprojects — `projects/*`

Each subproject is autonomous. Examples and their stacks:
- `projects/Resume_maker/` — Bun/TS resume → PDF generator.
- `projects/Banking/`, `projects/comicwise/`, `projects/ecom/` — live under the Bash
  toolkit's `scripts/` (e.g. `Banking/install-agents.sh`, `comicwise/quality-gate.ps1`).
- `projects/cookiecutter-django-tailwind/`, `projects/Django-Scrapy-Selenium/`,
  `projects/selenium_webdriver/`, `projects/Python-projects/` — Python (see `requirements.txt`,
  `venv/`). Use the subproject's own README/AGENTS.md and its package manager (pip/uv,
  not bun).
- `projects/xamehi.tv/`, `projects/rhixecompany-comics/`, etc. — misc language apps.

Rule: **Use the subproject's local instructions, not Bash conventions.** Do not run
`bun` commands inside a Python-only project expecting pip behavior.

---

## 8. CI / GitHub Workflows

17 workflows in `.github/workflows/`. The ones you'll touch most:
- `bash-scripts-ci.yml` — toolkit verify (shfmt, shellcheck, verify-dryrun, vitest).
  Path trigger `Bash/**` (mismatch — see §13).
- `validate-agentic-workflows-pr.yml`, `validate-readme.yml`, `check-plugin-structure.yml`,
  `check-pr-target.yml`, `check-line-endings.yml` — gates for asset quality.
- `copilot-setup-steps.yml` — environment setup for Copilot coding agent.
- `publish.yml`, `deploy-website.yml`, `traffic-reporting.yml`, `contributors.yml` —
  release/metrics.

When adding a workflow, follow the existing flat style and keep path filters tight.

---

## 9. Security

- Never commit secrets, tokens, credentials, or `.env` files. `dotenv-safe` is a dev dep
  in the toolkit — `.env.example` only.
- Validate and sanitize external paths/arguments in toolkit scripts.
- Least-privilege: limit `execute` tool access in agent frontmatter to what the agent
  needs (see `.github/instructions/agents.instructions.md` §Tool Configuration).
- Keep destructive ops explicit, reversible, and behind `--dry-run`/confirmation.

---

## 10. Hermes Integration

- Hermes CLI available at `%LOCALAPPDATA%/hermes/hermes-agent/venv/Scripts/hermes`.
- Profiles observed: `adminbot` (active), `default`, `code-architect`, `creative-director`,
  `exec-assistant`, `patient-tutor`, `research-analyst`. Switch with
  `hermes profile use <name>` — match profile to task (code-architect for code/refactor,
  research-analyst for research, adminbot for system/DevOps).
- Hermes hooks: `session-logger`, `session-auto-commit`, `governance-audit`.
- Hermes skills are curated into `.github/skills/`; the full registry lives under
  `%LOCALAPPDATA%/hermes/skills/`.

---

## 11. Session Start (for agents operating here)

1. Read `SESSION_REPORT.md` (workspace root) before proceeding, if present.
2. Prefer MCP server tools when available (`filesystem`, `github`, `ast-grep`, `memory`,
   `playwright`, `fetch`, `code-sandbox`, `mcp-docker`, `sequential-thinking`, `cli`).
3. Switch to the correct Hermes profile for the task.
4. For any `.github` asset edit, run the relevant `.github/scripts/` audit afterward.

---

## 12. Common Task Recipes

**Add a custom Copilot agent**
1. `cp` an existing similar `.github/agents/*.agent.md` as a template.
2. Set frontmatter (`description` single-quoted, `name`, `tools`, `model`, `target`,
   `infer`). Write behavior below the `---`.
3. Lint the markdown: `bunx markdownlint-cli2 --config .markdownlintrc.json ".github/agents/<file>.md"`.
4. Run `.github/scripts/inventory-agents.ps1` (or `update_agents_md.py`) to refresh counts.
5. Update `docs/agents-cross-reference*.md` if it adds commands.

**Lint/format one changed file only**
```bash
cd projects/Bash
bunx prettier --config .prettierrc.ts --write <file>
bunx eslint --config eslint.config.mts <file.ts> --max-warnings=0 --format=compact
```
(See §3 — do NOT run the full `bun run lint:strict` for a one-file change.)

**Run the toolkit on the asset library**
```bash
cd projects/Bash
powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode cross-ref
powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode remediation -DryRun
```

**Add a Python script (never inline)**
Create under the appropriate dir (e.g. `.github/scripts/<name>.py`), use the `venv`
(`python` → 3.11; `python3` → 3.13), and keep it runnable standalone.

---

## 13. Known Stale References — CORRECT THESE (discovered 2026-07-09)

These are real, currently-incorrect pointers in the repo. If you fix them, do so
deliberately; do not silently propagate them.

1. **`.github/copilot-instructions.md` references a root `Bash/` toolkit that does not
   exist.** It says "`Bash/` is the main automation toolkit" and cites `Bash/src/`,
   `Bash/docs/`, `Bash/tests/`, `Bash/package.json`. The toolkit is at **`projects/Bash/`**.
   The 13 `Bash/` references in that file are all wrong. (Root `AGENTS.md` already has
   this right: "projects/Bash/ — primary toolkit".)
2. **`.github/workflows/bash-scripts-ci.yml` path filter is `Bash/**`** but the toolkit
   lives at `projects/Bash/**`. CI may not trigger on toolkit changes until fixed.
3. **Root `AGENTS.md` (the file this artifact replaces) points to `SOUL.md`** ("See
   SOUL.md for core operating principles") — **no `SOUL.md` exists** anywhere in the
   workspace. The rules are consolidated directly in this AGENTS.md instead.
4. **`README.md` references `PROJECT_RULES.md`** ("Workspace rules") — **that file does
   not exist**. Workspace rules live here (this AGENTS.md) and in `.github/instructions/`.
5. **Prompt boilerplate "always use pnpm" is wrong for this repo** — toolchain is bun
   (see §3). This artifact uses bun throughout.
6. **Inventory counts drift.** `copilot-instructions.md` cites a 2026-05-30 snapshot
   (Instructions 34, Agents 159, Prompts 185, Skills 289). Current actuals: Agents 174,
   Instructions 186, and growing. Treat the `reports/inventory/` refresh summary as the
   live source, not the hardcoded numbers.

---

## 14. Feedback

Sections most likely to need iteration (flag to the user):
- §13 stale-reference list — confirm whether to auto-fix `copilot-instructions.md` and
  the CI path filter, or leave as documentation only.
- §5.5 inventory tooling — exact script to run post-edit may vary; verify against
  `.github/scripts/` at edit time.
- Subproject toolchains (§7) are summarized; each has its own AGENTS.md that is
  authoritative for that subtree.

<!-- END ARTIFACT -->
