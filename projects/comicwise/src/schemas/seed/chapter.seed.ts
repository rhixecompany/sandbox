/**
 * Zod schema for Chapter seed data with multi-format support
 * @module chapter.seed
 *
 * Supports multiple chapter data formats:
 * - Standard: { comic: { slug, title }, name, title, releaseDate, images }
 * - Alternative: { comictitle, comicslug, chaptername, updated_at, image_urls }
 */

import { z } from "zod";

/**
 * Chapter seed schema supporting:
 * - Multiple comic reference formats (explicit comic object OR comictitle/comicslug)
 * - Multiple date field names (releaseDate, updatedAt, updated_at)
 * - Multiple image formats (images array OR image_urls array)
 * - Auto-generated slugs and chapter numbers
 */
export const chapterSeedItemSchema = z.object({
  url: z.string().url("Invalid chapter URL").optional(),

  // Chapter name/identifier (supports both 'name' and 'chaptername')
  name: z.string().min(1, "Chapter name is required").optional(),
  chaptername: z.string().min(1, "Chapter name is required").optional(),

  // Chapter title (supports both 'title' and 'chaptertitle')
  title: z.string().default("Untitled Chapter").optional(),
  chaptertitle: z.string().optional(),

  // Chapter slug (auto-generated if missing)
  slug: z.string().min(1, "Slug is required").optional(),
  chapterslug: z.string().optional(),

  // ID field (not used in insertion, for deduplication)
  id: z.string().optional(),

  // Chapter number (extracted from name if missing)
  chapterNumber: z.coerce.number().min(0, "Chapter number must be >= 0").optional(),

  // Comic reference - format 1: explicit comic object
  comic: z
    .object({
      title: z.string(),
      slug: z.string(),
    })
    .optional(),

  // Comic reference - format 2: separate comictitle/comicslug fields
  comictitle: z.string().optional(),
  comicslug: z.string().optional(),

  // Date fields - multiple possible field names
  releaseDate: z
    .union([
      z.coerce.date(),
      z.string().transform((str) => {
        try {
          return new Date(str);
        } catch {
          return new Date();
        }
      }),
    ])
    .optional(),

  updatedAt: z
    .union([
      z.coerce.date(),
      z.string().transform((str) => {
        try {
          return new Date(str);
        } catch {
          return new Date();
        }
      }),
    ])
    .optional(),

  updated_at: z
    .union([
      z.coerce.date(),
      z.string().transform((str) => {
        try {
          return new Date(str);
        } catch {
          return new Date();
        }
      }),
    ])
    .optional(),

  // Image formats - format 1: images array with url property
  images: z
    .array(
      z.object({
        url: z.string().url("Invalid image URL"),
      })
    )
    .default([])
    .optional(),

  // Image formats - format 2: image_urls array with direct strings
  image_urls: z.array(z.string().url("Invalid image URL")).default([]).optional(),

  // Optional content/text for the chapter
  content: z.string().optional(),

  // Spider source (for tracking data origin)
  spider: z.string().optional(),
});

/**
 * Array schema for multiple chapters
 */
export const chapterSeedSchema = z.array(chapterSeedItemSchema);

/**
 * Inferred TypeScript type from the Zod schema (single item)
 */
export type ChapterSeed = z.infer<typeof chapterSeedItemSchema>;

/**
 * Array type for multiple chapters
 */
export type ChapterSeedArray = z.infer<typeof chapterSeedSchema>;
