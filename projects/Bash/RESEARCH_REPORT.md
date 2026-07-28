# RESEARCH_REPORT.md

## Project: Bash

**Type:** Automation toolkit (Bun/TypeScript CLI + PowerShell + Bash orchestration)
**Tech Stack:** TypeScript (strict), Node >=18, Bun >=1.3.14, PowerShell 5.1+, Bash, Vite, Vitest
**Status:** Active
**Updated:** 2026-07-28

---

## Similar Projects

| Project | Why Relevant |
|---------|--------------|
| tsx (4.x) | Zero-config TS execution — Bun makes tsx redundant |
| ts-node | Legacy Node.js TS execution — Bun's native TS is faster |
| Bun CLI Apps (oneuptime) | Production CLI patterns: parseArgs, subcommands, exit codes |
| CLI Builder (MCP Market) | Standardized Bun/TS CLI framework, subcommands, JSON output |

---

## Key Findings

**Bun rewritten from Zig to Rust (May 2026):** Jarred Sumner rewrote Bun from Zig to Rust using AI tools — >1M lines, passed test suite, merged within days.

**Bun v1.3.14 stable:** `Bun.$` cross-platform shell API replaces dax/cross-env/rimraf. 8ms cold start, 115K req/s HTTP.

**TS 7.0 "Corsa":** Go-based compiler — 5-10× faster compiles, ~50% less memory. Breaking: `--strict` on by default, ES5/AMD/UMD dropped.

**CLI Best Practices (2026):** Lazy-load heavy modules, handle SIGINT/SIGTERM, proper exit codes 0/1, compile to single binary via `bun build --compile`.

**Phase-Based Orchestration:** 6-phase pipeline (Discovery → Clone → Triage → Debug → Remediation → Cross-Reference) with 15+ wrappers across .sh + .ps1 + .bat.

---

## Cheatsheets & Quick Reference

| Topic | Resource |
|-------|----------|
| Bun TypeScript | https://bun.com/docs/typescript |
| Bun CLI Guide | https://oneuptime.com/blog/post/2026-01-31-bun-cli-applications/view |
| ESLint flat config | https://eslint.org/docs/latest/use/configure/configuration-files |
| Vitest | https://vitest.dev/guide/ |

```bash
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh
```

---

## Best Practices

1. **Bun-native** — `bun run` over `bunx tsx` for project TS files (faster, fewer deps)
2. **Multi-wrapper parity** — every script ships as `.sh` + `.ps1` + `.bat`
3. **Dry-run first** — all destructive commands support `--dry-run` for safe preview
4. **TypeScript strict** — `noUncheckedIndexedAccess`, `noImplicitOverride` on
5. **Separate type-checking** — Bun strips types on-the-fly; run `tsc --noEmit` separately
6. **Lockfile integrity** — commit `bun.lock`; verify in CI
7. **Signal handling** — trap SIGINT/SIGTERM for graceful cleanup in CLI tools

---

## Common Pitfalls

| Pitfall | Avoidance |
|---------|-----------|
| Missing `"types": ["bun"]` in tsconfig | Add to `compilerOptions` |
| Using `bunx tsx` for own scripts | Use `bun run src/foo.ts` directly |
| Missing `--help`/`--version` flag | Always include per CLI best practices |
| Concurrent `fs.readFile` on Bun | Limit concurrent file ops (risk of segfault) |

---

## Performance

| Metric | Bun 1.3 | Node.js 22 |
|--------|---------|------------|
| HTTP throughput | 115,000 req/s | 48,000 req/s |
| File I/O (10K files) | 310ms | 850ms |
| Cold startup | 8ms | 35ms |
| Package install (Next.js) | 4s | 28s (npm) |

- `Bun.file()`/`Bun.write()` — 2-3× faster than node:fs
- `Bun.$` shell — cross-platform, replaces dax/cross-env/rimraf

---

## Security

Bun has **no built-in permissions system**. June 2026 alert: npm worm targeting Bun via `binding.gyp` credential stealers (Miasma/Hades variant). Mitigations:

1. **Lockfile verification** in CI — prevents supply chain tampering
2. **Minimal trustedDependencies** — only protobufjs, esbuild, sharp
3. **`dotenv-safe`** for env validation — no hardcoded secrets
4. **`bun audit`** + CodeQL for vulnerability scanning

---

## Related Projects (in workspace)

- **Banking** — Bun + TS strict + Drizzle ORM + Next.js
- **comicwise** — TS strict + Next.js; shares CI quality gates
- **ecom** — install.sh pattern derived from Bash toolkit
- **mcp-servers** — TypeScript implementations share ESLint config
- **Resume_maker** — Shared Bun/TypeScript CLI architecture

---

## Resources

| Resource | URL |
|----------|-----|
| Bun TypeScript Docs | https://bun.com/docs/typescript |
| Node.js API compat tracker | https://bun.com/docs/runtime/nodejs-apis |
| Bun Wikipedia | https://en.wikipedia.org/wiki/Bun_(software) |
| SPECS.md | `projects/Bash/SPECS.md` |

### Methodology
3 Tavily advanced searches (`time_range=year`) + 3 prior searches (2026-07-16). Verified bun.com, oneuptime.com, tech-insider.org.

**Last verified:** 2026-07-28.