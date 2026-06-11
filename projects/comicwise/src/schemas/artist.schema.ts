/**
 * Artist-related Zod schemas
 * Validates artist queries, filters, and mutations
 */

import { z } from "zod";

/**
 * Schema for creating a new artist (admin only)
 */
export const createArtistSchema = z.object({
  name: z.string().min(1, "Name is required").max(255),
  bio: z.string().max(2000).optional(),
  image: z.string().url().optional().nullable(),
  isActive: z.boolean().optional().default(true),
});

export type CreateArtistInput = z.infer<typeof createArtistSchema>;

/**
 * Schema for updating an artist
 */
export const updateArtistSchema = createArtistSchema.partial().extend({
  id: z.number().int().positive(),
});

export type UpdateArtistInput = z.infer<typeof updateArtistSchema>;

/**
 * Schema for filtering artists
 */
export const artistFilterSchema = z.object({
  search: z.string().optional().default(""),
  isActive: z.boolean().optional(),
  page: z.number().int().min(1).optional().default(1),
  limit: z.number().int().min(1).max(50).optional().default(20),
});

export type ArtistFilter = z.infer<typeof artistFilterSchema>;
