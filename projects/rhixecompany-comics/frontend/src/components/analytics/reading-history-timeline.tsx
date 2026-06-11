/**
 * Reading History Timeline Component
 * Displays user's reading history in a vertical timeline format
 */

"use client";

import { formatDistanceToNow } from "date-fns";
import { ChevronDown } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface HistoryEntry {
  chapterId: number;
  chapterNumber: string;
  comicCover?: string;
  comicId: number;
  comicTitle: string;
  completedAt: Date | null;
  id: number;
  progress: string;
  startedAt: Date;
  timeSpentSeconds: number;
}

interface ReadingHistoryTimelineProps {
  entries: HistoryEntry[];
  hasMore?: boolean;
  isLoading?: boolean;
  onLoadMore?: () => Promise<void>;
}

/**
 * Group history entries by date
 */
function groupByDate(entries: HistoryEntry[]): Record<string, HistoryEntry[]> {
  const today = new Date();
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);

  const groups: Record<string, HistoryEntry[]> = {
    Today: [],
    Yesterday: [],
    "This Week": [],
    Older: [],
  };

  for (const entry of entries) {
    const entryDate = new Date(entry.startedAt);
    const entryDateOnly = new Date(entryDate.getFullYear(), entryDate.getMonth(), entryDate.getDate());
    const todayOnly = new Date(today.getFullYear(), today.getMonth(), today.getDate());
    const yesterdayOnly = new Date(yesterday.getFullYear(), yesterday.getMonth(), yesterday.getDate());

    if (entryDateOnly.getTime() === todayOnly.getTime()) {
      groups.Today.push(entry);
    } else if (entryDateOnly.getTime() === yesterdayOnly.getTime()) {
      groups.Yesterday.push(entry);
    } else if (entryDateOnly.getTime() > todayOnly.getTime() - 7 * 24 * 60 * 60 * 1000) {
      groups["This Week"].push(entry);
    } else {
      groups.Older.push(entry);
    }
  }

  return groups;
}

/**
 * Time duration formatter
 */
function formatDuration(seconds: number): string {
  const minutes = Math.round(seconds / 60);
  if (minutes < 60) {
    return `${minutes}m`;
  }
  const hours = Math.round(minutes / 60);
  const mins = minutes % 60;
  return `${hours}h ${mins}m`;
}

/**
 * Individual timeline entry
 */
function TimelineEntry({ entry }: { entry: HistoryEntry }) {
  return (
    <div className="relative flex gap-4">
      {/* Timeline dot and line */}
      <div className="flex flex-col items-center">
        <div className="h-3 w-3 rounded-full border-2 border-primary bg-background dark:bg-card" />
        <div className="absolute left-1.5 h-12 w-0 border-l-2 border-muted-foreground/30 dark:border-muted-foreground/20" />
      </div>

      {/* Entry content */}
      <div className="flex-1 pb-8">
        <Link href={`/comics/${entry.comicId}`}>
          <div className="group cursor-pointer rounded-lg border border-muted-foreground/20 p-3 transition-colors hover:border-primary hover:bg-accent dark:border-muted-foreground/10 dark:hover:bg-accent/50">
            <div className="flex gap-3">
              {/* Comic cover thumbnail */}
              {entry.comicCover && (
                <div className="relative h-16 w-12 shrink-0 overflow-hidden rounded">
                  <Image alt={entry.comicTitle} className="object-cover" fill sizes="48px" src={entry.comicCover} />
                </div>
              )}

              {/* Entry details */}
              <div className="min-w-0 flex-1">
                <h3 className="line-clamp-2 font-semibold text-foreground group-hover:text-primary dark:text-foreground dark:group-hover:text-primary">
                  {entry.comicTitle}
                </h3>
                <p className="text-sm text-muted-foreground dark:text-muted-foreground">
                  Chapter {entry.chapterNumber}
                </p>

                {/* Time and progress info */}
                <div className="mt-2 flex gap-3 text-xs text-muted-foreground dark:text-muted-foreground">
                  <span>{formatDistanceToNow(new Date(entry.startedAt), { addSuffix: true })}</span>
                  <span>•</span>
                  <span>{formatDuration(entry.timeSpentSeconds)}</span>
                  {entry.completedAt && (
                    <>
                      <span>•</span>
                      <span className="text-green-600 dark:text-green-500">Completed</span>
                    </>
                  )}
                </div>
              </div>
            </div>
          </div>
        </Link>
      </div>
    </div>
  );
}

/**
 * Reading History Timeline
 */
export function ReadingHistoryTimeline({
  entries,
  isLoading = false,
  onLoadMore,
  hasMore = true,
}: ReadingHistoryTimelineProps) {
  const [isLoadingMore, setIsLoadingMore] = useState(false);
  const groupedEntries = groupByDate(entries);

  const handleLoadMore = async () => {
    if (onLoadMore) {
      setIsLoadingMore(true);
      try {
        await onLoadMore();
      } finally {
        setIsLoadingMore(false);
      }
    }
  };

  if (isLoading && entries.length === 0) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Reading History</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {([0, 1, 2] as const).map((_, i) => (
              <div className="h-20 animate-pulse rounded bg-muted dark:bg-muted" key={i} />
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }

  const isEmpty = entries.length === 0;

  return (
    <Card className="border-muted-foreground/20 dark:border-muted-foreground/10">
      <CardHeader className="pb-4">
        <CardTitle className="text-foreground dark:text-foreground">Reading History</CardTitle>
        <p className="mt-1 text-sm text-muted-foreground dark:text-muted-foreground">Your recent reading activity</p>
      </CardHeader>
      <CardContent>
        {isEmpty ? (
          <div className="rounded-lg border-2 border-dashed border-muted-foreground/30 p-8 text-center dark:border-muted-foreground/20">
            <p className="text-muted-foreground dark:text-muted-foreground">
              No reading history yet. Start reading to see your timeline.
            </p>
          </div>
        ) : (
          <div className="space-y-2">
            {Object.entries(groupedEntries).map(([dateGroup, groupEntries]) =>
              groupEntries.length > 0 ? (
                <div key={dateGroup}>
                  <h3 className="mb-4 font-semibold text-foreground dark:text-foreground">{dateGroup}</h3>
                  <div className="mb-8 space-y-2">
                    {groupEntries.map((entry) => (
                      <TimelineEntry entry={entry} key={entry.id} />
                    ))}
                  </div>
                </div>
              ) : null
            )}

            {/* Load more button */}
            {hasMore && (
              <div className="flex justify-center pt-4">
                <Button
                  className="gap-2 dark:border-muted-foreground/30 dark:hover:bg-accent/50"
                  disabled={isLoadingMore}
                  onClick={() => void handleLoadMore()}
                  variant="outline"
                >
                  {isLoadingMore && (
                    <span className="h-4 w-4 animate-spin rounded-full border-2 border-primary border-t-transparent" />
                  )}
                  {isLoadingMore ? "Loading..." : "Load More"}
                  {!isLoadingMore && <ChevronDown className="h-4 w-4" />}
                </Button>
              </div>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
}

/**
 * Reading History Timeline Loading Skeleton
 */
export function ReadingHistoryTimelineSkeleton() {
  return <ReadingHistoryTimeline entries={[]} isLoading />;
}
