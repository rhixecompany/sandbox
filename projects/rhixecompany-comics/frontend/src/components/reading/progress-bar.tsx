"use client";

/**
 * Progress Bar Component
 * Displays reading progress with visual bar and optional label
 */

interface ProgressBarProps {
  className?: string;
  pageNumber?: number;
  percent: null | number;
  showLabel?: boolean;
  totalPages?: number;
}

export function ProgressBar({ percent, pageNumber, totalPages, showLabel = true, className = "" }: ProgressBarProps) {
  const clampedPercent = Math.min(100, Math.max(0, percent ?? 0));
  const progressLabel = `Progress: ${clampedPercent.toFixed(0)}%${
    pageNumber && totalPages ? ` (Page ${pageNumber} of ${totalPages})` : ""
  }`;

  return (
    <div className={`space-y-2 ${className}`}>
      {/* Progress track - ARIA progressbar container */}
      <div
        aria-label={progressLabel}
        aria-valuemax={100}
        aria-valuemin={0}
        aria-valuenow={clampedPercent}
        className="h-2 w-full overflow-hidden rounded-full bg-secondary dark:bg-secondary/50"
        role="progressbar"
      >
        {/* Progress fill */}
        <div
          aria-hidden="true"
          className="h-full bg-primary transition-all duration-500 dark:bg-primary/80"
          style={{ width: `${clampedPercent}%` }}
        />
      </div>

      {showLabel && (
        <div className="flex items-center justify-between text-sm text-muted-foreground dark:text-muted-foreground/90">
          <span>{clampedPercent.toFixed(0)}% read</span>
          {pageNumber && totalPages && (
            <span>
              Page {pageNumber} of {totalPages}
            </span>
          )}
        </div>
      )}
    </div>
  );
}
