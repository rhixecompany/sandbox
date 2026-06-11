import { z } from "zod";

export const notificationSeedItemSchema = z.object({
  userId: z.string().min(1),
  type: z.string().min(1),
  title: z.string().min(1),
  message: z.string().min(1),
  link: z.string().optional(),
  read: z.boolean().default(false),
  comicId: z.number().int().positive().optional(),
  chapterId: z.number().int().positive().optional(),
  createdAt: z.date().optional(),
});

export const notificationSeedSchema = z.array(notificationSeedItemSchema);

export type NotificationSeedItem = z.infer<typeof notificationSeedItemSchema>;
export type NotificationSeed = z.infer<typeof notificationSeedSchema>;
