import Credentials from "next-auth/providers/credentials";
import GitHub from "next-auth/providers/github";
import Keycloak from "next-auth/providers/keycloak";

import { getUserByUsername, verifyPassword } from "@/dal/auth-db";

import { getEnv } from "appConfig";

import type { Provider } from "next-auth/providers";

// CredentialsInput type removed; kept inline types for authorize to avoid unused-type warnings

export type User = {
  email: string;
  id: string;
  name?: string;
  passwordHash?: string;
  role?: string;
};

const env = getEnv();

const providers: Provider[] = [
  GitHub({ clientId: env.GITHUB_CLIENT_ID, clientSecret: env.GITHUB_CLIENT_SECRET }),
  Credentials({
    name: "Credentials",
    credentials: {
      username: { label: "Username", type: "text" },
      password: { label: "Password", type: "password" },
    },
    async authorize(credentials: Partial<Record<"password" | "username", unknown>>): Promise<null | User> {
      const username = typeof credentials.username === "string" ? credentials.username : undefined;
      const password = typeof credentials.password === "string" ? credentials.password : undefined;
      if (!username || !password) return null;
      const user = await getUserByUsername(username);
      if (user && user.passwordHash && (await verifyPassword(password, user.passwordHash))) return user;
      return null;
    },
  }),
  Keycloak({
    clientId: env.KEYCLOAK_CLIENT_ID!,
    clientSecret: env.KEYCLOAK_CLIENT_SECRET!,
    issuer: env.KEYCLOAK_ISSUER!,
  }),
];

export default providers;
