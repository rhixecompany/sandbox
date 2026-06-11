/**
 * Reading Goals Server Actions
 * Handles CRUD operations for reading goals and progress tracking
 */

"use server";

import { revalidatePath, revalidateTag } from "next/cache.js";

import { auth } from "@/auth";
import { readingGoalsDal } from "@/dal/reading-goals-dal";
import {
  CompleteGoalSchema,
  CreateReadingGoalSchema,
  DeleteGoalSchema,
  ResetGoalSchema,
  UpdateGoalProgressSchema,
} from "@/schemas/goals.schema";

import type { ActionResult } from "@/types/actions-types";

/**
 * Extract first error message from Zod validation error
 */
function getValidationError(error: unknown): string {
  if (error instanceof Error && "flatten" in error) {
    const flat = error as { flatten: () => { fieldErrors: Record<string, (string | undefined)[]> } };
    const errors = Object.values(flat.flatten().fieldErrors).flat();
    const firstError = errors.find((e): e is string => typeof e === "string");
    return firstError || "Invalid input";
  }
  return "Invalid input";
}

/**
 * Create a new reading goal
 */
export async function createReadingGoalAction(input: unknown): Promise<
  ActionResult<{
    currentCount: number;
    goalId: number;
    isActive: boolean;
    target: number;
    type: string;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = CreateReadingGoalSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const goal = await readingGoalsDal.createGoal({
      userId: session.user.id,
      ...parsed.data,
    });

    // 4. REVALIDATE
    revalidateTag("reading-goals", "max");
    revalidateTag(`reading-goals-${session.user.id}`, "max");
    revalidatePath("/analytics");

    // 5. RETURN
    return {
      ok: true,
      data: {
        goalId: goal.id,
        type: goal.type,
        target: goal.target,
        currentCount: goal.currentCount,
        isActive: goal.isActive,
      },
    };
  } catch (error) {
    console.error("[createReadingGoalAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to create goal";
    return { ok: false, error: message };
  }
}

/**
 * Update progress on a reading goal
 */
export async function updateGoalProgressAction(input: unknown): Promise<
  ActionResult<{
    currentCount: number;
    goalId: number;
    isCompleted: boolean;
    progress: number;
    target: number;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = UpdateGoalProgressSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const goal = await readingGoalsDal.updateGoalProgress(parsed.data.goalId, parsed.data.increment);

    // 4. REVALIDATE
    revalidateTag("reading-goals", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 5. RETURN (calculateProgress: currentCount / target * 100)
    const progress = (goal.currentCount / goal.target) * 100;
    return {
      ok: true,
      data: {
        goalId: goal.id,
        currentCount: goal.currentCount,
        target: goal.target,
        progress: Math.min(progress, 100),
        isCompleted: goal.completedAt !== null,
      },
    };
  } catch (error) {
    console.error("[updateGoalProgressAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to update goal progress";
    return { ok: false, error: message };
  }
}

/**
 * Mark a reading goal as complete
 */
export async function completeGoalAction(input: unknown): Promise<
  ActionResult<{
    completedAt: Date;
    goalId: number;
    isActive: boolean;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = CompleteGoalSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const goal = await readingGoalsDal.completeGoal(parsed.data.goalId);

    // 4. REVALIDATE
    revalidateTag("reading-goals", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 5. RETURN
    return {
      ok: true,
      data: {
        goalId: goal.id,
        isActive: goal.isActive,
        completedAt: goal.completedAt!,
      },
    };
  } catch (error) {
    console.error("[completeGoalAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to complete goal";
    return { ok: false, error: message };
  }
}

/**
 * Reset a reading goal to start over
 */
export async function resetGoalAction(input: unknown): Promise<
  ActionResult<{
    currentCount: number;
    goalId: number;
    isActive: boolean;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = ResetGoalSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    const goal = await readingGoalsDal.resetGoal(parsed.data.goalId);

    // 4. REVALIDATE
    revalidateTag("reading-goals", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 5. RETURN
    return {
      ok: true,
      data: {
        goalId: goal.id,
        currentCount: goal.currentCount,
        isActive: goal.isActive,
      },
    };
  } catch (error) {
    console.error("[resetGoalAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to reset goal";
    return { ok: false, error: message };
  }
}

/**
 * Delete a reading goal
 */
export async function deleteGoalAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  // 2. VALIDATE
  const parsed = DeleteGoalSchema.safeParse(input);
  if (!parsed.success) {
    return {
      ok: false,
      error: getValidationError(parsed.error),
    };
  }

  try {
    // 3. MUTATE via DAL
    await readingGoalsDal.deleteGoal(parsed.data.goalId);

    // 4. REVALIDATE
    revalidateTag("reading-goals", "max");
    revalidateTag("reading-stats", "max");
    revalidatePath("/analytics");

    // 5. RETURN
    return {
      ok: true,
      data: { success: true },
    };
  } catch (error) {
    console.error("[deleteGoalAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to delete goal";
    return { ok: false, error: message };
  }
}

/**
 * Get all reading goals for the user
 */
export async function getUserGoalsAction(): Promise<
  ActionResult<
    Array<{
      completedAt: Date | null;
      currentCount: number;
      goalId: number;
      isActive: boolean;
      progress: number;
      target: number;
      type: string;
    }>
  >
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // 2. QUERY via DAL
    const goals = await readingGoalsDal.getUserGoals(session.user.id);

    // 3. RETURN (with progress calculated)
    return {
      ok: true,
      data: goals.map((goal) => ({
        goalId: goal.id,
        type: goal.type,
        target: goal.target,
        currentCount: goal.currentCount,
        progress: Math.min((goal.currentCount / goal.target) * 100, 100),
        isActive: goal.isActive,
        completedAt: goal.completedAt,
      })),
    };
  } catch (error) {
    console.error("[getUserGoalsAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to fetch goals";
    return { ok: false, error: message };
  }
}

/**
 * Get goal statistics for the user
 */
export async function getGoalStatsAction(): Promise<
  ActionResult<{
    activeGoals: number;
    completedGoals: number;
    completionRate: number;
    totalGoals: number;
  }>
> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    // 2. QUERY via DAL
    const stats = await readingGoalsDal.getGoalStats(session.user.id);

    // 3. RETURN
    return {
      ok: true,
      data: {
        totalGoals: stats.totalGoals,
        activeGoals: stats.activeGoals,
        completedGoals: stats.completedGoals,
        completionRate: stats.completionRate,
      },
    };
  } catch (error) {
    console.error("[getGoalStatsAction] Failed:", error);
    const message = error instanceof Error ? error.message : "Failed to fetch goal stats";
    return { ok: false, error: message };
  }
}
