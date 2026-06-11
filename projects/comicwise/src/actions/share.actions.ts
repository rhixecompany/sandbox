/**
 * Share Server Actions
 * Handle sharing comics and chapters to activity feed
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { shareDal } from "@/dal/share-dal";
import { deleteShareSchema, shareChapterSchema, shareComicSchema } from "@/schemas/share.schema";

import type { ActionResult } from "@/types/actions-types";

export async function shareComicAction(input: unknown): Promise<ActionResult<{ shareId: number }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = shareComicSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const share = await shareDal.create({
      userId: session.user.id,
      resourceType: "comic",
      resourceId: parsed.data.comicId,
      message: parsed.data.message,
    });

    revalidatePath("/feed");
    revalidatePath(`/comics`);

    return { ok: true, data: { shareId: share.id } };
  } catch {
    return { ok: false, error: "Failed to share comic" };
  }
}

export async function shareChapterAction(input: unknown): Promise<ActionResult<{ shareId: number }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = shareChapterSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    const share = await shareDal.create({
      userId: session.user.id,
      resourceType: "chapter",
      resourceId: parsed.data.chapterId,
      message: parsed.data.message,
    });

    revalidatePath("/feed");

    return { ok: true, data: { shareId: share.id } };
  } catch {
    return { ok: false, error: "Failed to share chapter" };
  }
}

export async function deleteShareAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = deleteShareSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  try {
    await shareDal.deleteUserShare(parsed.data.shareId, session.user.id);

    revalidatePath("/feed");

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to delete share" };
  }
}

interface ShareType {
  createdAt: Date;
  id: number;
  message: null | string;
  resourceId: number;
  resourceType: string;
  userId: string;
}

export async function getUserSharesAction(
  userId: string,
  page = 1,
  limit = 20
): Promise<ActionResult<{ shares: ShareType[]; total: number }>> {
  try {
    const shares = await shareDal.getUserShares(userId, {
      offset: (page - 1) * limit,
      limit,
    });

    return { ok: true, data: { shares, total: shares.length } };
  } catch {
    return { ok: false, error: "Failed to get shares" };
  }
}

export async function getFeedSharesAction(
  userId: string,
  page = 1,
  limit = 20
): Promise<ActionResult<{ shares: ShareType[]; total: number }>> {
  try {
    const followingIds = await shareDal.getFollowingIds?.(userId);
    const shares = await shareDal.getFeedShares(followingIds || [], {
      offset: (page - 1) * limit,
      limit,
    });

    return { ok: true, data: { shares, total: shares.length } };
  } catch {
    return { ok: false, error: "Failed to get feed" };
  }
}
