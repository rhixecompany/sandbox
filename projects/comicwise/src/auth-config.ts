import { getEnv } from "appConfig";

import adapter from "./auth-adapter";
import providers from "./auth-providers";

import type { NextAuthConfig } from "next-auth";

type Session = {
  [key: string]: unknown;
  lastLogin?: null | number;
  user?: unknown;
};

type Token = {
  [key: string]: unknown;
  lastLogin?: number;
  provider?: string;
  role?: string;
  user?: unknown;
};

const session = {
  strategy: "database" as const,
  maxAge: 30 * 24 * 60 * 60, // 30 days
  updateAge: 24 * 60 * 60, // 1 day
};

// callbacks use a runtime object cast to the NextAuth callbacks type. We avoid
// `any` to satisfy lint rules while keeping flexibility across Auth.js/NextAuth
// versions. This is a narrow, reversible cast applied to the runtime object.
const callbacks = {
  async session({ session, token, user }: { session: Session; token: Token; user?: unknown }): Promise<Session> {
    session.user = user ?? token?.user;
    session.lastLogin = token?.lastLogin || null;
    return session;
  },
  async jwt({
    token,
    user,
    account,
  }: {
    account?: Record<string, unknown>;
    token: Token;
    user?: unknown;
  }): Promise<Token> {
    if (user) {
      token.user = user;
      const u = user as { role?: string };
      token.role = typeof u.role === "string" ? u.role : "user";
      token.lastLogin = Date.now();
    }
    if (account) token.provider = account.provider as string;
    return token;
  },
  async signIn({ user }: { user?: unknown }): Promise<boolean> {
    // Allow any authenticated user
    const u = user as { email?: unknown } | undefined;
    if (!u?.email) return false;
    return true;
  },
  async redirect({ url, baseUrl }: { baseUrl: string; url: string }): Promise<string> {
    // Respect original URL for authenticated users
    if (url.startsWith("/")) return `${baseUrl}${url}`;
    if (new URL(url).origin === baseUrl) return url;
    return `${baseUrl}/dashboard`;
  },
} as unknown as NextAuthConfig["callbacks"];

const env = getEnv();

const authConfig: NextAuthConfig = {
  adapter,
  providers,
  session,
  callbacks,
  secret: env.AUTH_SECRET,
  trustHost: true,
};

export default authConfig;
