import { z } from "zod";

export const bookmarkSeedItemSchema = z.object({
  userId: z.string().min(1),
  comicId: z.number().int().positive(),
  lastReadChapterId: z.number().int().positive().optional(),
  status: z.string().default("Reading"),
  notes: z.string().optional(),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const bookmarkSeedSchema = z.array(bookmarkSeedItemSchema);

export type BookmarkSeedItem = z.infer<typeof bookmarkSeedItemSchema>;
export type BookmarkSeed = z.infer<typeof bookmarkSeedSchema>;
