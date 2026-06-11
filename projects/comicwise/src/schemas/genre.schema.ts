/**
 * Genre-related Zod schemas
 * Validates genre queries, filters, and mutations
 */

import { z } from "zod";

/**
 * Schema for creating a new genre (admin only)
 */
export const createGenreSchema = z.object({
  name: z.string().min(1, "Name is required").max(100),
  slug: z
    .string()
    .min(1)
    .max(100)
    .regex(/^[a-z0-9-]+$/i, "Slug must be lowercase alphanumeric with dashes"),
  description: z.string().max(500).optional(),
  isActive: z.boolean().optional().default(true),
});

export type CreateGenreInput = z.infer<typeof createGenreSchema>;

/**
 * Schema for updating a genre
 */
export const updateGenreSchema = createGenreSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdateGenreInput = z.infer<typeof updateGenreSchema>;

/**
 * Schema for filtering genres
 */
export const genreFilterSchema = z.object({
  search: z.string().optional().default(""),
  isActive: z.boolean().optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(50).optional().default(20),
});

export type GenreFilter = z.infer<typeof genreFilterSchema>;
