"use client";

import { BookOpen } from "lucide-react";
import Link from "next/link";
import { useState } from "react";

import { Button } from "@/components/ui/button";

import type { BookmarkStatus } from "@/schemas/bookmark-schema";

interface ResumeButtonProps {
  /**
   * Optional CSS class for styling
   */
  className?: string;

  /**
   * Comic slug for building href
   */
  comicSlug: string;

  /**
   * First chapter ID (fallback if lastChapterId not available)
   * Defaults to 1
   */
  firstChapterId?: number;

  /**
   * Last read chapter ID
   * If not provided, will link to first chapter (chapter 1)
   */
  lastChapterId?: null | number;

  /**
   * Last read page number
   * If not provided, defaults to page 1
   */
  lastPageNumber?: null | number;

  /**
   * Show tooltip on hover
   */
  showTooltip?: boolean;

  /**
   * Button size
   */
  size?: "lg" | "md" | "sm";

  /**
   * Comic status (for determining button text and behavior)
   */
  status?: BookmarkStatus;
}

/**
 * ResumeButton
 *
 * Allows users to jump directly to:
 * - Last read chapter + page (if reading progress exists)
 * - First chapter (fallback)
 *
 * Features:
 * - Smart button text based on status ("Continue Reading" vs "Start Reading")
 * - Tooltip with chapter info
 * - Can be used as standalone button or in card
 * - Links directly to reader page
 *
 * Usage:
 * ```tsx
 * <ResumeButton
 *   comicSlug="my-manga"
 *   lastChapterId={15}
 *   lastPageNumber={42}
 *   status="Reading"
 *   firstChapterId={1}
 * />
 * ```
 */
export function ResumeButton({
  comicSlug,
  lastChapterId,
  lastPageNumber,
  status,
  firstChapterId = 1,
  className,
  size = "md",
  showTooltip = true,
}: ResumeButtonProps) {
  const [showingTooltip, setShowingTooltip] = useState(false);

  // Determine which chapter to link to
  const chapterId = lastChapterId || firstChapterId;
  const pageParam = lastPageNumber ? `&page=${lastPageNumber}` : "";

  // Build href to reader page
  const href = `/comics/${comicSlug}/chapter/${chapterId}?resume=true${pageParam}`;

  // Determine button text
  const isCompleted = status === "Completed";
  const hasProgress = lastChapterId && lastChapterId > 0;
  const buttonText = isCompleted ? "View Chapters" : hasProgress ? "Continue Reading" : "Start Reading";

  // Tooltip content
  const tooltipText = hasProgress
    ? `Continue from Chapter ${lastChapterId}${lastPageNumber ? `, Page ${lastPageNumber}` : ""}`
    : `Start from Chapter ${firstChapterId}`;

  const sizeStyles = {
    sm: "h-8 px-3 text-xs",
    md: "h-10 px-4",
    lg: "h-12 px-6",
  };

  // Construct href as an object to satisfy Next.js Link typing
  const linkHref = {
    pathname: href,
  };

  return (
    <div className="relative inline-block">
      <Link href={linkHref}>
        <Button
          className={className ?? sizeStyles[size]}
          onMouseEnter={() => setShowingTooltip(true)}
          onMouseLeave={() => setShowingTooltip(false)}
          size={size === "sm" ? "sm" : size === "lg" ? "lg" : undefined}
          variant={isCompleted ? "outline" : "default"}
        >
          <BookOpen className="mr-2 h-4 w-4" />
          {buttonText}
        </Button>
      </Link>

      {/* Tooltip */}
      {showTooltip && showingTooltip && (
        <div className="absolute top-full left-0 z-50 mt-2 rounded-md bg-gray-900 px-2 py-1 text-xs whitespace-nowrap text-white shadow-md dark:bg-gray-100 dark:text-gray-900">
          {tooltipText}
        </div>
      )}
    </div>
  );
}

export default ResumeButton;
