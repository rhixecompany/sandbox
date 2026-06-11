/**
 * Zod schema for Author seed data
 * @module author.seed
 */

import { z } from "zod";

/**
 * Author seed item schema
 */
export const authorSeedItemSchema = z.object({
  name: z.string().min(1, "Author name is required"),
  url: z.string().url("Invalid URL").optional(),
  bio: z.string().optional(),
});

/**
 * Array schema for multiple authors
 */
export const authorSeedSchema = z.array(authorSeedItemSchema);

/**
 * Inferred TypeScript type from the Zod schema (single item)
 */
export type AuthorSeed = z.infer<typeof authorSeedItemSchema>;

/**
 * Array type for multiple authors
 */
export type AuthorSeedArray = z.infer<typeof authorSeedSchema>;
