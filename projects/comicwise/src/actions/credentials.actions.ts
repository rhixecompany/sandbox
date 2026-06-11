"use server";

import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";
import { AuthError } from "next-auth";

import { signIn } from "@/auth";
import { db } from "@/database/db";
import { user as userTable } from "@/database/schema";

import type { ActionResult } from "@/types/actions-types";

/**
 * Server Action: Sign in with credentials (username + password)
 * @param username - Username for authentication
 * @param password - Plain text password
 * @returns ActionResult with success/error message
 */
export async function signInWithCredentialsAction(
  username: string,
  password: string
): Promise<ActionResult<{ success: true }>> {
  try {
    // Validate inputs
    if (!username || !password) {
      return {
        ok: false,
        error: "Username and password are required",
      };
    }

    // Attempt sign in with NextAuth credentials provider
    await signIn("credentials", {
      username,
      password,
      redirect: false,
    });

    return {
      ok: true,
      data: { success: true },
    };
  } catch (error) {
    console.error("Sign in error:", error);

    // Handle NextAuth specific errors
    if (error instanceof AuthError) {
      switch (error.type) {
        case "CredentialsSignin":
          return {
            ok: false,
            error: "Invalid username or password",
          };
        case "CallbackRouteError":
          return {
            ok: false,
            error: "Authentication callback failed. Please try again.",
          };
        default:
          return {
            ok: false,
            error: "Authentication failed. Please try again.",
          };
      }
    }

    return {
      ok: false,
      error: "An unexpected error occurred. Please try again.",
    };
  }
}

/**
 * Server Action: Register a new user with credentials
 * @param username - Desired username
 * @param email - User email address
 * @param password - Plain text password to be hashed
 * @returns ActionResult with success/error message
 */
export async function registerAction(
  username: string,
  email: string,
  password: string
): Promise<ActionResult<{ userId: string }>> {
  try {
    // Validate inputs
    if (!username || !email || !password) {
      return {
        ok: false,
        error: "All fields are required",
      };
    }

    // Validate username length
    if (username.length < 3) {
      return {
        ok: false,
        error: "Username must be at least 3 characters long",
      };
    }

    // Validate password length
    if (password.length < 8) {
      return {
        ok: false,
        error: "Password must be at least 8 characters long",
      };
    }

    // Check if username already exists
    const existingUserByUsername = await db.select().from(userTable).where(eq(userTable.name, username)).limit(1);

    if (existingUserByUsername.length > 0) {
      return {
        ok: false,
        error: "Username is already taken",
      };
    }

    // Check if email already exists
    const existingUserByEmail = await db.select().from(userTable).where(eq(userTable.email, email)).limit(1);

    if (existingUserByEmail.length > 0) {
      return {
        ok: false,
        error: "Email is already registered",
      };
    }

    // Hash password with bcrypt (10 rounds)
    const passwordHash = await bcrypt.hash(password, 10);

    // Create new user in database
    const [newUser] = await db
      .insert(userTable)
      .values({
        name: username,
        email,
        password: passwordHash,
        role: "user", // Default role
        status: true, // Active user
        emailVerified: null, // Email not verified yet
      })
      .returning({ id: userTable.id });

    if (!newUser) {
      return {
        ok: false,
        error: "Failed to create user account",
      };
    }

    return {
      ok: true,
      data: { userId: newUser.id },
    };
  } catch (error) {
    console.error("Registration error:", error);
    return {
      ok: false,
      error: "An unexpected error occurred during registration. Please try again.",
    };
  }
}
