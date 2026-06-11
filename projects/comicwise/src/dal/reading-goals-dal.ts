/**
 * Reading Goals DAL
 * Manages user reading goals and progress tracking
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { readingGoal } from "@/database/schema";

import { BaseDal } from "./base-dal";

type ReadingGoalType = typeof readingGoal.$inferSelect;

export type ReadingGoalInput = {
  endDate: Date;
  startDate: Date;
  target: number;
  type: "daily_chapters" | "monthly_minutes" | "weekly_comics";
  userId: string;
};

export class ReadingGoalsDal extends BaseDal<ReadingGoalType> {
  // Implement abstract methods
  async list(): Promise<ReadingGoalType[]> {
    return db.query.readingGoal.findMany({ limit: 100 });
  }

  async getById(id: number | string): Promise<null | ReadingGoalType> {
    const numId = typeof id === "string" ? parseInt(id) : id;
    const [result] = await db.select().from(readingGoal).where(eq(readingGoal.id, numId)).limit(1);
    return result || null;
  }

  async create(): Promise<ReadingGoalType> {
    throw new Error("Use createGoal() instead");
  }

  async update(): Promise<ReadingGoalType> {
    throw new Error("Use updateGoalProgress() instead");
  }

  async delete(id: number | string): Promise<void> {
    const numId = typeof id === "string" ? parseInt(id) : id;
    await db.delete(readingGoal).where(eq(readingGoal.id, numId));
  }

  // Business methods
  async createGoal(input: ReadingGoalInput): Promise<ReadingGoalType> {
    const [result] = await db
      .insert(readingGoal)
      .values({
        userId: input.userId,
        type: input.type,
        target: input.target,
        currentCount: 0,
        startDate: input.startDate,
        endDate: input.endDate,
        isActive: true,
      })
      .returning();

    if (!result) {
      throw new Error("Failed to create reading goal");
    }

    return result;
  }

  async getActiveGoals(userId: string): Promise<ReadingGoalType[]> {
    return db.query.readingGoal.findMany({
      where: and(eq(readingGoal.userId, userId), eq(readingGoal.isActive, true)),
      orderBy: [desc(readingGoal.endDate)],
    });
  }

  async getUserGoals(userId: string): Promise<ReadingGoalType[]> {
    return db.query.readingGoal.findMany({
      where: eq(readingGoal.userId, userId),
      orderBy: [desc(readingGoal.createdAt)],
    });
  }

  async getGoalById(goalId: number): Promise<null | ReadingGoalType> {
    const [result] = await db.select().from(readingGoal).where(eq(readingGoal.id, goalId)).limit(1);

    return result || null;
  }

  async updateGoalProgress(goalId: number, increment: number = 1): Promise<ReadingGoalType> {
    const goal = await this.getGoalById(goalId);

    if (!goal) {
      throw new Error(`Goal with id ${goalId} not found`);
    }

    const newCount = goal.currentCount + increment;
    const isCompleted = newCount >= goal.target;

    const [result] = await db
      .update(readingGoal)
      .set({
        currentCount: newCount,
        completedAt: isCompleted ? new Date() : goal.completedAt,
        isActive: isCompleted ? false : goal.isActive,
        updatedAt: new Date(),
      })
      .where(eq(readingGoal.id, goalId))
      .returning();

    if (!result) {
      throw new Error("Failed to update goal progress");
    }

    return result;
  }

  async completeGoal(goalId: number): Promise<ReadingGoalType> {
    const [result] = await db
      .update(readingGoal)
      .set({
        isActive: false,
        completedAt: new Date(),
        updatedAt: new Date(),
      })
      .where(eq(readingGoal.id, goalId))
      .returning();

    if (!result) {
      throw new Error("Failed to complete goal");
    }

    return result;
  }

  async resetGoal(goalId: number): Promise<ReadingGoalType> {
    const [result] = await db
      .update(readingGoal)
      .set({
        currentCount: 0,
        completedAt: null,
        isActive: true,
        updatedAt: new Date(),
      })
      .where(eq(readingGoal.id, goalId))
      .returning();

    if (!result) {
      throw new Error("Failed to reset goal");
    }

    return result;
  }

  async deleteGoal(goalId: number): Promise<void> {
    await db.delete(readingGoal).where(eq(readingGoal.id, goalId));
  }

  async getGoalProgress(goalId: number): Promise<number> {
    const goal = await this.getGoalById(goalId);

    if (!goal) {
      return 0;
    }

    return Math.min(Math.round((goal.currentCount / goal.target) * 100), 100);
  }

  async getGoalsByType(
    userId: string,
    type: "daily_chapters" | "monthly_minutes" | "weekly_comics"
  ): Promise<ReadingGoalType[]> {
    return db.query.readingGoal.findMany({
      where: and(eq(readingGoal.userId, userId), eq(readingGoal.type, type)),
      orderBy: [desc(readingGoal.createdAt)],
    });
  }

  async getGoalStats(userId: string): Promise<{
    activeGoals: number;
    completedGoals: number;
    completionRate: number;
    totalGoals: number;
  }> {
    const goals = await this.getUserGoals(userId);

    if (goals.length === 0) {
      return {
        totalGoals: 0,
        activeGoals: 0,
        completedGoals: 0,
        completionRate: 0,
      };
    }

    const activeGoals = goals.filter((g) => g.isActive).length;
    const completedGoals = goals.filter((g) => g.completedAt && !g.isActive).length;

    return {
      totalGoals: goals.length,
      activeGoals,
      completedGoals,
      completionRate: Math.round((completedGoals / goals.length) * 100),
    };
  }

  async checkAndCompleteGoals(userId: string): Promise<ReadingGoalType[]> {
    const goals = await this.getActiveGoals(userId);
    const completedGoals: ReadingGoalType[] = [];

    for (const goal of goals) {
      if (goal.currentCount >= goal.target && goal.isActive) {
        const completed = await this.completeGoal(goal.id);
        completedGoals.push(completed);
      }
    }

    return completedGoals;
  }
}

export const readingGoalsDal = new ReadingGoalsDal();
