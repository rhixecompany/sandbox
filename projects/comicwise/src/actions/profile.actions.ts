/**
 * User Profile Server Actions
 * Handle profile updates, password changes, and account management
 */

"use server";

import bcrypt from "bcryptjs";
import { count, eq } from "drizzle-orm";
import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { db } from "@/database/db";
import { bookmark, comment, rating, readingProgress, user } from "@/database/schema";
import { ChangePasswordSchema, ProfileUpdateSchema } from "@/schemas/profile.schema";

import type { ActionResult } from "@/types/actions-types";

/**
 * Get current user profile
 */
export async function getUserProfileAction(): Promise<
  ActionResult<{
    bio: null | string;
    email: string;
    id: string;
    image: null | string;
    name: null | string;
  }>
> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    const userRecord = await db.query.user.findFirst({
      where: eq(user.id, session.user.id),
      columns: {
        id: true,
        name: true,
        email: true,
        image: true,
      },
    });

    if (!userRecord) {
      return { ok: false, error: "User not found" };
    }

    // Get bio from userMetadata or return empty
    const bio = null;

    return {
      ok: true,
      data: {
        ...userRecord,
        bio,
      },
    };
  } catch (error) {
    console.error("[getUserProfileAction]", error);
    return { ok: false, error: "Failed to fetch profile" };
  }
}

/**
 * Update user profile
 */
export async function updateProfileAction(
  input: unknown
): Promise<ActionResult<{ email: string; image: null | string; name: null | string }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const parsed = ProfileUpdateSchema.safeParse(input);
    if (!parsed.success) {
      const flattened = parsed.error.flatten();
      const firstError = Object.values(flattened.fieldErrors)[0]?.[0];
      return {
        ok: false,
        error: firstError || "Invalid input",
      };
    }

    const { name, email, image } = parsed.data;

    const updated = await db
      .update(user)
      .set({
        name: name || null,
        email: email || undefined,
        image: image || null,
        updatedAt: new Date(),
      })
      .where(eq(user.id, session.user.id))
      .returning({
        name: user.name,
        email: user.email,
        image: user.image,
      });

    if (updated.length === 0) {
      return { ok: false, error: "Failed to update profile" };
    }

    revalidatePath("/profile");
    return { ok: true, data: updated[0] };
  } catch (error) {
    console.error("[updateProfileAction]", error);
    return { ok: false, error: "Failed to update profile" };
  }
}

/**
 * Change user password
 */
export async function changePasswordAction(input: unknown): Promise<ActionResult<null>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const parsed = ChangePasswordSchema.safeParse(input);
    if (!parsed.success) {
      const flattened = parsed.error.flatten();
      const firstError = Object.values(flattened.fieldErrors)[0]?.[0];
      return {
        ok: false,
        error: firstError || "Invalid input",
      };
    }

    const { currentPassword, newPassword } = parsed.data;

    // Get the user's current password hash
    const userRecord = await db.query.user.findFirst({
      where: eq(user.id, session.user.id),
      columns: {
        password: true,
      },
    });

    if (!userRecord || !userRecord.password) {
      return { ok: false, error: "Unable to verify current password" };
    }

    // Verify current password matches the stored hash
    const isPasswordValid = await bcrypt.compare(currentPassword, userRecord.password);
    if (!isPasswordValid) {
      return { ok: false, error: "Current password is incorrect" };
    }

    // Hash the new password with salt rounds = 10
    const hashedPassword = await bcrypt.hash(newPassword, 10);

    // Update the password in database
    await db
      .update(user)
      .set({
        password: hashedPassword,
        updatedAt: new Date(),
      })
      .where(eq(user.id, session.user.id));

    revalidatePath("/profile");
    return { ok: true, data: null };
  } catch (error) {
    console.error("[changePasswordAction]", error);
    return { ok: false, error: "Failed to change password" };
  }
}

/**
 * Delete user account
 */
export async function deleteAccountAction(): Promise<ActionResult<null>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // Delete user and all related data (cascade)
    await db.delete(user).where(eq(user.id, session.user.id));

    return { ok: true, data: null };
  } catch (error) {
    console.error("[deleteAccountAction]", error);
    return { ok: false, error: "Failed to delete account" };
  }
}

/**
 * Get user profile statistics
 */
export async function getUserProfileStatsAction(): Promise<
  ActionResult<{
    bookmarks: number;
    chaptersRead: number;
    commentsMade: number;
    ratingsGiven: number;
  }>
> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    const userId = session.user.id;

    // Get bookmark count
    const bookmarksResult = await db.select({ count: count() }).from(bookmark).where(eq(bookmark.userId, userId));

    // Get ratings given count
    const ratingsResult = await db.select({ count: count() }).from(rating).where(eq(rating.userId, userId));

    // Get comments made count
    const commentsResult = await db.select({ count: count() }).from(comment).where(eq(comment.userId, userId));

    // Get chapters read count (distinct chapters)
    const chaptersResult = await db
      .selectDistinct({ chapterId: readingProgress.chapterId })
      .from(readingProgress)
      .where(eq(readingProgress.userId, userId));

    return {
      ok: true,
      data: {
        bookmarks: bookmarksResult[0]?.count ?? 0,
        ratingsGiven: ratingsResult[0]?.count ?? 0,
        commentsMade: commentsResult[0]?.count ?? 0,
        chaptersRead: chaptersResult.length,
      },
    };
  } catch (error) {
    console.error("[getUserProfileStatsAction]", error);
    return {
      ok: true,
      data: {
        bookmarks: 0,
        ratingsGiven: 0,
        commentsMade: 0,
        chaptersRead: 0,
      },
    };
  }
}
