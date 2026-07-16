# Resume_maker — Research Report

> **Project:** Resume_maker — CLI document generator (JSON → Markdown + PDF)
> **Stack:** TypeScript (strict), Bun runtime, markdown-pdf (PhantomJS), Zod
> **Status:** Active
> **Date:** 2026-07-16

---

## 1. Executive Summary

Resume_maker's stack (Bun + TypeScript strict + markdown-pdf) is well-suited for a CLI document generator. Bun delivers fast cold start, native TypeScript execution, and standalone binary compilation. Primary risk is the PDF engine's heavyweight dependency — mitigated by always saving Markdown first. Note: **markdown-pdf v11 renders via PhantomJS** (HTML5 Boilerplate → PDF), not Puppeteer as previously assumed — PhantomJS is unmaintained, a supply-chain consideration.

## 2. Bun Runtime (v1.3.x, acquired by Anthropic Dec 2025)

- **Cold start:** single-digit ms vs Node.js ~45 ms — critical for CLI UX.
- **Native TypeScript:** full syntax — no tsc or ts-node needed.
- **Standalone binaries:** `bun build --compile --target=bun-windows-x64` → single executable.
- **Acquired by Anthropic** (Dec 3, 2025); remains MIT-licensed, >7M monthly downloads, 82K+ stars. Long-term runtime de-risked.

## 3. CLI Architecture

- **Argument parsing:** built-in `util.parseArgs()` — no external library.
- **Subcommand dispatch:** map commands (`resume`, `cover-letter`) to typed handlers.
- **Colorized output:** TTY-aware ANSI codes — no chalk needed.
- **Exit codes:** `0` success, `1` error.
- **Cross-compile** for Windows/Linux/macOS.
- **Standalone binaries:** `bun build --compile --target=bun-windows-x64` → single executable.

## 4. TypeScript Configuration

Current `strict: true` is solid. Recommended additions:

- `noUnusedLocals: true` — catches dead code.
- `noUnusedParameters: true` — prefix unused params with `_`.
- `exactOptionalPropertyTypes: true` — stricter optional handling.
- Add `"types": ["bun"]` (required on TS 6/7). Always run `bun tsc --noEmit` in CI.

## 5. Input Validation (Zod 4)

- **Zod 4 is now stable** (zod.dev) — TypeScript-first, zero external deps, 2kb gzipped core.
- **`safeParse` preferred** over `parse` — returns `{ success, data, error }`, no thrown exceptions.
- **Inferred types** via `z.infer<typeof ResumeSchema>` — single source of truth.
- **Recommendation:** replace manual `validateResumeData()` with Zod schemas.

## 6. Markdown → PDF Conversion

Current stack: `markdown-pdf` v11 (marked/Remarkable → HTML → PhantomJS → PDF).

| Factor | Detail |
|--------|--------|
| Pros | Proven, customizable CSS, CLI + programmatic API |
| Cons | PhantomJS unmaintained (~heavy, security debt), slower first-run |
| Mitigation | Save Markdown always; PDF as optional second pass |
| Alternatives | Puppeteer (active, 8M+ weekly dl), @react-pdf/renderer, PDFKit |

## 7. Security Considerations

1. **Input validation:** always use Zod `safeParse` — never trust raw input.
2. **Path traversal:** resolve paths relative to project root; reject `../` escapes.
3. **Output safety:** require `--force` to overwrite existing files.
4. **Supply chain:** `bun install --frozen-lockfile` in CI; pin exact versions.
5. **Markdown injection:** escape user text in templates.
6. **PDF engine:** prefer an actively-maintained renderer (Puppeteer) over PhantomJS.

## 8. Common Pitfalls

- **Windows paths:** PhantomJS/Chromium launch paths differ — test PDF on target OS.
- **ESM:** project uses `"type": "module"` — use `import` everywhere.
- **Headless launch:** may fail without system libs (libnss3, libx11).
- **PhantomJS EOL:** unmaintained — plan migration to Puppeteer.
- **High Bun open issues (~4,800):** stick to well-tested APIs.

## 9. Competitive Landscape

| Project | Stack | Differentiator |
|---------|-------|----------------|
| JSON Resume | JSON Schema + CLI | Community schema — consider adopting format |
| RenderCV | Python + Typst | High-quality PDF, Python-only |
| OpenResume | React, Next.js | Web-based, not CLI |
| **Resume_maker** | **Bun + TS strict** | Fastest cold start, native TS, standalone binary |

## 10. Recommendations

1. Adopt Zod 4 — replace manual validation with type-safe schemas.
2. Align with JSON Resume schema for community compatibility.
3. Add `bun build --compile` for zero-dep binary distribution.
4. Enable `noUnusedLocals`/`noUnusedParameters` in tsconfig.
5. Two-phase output: Markdown always, PDF optional.
6. Plan migration from PhantomJS (markdown-pdf) to Puppeteer.
7. Add smoke tests with `bun test`.

## Related Projects
- See `projects/RESEARCH_INDEX.md` for cross-project references (Bash shares Bun/CLI patterns).

## Resources
| Bun acquires Anthropic | https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone |
| Bun TypeScript docs | https://bun.com/docs/typescript |
| Zod 4 | https://zod.dev/ |
| markdown-pdf (npm) | https://www.npmjs.com/package/markdown-pdf |
| Puppeteer | https://pptr.dev/ |
| JSON Resume | https://jsonresume.org/ |
