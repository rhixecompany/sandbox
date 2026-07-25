# RESEARCH_REPORT.md

## Project: Bash

**Type:** Automation toolkit (Bun/TypeScript CLI + PowerShell + Bash orchestration)
**Tech Stack:** TypeScript (strict), Node >=18, Bun >=1.3.14, PowerShell 5.1+, Bash, Vite
**Status:** Active
**Updated:** 2026-07-24

---

## Similar Projects

| Project | Why Relevant |
|---------|--------------|
| tsx (4.x) | Zero-config TS execution — Bun makes tsx redundant |
| ts-node | Legacy Node.js TS execution — Bun's native TS is faster |
| tsup | Bundle TS with esbuild — partially replaced by `bun build` |
| Bun CLI Applications (oneuptime) | Production CLI patterns: parseArgs, subcommands |
| CLI Builder (MCP Market) | Standardized Bun/TS CLI framework, subcommands, JSON output |

---

## Key Findings

**Bun rewritten from Zig to Rust (May 2026):** Sumner rewrote Bun from Zig to Rust using AI tools — >1M lines, passed test suite, merged within days. Addresses memory safety for Anthropic-scale workloads.

**Bun v1.3.14 stable (May 13, 2026):** `Bun.$` cross-platform shell API replaces `dax`/`cross-env`/`rimraf` — portable across macOS, Linux, Windows. 8ms cold start, 115K req/s HTTP.

**TS 7.0 "Corsa" (mid/late 2026):** Go-based compiler — 5-10× faster compiles, ~50% less memory. Breaking: `--strict` on by default, ES5/AMD/UMD dropped, `node`/`node10` resolution removed.

**Phase-Based Orchestration:** 6-phase pipeline (Discovery → Clone → Triage → Debug → Remediation → Cross-Reference) with 15+ wrappers across .sh + .ps1 + .bat.

---

## Cheatsheets

| Topic | URL |
|-------|-----|
| Bun TypeScript | https://bun.com/docs/typescript |
| Bun + Vite | https://bun.com/docs/guides/ecosystem/vite |
| Bun CLI apps | https://oneuptime.com/blog/post/2026-01-31-bun-cli-applications/view |
| DeployHQ Bun | https://www.deployhq.com/cheatsheets/bun |
| ESLint flat config | https://eslint.org/docs/latest/use/configure/configuration-files |
| Vitest | https://vitest.dev/guide/ |

```bash
bun install --frozen-lockfile
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh
powershell -File orchestrator-unified.ps1 -Mode discover
```

---

## Best Practices

1. **Bun-native** — `bun run` over `bunx tsx` for project TS files (faster, fewer deps)
2. **Multi-wrapper parity** — every script ships as `.sh` + `.ps1` + `.bat`
3. **Dry-run first** — all destructive commands support `--dry-run` for safe preview
4. **TypeScript strict** — `noUncheckedIndexedAccess`, `noImplicitOverride` on
5. **Separate type-checking** — Bun strips types on-the-fly; run `tsc --noEmit` separately
6. **Lockfile integrity** — commit `bun.lock`; verify in CI
7. **TS 5.9+** — `strictInference: true`, `verbatimModuleSyntax: true`, `"types": ["bun"]`

---

## Common Pitfalls

| Pitfall | Avoidance |
|---------|-----------|
| Missing `"types": ["bun"]` in tsconfig | Add to `compilerOptions` |
| Using `bunx tsx` for own scripts | Use `bun run src/foo.ts` directly |
| `node:fs` missing `cp` | Use `fs-extra` or manual impl |
| Concurrent `fs.readFile` on Bun | Limit concurrent file ops (risk of segfault) |
| Workspace `resolutions` unsupported | Manual dedup with `npm ls` |

---

## Performance

| Metric | Bun 1.3 | Node.js 22 |
|--------|---------|------------|
| HTTP throughput | 115,000 req/s | 48,000 req/s |
| File I/O (10K files) | 310ms | 850ms |
| Cold startup | 8ms | 35ms |
| Package install (Next.js) | 4s | 28s (npm) |

- `Bun.file()`/`Bun.write()` — 2–3× faster than node:fs
- `Bun.$` shell — cross-platform, no need for dax/cross-env/rimraf

---

## Security

Bun has **no built-in permissions system** — Deno 2 is the only runtime with sandboxing. **June 2026 alert:** npm worm targeting Bun via `binding.gyp` credential stealers (Miasma/Hades variant) compromised 23 packages. Mitigations:

1. **Lockfile verification** in CI — prevents supply chain tampering
2. **Minimal trustedDependencies** — only `protobufjs`, `esbuild`, `sharp`
3. **`dotenv-safe`** for env validation — no hardcoded secrets
4. **`eslint-plugin-security`** + CodeQL-ready for code scanning
5. **`bun audit`** — regularly scan for known vulnerabilities

---

## Related Projects (in workspace)

- **Banking** — Bun package manager (`bun.lock`) + TS strict + Drizzle ORM + Next.js App Router
- **comicwise** — TS strict + Next.js; shares CI quality gates and lint patterns
- **ecom** — uses install.sh pattern derived from Bash toolkit; Python/Django stack
- **mcp-servers** — TypeScript implementations share ESLint config and module resolution
- **root SandBox** — shared CI in `.github/workflows/bash-scripts-ci.yml`

---

## Resources

| Resource | URL |
|----------|-----|
| Bun TypeScript Docs | https://bun.com/docs/typescript |
| Bun + Vite Guide | https://bun.com/docs/guides/ecosystem/vite |
| Node.js API compat tracker | https://bun.com/docs/runtime/nodejs-apis |
| Anthropic announcement | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone |
| Bun Wikipedia | https://en.wikipedia.org/wiki/Bun_(software) |
| SPECS.md | `projects/Bash/SPECS.md` |
| ORCHESTRATOR-IMPLEMENTATION.md | `projects/Bash/ORCHESTRATOR-IMPLEMENTATION.md` |

---

### Methodology
3 Tavily advanced searches (`time_range=year`) + 3 prior searches (2026-07-16). Verified bun.com, deployhq.com, Wikipedia.

**Last verified:** 2026-07-24.