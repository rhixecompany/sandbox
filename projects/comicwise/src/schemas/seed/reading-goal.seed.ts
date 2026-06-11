import { z } from "zod";

export const readingGoalSeedItemSchema = z.object({
  userId: z.string().min(1),
  type: z.enum(["daily_chapters", "weekly_comics", "monthly_minutes"]),
  target: z.number().int().positive(),
  currentCount: z.number().int().default(0),
  startDate: z.date(),
  endDate: z.date(),
  isActive: z.boolean().default(true),
  completedAt: z.date().optional(),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
});

export const readingGoalSeedSchema = z.array(readingGoalSeedItemSchema);

export type ReadingGoalSeedItem = z.infer<typeof readingGoalSeedItemSchema>;
export type ReadingGoalSeed = z.infer<typeof readingGoalSeedSchema>;
