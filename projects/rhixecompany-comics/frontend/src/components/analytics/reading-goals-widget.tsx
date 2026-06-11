/**
 * Reading Goals Widget Component
 * Displays and manages reading goals with progress tracking
 */

"use client";

import { Plus, RotateCcw, Trash2, Trophy } from "lucide-react";
import { useRouter } from "next/navigation";
import { useTransition } from "react";

import { completeGoalAction, deleteGoalAction, resetGoalAction } from "@/actions/goals.actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface GoalWithProgress {
  completedAt: Date | null;
  currentCount: number;
  goalId: number;
  isActive: boolean;
  progress: number;
  target: number;
  type: string;
}

interface ReadingGoalsWidgetProps {
  goals: GoalWithProgress[];
  isLoading?: boolean;
  onAddGoal?: () => void;
}

/**
 * Get goal type label and icon
 */
function getGoalTypeInfo(type: string): { color: string; label: string; unit: string } {
  switch (type) {
    case "daily_chapters":
      return { label: "Daily Chapters", unit: " chapters/day", color: "from-blue-500 to-blue-600" };
    case "weekly_comics":
      return { label: "Weekly Comics", unit: " comics/week", color: "from-purple-500 to-purple-600" };
    case "monthly_minutes":
      return { label: "Monthly Minutes", unit: " min/month", color: "from-orange-500 to-orange-600" };
    default:
      return { label: "Reading Goal", unit: "", color: "from-gray-500 to-gray-600" };
  }
}

/**
 * Goal progress bar component
 */
function GoalProgressBar({ progress, color }: { color: string; progress: number }) {
  return (
    <div className="relative h-2 overflow-hidden rounded-full bg-muted dark:bg-muted/50">
      <div
        className={`h-full bg-linear-to-r ${color} transition-all duration-300`}
        style={{ width: `${Math.min(progress, 100)}%` }}
      />
    </div>
  );
}

/**
 * Individual goal card
 */
function GoalCard({
  goal,
  onComplete,
  onReset,
  onDelete,
  isLoading,
}: {
  goal: GoalWithProgress;
  isLoading: boolean;
  onComplete: (goalId: number) => void;
  onDelete: (goalId: number) => void;
  onReset: (goalId: number) => void;
}) {
  const typeInfo = getGoalTypeInfo(goal.type);
  const isCompleted = goal.completedAt !== null;
  const daysRemaining = 0; // TODO: Calculate from goal dates

  return (
    <div className="space-y-3 rounded-lg border border-muted-foreground/20 p-4 dark:border-muted-foreground/10">
      {/* Goal header */}
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <h3 className="font-semibold text-foreground dark:text-foreground">{typeInfo.label}</h3>
            {isCompleted && <Trophy className="h-4 w-4 text-green-600 dark:text-green-500" />}
          </div>
          <p className="text-sm text-muted-foreground dark:text-muted-foreground">
            {goal.currentCount} / {goal.target}
            {typeInfo.unit}
          </p>
        </div>
      </div>

      {/* Progress bar */}
      <GoalProgressBar color={typeInfo.color} progress={goal.progress} />

      {/* Progress text */}
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium text-foreground dark:text-foreground">{Math.round(goal.progress)}%</span>
        {daysRemaining > 0 && (
          <span className="text-xs text-muted-foreground dark:text-muted-foreground">{daysRemaining} days left</span>
        )}
      </div>

      {/* Action buttons */}
      <div className="flex gap-2 pt-2">
        {!isCompleted && (
          <Button
            className="h-8 flex-1 text-xs"
            disabled={isLoading || !goal.isActive}
            onClick={() => onComplete(goal.goalId)}
            variant="default"
          >
            Complete
          </Button>
        )}
        {isCompleted && (
          <Button
            className="h-8 flex-1 text-xs"
            disabled={isLoading}
            onClick={() => onReset(goal.goalId)}
            variant="outline"
          >
            <RotateCcw className="h-3 w-3" />
            Reset
          </Button>
        )}
        <Button
          className="h-8 px-2"
          disabled={isLoading}
          onClick={() => onDelete(goal.goalId)}
          size="sm"
          variant="ghost"
        >
          <Trash2 className="h-4 w-4 text-destructive dark:text-destructive" />
        </Button>
      </div>
    </div>
  );
}

