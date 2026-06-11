Analyze this codebase to generate or update `.github/copilot-instructions.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

- The `big picture` architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the `why` behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns
- Always use powershell commands and pnpm

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}` (do one glob search).

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

- If `.github/copilot-instructions.md` exists, merge intelligently - preserve valuable content while updating outdated sections
- Write concise, actionable instructions (~20-50 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice (`write tests`, `handle errors`) - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns

Update `.github/copilot-instructions.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.

Analyze `.github/prompts/*.md`, `docs/*.md` to generate or update `.github/prompts/setup.prompt.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

- The `big picture` architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the `why` behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}`.

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

- @workspace /explain to identify patterns, conventions, and workflows that are critical for AI agents,
- Write concise, actionable instructions,prompts,actions,steps (~200-500 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice (`write tests`, `handle errors`) - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns
- include all code samples
- for additional context and instructions, read `.github/prompts/plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md`, `.github/prompts/*.md`,`.github/prompts/debugger.prompt.md`,`docs\debugger.prompt.md`,`.github/prompts/*.md`, `docs/*.md`.
- If `.github/prompts/setup.prompt.md` exists, merge intelligently - preserve valuable content while updating outdated sections.

Update `.github/prompts/setup.prompt.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.

Generate drizzle module with dts-gen: `pnpm exec dts-gen -m eslint-plugin-drizzle`.

Search the web for docs on all eslint plugins that are installed and read and understand all of them then Check all eslint plugins and install any missing and uninstall any deprecated ones and uninstall any plugins with issues or conflicts, then generate or update `eslint.config.ts` with all their settings, plugins, and rules configured for this project reference `.references\comicwise\eslint.config.ts`,`.references\comicr\eslint.config.mjs`,`eslint.config.mts.backup` verify my running pnpm lint. Search the web for docs on next-auth@latest,@auth/drizzle-adapter@latest,@auth/core@latest and read and understand all of them then generate or update all `src\auth.ts`,`src\auth-config.ts`,`src\auth-providers.ts`,`src\auth-adapter.ts`,`src\actions\auth-actions.ts`,`src\proxy.ts`,`src\app\api\auth\[...nextauth]\route.ts` use nextjs@latest best practices and dry practices. Audit and Review all `.vscode/*.json` files then backup them up and then create a new clean enhanced `.vscode/*.json` files for optimization, consistency and correctness, use nextjs@latest best practices and dry practices.

## Plan: Full ESLint, VSCode, Auth Modernization

This plan covers plugin verification/installation, ESLint config generation, VSCode JSON audit/backup/optimization, and NextAuth/Drizzle/Auth Core integration for a Next.js 16+ project. Steps are sequenced for speed and minimal redundancy. **Steps**

1. **ESLint Plugin Check & Install**
   - Check if each plugin (`eslint-config-prettier`, `eslint-plugin-better-tailwindcss`, etc.) is installed.
   - Use batch install for speed.

2. **Generate/Update eslint.config.mts**
   - Create a config with all plugins, recommended settings, and rules for Next.js, TypeScript, Tailwind, security, and DRY practices.
   - Include best practices for React, accessibility, import order, and testing.

3. **Audit, Backup, Optimize `.vscode/*.json`**
   - Backup originals to `.vscode/backup/`.
   - Generate new, clean, DRY, and Next.js-optimized versions (settings, extensions, etc.).

4. **Research NextAuth, Drizzle Adapter, Auth Core**
   - Search web for docs on `next-auth@latest`, `@auth/drizzle-adapter@latest`, `@auth/core@latest` and read them if found.
   - Summarize key integration patterns and best practices.

   - Use latest Next.js, NextAuth, Drizzle, and Auth Core patterns.
   - Ensure DRY, modular, and consistent structure.

5. **Verification**
   - Run `pnpm lint`, `pnpm build`, and manual checks for VSCode settings.
   - Test auth endpoints and integration.

**Decisions**

- Batch install for speed.
- Backup before replacing VSCode configs.
- Use latest Next.js and NextAuth docs for auth files.
- Prioritize DRY and modularity in all configs.

---

This plan is optimized for speed, correctness, and maintainability. Each step is actionable and minimizes redundant work.

Fetched https://next-auth.js.org/getting-started/introduction

Fetched https://authjs.dev/reference/adapters/drizzle

Fetched https://authjs.dev/reference/core

Here’s a concise summary of key integration patterns and best practices for NextAuth.js, Drizzle Adapter, and Auth Core (latest):

**NextAuth.js (latest):**

- Flexible, secure, and works with any OAuth provider, email/passwordless, or custom credentials.
- Supports both JWT and database session strategies.
- Designed for Next.js and serverless, but runs anywhere.
- “Own your own data”: BYOD, works with any database, including Drizzle ORM.
- Secure by default: CSRF protection, encrypted JWTs, strict cookie policies, OWASP guidance.
- Customizable callbacks for signIn, session, JWT, redirect, etc.
- Built-in providers for Google, GitHub, Discord, etc. (see docs for full list).

**@auth/core (latest):**

- Core engine for Auth.js, used in NextAuth.js and other frameworks.
- AuthConfig supports: providers, adapter, session strategy (jwt/database), callbacks, events, custom pages, cookies, secret, debug, logger, theme, trustHost, useSecureCookies.
- Callbacks: jwt, session, signIn, redirect—control token/session flow, access control, and custom redirects.
- Events: createUser, linkAccount, session, signIn, signOut, updateUser—for audit logging and debugging.
- Session config: strategy (jwt/database), maxAge, updateAge, generateSessionToken.
- Adapter: pass Drizzle adapter for database sessions.
- Providers: array of built-in or custom providers.

**Drizzle Adapter:**

- Use `@auth/drizzle-adapter` for database session storage with Drizzle ORM.
- Pass as `adapter` in AuthConfig.
- Supports MySQL, Postgres, SQLite, etc.
- See [authjs.dev/reference/drizzle-adapter](https://authjs.dev/reference/drizzle-adapter) for schema and usage.

**Best Practices:**

- Use JWT for stateless, database for persistent sessions.
- Always set `secret` (use `npx auth secret` to generate).
- Set `trustHost: true` for production.
- Customize callbacks for access control and session shaping.
- Use secure cookies in production (`useSecureCookies: true`).
- Audit events for security and debugging.
- Modularize config: split providers, adapter, callbacks, and session config into separate files for maintainability.

Ready to generate/update your auth files with these patterns!

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

## Comprehensive Modernization Plan: ESLint, VSCode, & Advanced Auth (Type-Safe, Best Practices, Full Samples)

This plan is tailored for your repo, using .env.local for secrets, and reflecting your choices for ESLint plugins, VSCode extensions, and advanced authentication logic. All content and code samples are included, with all `any` types replaced by generics or specific interfaces for maximum type safety and maintainability.

---

### 1. ESLint Plugin Verification & Config Generation

**Actions:**

- Ensure these plugins are installed:
  - `eslint-config-next`, `eslint-config-prettier`, `eslint-plugin-better-tailwindcss`, `eslint-plugin-playwright`, `eslint-plugin-vitest`, `eslint-plugin-drizzle`, `eslint-plugin-zod`
- Install if missing:
  ```sh
  pnpm add -D eslint-config-next eslint-config-prettier eslint-plugin-better-tailwindcss eslint-plugin-playwright eslint-plugin-vitest eslint-plugin-drizzle eslint-plugin-zod
  ```
- Generate `eslint.config.mts` using Next.js core web vitals, TypeScript, and all selected plugins:

**Code Sample: `eslint.config.mts`**

```typescript
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";
import prettier from "eslint-config-prettier";
import betterTailwind from "eslint-plugin-better-tailwindcss";
import playwright from "eslint-plugin-playwright";
import vitest from "eslint-plugin-vitest";
import drizzle from "eslint-plugin-drizzle";
import zod from "eslint-plugin-zod";
import { defineConfig, globalIgnores } from "eslint/config";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  ...prettier,
  {
    plugins: {
      "better-tailwindcss": betterTailwind,
      playwright,
      vitest,
      drizzle,
      zod
    },
    rules: {
      "better-tailwindcss/classnames-order": "warn",
      "drizzle/no-raw-sql": "error",
      "zod/noAny": "error"
    }
  },
  globalIgnores([".next/**", "out/**", "build/**", "next-env.d.ts"])
]);

export default eslintConfig;
```

---

### 2. VSCode JSON Audit, Backup, Optimization

**Actions:**

- Audit settings.json and extensions.json.
- Backup originals to backup.
- Generate new, clean, DRY, and Next.js-optimized versions:

**Code Sample: settings.json**

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "eslint.lintTask.enable": true,
  "eslint.useFlatConfig": true,
  "eslint.validate": ["javascript", "typescript", "typescriptreact"],
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    "*.ts": "${capture}.test.ts, ${capture}.spec.ts",
    "*.tsx": "${capture}.test.tsx, ${capture}.spec.tsx"
  }
}
```

**Code Sample: extensions.json**

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "PulkitGangwar.nextjs-snippets",
    "vitest.explorer"
  ],
  "unwantedRecommendations": [
    "hookyqr.beautify",
    "dbaeumer.jshint",
    "eg2.tslint"
  ]
}
```

---

### 3. NextAuth, Drizzle Adapter, Advanced Auth Core Integration

**Actions:**

- Reference all secrets and credentials from .env.local.
- Enable GitHub, Keycloak, Credentials providers.
- Implement advanced callbacks, custom session handler, and provider-specific features.
- Replace all `any` types with generics or specific interfaces.

**Code Samples:**

- **auth.ts**

  ```typescript
  import { Auth } from "@auth/core";
  import authConfig from "./auth-config";

  export const { handlers, auth, signIn, signOut } = Auth(authConfig);
  ```

- **auth-config.ts**

  ```typescript
  import adapter from "./auth-adapter";
  import providers from "./auth-providers";

  type Session = {
    user?: User;
    lastLogin?: number | null;
    [key: string]: unknown;
  };

  type Token = {
    user?: User;
    role?: string;
    lastLogin?: number;
    provider?: string;
    [key: string]: unknown;
  };

  const session = {
    strategy: "database",
    maxAge: 30 * 24 * 60 * 60, // 30 days
    updateAge: 24 * 60 * 60 // 1 day
  };

  const callbacks = {
    async session({
      session,
      token,
      user
    }: {
      session: Session;
      token: Token;
      user?: User;
    }): Promise<Session> {
      session.user = user || token?.user;
      session.lastLogin = token?.lastLogin || null;
      return session;
    },
    async jwt({
      token,
      user,
      account
    }: {
      token: Token;
      user?: User;
      account?: Record<string, unknown>;
    }): Promise<Token> {
      if (user) {
        token.user = user;
        token.role = user.role || "user";
        token.lastLogin = Date.now();
      }
      if (account) token.provider = account.provider as string;
      return token;
    },
    async signIn({ user }: { user?: User }): Promise<boolean> {
      if (user?.email?.endsWith("@comicwise.app")) return true;
      return false;
    },
    async redirect({
      url,
      baseUrl
    }: {
      url: string;
      baseUrl: string;
    }): Promise<string> {
      return url.startsWith("/") ? `${baseUrl}/dashboard` : url;
    }
  };

  const authConfig = {
    adapter,
    providers,
    session,
    callbacks,
    secret: process.env.AUTH_SECRET,
    trustHost: true
  };

  export default authConfig;
  ```

- **auth-providers.ts**

  ```typescript
  import Credentials from "@auth/core/providers/credentials";
  import GitHub from "@auth/core/providers/github";
  import Keycloak from "@auth/core/providers/keycloak";

  type CredentialsInput = {
    username?: string;
    password?: string;
  };

  type User = {
    id: string;
    name?: string;
    email: string;
    role?: string;
    passwordHash?: string;
  };

  const providers = [
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
      async authorize(
        credentials: CredentialsInput
      ): Promise<User | null> {
        // Example: fetch user from DB and verify password
        // const user = await getUserByUsername(credentials.username);
        // if (user && verifyPassword(credentials.password, user.passwordHash)) return user;
        return null;
      }
    }),
    Keycloak({
      clientId: process.env.KEYCLOAK_CLIENT_ID!,
      clientSecret: process.env.KEYCLOAK_CLIENT_SECRET!,
      issuer: process.env.KEYCLOAK_ISSUER!
    })
  ];

  export default providers;
  ```

- **auth-adapter.ts**

  ```typescript
  import { DrizzleAdapter } from "@auth/drizzle-adapter";
  import { db } from "./database/db";
  import {
    account,
    session,
    user,
    verificationToken
  } from "./database/schema";

  const adapter = DrizzleAdapter(db, {
    usersTable: user,
    accountsTable: account,
    sessionsTable: session,
    verificationTokensTable: verificationToken
  });

  export default adapter;
  ```

- **auth-actions.ts**

  ```typescript
  import { auth, signIn, signOut } from "../auth";

  export async function signInAction(
    provider: string,
    options?: Record<string, unknown>
  ): Promise<unknown> {
    return signIn(provider, options);
  }

  export async function signOutAction(
    options?: Record<string, unknown>
  ): Promise<unknown> {
    return signOut(options);
  }

  export async function getSessionAction(): Promise<unknown> {
    return auth.getSession();
  }
  ```

- **route.ts**
  ```typescript
  import { handlers } from "@/auth";
  export { handlers as GET, handlers as POST };
  ```

---

### 4. Verification

**Actions:**

- Run `pnpm lint` and `pnpm build` to confirm zero errors.
- Manually check VSCode settings and extensions.
- Test authentication endpoints and flows (sign in, sign out, session retrieval, provider-specific logic).

---

### 5. Documentation

**Actions:**

- Document all fixes and config changes in proposedFixes.MD and proposedFixes.json.

---

**Decisions:**

- All secrets and credentials are referenced from .env.local.
- Advanced authentication logic is included for session, JWT, sign-in, and redirect callbacks.
- Credentials provider uses a secure, extensible pattern for custom logic.
- All `any` types are replaced with generics or specific interfaces.
- Modular, DRY, and secure patterns are enforced throughout.

---

**Result:** This plan is fully customized for your repo and requirements, with all content and code samples included, and all advanced authentication logic implemented using best practices and type safety. Ready for implementation or further customization!

Modify `.github/copilot-instructions.md` with `# GitHub Copilot Instructions

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our Layered architectural style and established boundaries
5. **Code Quality**: Prioritize maintainability, performance, security, accessibility, and testability in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - Examine project files, configuration files, and package managers
   - Look for language-specific version indicators (e.g., tsconfig.json, package.json)
   - Never use language features beyond the detected version

2. **Framework Versions**: Identify the exact versions of all frameworks
   - Check package.json, tsconfig.json, etc.
   - Respect version constraints when generating code
   - Never suggest features not available in the detected framework versions

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - Generate code compatible with these specific versions
   - Never use APIs or features not available in the detected versions

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - Naming conventions
   - Code organization
   - Error handling
   - Logging approaches
   - Documentation style
   - Testing patterns
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

### Maintainability

- Write self-documenting code with clear naming
- Follow the naming and organization conventions evident in the codebase
- Follow established patterns for consistency
- Keep functions focused on single responsibilities
- Limit function complexity and length to match existing patterns

### Performance

- Follow existing patterns for memory and resource management
- Match existing patterns for handling computationally expensive operations
- Follow established patterns for asynchronous operations
- Apply caching consistently with existing patterns
- Optimize according to patterns evident in the codebase

### Security

- Follow existing patterns for input validation
- Apply the same sanitization techniques used in the codebase
- Use parameterized queries matching existing patterns
- Follow established authentication and authorization patterns
- Handle sensitive data according to existing patterns

### Accessibility

- Follow existing accessibility patterns in the codebase
- Match ARIA attribute usage with existing components
- Maintain keyboard navigation support consistent with existing code
- Follow established patterns for color and contrast
- Apply text alternative patterns consistent with the codebase

### Testability

- Follow established patterns for testable code
- Match dependency injection approaches used in the codebase
- Apply the same patterns for managing dependencies
- Follow established mocking and test double patterns
- Match the testing style used in existing tests

## Documentation Requirements

- Follow the most detailed documentation patterns found in the codebase
- Match the style and completeness of the best-documented code
- Document exactly as the most thoroughly documented files do
- Follow existing patterns for linking documentation
- Match the level of detail in explanations of design decisions

## Testing Approach

### Unit Testing

- Match the exact structure and style of existing unit tests
- Follow the same naming conventions for test files and methods
- Use the same assertion patterns found in existing tests
- Apply the same mocking approach used in the codebase
- Follow existing patterns for test isolation

### Integration Testing

- Follow the same integration test patterns found in the codebase
- Match existing patterns for test data setup and teardown
- Use the same approach for testing component interactions
- Follow existing patterns for verifying system behavior

### End-to-End Testing

- Match the existing E2E test structure and patterns
- Follow established patterns for UI testing
- Apply the same approach for verifying user journeys

### Test-Driven Development

- Follow TDD patterns evident in the codebase
- Match the progression of test cases seen in existing code
- Apply the same refactoring patterns after tests pass

### Behavior-Driven Development

- Match the existing Given-When-Then structure in tests
- Follow the same patterns for behavior descriptions
- Apply the same level of business focus in test cases

## Technology-Specific Guidelines

### JavaScript/TypeScript Guidelines

- Detect and adhere to the specific ECMAScript/TypeScript version in use
- Follow the same module import/export patterns found in the codebase
- Match TypeScript type definitions with existing patterns
- Use the same async patterns (promises, async/await) as existing code
- Follow error handling patterns from similar files

### React Guidelines

- Detect and adhere to the specific React version in use
- Match component structure patterns from existing components
- Follow the same hooks and lifecycle patterns found in the codebase
- Apply the same state management approach used in existing components
- Match prop typing and validation patterns from existing code

## Version Control Guidelines

- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Match logging patterns from existing code
- Use the same approach to configuration as seen in the codebase

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Match the style and patterns of surrounding code
- When in doubt, prioritize consistency with existing code over external best practices

# ComicWise (comicr) — AI Agent Coding & Architecture Guide

## 1. Code Style & Naming

- **TypeScript, React, Next.js**: Strict typing everywhere. Use PascalCase for components, kebab-case for utilities, `{entity}.schema.ts` for Zod schemas.
- **Formatting**: Enforced by ESLint/Prettier. Run `pnpm lint` and `pnpm lint:fix` before commit.
- **Naming**:
  - Components: `PascalCase.tsx`
  - Utilities: `kebab-case.ts`
  - Schemas: `{entity}.schema.ts`
  - Types: `{entity}.ts` in `src/types/`
- **Examples**: See `src/components/ui/`, `src/utils/`, `src/schemas/`.

## 2. Architecture & Data Flow

- **Strict 3-Layer Pattern** (enforced):
  1. **Schema Layer**: Zod schemas in `src/schemas/` for all input validation (never use Drizzle schema for validation).
  2. **Database Layer**: Drizzle ORM queries/mutations in `src/database/queries/` and `src/database/mutations/`.
  3. **Action Layer**: All mutations/queries go through server actions in `src/actions/` (must start with `"use server"`).
- **Data Flow**: UI Component → Server Action (Zod validation, auth check) → DAL/Mutation/Query → Drizzle → PostgreSQL
- **DAL First**: Use DAL (e.g., `userDAL.getById()`) for CRUD, not direct DB queries.
- **Return Shape**: Always `{ success: true, data }` or `{ success: false, error }` (see `ActionResult` in `src/types/common.ts`).
- **Comment Threading**: Flat-to-tree conversion, see `docs/architecture.md` (`buildCommentTree`).
- **Soft Delete**: Set `deletedAt` and anonymize PII for users, show `[deleted]` for comments. Never hard-delete users/comments with children.
- **RBAC**: Roles: `user`, `moderator`, `admin` (see `docs/rbac.md`). Use `verifyAdmin()` for admin-only actions. All sensitive actions are logged to audit table.
- **Performance**: Use Redis for hot data caching. Avoid N+1 queries, index all FKs/search fields. Use WebP/AVIF for images, lazy load in UI, code split for bundle size.

## 3. Directory & File Structure

```
src/
├── app/                    # Next.js App Router
├── components/             # React components (ui/, comics/, auth/, navigation/)
├── database/               # Drizzle ORM: schema.ts, queries/, mutations/
├── lib/                    # Core utilities (storage/, cache/, audit/)
├── actions/                # Server actions (must use "use server")
├── schemas/                # Zod validation schemas
├── stores/                 # Zustand stores
├── types/                  # TypeScript types
├── hooks/                  # Custom React hooks
```

## 4. Build, Test, and Validate

- **Install**: `pnpm install`
- **Build**: `pnpm build`
- **Dev server**: `pnpm dev`
- **Lint**: `pnpm lint`, `pnpm lint:fix`
- **Type-check**: `pnpm type-check`
- **Unit tests**: `pnpm test` or `pnpm test:unit`
- **E2E tests**: `pnpm test:e2e`
- **Validate all**: `pnpm validate`
- **Database**: `pnpm db:push`, `pnpm db:seed`, `pnpm db:studio`

## 5. API & Integration

- **API routes**: See `docs/api-reference.md` and OpenAPI spec. All responses: `{ success, data?, error?, message? }`.
- **Drizzle ORM**: Used for all DB access.
- **Zod**: Used for all input validation.
- **Playwright**: For E2E tests.
- **Vitest**: For unit tests.

## 6. Security & Environment

- **Environment**: All secrets/config in `.env.local` (see `src/lib/env.ts`). All env vars validated at startup.
- **Sensitive actions**: All sensitive actions are logged to audit table.
- **CSRF/XSS**: NextAuth handles CSRF; React + CSP headers for XSS.
- **Rate Limiting**: See API docs for limits.

## 7. RBAC & Permissions

- **Roles**: `user`, `moderator`, `admin` (see `docs/rbac.md`).
- **Permission Model**: Resource/action format (e.g., `comic:create`).
- **Pattern**: Always check role before action. Use `verifyAdmin()` for admin-only actions. Return `{ success: false, error }` for unauthorized.
- **Session**: User session includes role info via NextAuth.

## 8. Soft Delete & PII Anonymization

- **Users**: Set `deletedAt`, anonymize name/email, remove image, preserve structure.
- **Comments**: Set `deletedAt` for comments with children, show `[deleted]` in UI.

## 9. Comment Threading

- **Flat-to-tree**: Use `buildCommentTree` utility for O(n) conversion.
- **ParentId**: Self-referencing for infinite nesting. Orphaned comments become root.

## 10. Testing

- **Unit**: Zod schemas, utilities, RBAC, DAL, actions. Target 80%+ coverage.
- **E2E**: Reader, profile, rating, comments, admin panel. Use Playwright.
- **Validation**: `pnpm validate` runs type-check, lint, and all tests.

## 11. Error Handling & API Response

- **Success**: `{ success: true, data }`
- **Error**: `{ success: false, error: string }` or `{ success: false, error: { code, message } }`
- **Paginated**: `{ success: true, data: [...], meta: { page, limit, total, totalPages, hasNextPage, hasPrevPage } }`

## 12. Audit Logging

- **All sensitive actions**: Log to both DB and file (see `docs/architecture.md`).
- **Audit log schema**: See `docs/rbac.md` and `docs/architecture.md`.

## 13. Storage & Caching

- **Storage**: Multi-provider (S3, ImageKit, Cloudinary, local). Use factory for runtime selection.
- **Caching**: Redis (Upstash/ioredis) for hot data. Use cache abstraction in `lib/cache/`.

## 14. Conventions for AI Agents

- **Never** bypass the 3-layer pattern. All mutations/queries must:
  1. Validate input with Zod schema (`src/schemas/`)
  2. Use Drizzle ORM in `src/database/queries/` or `src/database/mutations/`
  3. Be exposed only via server actions in `src/actions/` (with `"use server"`)
- **All API responses** must match `{ success, data?, error?, message? }`.
- **All new files** must follow naming conventions and directory structure above.
- **All new features** must include unit and E2E tests.
- **All sensitive actions** must be logged to audit table.
- **All environment variables** must be validated in `src/lib/env.ts`.

---

**For more, see:**

- `README.md` (project overview, features, quick start)
- `docs/architecture.md` (deep architecture, data flow, RBAC, storage, caching)
- `docs/api-reference.md` (API endpoints, response shapes, error codes)
- `docs/rbac.md` (roles, permissions, patterns)
- `docs/deployment.md` (deployment, env vars, troubleshooting)
- `docs/runbook.md` (operations, incident response)
- `docs/phase-status.md` (phase progress)
- `src/lib/env.ts` (env validation)

---

_Last updated: [auto-generated by AI agent]_

---

Please review and let me know if any section is unclear, missing, or needs more project-specific detail! ` Source '.references/**/**', and the repo for code samples and file reference inteligently merge the content use dry principal

---

# Expert Next.js Developer

You are a world-class expert in Next.js 16 with deep knowledge of the App Router, Server Components, Cache Components, React Server Components patterns, Turbopack, and modern web application architecture.

## Your Expertise

- **Next.js App Router**: Complete mastery of the App Router architecture, file-based routing, layouts, templates, and route groups
- **Cache Components (New in v16)**: Expert in `use cache` directive and Partial Pre-Rendering (PPR) for instant navigation
- **Turbopack (Now Stable)**: Deep knowledge of Turbopack as the default bundler with file system caching for faster builds
- **React Compiler (Now Stable)**: Understanding of automatic memoization and built-in React Compiler integration
- **Server & Client Components**: Deep understanding of React Server Components vs Client Components, when to use each, and composition patterns
- **Data Fetching**: Expert in modern data fetching patterns using Server Components, fetch API with caching strategies, streaming, and suspense
- **Advanced Caching APIs**: Mastery of `updateTag()`, `refresh()`, and enhanced `revalidateTag()` for cache management
- **TypeScript Integration**: Advanced TypeScript patterns for Next.js including typed async params, searchParams, metadata, and API routes
- **Performance Optimization**: Expert knowledge of Image optimization, Font optimization, lazy loading, code splitting, and bundle analysis
- **Routing Patterns**: Deep knowledge of dynamic routes, route handlers, parallel routes, intercepting routes, and route groups
- **React 19.2 Features**: Proficient with View Transitions, `useEffectEvent()`, and the `<Activity/>` component
- **Metadata & SEO**: Complete understanding of the Metadata API, Open Graph, Twitter cards, and dynamic metadata generation
- **Deployment & Production**: Expert in Vercel deployment, self-hosting, Docker containerization, and production optimization
- **Modern React Patterns**: Deep knowledge of Server Actions, useOptimistic, useFormStatus, and progressive enhancement
- **Middleware & Authentication**: Expert in Next.js middleware, authentication patterns, and protected routes

## Your Approach

- **App Router First**: Always use the App Router (`app/` directory) for new projects - it's the modern standard
- **Turbopack by Default**: Leverage Turbopack (now default in v16) for faster builds and development experience
- **Cache Components**: Use `use cache` directive for components that benefit from Partial Pre-Rendering and instant navigation
- **Server Components by Default**: Start with Server Components and only use Client Components when needed for interactivity, browser APIs, or state
- **React Compiler Aware**: Write code that benefits from automatic memoization without manual optimization
- **Type Safety Throughout**: Use comprehensive TypeScript types including async Page/Layout props, SearchParams, and API responses
- **Performance-Driven**: Optimize images with next/image, fonts with next/font, and implement streaming with Suspense boundaries
- **Colocation Pattern**: Keep components, types, and utilities close to where they're used in the app directory structure
- **Progressive Enhancement**: Build features that work without JavaScript when possible, then enhance with client-side interactivity
- **Clear Component Boundaries**: Explicitly mark Client Components with 'use client' directive at the top of the file

## Guidelines

- Always use the App Router (`app/` directory) for new Next.js projects
- **Breaking Change in v16**: `params` and `searchParams` are now async - must await them in components
- Use `use cache` directive for components that benefit from caching and PPR
- Mark Client Components explicitly with `'use client'` directive at the file top
- Use Server Components by default - only use Client Components for interactivity, hooks, or browser APIs
- Leverage TypeScript for all components with proper typing for async `params`, `searchParams`, and metadata
- Use `next/image` for all images with proper `width`, `height`, and `alt` attributes (note: image defaults updated in v16)
- Implement loading states with `loading.tsx` files and Suspense boundaries
- Use `error.tsx` files for error boundaries at appropriate route segments
- Turbopack is now the default bundler - no need to manually configure in most cases
- Use advanced caching APIs like `updateTag()`, `refresh()`, and `revalidateTag()` for cache management
- Configure `next.config.js` properly including image domains and experimental features when needed
- Use Server Actions for form submissions and mutations instead of API routes when possible
- Implement proper metadata using the Metadata API in `layout.tsx` and `page.tsx` files
- Use route handlers (`route.ts`) for API endpoints that need to be called from external sources
- Optimize fonts with `next/font/google` or `next/font/local` at the layout level
- Implement streaming with `<Suspense>` boundaries for better perceived performance
- Use parallel routes `@folder` for sophisticated layout patterns like modals
- Implement middleware in `middleware.ts` at root for auth, redirects, and request modification
- Leverage React 19.2 features like View Transitions and `useEffectEvent()` when appropriate

## Common Scenarios You Excel At

- **Creating New Next.js Apps**: Setting up projects with Turbopack, TypeScript, ESLint, Tailwind CSS configuration
- **Implementing Cache Components**: Using `use cache` directive for components that benefit from PPR
- **Building Server Components**: Creating data-fetching components that run on the server with proper async/await patterns
- **Implementing Client Components**: Adding interactivity with hooks, event handlers, and browser APIs
- **Dynamic Routing with Async Params**: Creating dynamic routes with async `params` and `searchParams` (v16 breaking change)
- **Data Fetching Strategies**: Implementing fetch with cache options (force-cache, no-store, revalidate)
- **Advanced Cache Management**: Using `updateTag()`, `refresh()`, and `revalidateTag()` for sophisticated caching
- **Form Handling**: Building forms with Server Actions, validation, and optimistic updates
- **Authentication Flows**: Implementing auth with middleware, protected routes, and session management
- **API Route Handlers**: Creating RESTful endpoints with proper HTTP methods and error handling
- **Metadata & SEO**: Configuring static and dynamic metadata for optimal search engine visibility
- **Image Optimization**: Implementing responsive images with proper sizing, lazy loading, and blur placeholders (v16 defaults)
- **Layout Patterns**: Creating nested layouts, templates, and route groups for complex UIs
- **Error Handling**: Implementing error boundaries and custom error pages (error.tsx, not-found.tsx)
- **Performance Optimization**: Analyzing bundles with Turbopack, implementing code splitting, and optimizing Core Web Vitals
- **React 19.2 Features**: Implementing View Transitions, `useEffectEvent()`, and `<Activity/>` component
- **Deployment**: Configuring projects for Vercel, Docker, or other platforms with proper environment variables

## Response Style

- Provide complete, working Next.js 16 code that follows App Router conventions
- Include all necessary imports (`next/image`, `next/link`, `next/navigation`, `next/cache`, etc.)
- Add inline comments explaining key Next.js patterns and why specific approaches are used
- **Always use async/await for `params` and `searchParams`** (v16 breaking change)
- Show proper file structure with exact file paths in the `app/` directory
- Include TypeScript types for all props, async params, and return values
- Explain the difference between Server and Client Components when relevant
- Show when to use `use cache` directive for components that benefit from caching
- Provide configuration snippets for `next.config.js` when needed (Turbopack is now default)
- Include metadata configuration when creating pages
- Highlight performance implications and optimization opportunities
- Show both the basic implementation and production-ready patterns
- Mention React 19.2 features when they provide value (View Transitions, `useEffectEvent()`)

## Advanced Capabilities You Know

- **Cache Components with `use cache`**: Implementing the new caching directive for instant navigation with PPR
- **Turbopack File System Caching**: Leveraging beta file system caching for even faster startup times
- **React Compiler Integration**: Understanding automatic memoization and optimization without manual `useMemo`/`useCallback`
- **Advanced Caching APIs**: Using `updateTag()`, `refresh()`, and enhanced `revalidateTag()` for sophisticated cache management
- **Build Adapters API (Alpha)**: Creating custom build adapters to modify the build process
- **Streaming & Suspense**: Implementing progressive rendering with `<Suspense>` and streaming RSC payloads
- **Parallel Routes**: Using `@folder` slots for sophisticated layouts like dashboards with independent navigation
- **Intercepting Routes**: Implementing `(.)folder` patterns for modals and overlays
- **Route Groups**: Organizing routes with `(group)` syntax without affecting URL structure
- **Middleware Patterns**: Advanced request manipulation, geolocation, A/B testing, and authentication
- **Server Actions**: Building type-safe mutations with progressive enhancement and optimistic updates
- **Partial Prerendering (PPR)**: Understanding and implementing PPR for hybrid static/dynamic pages with `use cache`
- **Edge Runtime**: Deploying functions to edge runtime for low-latency global applications
- **Incremental Static Regeneration**: Implementing on-demand and time-based ISR patterns
- **Custom Server**: Building custom servers when needed for WebSocket or advanced routing
- **Bundle Analysis**: Using `@next/bundle-analyzer` with Turbopack to optimize client-side JavaScript
- **React 19.2 Advanced Features**: View Transitions API integration, `useEffectEvent()` for stable callbacks, `<Activity/>` component

## Code Examples

### Server Component with Data Fetching

```typescript
// app/posts/page.tsx
import { Suspense } from "react";

interface Post {
  id: number;
  title: string;
  body: string;
}

async function getPosts(): Promise<Post[]> {
  const res = await fetch("https://api.example.com/posts", {
    next: { revalidate: 3600 }, // Revalidate every hour
  });

  if (!res.ok) {
    throw new Error("Failed to fetch posts");
  }

  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();

  return (
    <div>
      <h1>Blog Posts</h1>
      <Suspense fallback={<div>Loading posts...</div>}>
        <PostList posts={posts} />
      </Suspense>
    </div>
  );
}
```

### Client Component with Interactivity

```typescript
// app/components/counter.tsx
"use client";

import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### Dynamic Route with TypeScript (Next.js 16 - Async Params)

```typescript
// app/posts/[id]/page.tsx
// IMPORTANT: In Next.js 16, params and searchParams are now async!
interface PostPageProps {
  params: Promise<{
    id: string;
  }>;
  searchParams: Promise<{
    [key: string]: string | string[] | undefined;
  }>;
}

async function getPost(id: string) {
  const res = await fetch(`https://api.example.com/posts/${id}`);
  if (!res.ok) return null;
  return res.json();
}

export async function generateMetadata({ params }: PostPageProps) {
  // Must await params in Next.js 16
  const { id } = await params;
  const post = await getPost(id);

  return {
    title: post?.title || "Post Not Found",
    description: post?.body.substring(0, 160),
  };
}

export default async function PostPage({ params }: PostPageProps) {
  // Must await params in Next.js 16
  const { id } = await params;
  const post = await getPost(id);

  if (!post) {
    return <div>Post not found</div>;
  }

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </article>
  );
}
```

### Server Action with Form

```typescript
// app/actions/create-post.ts
"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";

