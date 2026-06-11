import { z } from "zod";

/**
 * Chapter Schema (v1.0.0)
 * Normalized internal format for chapter data
 */
export const ChapterSchema = z.object({
  _version: z.literal("1.0.0").default("1.0.0"),
  id: z.number().int().positive(),
  comicId: z.number().int().positive(),
  chapterNumber: z.number().int().positive(),
  title: z.string().max(255).nullish(),
  images: z.array(z.string().url()).default([]),
  createdAt: z.date(),
  updatedAt: z.date(),
});

export type Chapter = z.infer<typeof ChapterSchema>;

/**
 * Create chapter input schema
 */
export const CreateChapterInputSchema = z.object({
  comicId: z.number().int().positive("Comic ID is required"),
  chapterNumber: z.number().int().positive("Chapter number must be positive"),
  title: z.string().min(1).max(255).optional(),
  images: z.array(z.string().url()).optional().default([]),
  releaseDate: z.string().datetime().optional(),
});

export type CreateChapterInput = z.infer<typeof CreateChapterInputSchema>;

/**
 * Update chapter input schema
 */
export const UpdateChapterInputSchema = z.object({
  id: z.number().int().positive(),
  title: z.string().min(1).max(255).optional(),
  images: z.array(z.string().url()).optional(),
  releaseDate: z.string().datetime().optional(),
});

export type UpdateChapterInput = z.infer<typeof UpdateChapterInputSchema>;

/**
 * Bulk create chapters input schema
 */
export const BulkCreateChapterInputSchema = z.object({
  chapters: z.array(CreateChapterInputSchema),
});

export type BulkCreateChapterInput = z.infer<typeof BulkCreateChapterInputSchema>;

/**
 * @deprecated Use ChapterSchema directly. This union was for scraper compatibility.
 * Migration: Normalize all scraper outputs to ChapterSchema format with images as string[].
 */
export const ChapterSchemaLegacy = z.array(
  z.union([
    z.object({
      url: z.string(),
      name: z.string(),
      title: z.string(),
      comic: z.object({ title: z.string(), slug: z.string() }),
      updatedAt: z.string(),
    }),
    z.object({
      url: z.string(),
      name: z.string(),
      title: z.string(),
      comic: z.object({ title: z.string(), slug: z.string() }),
      updatedAt: z.string(),
      images: z.array(z.object({ url: z.string() })),
    }),
    z.object({
      url: z.string(),
      name: z.string(),
      comic: z.object({ title: z.string(), slug: z.string() }),
      updatedAt: z.string(),
      images: z.array(z.object({ url: z.string() })),
    }),
    z.object({
      url: z.string(),
      updated_at: z.string(),
      comictitle: z.string(),
      comicslug: z.string(),
      chaptername: z.string(),
      chapterslug: z.string(),
      image_urls: z.array(z.string()),
      spider: z.string(),
    }),
    z.object({
      url: z.string(),
      updated_at: z.string(),
      comictitle: z.string(),
      comicslug: z.string(),
      chaptertitle: z.string(),
      chaptername: z.string(),
      chapterslug: z.string(),
      image_urls: z.array(z.string()),
      spider: z.string(),
    }),
    z.object({
      url: z.string(),
      updated_at: z.string(),
      comictitle: z.string(),
      comicslug: z.string(),
      chaptername: z.string(),
      chapterslug: z.string(),
      image_urls: z.array(z.string()),
      images: z.array(
        z.object({
          url: z.string(),
          path: z.string(),
          checksum: z.string(),
          status: z.string(),
        })
      ),
      spider: z.string(),
    }),
    z.object({
      url: z.string(),
      updated_at: z.string(),
      comictitle: z.string(),
      comicslug: z.string(),
      chaptertitle: z.string(),
      chaptername: z.string(),
      chapterslug: z.string(),
      image_urls: z.array(z.string()),
      images: z.array(
        z.object({
          url: z.string(),
          path: z.string(),
          checksum: z.string(),
          status: z.string(),
        })
      ),
      spider: z.string(),
    }),
  ])
);
