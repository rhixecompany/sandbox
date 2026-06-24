# Phase 4: Config Edits (5 edits)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 4: Config Edits (5 edits)

### 4.1 — `next.config.ts`

Add image domains, CDN/proxy support, security headers:

```ts
const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { protocol: "https", hostname: "**.cdnjs.cloudflare.com" },
      { protocol: "https", hostname: "**.githubusercontent.com" }
    ],
    formats: ["image/avif", "image/webp"]
  }
  // Keep existing experimental flags
};
```

### 4.2 — `eslint.config.mts`

Ensure `@typescript-eslint/no-explicit-any` is set to `"error"`:

```ts
"@typescript-eslint/no-explicit-any": "error",
"@typescript-eslint/no-unused-vars": ["error", { argsIgnorePattern: "^_" }],
```

### 4.3 — `tsconfig.json`

Verify strict mode, path aliases (`@/*`, `ui/`, `hooks/`, `lib/`, `schemas/`, `types/`, `utils/`).

### 4.4 — `next-sitemap.config.ts`

Add exclude patterns for admin and auth routes:

```ts
exclude: ["/admin/*", "/(auth)/*", "/api/*"],
```

### 4.5 — `package.json`

Verify scripts:

```json
{
  "scripts": {
    "type-gen": "next build --experimental-build-mode compile",
    "type-check": "tsc --noEmit",
    "lint:fix": "eslint . --fix && prettier --write .",
    "test": "vitest run",
    "test:ui": "playwright test",
    "db:push": "drizzle-kit push",
    "db:seed": "tsx src/scripts/seed.ts"
  }
}
```

---
