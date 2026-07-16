# RESEARCH_REPORT.md

## Project: Bash

**Type:** Automation toolkit (Bun/TypeScript CLI + PowerShell + Bash orchestration)
**Tech Stack:** TypeScript (strict), Node >=18, Bun >=1.3.14, PowerShell 5.1+, Bash, Vite
**Status:** Active
**Updated:** 2026-07-16

---

## Similar Projects

| Project | Why Relevant |
|---------|--------------|
| tsx (4.x) | Zero-config TS execution via esbuild — Bun makes tsx redundant |
| ts-node | Legacy Node.js TS execution — Bun's native TS support is faster |
| tsup | Bundle TS with esbuild — partially replaced by `bun build` |
| Bun CLI Applications guide (oneuptime) | Production CLI patterns: parseArgs, subcommands, single-binary |
| awesome-bun | Curated Bun ecosystem resources and tooling comparisons |

## Key Findings

**Bun acquired by Anthropic (Dec 3, 2025):** Bun remains open source + MIT-licensed; >7M monthly downloads, 82K+ GitHub stars. It powers Claude Code's native installer. This de-risks Bun as a long-term runtime choice for the toolkit.

**Bun v1.3.x stable (2026):** all-in-one runtime + package manager + bundler + test runner. Beats Node 22 on startup (8ms vs ~35ms), HTTP throughput (115K vs 48K req/s), and I/O (310ms vs 850ms for 10K files).

**Phase-Based Orchestration:** 6-phase pipeline (Discovery → Clone → Triage → Debug → Remediation → Cross-Reference) with 15+ wrappers across 3 languages (.sh, .ps1, .bat) and centralized TypeScript in `src/`.

## Cheatsheets & Quick Reference

| Topic | URL |
|-------|-----|
| Bun TypeScript config | https://bun.com/docs/typescript |
| Bun + Vite integration | https://bun.com/docs/guides/ecosystem/vite |
| Bun CLI Applications | https://oneuptime.com/blog/post/2026-01-31-bun-cli-applications/view |
| ESLint flat config | https://eslint.org/docs/latest/use/configure/configuration-files |
| Vitest | https://vitest.dev/guide/ |

```bash
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh
powershell -File orchestrator-unified.ps1 -Mode discover
```

## Best Practices
1. **Bun-native tooling** — `bun run` over `bunx tsx` for project TS files (faster, fewer deps)
2. **Multi-wrapper parity** — every script ships as `.sh` + `.ps1` + `.bat`
3. **Dry-run first** — all destructive commands support `--dry-run` for safe preview
4. **TypeScript strict** — full strict with `noUncheckedIndexedAccess`, `noImplicitOverride`
5. **Separate type-checking** — Bun strips types on-the-fly; run `tsc --noEmit` separately
6. **Lockfile integrity** — commit `bun.lock`; verify in CI
7. **TS 6/7 support** — keep `"types": ["bun"]` in `compilerOptions` (required on TS 6+)

## Common Pitfalls

| Pitfall | Avoidance |
|---------|-----------|
| Missing `"types": ["bun"]` in tsconfig | Add to `compilerOptions` |
| Using `bunx tsx` for own scripts | Use `bun run src/foo.ts` directly |
| `node:fs` missing `cp` | Use `fs-extra` or manual impl |
| Concurrent `fs.readFile` on Bun | Limit concurrent file ops (risk of segfault) |
| Workspace `resolutions` unsupported | Manual dedup with `npm ls` |

## Performance

| Metric | Bun 1.3 | Node.js 22 |
|--------|---------|------------|
| HTTP throughput | 115,000 req/s | 48,000 req/s |
| File I/O (10K files) | 310ms | 850ms |
| Cold startup | 8ms | 35ms |
| Package install (Next.js) | 4s | 28s (npm) |

- `Bun.file()`/`Bun.write()` — 2–3× faster than node:fs
- `Bun.sqlite` — outperforms better-sqlite3; `bun build --compile` — standalone binaries

## Security

Bun (like Node.js) has **no built-in permissions system** — Deno 2 is the only runtime with sandboxing. Mitigations used by the project:

1. **Lockfile verification** in CI — prevents supply chain tampering
2. **Minimal trustedDependencies** — only `protobufjs`, `esbuild`, `sharp`
4. **`dotenv-safe`** for env validation — no hardcoded secrets
5. **`eslint-plugin-security`** + CodeQL-ready for code scanning

## Related Projects (in workspace)
- **comicwise** — Bun/TS subproject sharing wrapper patterns and quality gates
- **Banking** — PowerShell + Bash scripts sharing orchestration infrastructure
- **ecom** — uses install.sh pattern derived from Bash toolkit
- **root SandBox** — shared CI in `.github/workflows/bash-scripts-ci.yml`

## Resources

| Resource | URL |
|----------|-----|
| Bun TypeScript Docs | https://bun.com/docs/typescript |
| Bun + Vite Guide | https://bun.com/docs/guides/ecosystem/vite |
| Node.js API compat tracker | https://bun.com/docs/runtime/nodejs-apis |
| Anthropic × Bun announcement | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone |
| SPECS.md | `projects/Bash/SPECS.md` |
| ORCHESTRATOR-IMPLEMENTATION.md | `projects/Bash/ORCHESTRATOR-IMPLEMENTATION.md` |

### Methodology
- 5 web searches (Bun vs Node 2026, Anthropic acquires Bun, Bun CLI apps, TS support) + 2 web_extract verifications (anthropic.com, bun.com/docs/typescript).
- **Last verified:** 2026-07-16.
