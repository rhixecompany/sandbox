/**
 * Reading Stats Card Component
 * Displays aggregated reading statistics in a responsive grid layout
 */

import { Book, Clock, TrendingUp, Zap } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface ReadingStatsCardProps {
  averageTimePerChapter: number;
  isLoading?: boolean;
  totalChaptersRead: number;
  totalComicsRead: number;
  totalMinutesSpent: number;
}

interface StatItemProps {
  icon: React.ReactNode;
  label: string;
  unit?: string;
  value: number | string;
}

/**
 * Individual stat item with icon and value
 */
function StatItem({ icon, label, value, unit }: StatItemProps) {
  return (
    <div className="flex items-start gap-4">
      <div className="rounded-lg bg-primary/10 p-2 dark:bg-primary/5">
        <div className="text-primary dark:text-primary">{icon}</div>
      </div>
      <div className="flex-1">
        <p className="text-sm font-medium text-muted-foreground dark:text-muted-foreground">{label}</p>
        <div className="mt-1 flex items-baseline gap-1">
          <p className="text-2xl font-bold text-foreground dark:text-foreground">{value}</p>
          {unit && <span className="text-sm text-muted-foreground dark:text-muted-foreground">{unit}</span>}
        </div>
      </div>
    </div>
  );
}

/**
 * Reading Stats Card - displays key reading metrics
 */
export function ReadingStatsCard({
  totalChaptersRead,
  totalMinutesSpent,
  totalComicsRead,
  averageTimePerChapter,
  isLoading = false,
}: ReadingStatsCardProps) {
  if (isLoading) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Reading Statistics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {([0, 1, 2, 3] as const).map((_, i) => (
              <div className="h-20 animate-pulse rounded bg-muted dark:bg-muted" key={i} />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="border-muted-foreground/20 dark:border-muted-foreground/10">
      <CardHeader className="pb-4">
        <CardTitle className="text-foreground dark:text-foreground">Reading Statistics</CardTitle>
        <p className="mt-1 text-sm text-muted-foreground dark:text-muted-foreground">Your reading activity overview</p>
      </CardHeader>
      <CardContent>
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
          <StatItem icon={<Book className="h-5 w-5" />} label="Chapters Read" value={totalChaptersRead} />
          <StatItem
            icon={<Clock className="h-5 w-5" />}
            label="Time Spent"
            unit="hours"
            value={Math.round(totalMinutesSpent / 60)}
          />
          <StatItem icon={<TrendingUp className="h-5 w-5" />} label="Comics Completed" value={totalComicsRead} />
          <StatItem
            icon={<Zap className="h-5 w-5" />}
            label="Avg Time/Chapter"
            unit="min"
            value={Math.round(averageTimePerChapter)}
          />
        </div>
      </CardContent>
    </Card>
  );
}

/**
 * Reading Stats Card Loading Skeleton
 */
export function ReadingStatsCardSkeleton() {
  return (
    <ReadingStatsCard
      averageTimePerChapter={0}
      isLoading
      totalChaptersRead={0}
      totalComicsRead={0}
      totalMinutesSpent={0}
    />
  );
}
