/**
 * Share DAL (Data Access Layer)
 * Manages sharing of comics and chapters to activity feed
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { share } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ShareType = typeof share.$inferSelect;

export interface ShareInput {
  message?: string;
  resourceId: number;
  resourceType: "chapter" | "comic";
  userId: string;
}

export class ShareDal extends BaseDal<ShareType> {
  async list(options?: DalOptions): Promise<ShareType[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.share.findMany({
      orderBy: desc(share.createdAt),
      limit,
      offset,
    });
  }

  async getById(id: number): Promise<null | ShareType> {
    return (
      (await db.query.share.findFirst({
        where: eq(share.id, id),
      })) ?? null
    );
  }

  async create(data: unknown): Promise<ShareType> {
    const input = data as ShareInput;
    const [result] = await db.insert(share).values(input).returning();

    if (!result) {
      throw new Error("Failed to create share");
    }

    return result;
  }

  async update(id: number, data: unknown): Promise<null | ShareType> {
    const input = data as Partial<ShareInput>;
    const [result] = await db.update(share).set(input).where(eq(share.id, id)).returning();

    return result ?? null;
  }

  async delete(id: number): Promise<void> {
    await db.delete(share).where(eq(share.id, id));
  }

  async getUserShares(userId: string, options?: DalOptions): Promise<ShareType[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.share.findMany({
      where: eq(share.userId, userId),
      orderBy: desc(share.createdAt),
      limit,
      offset,
    });
  }

  async getSharesForResource(
    resourceType: "chapter" | "comic",
    resourceId: number,
    options?: DalOptions
  ): Promise<ShareType[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.share.findMany({
      where: and(eq(share.resourceType, resourceType), eq(share.resourceId, resourceId)),
      orderBy: desc(share.createdAt),
      limit,
      offset,
    });
  }

  async deleteUserShare(shareId: number, userId: string): Promise<boolean> {
    const existing = await db.query.share.findFirst({
      where: and(eq(share.id, shareId), eq(share.userId, userId)),
    });

    if (!existing) {
      return false;
    }

    await db.delete(share).where(eq(share.id, shareId));
    return true;
  }

  async getFeedShares(userIds: string[], options?: DalOptions): Promise<ShareType[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    if (userIds.length === 0) {
      return [];
    }

    return db.query.share.findMany({
      where: eq(share.userId, userIds[0]),
      orderBy: desc(share.createdAt),
      limit,
      offset,
    });
  }

  async getFollowingIds(userId: string): Promise<string[]> {
    const { followDal } = await import("./follow-dal");
    return followDal.getFollowingIds(userId);
  }
}

export const shareDal = new ShareDal();
