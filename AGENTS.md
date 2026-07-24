# SandBox — AGENTS.md

Guidance for AI coding agents (GitHub Copilot, Codex, Hermes, etc.) in this workspace. Follow this FIRST, then subproject-local `AGENTS.md`.

> Verified against real repo files 2026-07-09. No aspirational practices.

## 1. Workspace Big Picture

**Hermes agent development workspace + Copilot config library + multi-language project portfolio.**

1. Workspace root — `AGENTS.md` (this), `.hermes.md`
2. Copilot asset library — `.github/prompts/`
3. Subprojects — `projects/*` (autonomous per-language)

## 2. Directory Map

```
SandBox/
├── AGENTS.md / .hermes.md / README.md   # root config
├── .github/prompts/      # canonical prompt library
├── projects/Bash/        # automation toolkit or projects root
├── projects/*/           # autonomous subprojects
├── research/
└── venv/ + requirements.txt # Python 3.11
```

## 3. Toolchain & Commands

**Do NOT use pnpm.** Package manager: `bun@1.3.14+`

| Tool | Config | Notes |
| ------ | -------- | ------- |
| **Bun** 1.3.14+ | `package.json` | runtime + pkg mgr + test runner |
| **TypeScript** strict | `tsconfig.json` | `tsc --noEmit` in toolkit |
| **ESLint** 10 flat | `eslint.config.mts` | zero-warning gate |
| **Prettier** 3 | `.prettierrc.ts` | |
| **markdownlint-cli2** | `.markdownlintrc.json` | |
| **Vitest** 4 | | toolkit unit tests |
| **EditorConfig** | `.editorconfig` | tab, indent=2, crlf, utf-8 |

**Validation from `projects/Bash/`:**

```bash
bun install --frozen-lockfile
bun run format / format:check   # prettier
bun run typecheck               # tsc --noEmit
bun run lint:strict             # eslint --max-warnings=0
bun run test                    # vitest
bash tests/verify-dryrun.sh
```

**Single-file lint:**

```bash
bunx eslint --config eslint.config.mts <file.ts> --max-warnings=0
bunx markdownlint-cli2 --config .markdownlintrc.json "<file.md>"
```

## 4. Conventions

- **Dry-run**: destructive actions require `--dry-run`; upgrades/cleanups need confirmation
- **No backup files**: git for rollback; never create `.bak`/`.old`
- **TypeScript strict**: no `any`, `noUncheckedIndexedAccess` on; `zod` v4 for runtime, `ts-morph` for AST
- **Naming**: Bash=kebab-case/.sh, PowerShell=PascalCase/.ps1, Python=PEP 8
- **CRLF** per `.editorconfig` (Windows host); CI enforces
- **Logs**: `logs/action_YYYYMMDD_HHMMSS.log`, no secrets

## 5. Hermes Integration

- CLI: `%LOCALAPPDATA%/hermes/hermes-agent/venv/Scripts/hermes`
- Profiles: `default`, `alexa`, `code-architect`, `creative-director`, `exec-assistant`, `patient-tutor`, `research-analyst`
- Switch: `hermes profile use <name>`
- Hooks: `session-logger`, `session-auto-commit`, `governance-audit`
- Plugins: disk-cleanup, security-guidance, model-providers/openrouter
- Session start: read `SESSION_REPORT.md` first; prefer validated MCP paths

## 6. Common Recipes

**Run toolkit**: `powershell.exe -NoProfile -File scripts/orchestrator-unified.ps1 -Mode <mode>` from `projects/Bash/` unless a subproject says otherwise.

**Lint one file**: `bunx eslint --config eslint.config.mts <file.ts> --max-warnings=0` and/or `bunx markdownlint-cli2 <file.md>`.

## 7. Model/Doc Lane Ownership

| File | Lane |
|------|------|
| `.github/copilot-instructions.md` | Use as Copilot dispatch only; authoritative behavior lives in `AGENTS.md` |
| `CLAUDE.md` | Claude-specific reasoning/tool behavior |
| `.cursorrules` | Cursor IDE formatting/safety rules only |
| `.hermes.md` | Hermes overrides/config sourcing |
| `SOUL.md`, `MEMORY.md`, `USER.md` | Persona/memory rules; durable canonical rules are in `MEMORY.md` |
