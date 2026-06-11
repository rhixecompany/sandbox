"use client";

/**
 * Continue Reading Card Component
 * Displays a single continue reading item with clickable navigation
 */

import { useRouter } from "next/navigation";

import { ProgressBar } from "./progress-bar";

import type { ContinueReadingItem } from "@/types/reading-progress";

interface ContinueReadingCardProps {
  item: ContinueReadingItem;
  onClick?: () => void;
}

export function ContinueReadingCard({ item, onClick }: ContinueReadingCardProps) {
  const router = useRouter();

  const handleNavigate = () => {
    onClick?.();
    const chapterId = String(item.chapterId);
    // Type cast needed: Next.js 16 dynamic routes with template literals
    // Route defined in src/app/(root)/chapter/[id]/page.tsx
    router.push(`/chapter/${chapterId}` as never);
  };

  return (
    <div
      className="flex cursor-pointer gap-4 rounded-lg border border-border p-4 transition-shadow hover:shadow-lg dark:border-border dark:hover:shadow-lg/50"
      onClick={handleNavigate}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          handleNavigate();
        }
      }}
      role="button"
      tabIndex={0}
    >
      {/* Comic Cover Placeholder */}
      <div className="relative h-24 w-16 shrink-0 rounded bg-secondary dark:bg-secondary/50">
        <div className="flex h-full w-full items-center justify-center text-muted-foreground dark:text-muted-foreground/70">
          <span className="text-xs">Comic</span>
        </div>
      </div>

      {/* Content */}
      <div className="min-w-0 flex-1">
        <h3 className="truncate font-semibold text-foreground dark:text-foreground">{item.comicTitle}</h3>

        <p className="mt-1 text-sm text-muted-foreground dark:text-muted-foreground/80">
          Chapter {item.chapterNumber}: {item.chapterTitle || "No title"}
        </p>

        <div className="mt-3">
          <ProgressBar pageNumber={item.pageNumber} percent={item.progressPercent} showLabel={true} />
        </div>

        <p className="mt-2 text-xs text-muted-foreground dark:text-muted-foreground/70">
          Last read: {item.lastReadAt ? new Date(item.lastReadAt).toLocaleDateString() : "Never"}
        </p>
      </div>
    </div>
  );
}
