/**
 * Zod schema for Genre seed data
 * @module genre.seed
 */

import { z } from "zod";

/**
 * Genre seed item schema
 */
export const genreSeedItemSchema = z.object({
  name: z.string().min(1, "Genre name is required"),
  slug: z.string().min(1, "Genre slug is required"),
  description: z.string().optional(),
});

/**
 * Array schema for multiple genres
 */
export const genreSeedSchema = z.array(genreSeedItemSchema);

/**
 * Inferred TypeScript type from the Zod schema (single item)
 */
export type GenreSeed = z.infer<typeof genreSeedItemSchema>;

/**
 * Array type for multiple genres
 */
export type GenreSeedArray = z.infer<typeof genreSeedSchema>;
