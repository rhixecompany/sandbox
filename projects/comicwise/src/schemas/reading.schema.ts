/**
 * Reading History Validation Schemas
 * Zod schemas for reading progress tracking
 */

import { z } from "zod";

/**
 * Schema for recording a chapter read event
 */
export const RecordReadingSchema = z.object({
  chapterId: z.number().int().positive("Chapter ID must be a positive integer"),
  timeSpentSeconds: z.number().int().min(0, "Time spent cannot be negative").default(0),
  progress: z
    .number()
    .min(0, "Progress cannot be less than 0%")
    .max(100, "Progress cannot be more than 100%")
    .default(0),
});

export type RecordReading = z.infer<typeof RecordReadingSchema>;

/**
 * Schema for filtering reading history
 */
export const ReadingHistoryFilterSchema = z.object({
  comicId: z.number().int().positive().optional(),
  startDate: z.date().optional(),
  endDate: z.date().optional(),
  limit: z.number().int().min(1).max(100).default(50),
  offset: z.number().int().min(0).default(0),
});

export type ReadingHistoryFilter = z.infer<typeof ReadingHistoryFilterSchema>;

/**
 * Schema for reading statistics response
 */
export const ReadingStatsSchema = z.object({
  totalChaptersRead: z.number().int().min(0),
  totalMinutesSpent: z.number().int().min(0),
  totalComicsRead: z.number().int().min(0),
  averageTimePerChapter: z.number().min(0),
  completionRate: z.number().min(0).max(100),
});

export type ReadingStats = z.infer<typeof ReadingStatsSchema>;

/**
 * Schema for reading history entry response
 */
export const ReadingHistoryEntrySchema = z.object({
  id: z.number().int(),
  userId: z.string().uuid(),
  comicId: z.number().int(),
  chapterId: z.number().int(),
  startedAt: z.date(),
  completedAt: z.date().nullable().optional(),
  timeSpentSeconds: z.number().int(),
  progress: z.number().min(0).max(100),
  createdAt: z.date(),
  updatedAt: z.date(),
  chapter: z
    .object({
      id: z.number().int(),
      title: z.string(),
      chapterNumber: z.number().int(),
      slug: z.string(),
    })
    .optional(),
  comic: z
    .object({
      id: z.number().int(),
      title: z.string(),
      slug: z.string(),
    })
    .optional(),
});

export type ReadingHistoryEntry = z.infer<typeof ReadingHistoryEntrySchema>;

/**
 * Schema for updating reading history progress (readingHistory table)
 * Used for Server Actions to validate progress updates
 */
export const UpdateHistoryProgressSchema = z.object({
  historyId: z.number().int().positive("History ID must be a positive integer"),
  timeSpentSeconds: z.number().int().min(0, "Time spent cannot be negative"),
  progress: z.number().min(0, "Progress cannot be less than 0%").max(100, "Progress cannot be more than 100%"),
});

export type UpdateHistoryProgressInput = z.infer<typeof UpdateHistoryProgressSchema>;

/**
 * Schema for completing a chapter via reading history (readingHistory table)
 */
export const CompleteHistoryChapterSchema = z.object({
  historyId: z.number().int().positive("History ID must be a positive integer"),
});

export type CompleteHistoryChapterInput = z.infer<typeof CompleteHistoryChapterSchema>;

/**
 * Schema for period selector in analytics dashboard
 */
export const ReadingPeriodSchema = z.enum(["week", "month", "year", "all"]);

export type ReadingPeriod = z.infer<typeof ReadingPeriodSchema>;

// Re-exports from reading-progress.schema.ts for backward compatibility
export type {
  MarkChapterCompleteInput,
  MarkChapterCompleteSchema,
  ReadingProgress,
  ReadingProgressSchema,
  UpdateReadingProgressInput,
  UpdateReadingProgressSchema,
} from "./reading-progress.schema";

/**
 * @deprecated Use UpdateReadingProgressSchema from reading-progress.schema.ts instead.
 */
export { UpdateReadingProgressSchema as LegacyUpdateReadingProgressSchema } from "./reading-progress.schema";

/**
 * @deprecated Use MarkChapterCompleteSchema from reading-progress.schema.ts instead.
 */
export { MarkChapterCompleteSchema as LegacyCompleteChapterSchema } from "./reading-progress.schema";
