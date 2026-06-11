/**
 * Reading Goals Validation Schemas
 * Zod schemas for user reading goals and progress
 */

import { z } from "zod";

/**
 * Schema for creating a new reading goal
 */
export const CreateReadingGoalSchema = z.object({
  type: z
    .enum(["daily_chapters", "weekly_comics", "monthly_minutes"])
    .describe('Goal type: "daily_chapters", "weekly_comics", or "monthly_minutes"'),
  target: z.number().int().min(1, "Target must be at least 1"),
  startDate: z.date().describe("Goal start date"),
  endDate: z.date().describe("Goal end date"),
});

export type CreateReadingGoal = z.infer<typeof CreateReadingGoalSchema>;

/**
 * Schema for updating goal progress
 */
export const UpdateGoalProgressSchema = z.object({
  goalId: z.number().int().positive("Goal ID must be positive"),
  increment: z.number().int().min(1, "Must increment by at least 1").default(1),
});

export type UpdateGoalProgress = z.infer<typeof UpdateGoalProgressSchema>;

/**
 * Schema for completing a goal
 */
export const CompleteGoalSchema = z.object({
  goalId: z.number().int().positive("Goal ID must be positive"),
});

export type CompleteGoal = z.infer<typeof CompleteGoalSchema>;

/**
 * Schema for resetting a goal
 */
export const ResetGoalSchema = z.object({
  goalId: z.number().int().positive("Goal ID must be positive"),
});

export type ResetGoal = z.infer<typeof ResetGoalSchema>;

/**
 * Schema for deleting a goal
 */
export const DeleteGoalSchema = z.object({
  goalId: z.number().int().positive("Goal ID must be positive"),
});

export type DeleteGoal = z.infer<typeof DeleteGoalSchema>;

/**
 * Schema for reading goal response
 */
export const ReadingGoalSchema = z.object({
  id: z.number().int(),
  userId: z.string().uuid(),
  type: z.enum(["daily_chapters", "weekly_comics", "monthly_minutes"]),
  target: z.number().int().min(1),
  currentCount: z.number().int().min(0),
  startDate: z.date(),
  endDate: z.date(),
  isActive: z.boolean(),
  completedAt: z.date().nullable().optional(),
  createdAt: z.date(),
  updatedAt: z.date(),
});

export type ReadingGoal = z.infer<typeof ReadingGoalSchema>;

/**
 * Schema for goal statistics
 */
export const GoalStatsSchema = z.object({
  totalGoals: z.number().int().min(0),
  activeGoals: z.number().int().min(0),
  completedGoals: z.number().int().min(0),
  completionRate: z.number().min(0).max(100),
});

export type GoalStats = z.infer<typeof GoalStatsSchema>;

/**
 * Schema for goal progress percentage
 */
export const GoalProgressSchema = z.object({
  goalId: z.number().int(),
  progress: z.number().min(0).max(100),
  currentCount: z.number().int().min(0),
  target: z.number().int().min(1),
});

export type GoalProgress = z.infer<typeof GoalProgressSchema>;

/**
 * Schema for filtering goals by type
 */
export const GoalTypeFilterSchema = z.enum(["daily_chapters", "weekly_comics", "monthly_minutes"]);

export type GoalTypeFilter = z.infer<typeof GoalTypeFilterSchema>;

/**
 * Schema for goal list response
 */
export const ReadingGoalListSchema = z.array(ReadingGoalSchema);

export type ReadingGoalList = z.infer<typeof ReadingGoalListSchema>;
