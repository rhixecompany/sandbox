/**
 * Comic-related Zod schemas
 * Validates comic queries, filters, and mutations
 */

import { z } from "zod";

/**
 * Schema for filtering and searching comics
 */
export const comicFilterSchema = z.object({
  query: z.string().optional().default(""),
  sortBy: z.enum(["latest", "popular", "rating", "trending"]).optional().default("latest"),
  genreId: z.string().optional(),
  authorId: z.string().optional(),
  type: z.enum(["manga", "manhua", "manhwa", "western"]).optional(),
  status: z.enum(["Ongoing", "Completed", "Hiatus", "Dropped", "Season End", "Coming Soon"]).optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(50).optional().default(20),
});

export type ComicFilter = z.infer<typeof comicFilterSchema>;

/**
 * Schema for creating a new comic (admin only)
 */
export const createComicSchema = z.object({
  title: z.string().min(1, "Title is required").max(255),
  slug: z
    .string()
    .min(1)
    .max(255)
    .regex(/^[a-z0-9-]+$/i),
  description: z.string().min(10).max(5000),
  coverImage: z.string().url().optional().nullable(),
  type: z.enum(["manga", "manhua", "manhwa", "western"]),
  status: z.enum(["Ongoing", "Completed", "Hiatus", "Dropped", "Season End", "Coming Soon"]),
  rating: z.number().min(0).max(5).optional().default(0),
  authorId: z.string().optional().nullable(),
  artistId: z.string().optional().nullable(),
  genreIds: z.array(z.string()).optional().default([]),
});

export type CreateComicInput = z.infer<typeof createComicSchema>;

/**
 * Schema for updating a comic
 */
export const updateComicSchema = createComicSchema.partial().extend({
  id: z.string().min(1),
});

export type UpdateComicInput = z.infer<typeof updateComicSchema>;

/**
 * Schema for rating a comic
 */
export const rateComicSchema = z.object({
  comicId: z.string().min(1),
  rating: z.number().min(1).max(5),
  review: z.string().max(1000).optional(),
});

export type RateComicInput = z.infer<typeof rateComicSchema>;
