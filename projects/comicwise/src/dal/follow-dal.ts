/**
 * Follow DAL (Data Access Layer)
 * Manages follow/unfollow operations between users
 */

import { and, desc, eq, sql } from "drizzle-orm";

import { db } from "@/database/db";
import { follow } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type FollowType = typeof follow.$inferSelect;

export interface FollowWithUser extends FollowType {
  follower?: {
    id: string;
    image: null | string;
    name: null | string;
  };
  following?: {
    id: string;
    image: null | string;
    name: null | string;
  };
}

export class FollowDal extends BaseDal<FollowType> {
  async list(_options?: DalOptions): Promise<FollowType[]> {
    throw new Error("Use getFollowers or getFollowing instead");
  }

  async getById(_id: number | string): Promise<FollowType | null> {
    throw new Error("Use getByUserAndTarget instead");
  }

  async create(_data: unknown): Promise<FollowType> {
    throw new Error("Use followUser instead");
  }

  async update(_id: number | string, _data: unknown): Promise<FollowType | null> {
    throw new Error("Follows cannot be updated");
  }

  async delete(_id: number | string): Promise<void> {
    throw new Error("Use unfollowUser instead");
  }

  async followUser(followerId: string, followingId: string): Promise<FollowType> {
    const [result] = await db
      .insert(follow)
      .values({
        followerId,
        followingId,
      })
      .onConflictDoNothing()
      .returning();

    if (!result) {
      throw new Error("Already following this user");
    }

    return result;
  }

  async unfollowUser(followerId: string, followingId: string): Promise<void> {
    await db.delete(follow).where(and(eq(follow.followerId, followerId), eq(follow.followingId, followingId)));
  }

  async isFollowing(followerId: string, followingId: string): Promise<boolean> {
    const result = await db.query.follow.findFirst({
      where: and(eq(follow.followerId, followerId), eq(follow.followingId, followingId)),
    });

    return result !== undefined;
  }

  async getFollowers(userId: string, options?: DalOptions): Promise<FollowWithUser[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.follow.findMany({
      where: eq(follow.followingId, userId),
      with: {
        follower: {
          columns: {
            id: true,
            name: true,
            image: true,
          },
        },
      },
      orderBy: desc(follow.createdAt),
      limit,
      offset,
    }) as Promise<FollowWithUser[]>;
  }

  async getFollowing(userId: string, options?: DalOptions): Promise<FollowWithUser[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.follow.findMany({
      where: eq(follow.followerId, userId),
      with: {
        following: {
          columns: {
            id: true,
            name: true,
            image: true,
          },
        },
      },
      orderBy: desc(follow.createdAt),
      limit,
      offset,
    }) as Promise<FollowWithUser[]>;
  }

  async getFollowersCount(userId: string): Promise<number> {
    const result = await db
      .select({ count: sql<number>`count(*)` })
      .from(follow)
      .where(eq(follow.followingId, userId));

    return result[0]?.count ?? 0;
  }

  async getFollowingCount(userId: string): Promise<number> {
    const result = await db
      .select({ count: sql<number>`count(*)` })
      .from(follow)
      .where(eq(follow.followerId, userId));

    return result[0]?.count ?? 0;
  }

  async getFollowersIds(userId: string): Promise<string[]> {
    const results = await db
      .select({ followerId: follow.followerId })
      .from(follow)
      .where(eq(follow.followingId, userId));

    return results.map((r) => r.followerId);
  }

  async getFollowingIds(userId: string): Promise<string[]> {
    const results = await db
      .select({ followingId: follow.followingId })
      .from(follow)
      .where(eq(follow.followerId, userId));

    return results.map((r) => r.followingId);
  }
}

export const followDal = new FollowDal();
