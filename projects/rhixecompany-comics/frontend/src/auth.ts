import NextAuth from "next-auth";

import authConfig from "./auth-config";

/**
 * Initialize NextAuth with configuration
 */
export const { handlers, auth, signIn, signOut } = NextAuth(authConfig);
