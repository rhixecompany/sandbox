/**
 * Reading Progress Server Actions
 * Handles recording and tracking user reading progress
 */

"use server";

import { revalidatePath, revalidateTag } from "next/cache.js";

import { auth } from "@/auth";
import { readingGoalsDal } from "@/dal/reading-goals-dal";
import { readingHistoryDal } from "@/dal/reading-history-dal";
import {
  CompleteHistoryChapterSchema,
  RecordReadingSchema,
  UpdateHistoryProgressSchema,
} from "@/schemas/reading.schema";

import type { ActionResult } from "@/types/actions-types";

/**
 * Extract first error message from Zod validation error
 */
function getValidationError(error: unknown): string {
  if (error instanceof Error && "flatten" in error) {
    const flat = error as { flatten: () => { fieldErrors: Record<string, (string | undefined)[]> } };
    const errors = Object.values(flat.flatten().fieldErrors).flat();
    const firstError = errors.find((e): e is string => typeof e === "string");
    return firstError || "Invalid input";
  }
  return "Invalid input";
}

/**
 * Record that a user started reading a chapter
 */
export async function recordReadingProgressAction(
  comicId: number,
  chapterId: number,
  input: unknown
): Promise<
  ActionResult<{
    historyId: number;
    progress: string;
    startedAt: Date;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = RecordReadingSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const entry = await readingHistoryDal.recordChapterRead(session.user.id, comicId, chapterId);

    // 4. REVALIDATE
    revalidateTag("reading-progress", "max");
    revalidateTag(`reading-progress-${comicId}`, "max");
    revalidatePath("/analytics");

    // 5. RETURN
    return {
      ok: true,
      data: {
        historyId: entry.id,
        startedAt: entry.startedAt,
        progress: entry.progress,
      },
    };
  } catch (error) {
    console.error("[recordReadingProgressAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to record reading";
    return { ok: false, error: message };
  }
}

/**
 * Update reading progress for an ongoing chapter
 */
export async function updateReadingProgressAction(input: unknown): Promise<
  ActionResult<{
    completedAt: Date | null;
    historyId: number;
    progress: string;
    timeSpentSeconds: number;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = UpdateHistoryProgressSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const entry = await readingHistoryDal.updateProgress(
      parsed.data.historyId,
      parsed.data.timeSpentSeconds,
      parsed.data.progress
    );

    // 4. Check if goals were completed
    if (entry.completedAt) {
      await readingGoalsDal.checkAndCompleteGoals(session.user.id);
    }

    // 5. REVALIDATE
    revalidateTag("reading-progress", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 6. RETURN
    return {
      ok: true,
      data: {
        historyId: entry.id,
        timeSpentSeconds: entry.timeSpentSeconds,
        progress: entry.progress,
        completedAt: entry.completedAt,
      },
    };
  } catch (error) {
    console.error("[updateReadingProgressAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to update progress";
    return { ok: false, error: message };
  }
}

/**
 * Mark a chapter as completely read
 */
export async function completeChapterAction(input: unknown): Promise<
  ActionResult<{
    completedAt: Date;
    historyId: number;
    progress: string;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = CompleteHistoryChapterSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const entry = await readingHistoryDal.completeChapter(parsed.data.historyId);

    // 4. Check if goals were completed
    await readingGoalsDal.checkAndCompleteGoals(session.user.id);

    // 5. REVALIDATE
    revalidateTag("reading-progress", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 6. RETURN
    return {
      ok: true,
      data: {
        historyId: entry.id,
        completedAt: entry.completedAt!,
        progress: entry.progress,
      },
    };
  } catch (error) {
    console.error("[completeChapterAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to complete chapter";
    return { ok: false, error: message };
  }
}

/**
 * Get reading stats for a user over a time period
 */
export async function getReadingStatsAction(
  startDate?: Date,
  endDate?: Date
): Promise<
  ActionResult<{
    averageTimePerChapter: number;
    completionRate: number;
    totalChaptersRead: number;
    totalComicsRead: number;
    totalMinutesSpent: number;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // 2. QUERY via DAL
    const stats = await readingHistoryDal.getReadingStats(session.user.id, startDate, endDate);

    // 3. RETURN
    return {
      ok: true,
      data: {
        totalChaptersRead: stats.totalChaptersRead,
        totalMinutesSpent: stats.totalMinutesSpent,
        totalComicsRead: stats.totalComicsRead,
        averageTimePerChapter: stats.averageTimePerChapter,
        completionRate: stats.completionRate,
      },
    };
  } catch (error) {
    console.error("[getReadingStatsAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to fetch reading stats";
    return { ok: false, error: message };
  }
}

/**
 * Get reading history for a user
 */
export async function getReadingHistoryAction(
  comicId?: number,
  limit: number = 50,
  offset: number = 0,
  startDate?: Date,
  endDate?: Date
): Promise<
  ActionResult<
    Array<{
      chapterId: number;
      comicId: number;
      completedAt: Date | null;
      id: number;
      progress: string;
      startedAt: Date;
      timeSpentSeconds: number;
    }>
  >
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // 2. QUERY via DAL
    let history;
    if (comicId) {
      history = await readingHistoryDal.getComicReadingHistory(session.user.id, comicId, limit);
    } else {
      history = await readingHistoryDal.getReadingHistory(session.user.id, limit, offset, startDate, endDate);
    }

    // 3. RETURN
    return {
      ok: true,
      data: history.map((h) => ({
        id: h.id,
        comicId: h.comicId,
        chapterId: h.chapterId,
        startedAt: h.startedAt,
        completedAt: h.completedAt,
        timeSpentSeconds: h.timeSpentSeconds,
        progress: h.progress,
      })),
    };
  } catch (error) {
    console.error("[getReadingHistoryAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to fetch reading history";
    return { ok: false, error: message };
  }
}

/**
 * Get recently read comics for user
 */
export async function getRecentlyReadComicsAction(limit: number = 10): Promise<
  ActionResult<
    Array<{
      comicId: number;
      lastReadAt: Date;
    }>
  >
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // 2. QUERY via DAL
    const comics = await readingHistoryDal.getRecentlyReadComics(session.user.id, limit);

    // 3. RETURN
    return {
      ok: true,
      data: comics.map((h) => ({
        comicId: h.comicId,
        lastReadAt: h.startedAt,
      })),
    };
  } catch (error) {
    console.error("[getRecentlyReadComicsAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to fetch recently read comics";
    return { ok: false, error: message };
  }
}
