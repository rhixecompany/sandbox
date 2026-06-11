import { z } from "zod";

export const ratingSeedItemSchema = z.object({
  userId: z.string().min(1),
  comicId: z.number().int().positive(),
  rating: z.number().int().min(1).max(5),
  review: z.string().optional(),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const ratingSeedSchema = z.array(ratingSeedItemSchema);

export type RatingSeedItem = z.infer<typeof ratingSeedItemSchema>;
export type RatingSeed = z.infer<typeof ratingSeedSchema>;
