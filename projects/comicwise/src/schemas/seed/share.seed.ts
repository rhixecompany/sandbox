import { z } from "zod";

export const shareSeedItemSchema = z.object({
  userId: z.string().min(1),
  resourceType: z.enum([
    "comic",
    "chapter",
    "user",
    "comment",
    "rating",
    "bookmark",
    "notification",
    "author",
    "artist",
    "genre",
    "type",
    "system",
  ]),
  resourceId: z.number().int().positive(),
  message: z.string().optional(),
  createdAt: z.date().optional(),
});

export const shareSeedSchema = z.array(shareSeedItemSchema);

export type ShareSeedItem = z.infer<typeof shareSeedItemSchema>;
export type ShareSeed = z.infer<typeof shareSeedSchema>;
