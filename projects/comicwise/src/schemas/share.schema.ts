/**
 * Share-related Zod schemas
 * Validates share operations
 */

import { z } from "zod";

/**
 * Schema for sharing a comic
 */
export const shareComicSchema = z.object({
  comicId: z.number().int().positive(),
  message: z.string().max(500).optional(),
});

export type ShareComicInput = z.infer<typeof shareComicSchema>;

/**
 * Schema for sharing a chapter
 */
export const shareChapterSchema = z.object({
  chapterId: z.number().int().positive(),
  message: z.string().max(500).optional(),
});

export type ShareChapterInput = z.infer<typeof shareChapterSchema>;

/**
 * Combined share schema
 */
export const shareResourceSchema = z.discriminatedUnion("resourceType", [
  shareComicSchema.extend({ resourceType: z.literal("comic") }),
  shareChapterSchema.extend({ resourceType: z.literal("chapter") }),
]);

export type ShareResourceInput = z.infer<typeof shareResourceSchema>;

/**
 * Schema for deleting a share
 */
export const deleteShareSchema = z.object({
  shareId: z.number().int().positive(),
});

export type DeleteShareInput = z.infer<typeof deleteShareSchema>;
