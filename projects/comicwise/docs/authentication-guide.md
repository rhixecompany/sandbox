# Authentication Implementation Guide

**Purpose:** Complete guide to implementing and managing user authentication in ComicWise using NextAuth

**Framework:** Next.js 16 | **Auth Library:** NextAuth 5+ | **Database:** PostgreSQL with Drizzle | **Password Hashing:** bcryptjs

**Last Updated:** March 1, 2026

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Architecture Overview](#architecture-overview)
3. [Authentication Providers](#authentication-providers)
4. [Database Integration](#database-integration)
5. [Session Management](#session-management)
6. [Protected Routes](#protected-routes)
7. [Server Actions](#server-actions)
8. [Sign-In/Sign-Out Flow](#sign-insign-out-flow)
9. [Role-Based Access Control](#role-based-access-control)
10. [Testing](#testing)
11. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Environment Setup

Create `.env.local` with required credentials:

```bash
# Base configuration (required)
AUTH_SECRET="generate-with: openssl rand -hex 32"
AUTH_URL="http://localhost:3000"  # Dev URL, prod: https://yourdomain.com
DATABASE_URL="postgresql://user:password@localhost:5432/comicwise"

# GitHub OAuth (optional)
GITHUB_CLIENT_ID="your_github_client_id"
GITHUB_CLIENT_SECRET="your_github_client_secret"

# Keycloak (optional)
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="your_keycloak_secret"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"
```

### Generate AUTH_SECRET

```bash
# macOS/Linux
openssl rand -hex 32

# Windows (PowerShell)
[Convert]::ToBase64String([Security.Cryptography.RandomNumberGenerator]::GetBytes(32))

# Or use online tool: https://generate-secret.vercel.app
```

### Initialize Database

```bash
# Create/migrate database tables (done automatically by NextAuth adapter)
pnpm db:push

# Verify auth tables created
pnpm db:studio  # Check: account, session, user, verificationToken, authenticator tables
```

### Start Application

```bash
# Install dependencies
pnpm install

# Run development server
pnpm dev

# Navigate to http://localhost:3000
# Click "Sign In" to test authentication
```

---

## Architecture Overview

### Authentication Flow Diagram

```text
User Browser
     ↓
Next.js App ← → NextAuth (auth.ts)
     ↓
Auth Providers (GitHub, Credentials, Keycloak)
     ↓
User/Account/Session Tables (PostgreSQL)
```

### Key Components

**1. `src/auth.ts` - NextAuth Initialization**

```typescript
// Exports handlers (GET/POST), auth(), signIn(), signOut()
export const { handlers, auth, signIn, signOut } =
  NextAuth(authConfig);
```

**2. `src/auth-config.ts` - Configuration**

```typescript
// Database strategy, session duration, callbacks
// Adapts providers, creates sessions
```

**3. `src/auth-adapter.ts` - Drizzle Integration**

```typescript
// Connects NextAuth to PostgreSQL via Drizzle
// Maps auth tables to database schema
```

**4. `src/auth-providers.ts` - Auth Providers (GitHub, Credentials, Keycloak)**

```typescript
// GitHub OAuth, username/password, Keycloak SSO
// Customizable credential validation
```

**5. `src/app/api/auth/[...nextauth]/route.ts` - API Route**

```typescript
// Handles /api/auth/* requests
// Routes to NextAuth handlers
```

---

## Authentication Providers

ComicWise supports three authentication methods:

### 1. GitHub OAuth

**Best for:** Open-source projects, developer users

**Setup:**

1. Go to [GitHub Settings → Developer settings → OAuth Apps](https://github.com/settings/developers)
2. Create new OAuth App
3. Set Authorization callback URL to `{AUTH_URL}/api/auth/callback/github`
4. Copy Client ID and Client Secret

**env.local:**

```bash
GITHUB_CLIENT_ID="xxx"
GITHUB_CLIENT_SECRET="xxx"
```

**Usage (Client Component):**

```typescript
"use client";
import { signIn } from "next-auth/react";

export function SignInButton() {
  return (
    <button onClick={() => signIn("github", { redirectTo: "/dashboard" })}>
      Sign In with GitHub
    </button>
  );
}
```

### 2. Credentials (Username/Password)

**Best for:** Internal testing, legacy systems

**How it works:**

1. User submits username + password
2. NextAuth calls `authorize()` function
3. Function validates against database
4. Session created if valid

**Implementation:**

```typescript
// src/auth-providers.ts
Credentials({
  name: "Credentials",
  credentials: {
    username: { label: "Username", type: "text" },
    password: { label: "Password", type: "password" },
  },
  async authorize(credentials): Promise<User | null> {
    const username = typeof credentials.username === "string" ? credentials.username : null;
    const password = typeof credentials.password === "string" ? credentials.password : null;

    if (!username || !password) return null;

    // Query database for user
    const user = await getUserByUsername(username);

    // Verify password
    if (user && user.passwordHash && (await verifyPassword(password, user.passwordHash))) {
      return user;  // Session created automatically
    }

    return null;  // Auth failed
  },
}),
```

**Usage (Sign-In Form):**

```typescript
"use client";
import { signIn } from "next-auth/react";
import { useState } from "react";

export function CredentialsForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSignIn = async (e: React.FormEvent) => {
    e.preventDefault();

    const result = await signIn("credentials", {
      username,
      password,
      redirect: false,
    });

    if (!result?.ok) {
      setError("Invalid username or password");
      return;
    }

    // Success - redirect to dashboard
    window.location.href = "/dashboard";
  };

  return (
    <form onSubmit={handleSignIn} className="space-y-4">
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      {error && <div className="text-red-600">{error}</div>}
      <button type="submit">Sign In</button>
    </form>
  );
}
```

### 3. Keycloak (SSO)

**Best for:** Enterprise, centralized identity management

**Setup:**

1. Deploy Keycloak instance (or use managed service)
2. Create realm, client
3. Configure Client with redirect URIs

**env.local:**

```bash
KEYCLOAK_CLIENT_ID="comicwise"
KEYCLOAK_CLIENT_SECRET="xxx"
KEYCLOAK_ISSUER="https://keycloak.example.com/realms/comicwise"
```

**Usage:**

```typescript
<button onClick={() => signIn("keycloak", { redirectTo: "/dashboard" })}>
  Sign In with Keycloak
</button>
```

---

## Database Integration

### NextAuth Tables (Auto-Created)

NextAuth with Drizzle adapter creates 5 tables:

#### 1. `user` Table

Stores user information:

```sql
CREATE TABLE "user" (
  "id" text PRIMARY KEY,
  "name" text,
  "email" text NOT NULL UNIQUE,
  "emailVerified" timestamp,
  "image" text,
  "password" text,  -- Added by ComicWise (not standard NextAuth)
  "role" text DEFAULT 'user',  -- Added by ComicWise (RBAC)
  "createdAt" timestamp DEFAULT now(),
  "updatedAt" timestamp DEFAULT now()
);
```

#### 2. `account` Table

OAuth provider accounts linked to users:

```sql
CREATE TABLE "account" (
  "userId" text NOT NULL REFERENCES "user"("id") ON DELETE cascade,
  "type" text NOT NULL,
  "provider" text NOT NULL,
  "providerAccountId" text NOT NULL,
  "refresh_token" text,
  "access_token" text,
  "expires_at" integer,
  "token_type" text,
  "scope" text,
  "id_token" text,
  "session_state" text,
  PRIMARY KEY("provider", "providerAccountId")
);
```

Example: GitHub account linked to user

- userId: "user_123"
- provider: "github"
- providerAccountId: "12345678" (GitHub user ID)

#### 3. `session` Table

Active user sessions:

```sql
CREATE TABLE "session" (
  "sessionToken" text PRIMARY KEY,
  "userId" text NOT NULL REFERENCES "user"("id") ON DELETE cascade,
  "expires" timestamp NOT NULL
);
```

Auto-cleaned: Sessions older than maxAge (30 days) removed.

#### 4. `verificationToken` Table

Email verification tokens:

```sql
CREATE TABLE "verificationToken" (
  "email" text NOT NULL,
  "token" text NOT NULL,
  "expires" timestamp NOT NULL,
  PRIMARY KEY("email", "token")
);
```

#### 5. `authenticator` Table

WebAuthn credentials for passwordless auth:

```sql
CREATE TABLE "authenticator" (
  "credentialID" text NOT NULL UNIQUE,
  "userId" text NOT NULL REFERENCES "user"("id") ON DELETE cascade,
  "providerAccountId" text NOT NULL,
  "credentialPublicKey" text NOT NULL,
  "counter" integer NOT NULL,
  "credentialDeviceType" text NOT NULL,
  "credentialBackedUp" boolean NOT NULL,
  "transports" text,
  PRIMARY KEY("userId", "credentialID")
);
```

---

## Session Management

### Session Duration

Configured in `auth-config.ts`:

```typescript
const session = {
  strategy: "database" as const,
  maxAge: 30 * 24 * 60 * 60, // 30 days
  updateAge: 24 * 60 * 60 // Refresh if older than 1 day
};
```

**What happens:**

- User signs in → Session created, expires in 30 days
- User returns within 30 days → Session extended
- Session age exceeds 30 days → User re-signed-out

### Session Callback

Customize session data returned to client:

```typescript
// auth-config.ts
const callbacks = {
  async session({ session, token, user }) {
    // Add custom fields to session
    session.user = user ?? token?.user;
    session.lastLogin = token?.lastLogin || null;
    return session;
  }
};
```

### JWT Callback

Customize JWT token passed between requests:

```typescript
// auth-config.ts
const callbacks = {
  async jwt({ token, user, account }) {
    // First sign-in
    if (user) {
      token.user = user;
      token.role = user.role || "user";
      token.lastLogin = Date.now();
    }

    // Store provider info
    if (account) {
      token.provider = account.provider;
    }

    return token;
  }
};
```

---

## Protected Routes

### Server Component (Recommended)

```typescript
// src/app/(root)/dashboard/page.tsx - Server Component
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function DashboardPage() {
  const session = await auth();

  // No session → redirect to login
  if (!session?.user) {
    redirect("/auth/signin");
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}</h1>
      <p>Email: {session.user.email}</p>
    </div>
  );
}
```

### Client Component with useSession

```typescript
// src/components/dashboard-client.tsx - Client Component
"use client";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export function DashboardContent() {
  const { data: session, status } = useSession();
  const router = useRouter();

  useEffect(() => {
    // Not signed-in → redirect to login
    if (status === "unauthenticated") {
      router.push("/auth/signin");
    }
  }, [status, router]);

  if (status === "loading") {
    return <div>Loading...</div>;
  }

  if (!session?.user) {
    return null;  // Redirecting...
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}</h1>
      {/* Protected content */}
    </div>
  );
}
```

### API Route Protection

```typescript
// src/app/api/profile/route.ts
import { auth } from "@/auth";
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const session = await auth();

  // Not authenticated
  if (!session?.user) {
    return NextResponse.json(
      { error: "Unauthorized" },
      { status: 401 }
    );
  }

  // Return protected data
  return NextResponse.json({
    id: session.user.id,
    email: session.user.email,
    name: session.user.name
  });
}
```

### Route Middleware Protection

```typescript
// src/proxy.ts - Middleware
import { auth } from "@/auth";
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export async function middleware(request: NextRequest) {
  // Check if accessing protected route
  if (request.nextUrl.pathname.startsWith("/dashboard")) {
    const session = await auth();

    if (!session?.user) {
      return NextResponse.redirect(
        new URL("/auth/signin", request.url)
      );
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*", "/admin/:path*", "/profile/:path*"]
};
```

---

## Server Actions

### Sign-In Action

```typescript
// src/actions/auth-actions.ts
"use server";
import { signIn } from "@/auth";

export async function signInAction(provider: string) {
  await signIn(provider, { redirectTo: "/dashboard" });
}
```

**Usage (Client Component):**

```typescript
"use client";
import { signInAction } from "@/actions/auth.actions";

export function SignInButton() {
  return (
    <button onClick={() => signInAction("github")}>
      Sign In with GitHub
    </button>
  );
}
```

### Sign-Out Action

```typescript
// src/actions/auth-actions.ts
"use server";
import { signOut } from "@/auth";

export async function signOutAction() {
  await signOut({ redirectTo: "/" });
}
```

### Get Current Session

```typescript
// src/actions/auth-actions.ts
"use server";
import { auth } from "@/auth";

export async function getCurrentSessionAction() {
  const session = await auth();

  if (!session?.user) {
    return null;
  }

  return {
    id: session.user.id,
    email: session.user.email,
    name: session.user.name,
    role: session.user.role
  };
}
```

---

## Sign-In/Sign-Out Flow

### Complete Sign-In Page

```typescript
// src/app/(auth)/signin/page.tsx
"use client";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function SignInPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const handleCredentialsSignIn = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    const result = await signIn("credentials", {
      username,
      password,
      redirect: false,
    });

    if (!result?.ok) {
      setError("Invalid credentials");
      setIsLoading(false);
      return;
    }

    router.push("/dashboard");
  };

  const handleGitHubSignIn = async () => {
    setIsLoading(true);
    await signIn("github", { redirectTo: "/dashboard" });
  };

  return (
    <div className="max-w-md w-full mx-auto py-12 px-4">
      <h1 className="text-2xl font-bold mb-8">Sign In</h1>

      {/* Credentials Form */}
      <form onSubmit={handleCredentialsSignIn} className="space-y-4 mb-6">
        <div>
          <label className="block text-sm font-medium">Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="mt-1 w-full px-3 py-2 border rounded-md"
            disabled={isLoading}
          />
        </div>

        <div>
          <label className="block text-sm font-medium">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="mt-1 w-full px-3 py-2 border rounded-md"
            disabled={isLoading}
          />
        </div>

        {error && <div className="p-3 bg-red-100 text-red-700 rounded">{error}</div>}

        <button
          type="submit"
          disabled={isLoading}
          className="w-full px-4 py-2 bg-blue-600 text-white rounded-md disabled:opacity-50"
        >
          {isLoading ? "Signing in..." : "Sign In"}
        </button>
      </form>

      <div className="relative mb-6">
        <div className="absolute inset-0 flex items-center">
          <div className="w-full border-t"></div>
        </div>
        <div className="relative flex justify-center text-sm">
          <span className="px-2 bg-white text-gray-500">Or continue with</span>
        </div>
      </div>

      {/* OAuth Buttons */}
      <div className="space-y-3">
        <button
          onClick={handleGitHubSignIn}
          disabled={isLoading}
          className="w-full px-4 py-2 border rounded-md disabled:opacity-50"
        >
          Sign in with GitHub
        </button>
      </div>
    </div>
  );
}
```

### Sign-Out Component

```typescript
// src/components/sign-out-button.tsx
"use client";
import { signOut } from "next-auth/react";

export function SignOutButton() {
  return (
    <button
      onClick={() => signOut({ redirectTo: "/" })}
      className="px-4 py-2 text-sm font-medium text-red-600 hover:bg-red-50 rounded"
    >
      Sign Out
    </button>
  );
}
```

---

## Role-Based Access Control

### User Roles

Available roles in database:

- `user` - Default user role
- `moderator` - Can moderate comments, delete inappropriate content
- `admin` - Full administrative access

### Check Role in Server Component

```typescript
// src/app/admin/page.tsx
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function AdminPage() {
  const session = await auth();

  // Not signed in
  if (!session?.user) {
    redirect("/auth/signin");
  }

  // Verify admin role
  const user = session.user as { role?: unknown };
  const isAdmin = typeof user.role === "string" && user.role === "admin";

  if (!isAdmin) {
    redirect("/dashboard");
  }

  return (
    <div>
      <h1>Admin Panel</h1>
      {/* Admin-only content */}
    </div>
  );
}
```

### Check Role in Server Action

```typescript
// src/actions/admin-actions.ts
"use server";
import { auth } from "@/auth";

export async function deleteCommentAction(commentId: number) {
  const session = await auth();

  // Verify authentication
  if (!session?.user) {
    return { ok: false, error: "Not authenticated" };
  }

  // Verify authorization
  const user = session.user as { role?: unknown };
  const isModerator =
    typeof user.role === "string" &&
    (user.role === "moderator" || user.role === "admin");

  if (!isModerator) {
    return { ok: false, error: "Insufficient permissions" };
  }

  // Perform action
  // ... delete comment logic
  return { ok: true };
}
```

### Role Helper Utilities

```typescript
// src/lib/auth-utils.ts
export function hasRole(
  user: unknown,
  requiredRole: "admin" | "moderator" | "user"
): boolean {
  const u = user as { role?: unknown };
  const userRole = typeof u.role === "string" ? u.role : "user";

  // Admin can do everything
  if (userRole === "admin") return true;

  // Moderator can do moderator tasks
  if (requiredRole === "moderator" && userRole === "moderator")
    return true;

  // User is default
  if (requiredRole === "user") return true;

  return false;
}

export function requireRole(
  user: unknown,
  requiredRole: "admin" | "moderator"
) {
  if (!hasRole(user, requiredRole)) {
    throw new Error(`Required role: ${requiredRole}`);
  }
}
```

---

## Testing

### Unit Tests

```typescript
// src/tests/auth.spec.ts
import { describe, it, expect } from "vitest";
import { verifyPassword } from "@/actions/auth-db";
import bcrypt from "bcryptjs";

describe("Authentication", () => {
  it("hashes and verifies passwords correctly", async () => {
    const plainPassword = "SecurePassword123!";
    const hash = await bcrypt.hash(plainPassword, 10);

    const isValid = await verifyPassword(plainPassword, hash);
    expect(isValid).toBe(true);

    const isInvalid = await verifyPassword("WrongPassword", hash);
    expect(isInvalid).toBe(false);
  });
});
```

### E2E Tests (Playwright)

```typescript
// playwright/auth.spec.ts
import { test, expect } from "@playwright/test";

test.describe("Authentication", () => {
  test("user can sign in and access dashboard", async ({ page }) => {
    // Navigate to sign-in
    await page.goto("/auth/signin");

    // Fill form
    await page.fill('input[name="username"]', "testuser");
    await page.fill('input[name="password"]', "password123");

    // Submit
    await page.click('button[type="submit"]');

    // Verify redirect to dashboard
    await expect(page).toHaveURL("/dashboard");
    await expect(page.getByText(/welcome/i)).toBeVisible();
  });

  test("user cannot access admin panel without admin role", async ({
    page
  }) => {
    // Sign in as regular user
    await page.goto("/auth/signin");
    await page.fill('input[name="username"]', "user");
    await page.fill('input[name="password"]', "password");
    await page.click('button[type="submit"]');

    // Try to access admin
    await page.goto("/admin");

    // Should redirect back
    await expect(page).toHaveURL("/dashboard");
  });
});
```

---

## Troubleshooting

### Issue: "AUTH_SECRET is not configured"

**Solution:**

```bash
# Generate secret
openssl rand -hex 32

# Add to .env.local
AUTH_SECRET="your_generated_secret"
```

### Issue: "Database connection failed"

**Solution:**

```bash
# Verify DATABASE_URL in .env.local
cat .env.local | grep DATABASE_URL

# Test connection
pnpm db:check

# Verify migrations applied
pnpm db:studio
```

### Issue: GitHub sign-in shows "validation error"

**Solution:**

1. Verify CLIENT_ID and CLIENT_SECRET in .env.local
2. Verify redirect URI in GitHub OAuth app settings matches: `{AUTH_URL}/api/auth/callback/github`
3. Restart dev server after changing env

### Issue: Session not persisting across requests

**Solution:**

```bash
# Verify session table has data
pnpm db:studio

# Check session hasn't expired
# Sessions expire after 30 days (configurable in auth-config.ts)

# Clear browser cookies and try again
```

### Issue: "Callback route not found"

**Solution:** Verify auth route exists:

```bash
# Should exist: src/app/api/auth/[...nextauth]/route.ts
ls src/app/api/auth/

# If missing, create it:
# export const { GET, POST } = handlers;
```

---

## Security Best Practices

### ✅ DO

- ✅ Use HTTPS in production (`AUTH_URL="https://"`)
- ✅ Store secrets in environment variables
- ✅ Use bcryptjs for password hashing
- ✅ Implement CSRF protection (NextAuth handles by default)
- ✅ Set `trustHost: true` in auth config
- ✅ Validate user input with Zod
- ✅ Check authentication before sensitive operations
- ✅ Implement rate limiting on sign-in attempts

### ❌ DON'T

- ❌ Hardcode secrets in code
- ❌ Store plaintext passwords
- ❌ Trust client-side role checks only
- ❌ Use HTTP in production
- ❌ Expose sensitive info in client components
- ❌ Skip email verification for public sign-ups
- ❌ Use weak passwords for test accounts
- ❌ Log authentication tokens

---

## References

- [NextAuth Documentation](https://authjs.dev/)
- [Drizzle Adapter](https://authjs.dev/reference/adapter/drizzle)
- [bcryptjs Documentation](https://github.com/dcodeIO/bcrypt.js)
- [Example Feature Implementation (Ratings)](./example-feature-implementation.md)

---

**Version:** 1.0.0 | **Updated:** March 1, 2026 | **Framework:** Next.js 16 | **Auth:** NextAuth 5+
