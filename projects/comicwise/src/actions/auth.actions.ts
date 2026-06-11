/**
 * Authentication Server Actions
 * Handle server-side authentication operations
 */

"use server";

import { auth, signIn, signOut } from "@/auth";

import type { ActionResult } from "@/types/actions-types";
import type { AuthError } from "next-auth";

/**
 * Get current session information
 */
export async function getSessionAction(): Promise<
  ActionResult<{
    user: {
      email: null | string;
      id: string;
      image: null | string;
      name: null | string;
      role?: string;
    } | null;
  }>
> {
  try {
    const session = await auth();
    return {
      ok: true,
      data: {
        user: session?.user
          ? {
              id: session.user.id as string,
              name: session.user.name ?? null,
              email: session.user.email ?? null,
              image: session.user.image ?? null,
              role: (session.user as { role?: string }).role,
            }
          : null,
      },
    };
  } catch (error) {
    console.error("[getSessionAction]", error);
    return { ok: false, error: "Failed to fetch session" };
  }
}

/**
 * Sign in with OAuth provider
 * Redirects to provider login
 */
export async function signInAction(provider: "discord" | "github" | "google"): Promise<ActionResult<void>> {
  try {
    await signIn(provider, { redirectTo: "/" });
    return { ok: true, data: undefined };
  } catch (error) {
    const authError = error as AuthError;
    console.error("[signInAction]", authError);
    return { ok: false, error: authError.message || "Sign in failed" };
  }
}

/**
 * Sign out current user with optional redirect
 */
export async function signOutAction(redirectTo?: string): Promise<ActionResult<void>> {
  try {
    await signOut({ redirectTo: redirectTo ?? "/" });
    return { ok: true, data: undefined };
  } catch (error) {
    console.error("[signOutAction]", error);
    return { ok: false, error: "Sign out failed" };
  }
}

/**
 * Custom signOut function for use in client components
 * Returns the signOut action to be called directly
 */
export async function customSignOut(redirectTo?: string): Promise<void> {
  try {
    await signOut({ redirectTo: redirectTo ?? "/" });
  } catch (error) {
    console.error("[customSignOut]", error);
    throw error;
  }
}

/**
 * Check if user is authenticated
 */
export async function isAuthenticatedAction(): Promise<ActionResult<boolean>> {
  try {
    const session = await auth();
    return { ok: true, data: !!session?.user };
  } catch (error) {
    console.error("[isAuthenticatedAction]", error);
    return { ok: false, error: "Failed to check authentication status" };
  }
}

/**
 * Check if current user is admin
 */
export async function isAdminAction(): Promise<ActionResult<boolean>> {
  try {
    const session = await auth();
    if (!session?.user) {
      return { ok: true, data: false };
    }

    const user = session.user as { role?: unknown };
    const isAdmin = typeof user?.role === "string" && user.role === "admin";
    return { ok: true, data: isAdmin };
  } catch (error) {
    console.error("[isAdminAction]", error);
    return { ok: false, error: "Failed to check admin status" };
  }
}
