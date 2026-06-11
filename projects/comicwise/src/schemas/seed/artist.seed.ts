/**
 * Zod schema for Artist seed data
 * @module artist.seed
 */

import { z } from "zod";

/**
 * Artist seed item schema
 */
export const artistSeedItemSchema = z.object({
  name: z.string().min(1, "Artist name is required"),
  url: z.string().url("Invalid URL").optional(),
  bio: z.string().optional(),
});

/**
 * Array schema for multiple artists
 */
export const artistSeedSchema = z.array(artistSeedItemSchema);

/**
 * Inferred TypeScript type from the Zod schema (single item)
 */
export type ArtistSeed = z.infer<typeof artistSeedItemSchema>;

/**
 * Array type for multiple artists
 */
export type ArtistSeedArray = z.infer<typeof artistSeedSchema>;
