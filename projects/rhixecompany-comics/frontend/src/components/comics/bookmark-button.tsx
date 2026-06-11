"use client";

import { Heart, Loader2 } from "lucide-react";
import { useSession } from "next-auth/react";
import { useCallback, useEffect, useState, useTransition } from "react";

import { addBookmarkAction, removeBookmarkAction } from "@/actions/bookmark.actions";
import { Button } from "@/components/ui/button";
import { useBookmarkStore } from "@/stores/use-bookmark-store";

import type { BookmarkStatus } from "@/schemas/bookmark-schema";

interface BookmarkButtonProps {
  /**
   * Optional CSS class for styling
   */
  className?: string;

  /**
   * Comic ID to bookmark
   */
  comicId: number;

  /**
   * Initial bookmark status (for server-side hydration)
   * If not provided, will use Zustand store
   */
  initialStatus?: BookmarkStatus | null;

  /**
   * Callback fired after bookmark action completes
   */
  onBookmarkChange?: (bookmarked: boolean, status?: BookmarkStatus) => void;

  /**
   * Show label text
   */
  showLabel?: boolean;

  /**
   * Size variant for button
   */
  size?: "lg" | "md" | "sm";
}

/**
 * BookmarkButton
 *
 * Allows users to add/remove comics from their bookmarks (library).
 * Features:
 * - Heart icon (outline when not bookmarked, filled when bookmarked)
 * - Optimistic UI updates via Zustand store
 * - Loading state during server action
 * - Toast-like feedback
 * - Requires authentication
 *
 * Usage:
 * ```tsx
 * <BookmarkButton
 *   comicId={123}
 *   initialStatus="Reading"
 *   onBookmarkChange={(bookmarked) => console.log(bookmarked)}
 * />
 * ```
 */
export function BookmarkButton({
  comicId,
  initialStatus,
  onBookmarkChange,
  className,
  size = "md",
  showLabel = false,
}: BookmarkButtonProps) {
  const { data: session } = useSession();
  const [isPending, startTransition] = useTransition();

  // Zustand store for optimistic updates
  const bookmarks = useBookmarkStore((state) => state.bookmarks);
  const addBookmark = useBookmarkStore((state) => state.addBookmark);
  const removeBookmark = useBookmarkStore((state) => state.removeBookmark);
  const isBookmarked = useBookmarkStore((state) => state.isBookmarked);

  // Local state for initial hydration
  const [feedback, setFeedback] = useState<null | string>(null);

  // Hydrate from initial status or check store
  useEffect(() => {
    if (initialStatus && typeof window !== "undefined") {
      addBookmark({ comicId, status: initialStatus, lastReadChapterId: null });
    }
  }, [initialStatus, comicId, addBookmark]);

  // Check if currently bookmarked
  const bookmarked = isBookmarked(comicId);
  const currentStatus = bookmarks[comicId]?.status as BookmarkStatus | undefined;

  // Handle bookmark toggle
  const handleToggle = useCallback(async () => {
    if (!session?.user?.id) {
      setFeedback("Please sign in to bookmark");
      setTimeout(() => setFeedback(null), 3000);
      return;
    }

    startTransition(async () => {
      try {
        if (bookmarked) {
          // Remove bookmark
          const result = await removeBookmarkAction(comicId);

          if (result.ok) {
            // Optimistic update
            removeBookmark(comicId);
            setFeedback("Removed from library");
            onBookmarkChange?.(false);
          } else {
            setFeedback(result.error || "Failed to remove bookmark");
          }
        } else {
          // Add bookmark with "Reading" status
          const result = await addBookmarkAction(comicId, "Reading");

          if (result.ok) {
            // Optimistic update
            addBookmark({
              comicId,
              status: "Reading",
              lastReadChapterId: null,
            });
            setFeedback("Added to library");
            onBookmarkChange?.(true, "Reading");
          } else {
            setFeedback(result.error || "Failed to add bookmark");
          }
        }

        // Clear feedback after 3 seconds
        setTimeout(() => setFeedback(null), 3000);
      } catch (error) {
        console.error("[BookmarkButton]", error);
        setFeedback("Something went wrong");
        setTimeout(() => setFeedback(null), 3000);
      }
    });
  }, [bookmarked, comicId, session, addBookmark, removeBookmark, onBookmarkChange]);

  const iconSizes = {
    sm: "h-4 w-4",
    md: "h-5 w-5",
    lg: "h-6 w-6",
  };

  return (
    <div className="relative">
      <Button
        aria-label={bookmarked ? `Remove "${comicId}" from library` : `Add "${comicId}" to library`}
        className={className}
        disabled={isPending}
        onClick={() => void handleToggle()}
        size="icon"
        title={bookmarked ? "Remove from library" : "Add to library"}
        variant="ghost"
      >
        {isPending ? (
          <Loader2 className={`${iconSizes[size]} animate-spin`} />
        ) : (
          <Heart
            className={`${iconSizes[size]} transition-all duration-200 ${
              bookmarked
                ? "fill-red-500 text-red-500"
                : "text-gray-600 hover:text-red-500 dark:text-gray-400 dark:hover:text-red-500"
            }`}
          />
        )}
      </Button>

      {/* Feedback toast */}
      {feedback && (
        <div className="absolute top-full right-0 z-50 mt-2 rounded-md bg-gray-900 px-3 py-1.5 text-sm font-medium whitespace-nowrap text-white shadow-md dark:bg-gray-100 dark:text-gray-900">
          {feedback}
        </div>
      )}

      {/* Label (optional) */}
      {showLabel && <span className="ml-2 text-sm font-medium">{bookmarked ? currentStatus || "Saved" : "Save"}</span>}
    </div>
  );
}

export default BookmarkButton;
