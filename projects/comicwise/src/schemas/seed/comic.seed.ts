/**
 * Zod schema for Comic seed data with relation resolution
 * @module comic.seed
 */

import { z } from "zod";

/**
 * Comic status enum - must be Title-Case per database constraint
 */
const comicStatusEnum = z.enum(["Ongoing", "Completed", "Hiatus", "Dropped", "Season End", "Coming Soon"]);

/**
 * Comic seed schema with support for multiple JSON format variants
 * Handles nested author/artist/type/genres objects that will be resolved to FK IDs
 */
export const comicSeedItemSchema = z.object({
  title: z.string().min(1, "Title is required"),
  slug: z.string().min(1, "Slug is required"),
  description: z.string().default("").optional(),
  url: z.string().url("Invalid URL").optional(),
  rating: z.coerce.number().min(0, "Rating must be >= 0").max(10, "Rating must be <= 10").default(0),
  status: comicStatusEnum.default("Ongoing"),
  serialization: z.string().optional(),
  updatedAt: z
    .union([z.instanceof(Date), z.number(), z.string()])
    .transform((val) => {
      if (val instanceof Date) {
        return val;
      }
      if (typeof val === "number") {
        return new Date(val);
      }
      try {
        const parsed = new Date(val);
        return !isNaN(parsed.getTime()) ? parsed : new Date();
      } catch {
        return new Date();
      }
    })
    .default(() => new Date()),
  views: z.coerce.number().min(0).default(0),
  coverImage: z.string().url("Invalid cover image URL").nullable().optional(),

  // Relations - will be resolved to IDs during seeding
  type: z
    .union([
      z.object({ name: z.string() }),
      z.string(), // Handle "Manhwa" / "Manhua" type directly
    ])
    .optional()
    .transform((val) => {
      if (!val) return undefined;
      if (typeof val === "string") {
        return { name: val };
      }
      return val;
    }),

  author: z
    .union([
      z.object({ name: z.string() }),
      z.string(), // Handle string author names
    ])
    .nullable()
    .optional()
    .transform((val) => {
      if (!val || val === "_") return undefined;
      if (typeof val === "string") {
        return { name: val };
      }
      return val;
    }),

  artist: z
    .union([
      z.object({ name: z.string() }),
      z.string(), // Handle string artist names
    ])
    .nullable()
    .optional()
    .transform((val) => {
      if (!val || val === "_") return undefined;
      if (typeof val === "string") {
        return { name: val };
      }
      return val;
    }),

  // Handle both "genres" array and "category" single field
  category: z.string().optional(), // Alternative single-genre field
  genres: z
    .union([
      z.array(
        z.union([
          z.object({ name: z.string() }),
          z.string(), // Handle string genre names
        ])
      ),
      z.string(), // Single category field
    ])
    .default([])
    .transform((val) => {
      if (typeof val === "string") {
        return [{ name: val }];
      }
      if (Array.isArray(val)) {
        return val.map((g) => (typeof g === "string" ? { name: g } : g));
      }
      return [];
    }),

  // Images for comic cover variants
  images: z
    .array(z.union([z.object({ url: z.string().url("Invalid image URL") }), z.string().url("Invalid image URL")]))
    .default([])
    .transform((items) => {
      return items.map((item) => (typeof item === "string" ? { url: item } : item));
    }),
});

/**
 * Array schema for multiple comics
 */

export const comicSeedSchema = z.array(comicSeedItemSchema);

/**
 * Inferred TypeScript type from the Zod schema (single item)
 */
export type ComicSeed = z.infer<typeof comicSeedItemSchema>;

/**
 * Array type for multiple comics
 */
export type ComicSeedArray = z.infer<typeof comicSeedSchema>;

/**
 * Single comic seed item type (for compatibility)
 */
export type ComicSeedItem = z.infer<typeof comicSeedItemSchema>;
