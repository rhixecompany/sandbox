import { z } from "zod";

export const commentSeedItemSchema = z.object({
  content: z.string().min(1),
  userId: z.string().min(1),
  chapterId: z.number().int().positive(),
  parentId: z.number().int().positive().optional(),
  deletedAt: z.date().optional(),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const commentSeedSchema = z.array(commentSeedItemSchema);

export type CommentSeedItem = z.infer<typeof commentSeedItemSchema>;
export type CommentSeed = z.infer<typeof commentSeedSchema>;
