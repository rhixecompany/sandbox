/**
 * Reading Dashboard Component
 * Main analytics dashboard orchestrating all reading analytics components
 */

import { Suspense } from "react";

import { getUserGoalsAction } from "@/actions/goals.actions";
import { getReadingHistoryAction, getReadingStatsAction } from "@/actions/reading.actions";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

import { ReadingGoalsWidget, ReadingGoalsWidgetSkeleton } from "./reading-goals-widget";
import { ReadingHistoryTimeline, ReadingHistoryTimelineSkeleton } from "./reading-history-timeline";
import { ReadingStatsCard, ReadingStatsCardSkeleton } from "./reading-stats-card";

interface ReadingDashboardProps {
  /**
   * Time period filter: "all", "30days", "7days"
   */
  timePeriod?: string;
}

/**
 * Stats section - async data fetching
 */
async function StatsSection({ timePeriod }: { timePeriod?: string }) {
  try {
    let startDate: Date | undefined;

    if (timePeriod === "7days") {
      startDate = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    } else if (timePeriod === "30days") {
      startDate = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);
    }

    const result = await getReadingStatsAction(startDate);

    if (!result.ok) {
      throw new Error(result.error);
    }

    return (
      <ReadingStatsCard
        averageTimePerChapter={result.data.averageTimePerChapter}
        totalChaptersRead={result.data.totalChaptersRead}
        totalComicsRead={result.data.totalComicsRead}
        totalMinutesSpent={result.data.totalMinutesSpent}
      />
    );
  } catch (error) {
    console.error("[StatsSection] Error:", error);
    return (
      <Card className="border-destructive/50">
        <CardHeader>
          <CardTitle className="text-destructive">Unable to Load Statistics</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            There was an error loading your reading statistics. Please try again later.
          </p>
        </CardContent>
      </Card>
    );
  }
}

/**
 * History section - async data fetching
 */
async function HistorySection({ timePeriod }: { timePeriod?: string }) {
  try {
    let startDate: Date | undefined;

    if (timePeriod === "7days") {
      startDate = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    } else if (timePeriod === "30days") {
      startDate = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);
    }

    const result = await getReadingHistoryAction(undefined, 20, 0, startDate);

    if (!result.ok) {
      throw new Error(result.error);
    }

    const entries = result.data.map((h) => ({
      id: h.id,
      comicId: h.comicId,
      comicTitle: "Comic Title", // TODO: Fetch actual comic title
      chapterId: h.chapterId,
      chapterNumber: h.progress,
      startedAt: h.startedAt,
      completedAt: h.completedAt,
      timeSpentSeconds: h.timeSpentSeconds,
      progress: h.progress,
    }));

    return (
      <ReadingHistoryTimeline
        entries={entries}
        hasMore={entries.length >= 20}
        onLoadMore={async () => {
          // TODO: Implement pagination
        }}
      />
    );
  } catch (error) {
    console.error("[HistorySection] Error:", error);
    return (
      <Card className="border-destructive/50">
        <CardHeader>
          <CardTitle className="text-destructive">Unable to Load History</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            There was an error loading your reading history. Please try again later.
          </p>
        </CardContent>
      </Card>
    );
  }
}

/**
 * Goals section - async data fetching
 */
async function GoalsSection() {
  try {
    const result = await getUserGoalsAction();

    if (!result.ok) {
      throw new Error(result.error);
    }

    return (
      <ReadingGoalsWidget
        goals={result.data.map((g) => ({
          goalId: g.goalId,
          type: g.type,
          target: g.target,
          currentCount: g.currentCount,
          progress: g.progress,
          isActive: g.isActive,
          completedAt: g.completedAt,
        }))}
        onAddGoal={() => {
          // TODO: Open add goal dialog
        }}
      />
    );
  } catch (error) {
    console.error("[GoalsSection] Error:", error);
    return (
      <Card className="border-destructive/50">
        <CardHeader>
          <CardTitle className="text-destructive">Unable to Load Goals</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            There was an error loading your reading goals. Please try again later.
          </p>
        </CardContent>
      </Card>
    );
  }
}

/**
 * Tips/Insights card
 */
function InsightsCard() {
  return (
    <Card className="border-muted-foreground/20 dark:border-muted-foreground/10">
      <CardHeader className="pb-4">
        <CardTitle className="text-foreground dark:text-foreground">Tips & Insights</CardTitle>
      </CardHeader>
      <CardContent>
        <ul className="space-y-3 text-sm">
          <li className="flex gap-2">
            <span className="text-primary dark:text-primary">→</span>
            <span className="text-muted-foreground dark:text-muted-foreground">
              Set reading goals to stay motivated and track your progress
            </span>
          </li>
          <li className="flex gap-2">
            <span className="text-primary dark:text-primary">→</span>
            <span className="text-muted-foreground dark:text-muted-foreground">
              Check your reading history to identify your favorite reading times
            </span>
          </li>
          <li className="flex gap-2">
            <span className="text-primary dark:text-primary">→</span>
            <span className="text-muted-foreground dark:text-muted-foreground">
              Keep consistent reading habits to build a stronger reading streak
            </span>
          </li>
        </ul>
      </CardContent>
    </Card>
  );
}

/**
 * Reading Dashboard - main component
 */
export function ReadingDashboard({ timePeriod = "all" }: ReadingDashboardProps) {
  return (
    <div className="space-y-6">
      {/* Statistics section */}
      <Suspense fallback={<ReadingStatsCardSkeleton />}>
        <StatsSection timePeriod={timePeriod} />
      </Suspense>

      {/* Main content grid */}
      <div className="grid gap-6 lg:grid-cols-3">
        {/* Timeline - takes 2 columns on desktop */}
        <div className="lg:col-span-2">
          <Suspense fallback={<ReadingHistoryTimelineSkeleton />}>
            <HistorySection timePeriod={timePeriod} />
          </Suspense>
        </div>

        {/* Right sidebar - takes 1 column on desktop */}
        <div className="space-y-6">
          {/* Goals widget */}
          <Suspense fallback={<ReadingGoalsWidgetSkeleton />}>
            <GoalsSection />
          </Suspense>

          {/* Tips card */}
          <InsightsCard />
        </div>
      </div>
    </div>
  );
}