/**
 * Reading Goals Widget
 */
export function ReadingGoalsWidget({ goals, isLoading = false, onAddGoal }: ReadingGoalsWidgetProps) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  const handleComplete = (goalId: number) => {
    startTransition(async () => {
      const result = await completeGoalAction({ goalId });
      if (result.ok) {
        router.refresh();
      }
    });
  };

  const handleReset = (goalId: number) => {
    startTransition(async () => {
      const result = await resetGoalAction({ goalId });
      if (result.ok) {
        router.refresh();
      }
    });
  };

  const handleDelete = (goalId: number) => {
    startTransition(async () => {
      const result = await deleteGoalAction({ goalId });
      if (result.ok) {
        router.refresh();
      }
    });
  };

  const activeGoals = goals.filter((g) => g.isActive);
  const completedGoals = goals.filter((g) => !g.isActive && g.completedAt);

  if (isLoading && goals.length === 0) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Reading Goals</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {([0, 1] as const).map((_, i) => (
              <div className="h-24 animate-pulse rounded bg-muted dark:bg-muted" key={i} />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  const isEmpty = goals.length === 0;

  return (
    <Card className="border-muted-foreground/20 dark:border-muted-foreground/10">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-4">
        <div>
          <CardTitle className="text-foreground dark:text-foreground">Reading Goals</CardTitle>
          <p className="mt-1 text-sm text-muted-foreground dark:text-muted-foreground">Track your reading targets</p>
        </div>
        <Button className="gap-2 dark:border-muted-foreground/30" onClick={onAddGoal} size="sm" variant="outline">
          <Plus className="h-4 w-4" />
          <span className="hidden sm:inline">Add Goal</span>
        </Button>
      </CardHeader>
      <CardContent className="space-y-6">
        {isEmpty ? (
          <div className="rounded-lg border-2 border-dashed border-muted-foreground/30 p-6 text-center dark:border-muted-foreground/20">
            <Trophy className="mx-auto h-8 w-8 text-muted-foreground/50 dark:text-muted-foreground/40" />
            <p className="mt-2 text-sm text-muted-foreground dark:text-muted-foreground">
              No reading goals yet. Create one to get started!
            </p>
          </div>
        ) : (
          <>
            {/* Active goals */}
            {activeGoals.length > 0 && (
              <div className="space-y-3">
                <h3 className="text-sm font-semibold text-foreground dark:text-foreground">Active Goals</h3>
                <div className="space-y-3">
                  {activeGoals.map((goal) => (
                    <GoalCard
                      goal={goal}
                      isLoading={isPending}
                      key={goal.goalId}
                      onComplete={handleComplete}
                      onDelete={handleDelete}
                      onReset={handleReset}
                    />
                  ))}
                </div>
              </div>
            )}

            {/* Completed goals */}
            {completedGoals.length > 0 && (
              <div className="space-y-3 border-t border-muted-foreground/20 pt-6 dark:border-muted-foreground/10">
                <h3 className="text-sm font-semibold text-foreground dark:text-foreground">Completed Goals</h3>
                <div className="space-y-3">
                  {completedGoals.map((goal) => (
                    <GoalCard
                      goal={goal}
                      isLoading={isPending}
                      key={goal.goalId}
                      onComplete={handleComplete}
                      onDelete={handleDelete}
                      onReset={handleReset}
                    />
                  ))}
                </div>
              </div>
            )}
          </>
        )}
      </CardContent>
    </Card>
  );
}

/**
 * Reading Goals Widget Loading Skeleton
 */
export function ReadingGoalsWidgetSkeleton() {
  return <ReadingGoalsWidget goals={[]} isLoading />;
}
