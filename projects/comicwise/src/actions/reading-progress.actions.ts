/**
 * Reading Progress Server Actions (Section 23.2 from docs/dev.content.md)
 * Pattern: auth → validate → DAL → revalidate → return ActionResult<T>
 * Idempotent upserts via composite key conflict handling
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { readingProgressDal } from "@/dal/reading-progress-dal";

import type { ActionResult } from "@/types/actions-types";

export interface UpdateProgressInput {
  chapterId?: number;
  comicId: number;
  pageNumber?: number;
  scrollPercentage?: number;
}

export interface ReadingProgressData {
  chapterId?: number;
  comicId: number;
  id: number;
  lastReadAt: Date;
  pageNumber: number;
  progressPercent?: number;
  userId: string;
}

export interface ContinueReadingItem {
  chapterId: null | number;
  chapterNumber?: null | number;
  chapterTitle?: null | string;
  comicId: number;
  comicSlug: string;
  comicTitle: string;
  lastReadAt: Date;
  pageNumber: number;
  progressPercent: null | number;
}

/**
 * Update reading progress (idempotent upsert)
 * Section 23.2: Idempotent Upsert Pattern
 */
export async function updateProgressAction(input: UpdateProgressInput): Promise<ActionResult<ReadingProgressData>> {
  try {
    // Step 1: Authenticate
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    // Step 2: Validate input
    if (!input.comicId || input.comicId <= 0) {
      return { ok: false, error: "Invalid comic ID" };
    }

    // Step 3: Update via DAL (idempotent via composite key)
    const progress = await readingProgressDal.updateProgress({
      userId: session.user.id,
      comicId: input.comicId,
      chapterId: input.chapterId,
      pageNumber: input.pageNumber || 0,
      scrollPercentage: input.scrollPercentage,
    });

    if (!progress) {
      return { ok: false, error: "Failed to update reading progress" };
    }

    // Step 4: Revalidate cache
    revalidatePath(`/comics/${progress.comicId}`); // Comic detail page
    revalidatePath("/reading-progress"); // Reading progress list

    // Step 5: Return result
    return {
      ok: true,
      data: {
        id: progress.id,
        userId: progress.userId,
        comicId: progress.comicId,
        chapterId: progress.chapterId,
        pageNumber: progress.pageNumber || 0,
        progressPercent: progress.progressPercent,
        lastReadAt: progress.lastReadAt,
      },
    };
  } catch (error) {
    console.error("updateProgressAction error:", error);
    return { ok: false, error: "Failed to update progress" };
  }
}

/**
 * Get user's "Continue Reading" list
 * Section 23.2: Single JOIN query pattern
 */
export async function getContinueReadingAction(limit = 10): Promise<ActionResult<ContinueReadingItem[]>> {
  try {
    // Step 1: Authenticate
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    // Step 2: Fetch from DAL (single JOIN query, no N+1)
    const items = await readingProgressDal.getContinueReadingList(session.user.id, limit);

    // Step 3: Return result
    return {
      ok: true,
      data: items.map((item) => ({
        comicId: item.comicId,
        comicTitle: item.comicTitle,
        comicSlug: item.comicSlug,
        chapterId: item.chapterId,
        pageNumber: item.pageNumber || 0,
        progressPercent: item.progressPercent,
        lastReadAt: item.lastReadAt,
        chapterNumber: item.chapterNumber ?? undefined,
        chapterTitle: item.chapterTitle ?? undefined,
      })),
    };
  } catch (error) {
    console.error("getContinueReadingAction error:", error);
    return { ok: false, error: "Failed to fetch reading progress" };
  }
}

/**
 * Mark comic as completed
 */
export async function markComicCompletedAction(comicId: number): Promise<ActionResult<ReadingProgressData>> {
  try {
    // Step 1: Authenticate
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    // Step 2: Validate
    if (!comicId || comicId <= 0) {
      return { ok: false, error: "Invalid comic ID" };
    }

    // Step 3: Mark as completed via DAL
    const progress = await readingProgressDal.markCompleted(session.user.id, comicId);

    if (!progress) {
      return { ok: false, error: "Failed to mark comic as completed" };
    }

    // Step 4: Revalidate cache
    revalidatePath("/reading-progress");
    revalidatePath(`/comics/${comicId}`);

    // Step 5: Return result
    return {
      ok: true,
      data: {
        id: progress.id,
        userId: progress.userId,
        comicId: progress.comicId,
        chapterId: progress.chapterId,
        pageNumber: progress.pageNumber || 0,
        progressPercent: progress.progressPercent,
        lastReadAt: progress.lastReadAt,
      },
    };
  } catch (error) {
    console.error("markComicCompletedAction error:", error);
    return { ok: false, error: "Failed to mark comic as completed" };
  }
}

/**
 * Get user reading stats
 */
export async function getUserReadingStatsAction(): Promise<
  ActionResult<{
    completed: number;
    currentlyReading: number;
    totalRead: number;
  }>
> {
  try {
    // Step 1: Authenticate
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Not authenticated" };
    }

    // Step 3: Fetch stats from DAL
    const stats = await readingProgressDal.getUserStats(session.user.id);

    // Step 4: Return result
    return {
      ok: true,
      data: {
        totalRead: stats.totalChaptersRead,
        currentlyReading: 0, // Will be calculated from reading history
        completed: stats.totalChaptersCompleted,
      },
    };
  } catch (error) {
    console.error("getUserReadingStatsAction error:", error);
    return { ok: false, error: "Failed to fetch reading stats" };
  }
}