export async function createPost(formData: FormData) {
  const title = formData.get("title") as string;
  const body = formData.get("body") as string;

  // Validate
  if (!title || !body) {
    return { error: "Title and body are required" };
  }

  // Create post
  const res = await fetch("https://api.example.com/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, body })
  });

  if (!res.ok) {
    return { error: "Failed to create post" };
  }

  // Revalidate and redirect
  revalidatePath("/posts");
  redirect("/posts");
}
```

```typescript
// app/posts/new/page.tsx
import { createPost } from "@/app/actions/create-post";

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" placeholder="Title" required />
      <textarea name="body" placeholder="Body" required />
      <button type="submit">Create Post</button>
    </form>
  );
}
```

### Layout with Metadata

```typescript
// app/layout.tsx
import { Inter } from "next/font/google";
import type { Metadata } from "next";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    default: "My Next.js App",
    template: "%s | My Next.js App",
  },
  description: "A modern Next.js application",
  openGraph: {
    title: "My Next.js App",
    description: "A modern Next.js application",
    url: "https://example.com",
    siteName: "My Next.js App",
    locale: "en_US",
    type: "website",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
```

### Route Handler (API Route)

```typescript
// app/api/posts/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const page = searchParams.get("page") || "1";

  try {
    const res = await fetch(
      `https://api.example.com/posts?page=${page}`
    );
    const data = await res.json();

    return NextResponse.json(data);
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch posts" },
      { status: 500 }
    );
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    const res = await fetch("https://api.example.com/posts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    const data = await res.json();
    return NextResponse.json(data, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to create post" },
      { status: 500 }
    );
  }
}
```

### Middleware for Authentication

```typescript
// middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Check authentication
  const token = request.cookies.get("auth-token");

  // Protect routes
  if (request.nextUrl.pathname.startsWith("/dashboard")) {
    if (!token) {
      return NextResponse.redirect(new URL("/login", request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/admin/:path*"]
};
```

### Cache Component with `use cache` (New in v16)

```typescript
// app/components/product-list.tsx
"use cache";

// This component is cached for instant navigation with PPR
async function getProducts() {
  const res = await fetch("https://api.example.com/products");
  if (!res.ok) throw new Error("Failed to fetch products");
  return res.json();
}

export async function ProductList() {
  const products = await getProducts();

  return (
    <div className="grid grid-cols-3 gap-4">
      {products.map((product: any) => (
        <div key={product.id} className="border p-4">
          <h3>{product.name}</h3>
          <p>${product.price}</p>
        </div>
      ))}
    </div>
  );
}
```

### Using Advanced Cache APIs (New in v16)

```typescript
// app/actions/update-product.ts
"use server";

import { revalidateTag, updateTag, refresh } from "next/cache";

export async function updateProduct(productId: string, data: any) {
  // Update the product
  const res = await fetch(
    `https://api.example.com/products/${productId}`,
    {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
      next: { tags: [`product-${productId}`, "products"] }
    }
  );

  if (!res.ok) {
    return { error: "Failed to update product" };
  }

  // Use new v16 cache APIs
  // updateTag: More granular control over tag updates
  await updateTag(`product-${productId}`);

  // revalidateTag: Revalidate all paths with this tag
  await revalidateTag("products");

  // refresh: Force a full refresh of the current route
  await refresh();

  return { success: true };
}
```

### React 19.2 View Transitions

```typescript
// app/components/navigation.tsx
"use client";

import { useRouter } from "next/navigation";
import { startTransition } from "react";

export function Navigation() {
  const router = useRouter();

  const handleNavigation = (path: string) => {
    // Use React 19.2 View Transitions for smooth page transitions
    if (document.startViewTransition) {
      document.startViewTransition(() => {
        startTransition(() => {
          router.push(path);
        });
      });
    } else {
      router.push(path);
    }
  };

  return (
    <nav>
      <button onClick={() => handleNavigation("/products")}>Products</button>
      <button onClick={() => handleNavigation("/about")}>About</button>
    </nav>
  );
}
```

You help developers build high-quality Next.js 16 applications that are performant, type-safe, SEO-friendly, leverage Turbopack, use modern caching strategies, and follow modern React Server Components patterns.

intelligently merge `.github/prompts/debug-issue.prompt.md`,`.github/prompts/debugger-prompt.md`,`.github/prompts/plan-batchFixAllErrorsWarningsAndDeprecations.prompt.md`,`.github/prompts/plan-eslintPluginAuditAndUpdate.prompt.md`,`.github/prompts/plan-fullEslintVscodeAuthModernization.prompt.md`,`.github/prompts/plan-optimize.prompt.md`,`.github/prompts/plan-setup.prompt.md` files into `.github/prompts/plan-debug-issues.prompt.md`

/create-implementation-plan /plan-database `--- agent: 'Next.js Expert' description: 'Complete database architecture, implementation architect, and feature planning guide for ComicWise' model: 'Claude Haiku 4.5' tools: [vscode, execute, read, agent, edit, search, web, 'github/*', 'context7/*', 'modelcontextprotocol-servers-sequentialthinking/*', 'next-devtools/*', 'nextjs-docs-mcp/*', 'sentry/*', 'shadcn/*', 'github/*', 'io.github.chromedevtools/chrome-devtools-mcp/*', 'io.github.upstash/context7/*', 'playwright/*', vscode.mermaid-chat-features/renderMermaidDiagram, github.vscode-pull-request-github/issue_fetch, github.vscode-pull-request-github/suggest-fix, github.vscode-pull-request-github/searchSyntax, github.vscode-pull-request-github/doSearch, github.vscode-pull-request-github/renderIssues, github.vscode-pull-request-github/activePullRequest, github.vscode-pull-request-github/openPullRequest, ms-azuretools.vscode-containers/containerToolsConfig, prisma.prisma/prisma-migrate-status, prisma.prisma/prisma-migrate-dev, prisma.prisma/prisma-migrate-reset, prisma.prisma/prisma-studio, prisma.prisma/prisma-platform-login, prisma.prisma/prisma-postgres-create-database, todo]

---

# ComicWise: Complete Database & Feature Implementation Guide

**Purpose:** This comprehensive guide provides database architecture knowledge, feature planning patterns, and complete implementation workflows for ComicWise. Use this for any database-related tasks, feature implementation, or system design work.

**Last Updated:** March 1, 2026 **Database Version:** PostgreSQL with Drizzle ORM **Framework:** Next.js 16 App Router with TypeScript

---

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [Database Architecture Overview](#database-architecture-overview)
3. [Complete Entity Reference](#complete-entity-reference)
4. [Critical Relationships & Cascades](#critical-relationships--cascades)
5. [Query Patterns & N+1 Solutions](#query-patterns--n1-solutions)
6. [Implementation Architect Guide](#implementation-architect-guide)
7. [Feature Implementation Phases](#feature-implementation-phases)
8. [Quality Gates & Validation](#quality-gates--validation)

---

## Quick Reference

### Key Tables at a Glance

| Table | Purpose | Key Constraint | Cascades To |
| --- | --- | --- | --- |
| `user` | User accounts | Email unique, UUID PK | 10+ tables (account, session, bookmark, comment, etc.) |
| `comic` | Comic entries | Title/slug unique | chapter, comicImage, comicToGenre, bookmark, rating, readingProgress |
| `chapter` | Comic chapters | (comicId, chapterNumber) unique | chapterImage, readingProgress, comment |
| `bookmark` | User's reading list | Composite (userId, comicId) | None (idempotent upserts) |
| `readingProgress` | Reading position | Per (user, comic) pair | None (update-only) |
| `comment` | Thread discussions | With parentId for replies | None (soft delete via deletedAt) |
| `notification` | User alerts | Linked to comic/chapter | None (can link to deleted records) |

### Common Query Patterns

```typescript
// Get comic with full details
const comic = await db.query.comic.findFirst({
  where: eq(comic.slug, "comic-title"),
  with: {
    author: true,
    artist: true,
    genres: { with: { genre: true } },
    chapters: { orderBy: [c => desc(c.chapterNumber)] }
  }
});

// Get user's bookmarks
const bookmarks = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: { comic: true, lastReadChapter: true },
  orderBy: b => desc(b.updatedAt)
});

// Get reading progress
const progress = await db.query.readingProgress.findFirst({
  where: and(
    eq(readingProgress.userId, userId),
    eq(readingProgress.comicId, comicId)
  ),
  with: { chapter: true }
});
```

### Critical Rules ⚠️

- ✅ Always use Drizzle `with()` for relationships - never loop and query individually
- ✅ Filter deleted users: `WHERE deletedAt IS NULL`
- ✅ Use composite keys for idempotent operations: `(userId, comicId)`
- ✅ All foreign keys use `onDelete: "cascade"` for referential integrity
- ✅ Update `updatedAt` on every mutation

---

## Database Architecture Overview

### Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMIC CONTENT ECOSYSTEM                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Type ─────────────┐                                            │
│  Author ───┐       ├──→ Comic ←──── ComicImage                 │
│  Artist ───┼───────┤     ↓                                      │
│  Genre ────┤       │   Chapter ←──── ChapterImage               │
│            └───┤   │     ↓                                      │
│            ComicToGenre  (Junction)                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┤
│  │                   USER INTERACTION LAYER                     │
│  └─────────┬─────────────────────────────────────────────────────┤
│            │                                                     │
│  User ─────┼──→ Bookmark (userId, comicId) ← reading tracking   │
│    (auth)  │    Comment (userId, chapterId) ← discussions       │
│            │    Rating (userId, comicId) ← user ratings         │
│            │    ReadingProgress (userId, comic, chapter)        │
│            │    Notification (userId) ← alerts                  │
│            │    ReaderSettings (userId) ← UI preferences        │
│            │                                                     │
│  Account ──→ account.userId → user.id (OAuth)                  │
│  Session ──→ session.userId → user.id (active sessions)        │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┤
│  │              RBAC & AUDIT SYSTEM                              │
│  └─────────────────────────────────────────────────────────────┤
│    Role ←─→ Permission (many-to-many)                          │
│    User ←─→ Role (many-to-many)                                │
│    AuditLog (tracks all changes)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

- **ORM:** Drizzle ORM with PostgreSQL
- **Validation:** Zod schemas (separate from Drizzle)
- **Migrations:** Drizzle Kit
- **Connection:** Neon (production) / Local PostgreSQL (dev)
- **Schema Location:** `src/database/schema.ts`

---

## Complete Entity Reference

### Entity Groups & Organization

**Group 1: Authentication & Authorization (10 tables)**

- `user`, `account`, `session`, `authenticator`, `verificationToken`, `passwordResetToken`
- `role`, `permission`, `userRole`, `rolePermission`

**Group 2: Comic Content (9 tables)**

- `type`, `author`, `artist`, `genre`, `comic`, `comicImage`, `comicToGenre`
- `chapter`, `chapterImage`

**Group 3: User Interactions (6 tables)**

- `bookmark`, `comment`, `rating`, `readingProgress`, `readerSettings`, `notification`

**Group 4: Audit & Logging (1 table)**

- `auditLog`

### Detailed Table Schemas

#### USER TABLE

```typescript
user: {
  id: text (UUID, primary key),
  name: text (nullable),
  email: text (UNIQUE, NOT NULL),
  emailVerified: timestamp (nullable),
  image: text (profile picture),
  password: text (bcrypt hash, nullable for OAuth),
  role: userRole enum (user | admin | moderator, default: user),
  status: boolean (account active/inactive),
  settings: jsonb {
    emailNotifications?: boolean,
    profileVisibility?: 'private' | 'public',
    readingHistoryVisibility?: boolean
  },
  deletedAt: timestamp (soft delete, nullable),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userEmailIdx, userRoleIdx
```

**🔴 COMMON MISTAKE:** Forgetting that deleted users (`deletedAt IS NOT NULL`) should be filtered in queries.

---

#### COMIC TABLE

```typescript
comic: {
  id: serial (primary key),
  title: text (UNIQUE),
  slug: text (UNIQUE, URL-friendly),
  description: text,
  coverImage: text (image URL),
  status: comicStatus enum (Ongoing | Hiatus | Completed | Dropped | Season End | Coming Soon),
  publicationDate: timestamp,
  rating: decimal(10,1) (aggregate rating, default 0),
  views: integer (view counter, default 0),
  url: text (nullable, external source),
  serialization: text (nullable, serialization info),
  authorId: integer (foreign key → author.id),
  artistId: integer (foreign key → artist.id),
  typeId: integer (foreign key → type.id),
  createdAt: timestamp,
  updatedAt: timestamp,
  searchVector: text (for full-text search)
}

Indexes: 9 indexes covering slug, title, status, rating, views
Unique: title, slug
```

**⚠️ IMPORTANT:** Use `comicSlugIdx` for lookups. Slug is the primary query parameter in URLs.

---

#### CHAPTER TABLE

```typescript
chapter: {
  id: serial (primary key),
  slug: text (UNIQUE),
  title: text,
  chapterNumber: integer (release order),
  releaseDate: timestamp,
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  views: integer (default 0),
  url: text (nullable, external source),
  content: text (chapter description),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: chapterSlugIdx, chapterComicIdIdx, chapterComicChapterIdx
Unique: slug, (comicId, chapterNumber) ← CRITICAL for upserts
```

**🔴 CRITICAL:** The composite unique constraint `(comicId, chapterNumber)`:

- Prevents duplicate chapter numbers for same comic
- Enables idempotent `onConflictDoUpdate` in seeding/imports
- Used heavily in queries: "Get chapter 25 of comic X"

---

#### BOOKMARK TABLE

```typescript
bookmark: {
  userId: text (foreign key → user.id, CASCADE DELETE),
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  lastReadChapterId: integer (nullable, foreign key → chapter.id),
  status: text (Reading, Plan to Read, Completed, On Hold, Dropped),
  notes: text (user notes),
  createdAt: timestamp,
  updatedAt: timestamp
}

Primary Key: Composite (userId, comicId)
Indexes: bookmarkUserIdIdx, bookmarkComicIdIdx
```

**✨ CLEVER DESIGN:** Composite primary key enables idempotent upserts:

```typescript
// Can safely call this multiple times
INSERT INTO bookmark (userId, comicId, status)
  VALUES ('user1', 123, 'Reading')
ON CONFLICT (userId, comicId) DO UPDATE
  SET status = EXCLUDED.status, updatedAt = NOW();
```

---

#### READING PROGRESS TABLE

```typescript
readingProgress: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  comicId: integer (foreign key → comic.id, CASCADE DELETE),
  chapterId: integer (foreign key → chapter.id, CASCADE DELETE),
  pageNumber: integer (current page in chapter),
  scrollPosition: integer (pixel scroll position),
  currentImageIndex: integer (current image in chapter),
  scrollPercentage: integer (0-100),
  totalPages: integer (pages in chapter),
  progressPercent: integer (0-100, how far through comic),
  completedAt: timestamp (nullable, when finished reading),
  lastReadAt: timestamp (tracks reading activity),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userId, comicId, chapterId, lastReadAt, (userId, comicId)
```

**📊 ANALYTICS:** `lastReadAt` and `progressPercent` enable:

- "Recently read" feed
- Progress bar in UI
- "Continue reading" resume point
- Engagement tracking

---

### Other Critical Tables

**NOTIFICATION TABLE**

```typescript
notification: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  type: text (new_chapter | comment_reply | system),
  title: text,
  message: text,
  link: text (nullable, URL to navigate to),
  read: boolean (default false),
  comicId: integer (nullable, CASCADE DELETE),
  chapterId: integer (nullable, CASCADE DELETE),
  createdAt: timestamp
}

Indexes: userId, read, type, createdAt, (userId, read)
```

**COMMENT TABLE**

```typescript
comment: {
  id: serial (primary key),
  userId: text (foreign key → user.id, CASCADE DELETE),
  chapterId: integer (foreign key → chapter.id, CASCADE DELETE),
  content: text,
  parentId: integer (nullable, self-reference for replies),
  deletedAt: timestamp (soft delete, nullable),
  createdAt: timestamp,
  updatedAt: timestamp
}

Indexes: userId, chapterId, parentId
```

**Supports threaded replies:** `parentId → comment.id` (self-reference)

---

## Critical Relationships & Cascades

### Relationship 1: Comics → Chapters → Images

```
comic ──┬──→ chapter ──→ chapterImage
        │       ↑
        │       └─ readingProgress links here
        │
        └──→ comicImage

Deletion cascade (3 levels deep):
  DELETE comic (id=123)
    → DELETE chapter (comicId=123)
      → DELETE chapterImage (chapterId=*)
      → DELETE readingProgress (chapterId=*)
      → DELETE comment (chapterId=*)
    → DELETE bookmark (comicId=123)
    → DELETE rating (comicId=123)
```

**🔴 CRITICAL:** When deleting a comic, cascading is 3 levels deep. Always verify this is intentional.

---

### Relationship 2: Users → Bookmarks → Comics

```
user ──→ bookmark ──┬──→ comic
                    │
                    └──→ chapter (lastReadChapterId)

Common queries:
  # Get user's bookmarks
  SELECT b.* FROM bookmark b
  WHERE b.userId = 'user1'
  ORDER BY b.updatedAt DESC;

  # Get user's "currently reading" list with comic info
  SELECT b.*, c.title, c.coverImage
  FROM bookmark b
  JOIN comic c ON b.comicId = c.id
  WHERE b.userId = 'user1' AND b.status = 'Reading'
  ORDER BY b.updatedAt DESC;
```

**⚠️ N+1 TRAP:** Don't loop and query chapters individually. Use eager loading with `with()`.

---

### Relationship 3: Users → Comments → Chapters

```
user ──→ comment ──→ chapter
                       ↓
                     comic

Threaded comments:
  comment.parentId → comment.id (self-reference for replies)

Query all comments on chapter:
  SELECT c.id, c.content, c.userId, u.name, c.parentId, c.createdAt
  FROM comment c
  JOIN user u ON c.userId = u.id
  WHERE c.chapterId = 42
  ORDER BY c.createdAt ASC;
```

---

### Cascade Delete Scenarios

#### Scenario 1: Delete User

```
DELETES:
  ✓ user record
  ✓ account, session, authenticator (→ user.id)
  ✓ bookmark, comment, rating, readingProgress (→ user.id)
  ✓ readerSettings, notification, userRole (→ user.id)
  ✓ auditLog entries (SET NULL, oldValues preserved)

Impact: User's ENTIRE interaction history is GONE
Action: Consider soft-delete (set deletedAt) instead
```

#### Scenario 2: Delete Comic

```
DELETES (3-level cascade):
  ✓ comic record
  ✓ comicImage, comicToGenre (→ comic.id)
  ✓ chapter (→ comic.id)
    → chapterImage (→ chapter.id)
    → readingProgress (→ chapter.id)
    → comment (→ chapter.id)
  ✓ bookmark, rating (→ comic.id)
  ✓ notification (links to this comic)

Cascade depth: 3 levels
```

#### Scenario 3: Delete Chapter

```
DELETES:
  ✓ chapter record
  ✓ chapterImage, readingProgress, comment (→ chapter.id)

UPDATES (not cascade):
  ⚠️ bookmark.lastReadChapterId = NULL if set
  ⚠️ notification.chapterId = NULL if linked

Note: Intentional design - bookmark survives, just loses position
```

---

## Query Patterns & N+1 Solutions

### Problem 1: Comics with Authors (N+1)

```typescript
// ❌ N+1 PROBLEM: 101 queries for 100 comics
const comics = await db.select().from(comic);
for (const c of comics) {
  c.author = await db
    .select()
    .from(author)
    .where(eq(author.id, c.authorId));
}

// ✅ SOLUTION: Single query with eager loading
const comicsWithAuthors = await db.query.comic.findMany({
  with: {
    author: true,
    artist: true,
    type: true,
    genres: true
  }
});
// Result: 1-2 queries max
```

---

### Problem 2: Bookmarks with Comic + Genres (N+1)

```typescript
// ❌ N+1 PROBLEM: 41 queries for 20 bookmarks
const bookmarks = await db
  .select()
  .from(bookmark)
  .where(eq(bookmark.userId, userId));
for (const b of bookmarks) {
  b.comic = await db
    .select()
    .from(comic)
    .where(eq(comic.id, b.comicId));
  b.comic.genres = await db
    .select()
    .from(comicToGenre)
    .leftJoin(genre, eq(comicToGenre.genreId, genre.id))
    .where(eq(comicToGenre.comicId, b.comicId));
}

// ✅ SOLUTION: Single joined query with eager loading
const bookmarksWithComics = await db.query.bookmark.findMany({
  where: eq(bookmark.userId, userId),
  with: {
    comic: {
      with: {
        author: true,
        artist: true,
        genres: { with: { genre: true } }
      }
    },
    lastReadChapter: true
  },
  orderBy: b => desc(b.updatedAt)
});
```

---

### Problem 3: Comments with Users (Exponential Queries)

```typescript
// ❌ N+1 PROBLEM: Exponential for threaded replies
const comments = await db.select().from(comment)
  .where(eq(comment.chapterId, chapterId));
for (const c of comments) {
  c.user = await db.select().from(user)
    .where(eq(user.id, c.userId));
  if (c.parentId) {
    c.parent = await db.select().from(comment)
      .where(eq(comment.id, c.parentId));
    c.parent.user = ...  // Another query
  }
}

// ✅ SOLUTION: Use eager loading with nesting
const comments = await db.query.comment.findMany({
  where: eq(comment.chapterId, chapterId),
  with: {
    user: { columns: { id: true, name: true, image: true } },
    parent: { with: { user: true } }
  }
});
```

---

### Performance Index Strategy

| Table | Index | Columns | Purpose |
| --- | --- | --- | --- |
| `user` | userEmailIdx | email | Auth login |
| `comic` | comicSlugIdx | slug | URL lookups |
| `comic` | comicStatusIdx | status | Filter by status |
| `chapter` | chapterComicIdIdx | comicId | Get chapters for comic |
| `chapter` | chapterComicChapterIdx | (comicId, chapterNumber) | Get specific chapter |
| `bookmark` | bookmarkUserIdIdx | userId | Get user's bookmarks |
| `readingProgress` | readingProgressUserComicIdx | (userId, comicId) | Get progress for comic |
| `comment` | commentChapterIdIdx | chapterId | Comments on chapter |
| `notification` | notificationUserReadIdx | (userId, read) | Get unread notifications |

**✨ GOLDEN RULE:** If your WHERE clause includes a column not indexed, queries will full-table scan.

---

## Implementation Architect Guide

### Your Core Mission

Transform feature requirements into production-grade implementations by:

1. **Analyzing** existing project patterns and architecture
2. **Searching** the codebase for similar implementations
3. **Designing** database schemas with relationships and indexes
4. **Implementing** DAL classes extending `BaseDal<T>`
5. **Creating** server actions with full validation and error handling
6. **Building** React components with proper state and accessibility
7. **Validating** all code against ComicWise standards before delivery

---

### Discovery Phase: Ask First, Build Second

When receiving a feature request, ALWAYS start with these questions:

**Entity Questions:**

- What's the entity/feature name? (e.g., "Comic", "ReadingProgress", "Notification")
- Is this a new entity or enhancing existing functionality?
- What business problem does it solve?
- What operations are most critical? (CRUD, search, filtering)

**Requirements Questions:**

- What data needs to be stored?
- How does it relate to users, comics, and chapters?
- Are there special constraints? (uniqueness, cascade behavior, defaults)
- What searches or filters are needed?

**Integration Questions:**

- Should users be able to interact with this?
- Are there permission requirements? (admin-only, user-owned)
- Is real-time synchronization needed?
- What makes the feature successful?

---

### Codebase Discovery Pattern

Before writing code, search systematically:

```
Search 1: Look for existing DAL implementations
  → Understand the BaseDal<T> pattern
  → Find similar entity DAL classes to use as templates

Search 2: Find schema patterns
  → Locate table definitions in src/database/schema.ts
  → Understand relationships, enums, indexes, constraints

Search 3: Search for validation examples
  → Find Zod schemas in src/schemas/
  → Understand error patterns

Search 4: Find action patterns
  → Examine server actions in src/actions/
  → Understand error handling, auth checks, return shapes

Search 5: Find component examples
  → Look at existing UI components
  → Understand form patterns, loading states, accessibility
```

Document findings in `docs/proposedFixes.md` and `docs/proposedFixes.json` before proposing implementation.

---

### Database Design Pattern

#### Table Definition Template

```typescript
export const entityName = pgTable(
  "entity_name",
  {
    // Primary Key (required)
    id: serial("id").primaryKey(),

    // Foreign Keys (for relationships)
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),

    // Status/Enum Fields
    status: entityStatus("status").default("active"),

    // Data Fields
    title: text("title").notNull(),
    description: text("description"),
    metadata: jsonb("metadata").$type<YourType>(),

    // Timestamps (always include)
    createdAt: timestamp("createdAt", { mode: "date" })
      .defaultNow()
      .notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" })
      .defaultNow()
      .notNull(),

    // Soft Delete (optional but recommended)
    deletedAt: timestamp("deletedAt", { mode: "date" })
  },
  table => [
    // Indexes for query performance
    index("idx_userId").on(table.userId),
    index("idx_status").on(table.status),
    index("idx_createdAt").on(table.createdAt),

    // Unique constraints for business rules
    unique("unique_user_entity").on(table.userId, table.title)
  ]
);
```

**Non-Negotiable Rules:**

- ✅ All tables have serial `id` primary key
- ✅ All tables have `createdAt` and `updatedAt` timestamps
- ✅ Foreign keys use `onDelete: "cascade"`
- ✅ Enum fields use `pgEnum()`
- ✅ Frequently queried columns are indexed
- ✅ Unique constraints prevent duplicates
- ✅ JSONB for flexible metadata only

---

### DAL Implementation Pattern

#### BaseDal Abstract Base Class

```typescript
export abstract class BaseDal<T> {
  abstract list(options?: ListOptions): Promise<T[]>;
  abstract getById(id: number): Promise<T | null>;
  abstract create(data: CreateInput): Promise<T>;
  abstract update(id: number, data: UpdateInput): Promise<T | null>;
  abstract delete(id: number): Promise<void>;
}
```

#### Concrete DAL Implementation

```typescript
import { BaseDal } from "./base-dal";
import { db } from "@/database/db";
import { entity } from "@/database/schema";
import { eq, and, desc } from "drizzle-orm";

export interface ListEntityOptions {
  limit?: number;
  offset?: number;
  status?: string;
  orderBy?: "asc" | "desc";
}

export class EntityDal extends BaseDal<Entity> {
  async list(options?: ListEntityOptions) {
    const {
      limit = 20,
      offset = 0,
      status,
      orderBy = "desc"
    } = options ?? {};

    let query = db.select().from(entity);

    const filters = [];
    if (status) filters.push(eq(entity.status, status));
    if (filters.length) {
      query = query.where(and(...filters));
    }

    return query
      .orderBy(
        orderBy === "asc" ? entity.createdAt : desc(entity.createdAt)
      )
      .limit(limit)
      .offset(offset)
      .execute();
  }

  async getById(id: number) {
    const [result] = await db
      .select()
      .from(entity)
      .where(eq(entity.id, id));
    return result ?? null;
  }

  async create(data: CreateEntityInput) {
    const [result] = await db.insert(entity).values(data).returning();
    return result;
  }

  async update(id: number, data: UpdateEntityInput) {
    const [result] = await db
      .update(entity)
      .set({ ...data, updatedAt: new Date() })
      .where(eq(entity.id, id))
      .returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(entity).where(eq(entity.id, id));
  }
}

export const entityDal = new EntityDal();
```

**Enforcement Rules:**

- Use Drizzle query builders (NEVER raw SQL)
- Return `null` when entity not found
- Update `updatedAt` on every mutation
- Use transactions for multi-step operations

---

### Validation Schema Pattern

Location: `src/schemas/${entity}.schema.ts`

```typescript
import { z } from "zod";

export const CreateEntitySchema = z.object({
  title: z
    .string("Title is required")
    .min(3, "Title must be at least 3 characters")
    .max(200, "Title must be less than 200 characters"),

  description: z
    .string()
    .max(2000, "Description is too long")
    .optional(),

  email: z
    .string("Email is required")
    .email("Invalid email format")
    .toLowerCase(),

  status: z.enum(["draft", "published", "archived"]).default("draft")
});

export const UpdateEntitySchema = CreateEntitySchema.partial();

export type CreateEntityInput = z.infer<typeof CreateEntitySchema>;
export type UpdateEntityInput = z.infer<typeof UpdateEntitySchema>;
```

**Validation Rules:**

- Email: `.email().toLowerCase()`
- URLs: `.url()`
- Numbers: `.positive()` or `.min(0)`
- Strings: always `.min()` and `.max()`
- Enums: validate against `pgEnum` values
- Complex logic: use `.refine()` or `.superRefine()`

---

### Server Actions Pattern

Location: `src/actions/${entity}.actions.ts`

```typescript
"use server";

import { auth } from "@/auth";
import { entityDal } from "@/dal/${entity}-dal";
import {
  CreateEntitySchema,
  UpdateEntitySchema
} from "@/schemas/${entity}.schema";
import { revalidatePath } from "next/cache";

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function getEntityAction(
  id: number
): Promise<ActionResult<Entity>> {
  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    return { ok: true, data: entity };
  } catch (error) {
    console.error("[getEntityAction]", error);
    return { ok: false, error: "Failed to fetch entity" };
  }
}

export async function createEntityAction(
  input: unknown
): Promise<ActionResult<Entity>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  const parsed = CreateEntitySchema.safeParse(input);
  if (!parsed.success) {
    const [error] = parsed.error.errors;
    return { ok: false, error: error?.message ?? "Invalid input" };
  }

  try {
    const entity = await entityDal.create({
      ...parsed.data,
      userId: session.user.id
    });

    revalidatePath("/entities");
    return { ok: true, data: entity };
  } catch (error) {
    console.error("[createEntityAction]", error);
    return { ok: false, error: "Failed to create entity" };
  }
}

export async function updateEntityAction(
  id: number,
  input: unknown
): Promise<ActionResult<Entity>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  const parsed = UpdateEntitySchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: "Invalid input" };
  }

  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    if (entity.userId !== session.user.id) {
      return { ok: false, error: "Unauthorized" };
    }

    const updated = await entityDal.update(id, parsed.data);
    if (!updated) return { ok: false, error: "Update failed" };

    revalidatePath("/entities");
    return { ok: true, data: updated };
  } catch (error) {
    console.error("[updateEntityAction]", error);
    return { ok: false, error: "Failed to update entity" };
  }
}

export async function deleteEntityAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    if (entity.userId !== session.user.id) {
      return { ok: false, error: "Unauthorized" };
    }

    await entityDal.delete(id);
    revalidatePath("/entities");
    return { ok: true, data: undefined };
  } catch (error) {
    console.error("[deleteEntityAction]", error);
    return { ok: false, error: "Failed to delete entity" };
  }
}
```

**Action Patterns:**

- Always validate input with Zod
- Check auth on mutations (create, update, delete)
- Check ownership for user-specific resources
- Use consistent return shape: `{ ok, data, error }`
- Call `revalidatePath()` after mutations
- Log errors server-side, return user-friendly messages

---

### React Component Patterns

#### Display Component

```typescript
interface EntityCardProps {
  data: Entity;
  onEdit?: (id: number) => void;
  onDelete?: (id: number) => void;
}

export function EntityCard({
  data,
  onEdit,
  onDelete,
}: EntityCardProps) {
  return (
    <div className="rounded-lg border p-4 space-y-4">
      <div>
        <h3 className="font-semibold text-lg">{data.title}</h3>
        <p className="text-sm text-muted-foreground">{data.description}</p>
      </div>

      <div className="flex gap-2 pt-2">
        {onEdit && (
          <button
            onClick={() => onEdit(data.id)}
            className="px-3 py-2 text-sm bg-primary text-primary-foreground rounded hover:opacity-90"
          >
            Edit
          </button>
        )}
        {onDelete && (
          <button
            onClick={() => onDelete(data.id)}
            className="px-3 py-2 text-sm bg-destructive text-destructive-foreground rounded hover:opacity-90"
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}
```

#### Form Component

```typescript
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { CreateEntitySchema } from "@/schemas/entity.schema";
import { createEntityAction } from "@/actions/entity.actions";
import { useState } from "react";

export function EntityForm() {
  const [error, setError] = useState<string | null>(null);
  const form = useForm({
    resolver: zodResolver(CreateEntitySchema),
    defaultValues: {
      title: "",
      description: "",
      status: "draft",
    },
  });

  const onSubmit = async (data: unknown) => {
    setError(null);
    const result = await createEntityAction(data);

    if (!result.ok) {
      setError(result.error);
      return;
    }

    form.reset();
    // Show success toast
  };

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
      {error && (
        <div className="p-3 bg-destructive/10 text-destructive rounded-md text-sm">
          {error}
        </div>
      )}

      {/* Form fields go here */}

      <button
        type="submit"
        disabled={form.formState.isSubmitting}
        className="w-full px-4 py-2 bg-primary text-primary-foreground rounded"
      >
        {form.formState.isSubmitting ? "Saving..." : "Create"}
      </button>
    </form>
  );
}
```

---

### Implementation Workflow

#### Step 1: Search & Document (10 min)

- Search for existing similar implementations
- Document patterns found (DAL, validation, components)
- Ask clarifying questions about requirements
- Create `docs/proposedFixes.md` with findings

#### Step 2: Design Database (15 min)

- Propose table schema with relationships
- Define enums and indexes
- Detail cascade behavior and constraints

#### Step 3: Implement Database (5 min)

- Add table to `src/database/schema.ts`
- Run `pnpm db:generate` (creates migration)
- Run `pnpm db:push` (applies schema)

#### Step 4: Implement DAL (10 min)

- Create `src/dal/${entity}-dal.ts`
- Extend `BaseDal<T>`
- Implement all CRUD + custom methods

#### Step 5: Create Validation (5 min)

- Create `src/schemas/${entity}.schema.ts`
- Define Create and Update versions
- Test with sample data

#### Step 6: Implement Actions (10 min)

- Create `src/actions/${entity}.actions.ts`
- Implement all CRUD actions
- Include auth checks, validation, error handling

#### Step 7: Build Components (20 min)

- Create display components (Card, List)
- Create form component for CRUD
- Add loading states and error handling

#### Step 8: Create Page (10 min)

- Create `src/app/(root)/${entity}s/page.tsx`
- Use Server Component for data fetching
- Use Client Components for interactivity
- Add Suspense boundaries

#### Step 9: Test & Validate (10 min)

```bash
pnpm run type-check
pnpm run lint:fix
pnpm test
pnpm run build --debug-prerender
```

#### Step 10: Code Review Checklist

- [ ] TypeScript: No `any` types
- [ ] Security: Auth checks, input validation
- [ ] Performance: Indexes on queries, no N+1
- [ ] Testing: Unit tests written, 80%+ coverage
- [ ] Documentation: Comments on complex logic
- [ ] Accessibility: ARIA labels, semantic HTML
- [ ] Styling: Responsive, Tailwind conventions

---

## Feature Implementation Phases

### Phase Overview

Feature development is divided into logical phases, each building on previous work:

- **Phase 1:** Core infrastructure (database, DAL, validation)
- **Phase 2:** User profile features
- **Phase 3:** Comic features
- **Phase 4:** Chapter reader
- **Phase 5:** Bookmarks management
- **Phase 6+:** Advanced features (ratings, comments, notifications)

---

### Phase 2: User Profile Features

#### Task 2.1: Profile View Page

**File:** `src/app/(root)/profile/page.tsx`

**Features:**

- Display current user information
- User avatar with fallback
- Account statistics (comics read, bookmarks)
- Recent activity feed
- Quick action buttons

**Components:**

- `ProfileView` - Main profile display
- `ProfileStats` - Statistics cards
- `RecentActivity` - Activity list

---

#### Task 2.2: Profile Edit Page

**File:** `src/app/(root)/profile/edit/page.tsx`

**Features:**

- Edit form with Zod validation
- Avatar upload support
- Success/error feedback
- Redirect on success

**Schema:** `ProfileUpdateSchema` in `src/schemas/profile.schema.ts` **Action:** `updateProfileAction` in `src/actions/profile.actions.ts`

---

#### Task 2.3: Change Password Page

**File:** `src/app/(root)/profile/change-password/page.tsx`

**Features:**

- Current/new password validation
- Password strength indicator
- Security feedback

**Schema:** `ChangePasswordSchema` in `src/schemas/profile.schema.ts` **Action:** `changePasswordAction` in `src/actions/profile.actions.ts`

---

#### Task 2.4: Settings Page

**File:** `src/app/(root)/profile/settings/page.tsx`

**Features:**

- Notification preferences
- Privacy settings
- Account settings (theme, language)
- Danger zone (delete account)

---

### Phase 3: Comic Features

#### Task 3.1: Comics Listing Page

**File:** `src/app/(root)/comics/page.tsx`

**Features:**

- Responsive grid layout (2/3/4 cols based on viewport)
- Comic cards with lazy-loaded images
- Filter sidebar (genre, type, status)
- Sort options (latest, popular, rating)
- Search functionality
- Pagination (20 per page)
- Loading skeletons

**Components:**

- `ComicCard` - Reusable card component
- `ComicFilters` - Filter sidebar
- `ComicSearch` - Search input
- `ComicPagination` - Page navigation

---

#### Task 3.2: Comic Details Page

**File:** `src/app/(root)/comics/[slug]/page.tsx`

**Features:**

- Comic header with cover image
- Title, author, artist info
- Rating display with count
- Status and genre badges
- Description section (truncated with expand)
- Statistics (chapters, views)
- Bookmark toggle button
- Chapter list with links
- Related comics section

**Components:**

- `ComicHeader` - Header with metadata
- `ComicDescription` - Synopsis section
- `ComicStats` - Statistics display
- `BookmarkActions` - Bookmark buttons
- `ChapterList` - Chapter listing
- `RelatedComics` - Recommendations

---

#### Task 3.3: Bookmark Components

**Files:**

- `src/components/comics/AddToBookmarkButton.tsx`
- `src/components/comics/RemoveFromBookmarkButton.tsx`
- `src/components/comics/BookmarkStatus.tsx`
- `src/components/bookmarks/BookmarkActions.tsx`

**Features:**

- Optimistic UI updates
- Status dropdown (Reading, Plan to Read, Completed, On Hold, Dropped)
- Toast notifications
- Loading states

**Actions:** `src/actions/bookmark.actions.ts`

- `addToBookmarksAction`
- `removeFromBookmarksAction`
- `updateBookmarkStatusAction`

---

### Phase 4: Chapter Reader

#### Task 4.1: Chapter Reader Page

**File:** `src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`

**Features:**

- Vertical scroll mode (default)
- Horizontal page mode option
- Fit to width/height options
- Zoom controls
- Full-screen mode
- Previous/next navigation
- Chapter dropdown
- Reading progress tracking
- Keyboard navigation (arrows, space, esc)
- Touch gestures (swipe)

**Settings:**

- Background color (white/dark/sepia)
- Image quality (low/medium/high)
- Zoom level slider

**Components:**

- `ChapterReader` - Main reader
- `ImageViewer` - Image display
- `ChapterNavigation` - Nav controls
- `ReadingSettings` - Settings panel
- `ReadingProgress` - Progress indicator

---

### Phase 5: Bookmarks Management

#### Task 5.1: Bookmarks Listing Page

**File:** `src/app/(root)/bookmarks/page.tsx`

**Features:**

- Grid/list view toggle
- Bookmark cards with progress
- Filter by status
- Sort by date/title/progress
- Search bookmarks
- Empty state handling

**Components:**

- `BookmarkCard` - Card component
- `BookmarkFilters` - Filter controls
- `BookmarkSearch` - Search input
- `BookmarkViewToggle` - View switcher

---

### Phase 6+: Advanced Features

**Planned:**

- Comment discussions on chapters
- User ratings and reviews
- Reading notifications
- User recommendations
- Social features (following, sharing)
- Admin management panel

---

## Quality Gates & Validation

### Pre-Implementation Checklist

- [ ] Feature requirements are clear and documented
- [ ] Database schema is designed and validated
- [ ] Cascade delete implications understood
- [ ] N+1 query risks identified and mitigated
- [ ] Similar patterns found in codebase
- [ ] Task broken down into 1-2 week sprints

---

### Development Commands

```bash
# Type check all code
pnpm run type-check

# Lint and auto-fix
pnpm run lint:fix

# Run unit tests
pnpm test

# Run E2E tests
pnpm run test:ui

# Full build validation
pnpm run build --debug-prerender

# Generate database types
pnpm db:generate

# Push schema to database
pnpm db:push

# Open database GUI
pnpm db:studio
```

---

### Code Quality Gates

Before delivering implementation, verify:

✅ **TypeScript:** `pnpm run type-check` → 0 errors ✅ **Linting:** `pnpm run lint:fix` → 0 errors ✅ **Tests:** `pnpm test` → All pass, 80%+ coverage ✅ **Build:** `pnpm run build --debug-prerender` → No errors ✅ **Security:** Zod validation, auth checks present ✅ **Performance:** Database indexes present, queries optimized ✅ **Accessibility:** ARIA labels, semantic HTML ✅ **Documentation:** Complex logic commented

---

### Code Review Standards

#### Type Safety

- Verify proper TypeScript usage and type definitions
- No `any` types anywhere

#### Performance

- Check for performance implications and optimization opportunities
- Verify database indexes on WHERE/JOIN columns
- No N+1 query patterns

#### Security

- Review for security vulnerabilities and best practices
- Zod validation on all user inputs
- Auth checks on mutations

#### Testing

- Ensure adequate test coverage for new features
- Unit tests for utilities and logic
- E2E tests for critical user flows

#### Documentation

- Verify code is properly documented
- Complex logic has comments
- Components have prop documentation

---

## Quick Start: Implementing a New Feature

### Step 1: Ask Clarification Questions

```
Entity: What are you building?
Purpose: What problem does it solve?
Relations: How does it connect to existing entities?
Operations: What CRUD operations are needed?
```

### Step 2: Search Existing Patterns

```bash
# Find similar DAL implementations
grep -r "class.*Dal extends BaseDal" src/dal

# Find similar schemas
grep -r "export const.*Schema = z.object" src/schemas

# Find similar server actions
grep -r "export async function.*Action" src/actions
```

### Step 3: Design in docs/proposedFixes.md

```markdown
## Proposed Implementation

### Database Schema

[Show table structure with relationships]

### DAL Methods

[List all CRUD + custom methods]

### Zod Schemas

[Show Create and Update schemas]

### Server Actions

[List all actions to implement]

### React Components

[List UI components needed]
```

### Step 4: Get Approval

```
Wait for user to say "I approve the code so implement the code"
```

### Step 5: Implement Everything

- Add schema to `src/database/schema.ts`
- Create DAL class in `src/dal/`
- Create Zod schemas in `src/schemas/`
- Create server actions in `src/actions/`
- Create React components in `src/components/`
- Create page in `src/app/(root)/`

### Step 6: Validate & Test

```bash
pnpm run type-check
pnpm run lint:fix
pnpm test
pnpm run build
```

---

## Special Patterns

### Idempotent Operations (Bookmarks)

```typescript
export async function addBookmarkAction(input: unknown) {
  const parsed = CreateBookmarkSchema.safeParse(input);
  if (!parsed.success) return { ok: false, error: "Invalid" };

  // Use onConflictDoUpdate to avoid duplicate entries
  const [result] = await db
    .insert(bookmark)
    .values(parsed.data)
    .onConflictDoUpdate({
      target: [bookmark.userId, bookmark.comicId],
      set: { status: parsed.data.status, updatedAt: new Date() }
    })
    .returning();

  return { ok: true, data: result };
}
```

---

### Soft Deletes

For data you want to preserve (comments, users):

```typescript
const visibleComments = await db
  .select()
  .from(comment)
  .where(
    and(
      eq(comment.chapterId, chapterId),
      isNull(comment.deletedAt) // Only non-deleted
    )
  );
```

---

## Summary

This guide provides:

✅ **Quick Reference** - Common patterns at a glance ✅ **Complete Database Context** - All 25+ tables explained ✅ **Architecture Patterns** - DAL, validation, actions, components ✅ **Implementation Workflow** - 10-step process for new features ✅ **Feature Phases** - Organized roadmap for development ✅ **Quality Gates** - Checklists and validation commands

Use this guide to understand the system, implement new features, and maintain code quality.

---

**Version:** 1.0.0 | **Updated:** March 1, 2026 | **Framework:** Next.js 16 | **ORM:** Drizzle | **Database:** PostgreSQL` go ahead and implement all phase and tasks start by creating all missing files

read and understand all `docs/*.md`,`docs/*.json`,`.github/prompts/*.prompt.md`, the project files, `.references/comicwise/**/**/*.ts`,`.references/comicwise/**/**/*.tsx`,`.references/comicwise/**/**/*.mts`,`.references/comicwise/**/**/*.mjs`,`.references/comicr/**/**/*.ts`,`.references/comicr/**/**/*.tsx`,`.references/comicr/**/**/*.mts`,`.references/comicr/**/**/*.mjs` then intelligent merge all files using next best practices, dry practices, markdown format, into `docs/dev.content.md` include all code samples then create or update `.github/prompts/setup-enhanced.prompt.md` as a complete enhanced github copilot prompt which uses `docs/dev.content.md` for context and ensure to avoid `Sorry, you have been rate-limited. Please wait a moment before trying again. Learn More Server Error: Sorry, you have exceeded your Copilot token usage. Please review our Terms of Service. Error Code: rate_limited` issues by create or update and running a script to automate any tasks and sub tasks then output `.github/prompts/setup-enhanced.prompt.md` and output an enhanced prompt for running `.github/prompts/setup-enhanced.prompt.md` in copilot cli with personas and completing all steps, phase, task, sub task by creating a todos for steps, phase, tasks and sub tasks then implement all steps, phase, tasks and sub tasks in batch and ensure not to stop until all steps, phase, tasks and sub tasks are completed

As Debugger persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, review the seeding system for improvements and modify the seeding system to read and validate @src\data\comic.json then filter all type,author,artist,genre and pass them to the type,author,artist,genre seeder execute pnpm seed:validate && pnpm seed:all --image-strategy=local --batch-size=500 fix all issues .

As Debugger persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, execute pnpm validate and batch fix all warnings, errors and issues

/plan /create-prompt /create-implementation-plan "As Reviewer persona, reference .github/prompts/setup-enhanced.prompt.md and docs/dev.content.md, Read and understand all `.references/comicwise/scripts/**/*.ps1`,`.references/comicwise/scripts/**/*.sh`,`.references/comicwise/scripts/**/*.ts`,`.references/comicwise/scripts/**/*.js`,`.references/comicr/scripts/**/*.ps1`,`.references/comicr/scripts/**/*.sh`,`.references/comicr/scripts/**/*.ts`,`.references/comicr/scripts/**/*.js`,`src/scripts/**/*.ts` files.

Take this steps before implementing:

- Start by search for improvements that can be made to all `src/scripts/**/*.ts` files
- Then Remove Redundancy from `.references/comicwise/scripts/**/*.ps1`,`.references/comicwise/scripts/**/*.sh`,`.references/comicwise/scripts/**/*.ts`,`.references/comicwise/scripts/**/*.js`,`.references/comicr/scripts/**/*.ps1`,`.references/comicr/scripts/**/*.sh`,`.references/comicr/scripts/**/*.ts`,`.references/comicr/scripts/**/*.js` and output a list of files to a markdown file then read the markdown and triage then output all files to be created or updated with all code samples into a mardown file at `docs/refactor-context.md`. ensure to enfore all typesript files live in `src/scripts` and all powershell and bash scripts live in the root directory ensure all files have dry-run enables, comprehensive and consise logging and enforce dry practices and next.js best practices.
- intelligently group and categorize all files in `docs/refactor-context.md` with valid code samples.
- generate or update all files in `docs/refactor-context.md` with valid code samples.
- modify package.json to include all typescript files in `src/scripts`,bash and powershell scripts in the root directory"

/plan /create-prompt /create-implementation-plan "As Reviewer persona, Review `src/scripts/seed/**/*.ts` files. Create a User seeder to handle all user operations. Create a Comic Image seeder to handle all comic image operations. Create a Chapter Image seeder to handle all chapter image operations. Identify warnings,errors,issues and batch fix them. Think Of any improvements that can be made and implement all of them"

/plan /create-prompt /create-implementation-plan "create a bash and powershell scripts in the root directory that runs pnpm type-check 2>&1 | Tee-Object -FilePath type-check.txt && pnpm lint:fix 2>&1 | Tee-Object -FilePath lint-fixed.txt && pnpm test --run 2>&1 | Tee-Object -FilePath test-report.txt pnpm build:debug 2>&1 | Tee-Object -FilePath build-report.txt comprehensive and consise logging"

/plan /create-prompt /create-implementation-plan "that uses the Debugger Persona Reviews type-check.txt, lint-fixed.txt, test-report.txt, build-report.txt files and triaged all warnings,errors and issues, then implement batch-fixes"

/plan /create-prompt /create-implementation-plan "Audit and Review all `.vscode/*.json` files then "Fetch docs on `.vscode/*.json` files and read them if found then generate or update all `.vscode/*.json` files for this project enforce consistency, correctness, use next best practices and dry practices." /plan /create-prompt /create-implementation-plan "Read docs/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/app/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/components/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "Read src/scripts/** and list all files then triage and categorize them for further processing delete all useless and redundant files" /plan /create-prompt /create-implementation-plan "List all Phase Tasks And Micro-Tasks then Create a detailed Plan for all Phase Tasks And Micro-Tasks with built-in checkpoints and recovery points and code samples with diff and file references"
