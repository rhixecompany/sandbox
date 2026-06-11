import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { user as userTable } from "@/database/schema";

import type { User } from "@/auth-providers";

/**
 * Fetch a user by username from the database.
 */
export async function getUserByUsername(username: string): Promise<null | User> {
  // Drizzle ORM query: use imported 'eq' for where clause
  // 'name' can be null, so map to User type
  // Import 'eq' from drizzle-orm
  const result = await db.select().from(userTable).where(eq(userTable.name, username));
  if (!result[0]) return null;
  const dbUser = result[0];
  return {
    id: dbUser.id,
    name: dbUser.name ?? undefined,
    email: dbUser.email,
    role: dbUser.role,
    passwordHash: dbUser.password ?? undefined,
  };
}

/**
 * Verify a plain password against a hashed password.
 */
export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
