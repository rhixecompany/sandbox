# Plan: Full ESLint, VSCode, Auth Modernization (Optimized & Merged)

> Extracted from `debugger.prompt.md`.

## Plan: Full ESLint, VSCode, Auth Modernization (Optimized & Merged)

This plan merges all best practices, code samples, and config patterns from your main and reference files. It ensures zero lint/build errors, DRY config, and modern Next.js/TypeScript/Auth/VSCode integration.

---

### 1. ESLint Plugin Verification & Config Generation

- Verify all plugins are installed:
  - `eslint-config-prettier`, `eslint-plugin-better-tailwindcss`, `eslint-plugin-playwright`, `eslint-plugin-vitest`, `eslint-plugin-drizzle`, `eslint-plugin-sonarjs`.

  ```sh

  ```

- Research latest docs for `eslint-config-prettier`, `eslint-plugin-better-tailwindcss`, `eslint-plugin-playwright`, `eslint-plugin-vitest`, `eslint-plugin-drizzle`, `eslint-plugin-sonarjs` and Summarize key integration patterns and best practices.

---

- Backup originals to backup.
- Generate new, clean, DRY, and Next.js-optimized versions:
  - **Settings Example:**
    ```json
    {
      "editor.formatOnSave": true,
      "editor.tabSize": 2,
      "eslint.lintTask.enable": true,
      "eslint.useFlatConfig": true,
      "eslint.validate": [
        "javascript",
        "typescript",
        "typescriptreact"
      ],
      "explorer.fileNesting.enabled": true,
      "explorer.fileNesting.patterns": {
        "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
        "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
      }
    }
    ```
  - **Extensions Example:**
    ```json
    {
      "recommendations": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "bradlc.vscode-tailwindcss",
        "PulkitGangwar.nextjs-snippets",
        "Prisma.prisma",
        "vitest.explorer",
        "github.copilot-chat"
      ],
      "unwantedRecommendations": [
        "hookyqr.beautify",
        "dbaeumer.jshint",
        "eg2.tslint"
      ]
    }
    ```

---

### 3. NextAuth, Drizzle Adapter, Auth Core Research & Integration

**Actions:**

- Research latest docs for:
  - [next-auth@latest](https://authjs.dev/)
  - [@auth/drizzle-adapter@latest](https://authjs.dev/reference/adapter/drizzle)
  - [@auth/core@latest](https://authjs.dev/reference/core)
- Generate/update all auth files for modular, DRY, and secure integration:
  - auth.ts
    ```typescript
    import { Auth } from "@auth/core";
    import { authConfig } from "./auth-config";
    export default function handler(request: Request) {
      return Auth(request, authConfig);
    }
    ```
  - auth-config.ts
    ```typescript
    import { adapter } from "./auth-adapter";
    import { providers } from "./auth-providers";
    export const authConfig = {
      providers,
      adapter,
      session: {
        strategy: "database",
        maxAge: 2592000,
        updateAge: 86400
      },
      secret: process.env.AUTH_SECRET!,
      trustHost: true,
      useSecureCookies: process.env.NODE_ENV === "production",
      callbacks: {
        async session({ session }) {
          return session;
        },
        async jwt({ token }) {
          return token;
        },
        async signIn() {
          return true;
        },
        async redirect({ url, baseUrl }) {
          return url.startsWith("/") ? `${baseUrl}${url}` : url;
        }
      }
    };
    ```
  - auth-providers.ts
    ```typescript
    import GitHub from "@auth/core/providers/github";
    import Credentials from "@auth/core/providers/credentials";
    import Keycloak from "@auth/core/providers/keycloak";
    export const providers = [
      GitHub({
        clientId: process.env.GITHUB_CLIENT_ID!,
        clientSecret: process.env.GITHUB_CLIENT_SECRET!
      }),
      Credentials({
        name: "Credentials",
        credentials: {
          username: { label: "Username", type: "text" },
          password: { label: "Password", type: "password" }
        },
        authorize: async () => null
      }),
      Keycloak({
        clientId: process.env.KEYCLOAK_CLIENT_ID!,
        clientSecret: process.env.KEYCLOAK_CLIENT_SECRET!,
        issuer: process.env.KEYCLOAK_ISSUER!
      })
    ];
    ```
  - auth-adapter.ts
    ```typescript
    import { db } from "@/database/db";
    import {
      user,
      account,
      session,
      verificationToken
    } from "@/database/schema";
    import { DrizzleAdapter } from "@auth/drizzle-adapter";
    export const adapter = DrizzleAdapter(db, {
      usersTable: user,
      accountsTable: account,
      sessionsTable: session,
      verificationTokensTable: verificationToken
    });
    ```
  - auth-actions.ts
    ```typescript
    export const signIn = async (provider: string, options?: any) => {
      /* ... */
    };
    export const signOut = async () => {
      /* ... */
    };
    export const getSession = async () => {
      /* ... */
    };
    ```
  - proxy.ts
    ```typescript
    export const proxyUrl = process.env.AUTH_PROXY_URL || "";
    export default function proxy() {
      return Response.json({ status: "ok" });
    }
    ```
  - route.ts
    ```typescript
    import handler from "@/auth";
    export { handler as GET, handler as POST };
    ```

---

### 4. Verification

**Actions:**

- Run:
  ```sh
  pnpm lint
  pnpm build
  ```
- Manually check VSCode settings and extensions.
- Test auth endpoints and integration.

---

### 5. Documentation

**Actions:**

- Document all fixes and config changes in:
  - proposedFixes.MD
  - proposedFixes.json

---

**Decisions:**

- Use batch install for speed.
- Backup before replacing VSCode configs.
- Use latest Next.js and NextAuth docs for auth files.
- Prioritize DRY and modularity in all configs.

---

**Result:** This plan ensures zero lint/build errors, DRY and maintainable config, and modern, secure authentication. Let me know if you want this applied or further customized!
