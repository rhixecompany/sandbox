import { z } from "zod";

export const followSeedItemSchema = z.object({
  followerId: z.string().min(1),
  followingId: z.string().min(1),
  createdAt: z.date().optional(),
});

export const followSeedSchema = z.array(followSeedItemSchema);

export type FollowSeedItem = z.infer<typeof followSeedItemSchema>;
export type FollowSeed = z.infer<typeof followSeedSchema>;
