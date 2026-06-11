import { z } from "zod";

export const readingHistorySeedItemSchema = z.object({
  userId: z.string().min(1),
  comicId: z.number().int().positive(),
  chapterId: z.number().int().positive(),
  startedAt: z.date().optional(),
  completedAt: z.date().optional(),
  timeSpentSeconds: z.number().int().default(0),
  progress: z.number().min(0).max(100).default(0),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const readingHistorySeedSchema = z.array(readingHistorySeedItemSchema);

export type ReadingHistorySeedItem = z.infer<typeof readingHistorySeedItemSchema>;
export type ReadingHistorySeed = z.infer<typeof readingHistorySeedSchema>;
