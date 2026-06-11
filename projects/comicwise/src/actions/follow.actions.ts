/**
 * Follow Server Actions
 * Handle follow/unfollow operations between users
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { followDal } from "@/dal/follow-dal";
import { notificationDal } from "@/dal/notification-dal";
import { followUserSchema, unfollowUserSchema } from "@/schemas/follow.schema";

import type { ActionResult } from "@/types/actions-types";

export async function followUserAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = followUserSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  const { targetUserId } = parsed.data;

  if (targetUserId === session.user.id) {
    return { ok: false, error: "Cannot follow yourself" };
  }

  try {
    await followDal.followUser(session.user.id, targetUserId);

    await notificationDal.create({
      userId: targetUserId,
      type: "follow",
      title: "New Follower",
      message: `${session.user.name || "Someone"} started following you`,
      link: `/profile/${session.user.id}`,
      read: false,
      comicId: null,
      chapterId: null,
    });

    revalidatePath(`/profile/${targetUserId}`);
    revalidatePath(`/profile/${session.user.id}/followers`);
    revalidatePath(`/profile/${session.user.id}/following`);

    return { ok: true, data: { success: true } };
  } catch (error) {
    if (error instanceof Error && error.message.includes("Already following")) {
      return { ok: false, error: "Already following this user" };
    }
    return { ok: false, error: "Failed to follow user" };
  }
}

export async function unfollowUserAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = unfollowUserSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: parsed.error.issues[0]?.message ?? "Invalid input",
    };
  }

  const { targetUserId } = parsed.data;

  try {
    await followDal.unfollowUser(session.user.id, targetUserId);

    revalidatePath(`/profile/${targetUserId}`);
    revalidatePath(`/profile/${session.user.id}/followers`);
    revalidatePath(`/profile/${session.user.id}/following`);

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to unfollow user" };
  }
}

interface FollowWithUser {
  createdAt: Date;
  follower?: {
    id: string;
    image: null | string;
    name: null | string;
  };
  followerId: string;
  followingId: string;
}

export async function getFollowersAction(
  userId: string,
  page = 1,
  limit = 20
): Promise<ActionResult<{ followers: FollowWithUser[]; total: number }>> {
  try {
    const followers = await followDal.getFollowers(userId, {
      offset: (page - 1) * limit,
      limit,
    });
    const total = await followDal.getFollowersCount(userId);

    return { ok: true, data: { followers, total } };
  } catch {
    return { ok: false, error: "Failed to get followers" };
  }
}

export async function getFollowingAction(
  userId: string,
  page = 1,
  limit = 20
): Promise<ActionResult<{ following: FollowWithUser[]; total: number }>> {
  try {
    const following = await followDal.getFollowing(userId, {
      offset: (page - 1) * limit,
      limit,
    });
    const total = await followDal.getFollowingCount(userId);

    return { ok: true, data: { following, total } };
  } catch {
    return { ok: false, error: "Failed to get following" };
  }
}

export async function isFollowingAction(targetUserId: string): Promise<ActionResult<boolean>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const isFollowing = await followDal.isFollowing(session.user.id, targetUserId);
    return { ok: true, data: isFollowing };
  } catch {
    return { ok: false, error: "Failed to check follow status" };
  }
}

export async function getFollowStatsAction(
  userId: string
): Promise<ActionResult<{ followers: number; following: number }>> {
  try {
    const followers = await followDal.getFollowersCount(userId);
    const following = await followDal.getFollowingCount(userId);

    return { ok: true, data: { followers, following } };
  } catch {
    return { ok: false, error: "Failed to get follow stats" };
  }
}
