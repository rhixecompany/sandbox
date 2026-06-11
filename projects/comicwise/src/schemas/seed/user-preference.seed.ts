import { z } from "zod";

export const userPreferenceSeedItemSchema = z.object({
  userId: z.string().min(1),
  theme: z.enum(["light", "dark", "system"]).default("system"),
  defaultLayout: z.enum(["webtoon", "comic", "book"]).default("webtoon"),
  pageNavigationStyle: z.enum(["buttons", "swipe", "click"]).default("buttons"),
  fontSize: z.number().int().default(16),
  lineHeight: z.enum(["compact", "normal", "relaxed"]).default("normal"),
  notifyNewChapters: z.boolean().default(true),
  notifyComments: z.boolean().default(true),
  notifyBookmarkUpdates: z.boolean().default(false),
  profilePublic: z.boolean().default(false),
  showReadingHistory: z.boolean().default(false),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const userPreferenceSeedSchema = z.array(userPreferenceSeedItemSchema);

export type UserPreferenceSeedItem = z.infer<typeof userPreferenceSeedItemSchema>;
export type UserPreferenceSeed = z.infer<typeof userPreferenceSeedSchema>;
