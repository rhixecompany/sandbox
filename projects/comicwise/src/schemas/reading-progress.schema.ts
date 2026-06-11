import { z } from "zod";

/**
 * Reading Progress Validation Schema
 * Validates user reading progress for chapters
 */

export const ReadingProgressSchema = z.object({
  userId: z.string().uuid("User ID must be a valid UUID").describe("User's UUID identifier"),
  chapterId: z
    .number()
    .int("Chapter ID must be an integer")
    .positive("Chapter ID must be positive")
    .describe("Chapter's database identifier"),
  comicId: z
    .number()
    .int("Comic ID must be an integer")
    .positive("Comic ID must be positive")
    .describe("Comic's database identifier (for validation)"),
  pageNumber: z
    .number()
    .int("Page number must be an integer")
    .nonnegative("Page number cannot be negative")
    .default(0)
    .describe("Current page number (0-indexed)"),
  scrollPercentage: z
    .number()
    .min(0, "Scroll percentage must be between 0 and 100")
    .max(100, "Scroll percentage must be between 0 and 100")
    .default(0)
    .describe("Page scroll progress as a percentage"),
  completedAt: z.date().optional().describe("Timestamp when chapter was marked complete"),
  lastReadAt: z.date().optional().describe("Timestamp of last read activity"),
});

/**
 * Update Reading Progress Schema
 * Used for Server Actions to validate incoming progress updates
 */
export const UpdateReadingProgressSchema = z.object({
  comicId: z.number().int("Comic ID must be an integer").positive("Comic ID must be positive"),
  chapterId: z.number().int("Chapter ID must be an integer").positive("Chapter ID must be positive").optional(),
  pageNumber: z.number().int("Page number must be an integer").nonnegative("Page number cannot be negative").optional(),
  scrollPercentage: z
    .number()
    .min(0, "Scroll percentage must be between 0 and 100")
    .max(100, "Scroll percentage must be between 0 and 100")
    .optional(),
});

/**
 * Mark Complete Schema
 * Validates chapter completion requests
 */
export const MarkChapterCompleteSchema = z.object({
  comicId: z.number().int("Comic ID must be an integer").positive("Comic ID must be positive"),
  chapterId: z.number().int("Chapter ID must be an integer").positive("Chapter ID must be positive"),
});

/**
 * Type inference for progress tracking
 */
export type ReadingProgress = z.infer<typeof ReadingProgressSchema>;
export type UpdateReadingProgressInput = z.infer<typeof UpdateReadingProgressSchema>;
export type MarkChapterCompleteInput = z.infer<typeof MarkChapterCompleteSchema>;

/**
 * Safe validation functions with error handling
 */
export function validateReadingProgress(data: unknown): ReadingProgress {
  const result = ReadingProgressSchema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}

export function validateUpdateProgress(data: unknown): UpdateReadingProgressInput {
  const result = UpdateReadingProgressSchema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}

export function validateMarkComplete(data: unknown): MarkChapterCompleteInput {
  const result = MarkChapterCompleteSchema.safeParse(data);
  if (!result.success) {
    throw new Error(`Validation failed: ${result.error}`);
  }
  return result.data;
}
