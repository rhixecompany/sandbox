import { z } from "zod";

export const readerSettingsSeedItemSchema = z.object({
  userId: z.string().min(1),
  backgroundMode: z.enum(["white", "black", "sepia"]).default("white"),
  readingMode: z.enum(["vertical", "horizontal", "webtoon"]).default("vertical"),
  defaultQuality: z.enum(["low", "medium", "high"]).default("medium"),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const readerSettingsSeedSchema = z.array(readerSettingsSeedItemSchema);

export type ReaderSettingsSeedItem = z.infer<typeof readerSettingsSeedItemSchema>;
export type ReaderSettingsSeed = z.infer<typeof readerSettingsSeedSchema>;
