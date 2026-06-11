/**
 * User Preferences DAL
 * Data access layer for user preferences
 */

import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { userPreference } from "@/database/schema";
import { DEFAULT_PREFERENCES } from "@/types/user-preferences";

import { BaseDal } from "./base-dal";

import type { UpdateUserPreferenceInput, UserPreference } from "@/types/user-preferences";

type UserPreferenceRecord = typeof userPreference.$inferSelect;

export class UserPreferenceDal extends BaseDal<UserPreference> {
  /**
   * Get user preferences by user ID
   * Returns default preferences if not found
   */
  async getByUserId(userId: string): Promise<UserPreference> {
    const prefs = await db.query.userPreference.findFirst({
      where: eq(userPreference.userId, userId),
    });

    if (!prefs) {
      // Return defaults for new users
      return { ...DEFAULT_PREFERENCES, userId };
    }

    return this.mapRecord(prefs);
  }

  /**
   * Create or update user preferences
   */
  async upsertPreferences(userId: string, data: UpdateUserPreferenceInput): Promise<UserPreference> {
    const result = await db
      .insert(userPreference)
      .values({
        userId,
        ...data,
        updatedAt: new Date(),
      })
      .onConflictDoUpdate({
        target: userPreference.userId,
        set: {
          ...data,
          updatedAt: new Date(),
        },
      })
      .returning();

    return this.mapRecord(result[0]);
  }

  /**
   * Update specific preference fields
   */
  async updatePreferences(userId: string, data: Partial<UpdateUserPreferenceInput>): Promise<null | UserPreference> {
    const result = await db
      .update(userPreference)
      .set({
        ...data,
        updatedAt: new Date(),
      })
      .where(eq(userPreference.userId, userId))
      .returning();

    return result.length > 0 ? this.mapRecord(result[0]) : null;
  }

  /**
   * Get all preferences
   */
  async list(): Promise<UserPreference[]> {
    const results = await db.query.userPreference.findMany();
    return results.map((r) => this.mapRecord(r));
  }

  /**
   * Get by ID
   */
  async getById(id: number | string): Promise<null | UserPreference> {
    const result = await db.query.userPreference.findFirst({
      where: eq(userPreference.id, Number(id)),
    });

    return result ? this.mapRecord(result) : null;
  }

  /**
   * Create preferences
   */
  async create(data: unknown): Promise<UserPreference> {
    const validated = data as UpdateUserPreferenceInput & { userId: string };
    const { userId, ...rest } = validated;
    const result = await db
      .insert(userPreference)
      .values({
        userId,
        ...rest,
      })
      .returning();

    return this.mapRecord(result[0]);
  }

  /**
   * Update preferences
   */
  async update(id: number | string, data: unknown): Promise<null | UserPreference> {
    const updateData = data as UpdateUserPreferenceInput;
    const result = await db
      .update(userPreference)
      .set({
        ...updateData,
        updatedAt: new Date(),
      })
      .where(eq(userPreference.id, Number(id)))
      .returning();

    return result.length > 0 ? this.mapRecord(result[0]) : null;
  }

  /**
   * Delete preferences
   */
  async delete(id: number | string): Promise<void> {
    await db.delete(userPreference).where(eq(userPreference.id, Number(id)));
  }

  /**
   * Map database record to interface
   */
  private mapRecord(record: UserPreferenceRecord): UserPreference {
    return {
      id: record.id,
      userId: record.userId,
      theme: record.theme || "system",
      defaultLayout: record.defaultLayout || "webtoon",
      pageNavigationStyle: record.pageNavigationStyle || "buttons",
      fontSize: record.fontSize || 16,
      lineHeight: record.lineHeight || "normal",
      notifyNewChapters: record.notifyNewChapters ?? true,
      notifyComments: record.notifyComments ?? true,
      notifyBookmarkUpdates: record.notifyBookmarkUpdates ?? false,
      profilePublic: record.profilePublic ?? false,
      showReadingHistory: record.showReadingHistory ?? false,
      createdAt: record.createdAt,
      updatedAt: record.updatedAt,
    };
  }
}

export const userPreferenceDal = new UserPreferenceDal();
