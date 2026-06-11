/**
 * Bookmark Schema
 * Validation schema for bookmark operations
 */

import { z } from "zod";

export const bookmarkStatusEnum = z.enum(["Reading", "Plan to Read", "Completed", "On Hold", "Dropped"]);
export type BookmarkStatus = z.infer<typeof bookmarkStatusEnum>;

export const bookmarkFilterSchema = z.object({
  status: bookmarkStatusEnum.optional(),
  search: z.string().optional(),
  sortBy: z.enum(["date", "title", "progress"]).optional().default("date"),
  page: z.number().int().positive().optional().default(1),
  limit: z.number().int().positive().max(100).optional().default(20),
});

export type BookmarkFilter = z.infer<typeof bookmarkFilterSchema>;

export const updateBookmarkStatusSchema = z.object({
  comicId: z.number().positive(),
  status: bookmarkStatusEnum,
});

export type UpdateBookmarkStatusInput = z.infer<typeof updateBookmarkStatusSchema>;
