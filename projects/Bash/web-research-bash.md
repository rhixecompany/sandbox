# Web Research — Bash Project

**Tech Stack:** TypeScript, Node, Bun, Vite  
**Date:** 2026-07-16  
**Source:** Web research (5 targeted queries, multiple article extractions)

---

## Table of Contents

1. [Runtime Landscape: Bun vs Node.js vs Deno](#1-runtime-landscape-bun-vs-nodejs-vs-deno)
2. [Bun with TypeScript: Best Practices](#2-bun-with-typescript-best-practices)
3. [Vite Integration with Bun and TypeScript](#3-vite-integration-with-bun-and-typescript)
4. [Common Pitfalls & Migration Gotchas](#4-common-pitfalls--migration-gotchas)
5. [Performance Optimization Tips](#5-performance-optimization-tips)
6. [Security Considerations](#6-security-considerations)
7. [Similar Projects & References](#7-similar-projects--references)

---

## 1. Runtime Landscape: Bun vs Node.js vs Deno

### Overview (2026)

The JavaScript runtime market has reached "stable pluralism" — three reliable options coexist:

| Runtime | Engine | Language | Package Manager | TypeScript Support |
|---------|--------|----------|-----------------|-------------------|
| **Node.js 22 LTS** | V8 (Chrome) | C++ | npm (bundled) | Via transpiler (`--experimental-strip-types`) |
| **Deno 2** | V8 | Rust | Built-in + npm native | ✅ Native |
| **Bun 1.3+** | JavaScriptCore (Safari) | Zig + C++ | Built-in (`bun install`) | ✅ Native |

### Why Bun for This Project

- **Bun is the designated runtime** for the Bash project (packageManager: `bun@1.3.14`, engines.bun: `>=1.3.14`)
- Bun provides a single-executable toolkit: runtime, package manager, bundler, and test runner in one binary
- Written in Zig, built on JavaScriptCore — prioritizes fast startup and low memory usage

### Key Performance Benchmarks (Source: PkgPulse, 2026)

| Metric | Node.js 22 | Deno 2 | Bun 1.2 |
|--------|-----------|--------|---------|
| HTTP throughput (req/s) | 48,000 | 62,000 | **115,000** |
| File I/O (10k files) | 850ms | 720ms | **310ms** |
| Package install (Next.js) | 28s (npm) | — | **4s** |
| Cold startup | 35ms | 25ms | **8ms** |

**Bottom line for Bash:** Bun's 4x faster startup and 2-3x faster I/O directly benefit an automation toolkit that runs many short-lived scripts.

### Production Readiness

- Bun crossed **2M weekly npm downloads** in late 2025
- Companies like Vercel and Railway support Bun deployments
- Bun has shifted from "blazing fast but sometimes brittle" to "blazing fast and increasingly sturdy"
- For non-critical microservices and internal tools (like automation scripts), Bun is production-ready
- Teams commonly use Bun for **testing + dev** and Node.js for **production deployment** as a hybrid approach

---

## 2. Bun with TypeScript: Best Practices

### Official Bun TypeScript Configuration

From Bun's official docs, the recommended `tsconfig.json` compilerOptions:

```jsonc
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,
    "types": ["bun"],

    // Bundler mode — must use these for Bun compatibility
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Stricter flags (disabled by default — opt in as needed)
    "noUnusedLocals": false,
    "noUnusedParameters": false,
    "noPropertyAccessFromIndexSignature": false
  }
}
```

**Key differences from a Node-focused tsconfig:**
- `"module": "Preserve"` — lets Bun handle module resolution natively
- `"moduleResolution": "bundler"` — required for Bun-style module resolution
- `"types": ["bun"]` — provides types for `Bun` global API (install via `bun add -d @types/bun`)
- `"noEmit": true` — Bun transpiles on-the-fly; no need for `tsc` to emit files
- `"verbatimModuleSyntax": true` — ensures proper ESM behavior

### TypeScript 6/7 with Bun

If using TypeScript 6.0+, you also need `"types": ["bun"]` in compilerOptions.

### Zero-Config TypeScript Execution

Bun runs `.ts` and `.tsx` files directly without any transpilation setup:

```bash
bun run hello.ts    # No tsc, no ts-node, no config needed
```

Bun's transpiler **strips types only** — it does NOT perform type checking during execution for performance. Use `tsc --noEmit` for type checking:

```bash
bunx tsc --noEmit
# or
bun --bun tsc --noEmit
```

Suggested package.json scripts:
```jsonc
{
  "scripts": {
    "typecheck": "tsc --noEmit",
    "typecheck:watch": "tsc --noEmit --watch"
  }
}
```

### Project-Specific Observations

The Bash project's current tsconfig.json uses:
- `"module": "ESNext"` and `"moduleResolution": "bundler"` — compatible with Bun
- `"strict": true` — matches Bun's recommendation
- `"noEmit": true` — correct for Bun
- `"types": ["bun"]` — NOT currently set (may need `@types/bun`)

---

## 3. Vite Integration with Bun and TypeScript

### Official Setup (from bun.com/docs)

Vite works out of the box with Bun:

```bash
bun create vite my-app           # Scaffold with a Vite template
cd my-app
bun install                      # Install dependencies
bunx --bun vite                  # Run Vite CLI via Bun
bunx --bun vite build            # Production build via Bun
```

The `--bun` flag tells Bun to execute Vite's CLI with Bun instead of Node.js (by default Bun respects the `#!/usr/bin/env node` shebang).

**Simplified package.json scripts:**

```jsonc
{
  "scripts": {
    "dev": "bunx --bun vite",
    "build": "bunx --bun vite build",
    "serve": "vite preview"
  }
}
```

### Vite Architecture for TypeScript (Steve Kinney)

Vite uses a **two-phase approach**:
1. **Development:** Serves TypeScript files as native ESM — transpiles on-demand (no bundling)
2. **Production:** Uses Rollup for bundling and optimization

**Key insight:** Vite does NOT type-check during dev by default — it only strips types. Use `vite-plugin-checker` for parallel type checking:

```bash
bun add -D vite-plugin-checker
```

```typescript
// vite.config.ts
import checker from 'vite-plugin-checker';

export default defineConfig({
  plugins: [
    react(),
    checker({
      typescript: true,
      overlay: { initialIsOpen: false, position: 'br' },
      terminal: true,
    }),
  ],
});
```

### Optimized tsconfig for Vite + Bun Projects

```jsonc
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "strict": true,
    "skipLibCheck": true,
    "incremental": true,
    "tsBuildInfoFile": ".tsbuildinfo",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    },
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true
  },
  "include": ["src", "vite.config.ts"],
  "exclude": ["node_modules", "dist"]
}
```

### Vite Production Build Optimization

**Manual chunking strategy** for better caching:

```typescript
// vite.config.ts
export default defineConfig({
  build: {
    target: 'es2015',
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: (id) => {
          if (id.includes('react') || id.includes('react-dom')) return 'react';
          if (id.includes('node_modules')) return 'vendor';
        },
        chunkFileNames: 'js/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash][extname]',
      },
    },
    treeshake: { preset: 'recommended', moduleSideEffects: false },
    cssCodeSplit: true,
    chunkSizeWarningLimit: 500,
  },
});
```

**Additional production optimizations:**
- `splitVendorChunkPlugin()` — automatic vendor chunk splitting
- `vite-plugin-compression` — Brotli/Gzip compression
- `rollup-plugin-visualizer` — bundle analysis (`mode === 'analyze'`)
- Dependency pre-bundling with `optimizeDeps.include` / `optimizeDeps.exclude`

### Note on Bun's Native Bundler

Bun has its own built-in bundler (`bun build`) that can replace Vite for simpler projects. The Bun docs note:
> "You can use Vite with Bun, but many projects get faster builds & drop hundreds of dependencies by switching to HTML imports."

For the Bash project (an automation toolkit, not a frontend app), the Vite dependency in package.json is for tools like `vitest` — Vite itself may not be needed for production builds of CLI scripts.

---

## 4. Common Pitfalls & Migration Gotchas

### Migrating from Node.js to Bun

Based on real-world migration reports (300+ package monorepo, GitHub discussion #3955):

#### Critical Issues Found

| Issue | Impact | Workaround |
|-------|--------|------------|
| `node:fs` missing `cp` | File copy operations fail | Implement manually or use `fs-extra` |
| `Module._nodeModulePaths` not exposed | Packages like `app-module-path` break | Replace or patch the dependency |
| Workspace `resolutions` not supported | Duplicate dependency versions (e.g., 2 copies of React) | Manual deduplication with `npm ls` |
| Memory/segfault with heavy `fs.readFile` | Random memory corruption on concurrent reads | Limit concurrent file operations |
| Native addons (sharp, bcrypt) need Bun versions | Some C++ addons don't work | Use Bun-specific versions or WASM alternatives |
| `@swc/wasm` not supported | `bun build --compile` may fail for dynamic imports | Expose as TypeScript source |

#### Compatibility Level

- **Works well:** Express, Fastify, Hono, Prisma, Drizzle, Next.js, SvelteKit, Astro
- **Partial:** Some native addons, `node:fs` edge cases, CommonJS-specific APIs
- See the [Bun compatibility tracker](https://bun.com/docs/runtime/nodejs-apis) for current status

#### Dual-Runtime Strategy

For teams wanting to run both Node and Bun:
```jsonc
{
  "compilerOptions": {
    "moduleResolution": "bundler",
    "module": "esnext",
    "target": "esnext",
    "strict": true,
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "types": ["bun"]  // Remove for Node.js
  }
}
```

Create a migration script to toggle `tsconfig.json` and `package.json` between runtimes.

### npm Compatibility Patterns (2026)

- **Bun:** ~90%+ npm package compatibility. Framework support is strong.
- **Deno 2:** Near-complete Node.js compatibility via `npm:` specifier and optional `package.json`/`node_modules`.
- **Node.js:** 100% — the reference implementation.

**Recommendation for Bash:** Since the project already uses Bun as its package manager, test all npm-sourced dependencies under Bun before relying on them in production paths.

### General TypeScript + Vite Pitfalls

1. **Path alias mismatch** — Aliases in `tsconfig.json` must be mirrored in `vite.config.ts`'s `resolve.alias`
2. **Missing `.js` extension in imports** — Vite/ESM requires full extensions for relative imports (or use `"allowImportingTsExtensions": true`)
3. **`isolatedModules: true`** — Required by Vite; forbids certain TypeScript features like `const enum` exports
4. **Type-checking lag** — Vite doesn't check types; must run `tsc --noEmit` separately or use `vite-plugin-checker`
5. **Environment variable access** — Must use `import.meta.env.VITE_*` (VITE_ prefix convention), not `process.env`

---

## 5. Performance Optimization Tips

### Bun-Specific Optimizations

| Technique | Details |
|-----------|---------|
| **Use `bun` instead of `bunx` for scripts** | Run your own TS files with `bun run`, not `bunx` (reserved for npm-published CLIs) |
| **Leverage Bun's SQLite** | `Bun.sqlite` is dramatically faster than `better-sqlite3` |
| **Use `Bun.file()` and `Bun.write()`** | Native I/O is 2-3x faster than `node:fs` equivalents |
| **Minimize `fs.readFile` concurrency** | Too many simultaneous reads can trigger memory issues (reported bug) |
| **Use `bun build --compile`** | Generate standalone binaries for deployment — no runtime needed |
| **Bun's test runner** | `bun test` is faster than Jest/Vitest for CLI-heavy test suites |

### Vite Dev Server Optimization

```typescript
// vite.config.ts
export default defineConfig({
  server: {
    warmup: {
      // Pre-transform frequently used files on startup
      clientFiles: ['./src/main.tsx', './src/App.tsx', './src/components/**/*.tsx'],
    },
  },
  optimizeDeps: {
    include: ['react', 'react-dom'],  // Force pre-bundle critical deps
    exclude: ['@faker-js/faker'],     // Exclude large rarely-used deps
  },
});
```

### Production Build Optimizations

1. **Set `build.target: 'es2015'`** for broader browser support or `'esnext'` for minimal transpilation
2. **Use `esbuild` minifier** (default) — faster than `terser` for comparable output
3. **Enable `cssCodeSplit: true`** (default) for CSS per-chunk
4. **Tree shaking** — Vite uses Rollup's tree shaking by default; ensure ESM imports for maximum benefit
5. **Source maps** — Disable in production (`sourcemap: false`)

### Build Size Management

- Set `chunkSizeWarningLimit: 500` (default) to get warnings on large chunks
- Use `rollup-plugin-visualizer` for bundle analysis
- Monitor dependency weight — the Bash project's devDependencies include many ESLint plugins that should not affect production builds

---

## 6. Security Considerations

### Supply Chain Security

| Runtime | Built-in Permissions | Risk Level |
|---------|---------------------|------------|
| **Node.js** | ❌ None | Trusts all code implicitly |
| **Deno** | ✅ Permission system (fs, net, env) | Most secure by default |
| **Bun** | ❌ None | Trusts all code implicitly |

**Implications for Bash:**
- Since the Bash project runs automation scripts (cache cleanup, migrations, git operations), the scripts have access to the full filesystem
- No built-in sandboxing means any compromised dependency can access everything
- Mitigation: Audit `trustedDependencies` in `package.json` (currently: protobufjs, esbuild, sharp), use `bun install --ignore-scripts` where possible

### Recommended Security Practices

1. **Lockfile integrity** — Commit `bun.lock` to version control and verify with CI checks
2. **Dependency auditing** — Use `bun audit` (or `npm audit`) to check for known vulnerabilities
3. **Minimal trusted dependencies** — Only mark as trusted what absolutely needs postinstall scripts
4. **Environment variables** — Use `dotenv` or `dotenv-safe` (already in devDependencies); never hardcode secrets
5. **Code scanning** — Consider GitHub's CodeQL or `eslint-plugin-security` (already in devDependencies)
6. **Dependency updates** — The project already includes `npm-check-updates` for tracking updates

### Security Features in Bun

- Bun has a `--bun` flag security model — it won't run Node.js-based scripts unless explicitly told
- Bun's `fetch()` and Web API implementations follow standard security models
- Bun lacks Deno's permissions system, but it does support `bun install --ignore-scripts` to block postinstall attacks

### Vite Security

- Vite's dev server should NOT be exposed to the public internet (use `server.host` carefully)
- Environment variables prefixed with `VITE_` are inlined into client-side code — never put secrets there
- Use `dotenv-safe` for required env validation (recommended pattern in the OneUptime blog guide)

---

## 7. Similar Projects & References

### Comparable Projects

| Project | Description | Relevance |
|---------|-------------|-----------|
| **tsx** (4.x) | TypeScript Execute — run TS files via Node.js (uses esbuild) | Similar goal: zero-config TS execution. Bun makes tsx redundant. |
| **ts-node** | TypeScript execution and REPL for Node.js | Legacy approach; Bun's native TS support is faster |
| **npx/npm exec** | Run npm package binaries | Bunx replaces this with `bunx` |
| **esbuild** | Extremely fast bundler (Go-based) | Bun's internal bundler is inspired by esbuild's speed |
| **tsup** | Bundle TS with esbuild, no config | Partially replaced by Bun's `bun build` |
| **tsc** (TypeScript Compiler) | Official TS compiler | Still needed for type checking even with Bun |

### Key Articles Referenced

1. **Bun Official Docs — TypeScript** — https://bun.com/docs/typescript
   - Suggested compilerOptions, `@types/bun`, TypeScript 6/7 notes

2. **Bun Official Docs — Vite Integration** — https://bun.com/docs/guides/ecosystem/vite
   - `bun create vite`, `bunx --bun vite`, production build commands

3. **Node.js vs Deno vs Bun: The Ultimate Runtime Guide (2026)** — dev.to/dataformathub
   - Benchmarks: Bun 115K req/s vs Node 48K, 4x faster startup
   - Architecture analysis: JavaScriptCore vs V8, Zig vs C++

4. **Vite + React TypeScript Optimization** — Steve Kinney
   - Parallel type checking, optimized tsconfig, code splitting strategies

5. **PkgPulse Runtime Comparison (2026)** — pkgpulse.com
   - Decision framework: Node for stability, Deno for security, Bun for speed

6. **Large Codebase Migration Story** — GitHub Discussion #3955
   - Real migration pitfalls: fs bugs, workspace resolutions, native addons

7. **OneUptime Production Setup Guide** — oneuptime.com
   - Production-ready ESLint, Prettier, path aliases, build config

8. **How to Use TypeScript with Bun** — oneuptime.com
   - Zero-config TS, type checking with `tsc --noEmit`, tsconfig recommendations

### Tools in the Bash Project That Match Recommendations

- ✅ `@types/bun` — installed for Bun type definitions
- ✅ `eslint-plugin-security` — installed for security linting
- ✅ `tsc --noEmit --pretty` — typecheck script matches best practice
- ✅ `bunx tsx` — used in scripts (consider `bun run` for own code)
- ✅ `dotenv-safe` — environmental configuration
- ✅ `vitest` for testing (but consider `bun test` for faster runs)
- ✅ `typescript-eslint` for TS-aware linting

### Potential Improvements

| Area | Current State | Recommendation |
|------|--------------|----------------|
| Types config | `"types": ["bun"]` not in tsconfig | Add `"types": ["bun"]` for full Bun API types |
| Type checking | `tsc --noEmit` via npm script | Works well, but consider `vite-plugin-checker` if Vite is used for UI |
| Script runner | Uses `bunx tsx` for many scripts | Change to `bun run` for project's own TS files (faster, no tsx dependency) |
| Test runner | vitest | `bun test` is native and faster for CLI/automation tests |
| Production builds | Not using Bun's bundler | For CLI scripts, `bun build --compile` produces standalone binaries |
| Lockfile | bun.lock at 277KB | Keep committed; verify in CI |

---

*Research compiled from 5 web search queries and 8+ detailed article extractions on 2026-07-16.*
