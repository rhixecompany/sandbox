"use client";

import { Bookmark, ChevronLeft, ChevronRight, MoreVertical, Settings, Share2 } from "lucide-react";
import Link from "next/link";
import { useCallback, useState } from "react";

import { Button } from "@/components/ui/button";

import { ReaderSettings } from "./reader-settings";

import type { Route } from "next";

interface ReaderControlsProps {
  chapterNumber: number;
  chapterTitle: string;
  comicSlug: string;
  isBookmarked?: boolean;
  onBookmarkToggle?: () => void;
  totalChapters: number;
}

export function ReaderControls({
  comicSlug,
  chapterNumber,
  chapterTitle,
  totalChapters,
  isBookmarked = false,
  onBookmarkToggle,
}: ReaderControlsProps) {
  const [showSettings, setShowSettings] = useState(false);
  const [showMenu, setShowMenu] = useState(false);

  const previousChapterUrl = chapterNumber > 1 ? (`/comics/${comicSlug}/${chapterNumber - 1}` as Route) : null;

  const nextChapterUrl = chapterNumber < totalChapters ? (`/comics/${comicSlug}/${chapterNumber + 1}` as Route) : null;

  const handleBookmarkClick = useCallback(() => {
    onBookmarkToggle?.();
  }, [onBookmarkToggle]);

  const handleShare = useCallback(() => {
    if (navigator.share) {
      navigator.share({
        title: chapterTitle,
        text: `Reading ${chapterTitle}`,
        url: window.location.href,
      });
    } else {
      // Fallback: copy to clipboard
      navigator.clipboard.writeText(window.location.href);
      alert("Link copied to clipboard!");
    }
  }, [chapterTitle]);

  return (
    <>
      <div className="fixed bottom-4 left-1/2 z-40 -translate-x-1/2">
        <div className="flex items-center gap-2 rounded-full bg-white/95 px-2 py-2 shadow-lg backdrop-blur-sm dark:bg-gray-900/95">
          {/* Previous Chapter */}
          {previousChapterUrl ? (
            <Link href={previousChapterUrl}>
              <Button className="gap-1" size="sm" title={`Chapter ${chapterNumber - 1}`} variant="ghost">
                <ChevronLeft className="h-4 w-4" />
                <span className="hidden text-xs sm:inline">Prev</span>
              </Button>
            </Link>
          ) : (
            <Button className="gap-1" disabled size="sm" variant="ghost">
              <ChevronLeft className="h-4 w-4" />
              <span className="hidden text-xs sm:inline">Prev</span>
            </Button>
          )}

          {/* Chapter Info */}
          <div className="hidden px-2 text-center sm:block">
            <p className="text-xs font-medium">{chapterTitle}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400">
              {chapterNumber} / {totalChapters}
            </p>
          </div>

          {/* Bookmark Button */}
          <Button
            className={isBookmarked ? "text-yellow-500" : ""}
            onClick={handleBookmarkClick}
            size="sm"
            title={isBookmarked ? "Remove bookmark" : "Bookmark this chapter"}
            variant="ghost"
          >
            <Bookmark className="h-4 w-4" fill={isBookmarked ? "currentColor" : "none"} />
          </Button>

          {/* Share Button */}
          <Button onClick={handleShare} size="sm" title="Share chapter" variant="ghost">
            <Share2 className="h-4 w-4" />
          </Button>

          {/* Settings Button */}
          <Button onClick={() => setShowSettings(true)} size="sm" title="Reader settings" variant="ghost">
            <Settings className="h-4 w-4" />
          </Button>

          {/* More Menu */}
          <div className="relative">
            <Button onClick={() => setShowMenu(!showMenu)} size="sm" variant="ghost">
              <MoreVertical className="h-4 w-4" />
            </Button>
            {showMenu && (
              <div className="absolute right-0 bottom-full mb-2 overflow-hidden rounded-lg bg-white shadow-lg dark:bg-gray-800">
                <Link
                  className="block w-full px-4 py-2 text-left text-sm hover:bg-gray-100 dark:hover:bg-gray-700"
                  href={`/comics/${comicSlug}`}
                  onClick={() => setShowMenu(false)}
                >
                  Back to Comic
                </Link>
                <button
                  className="block w-full px-4 py-2 text-left text-sm hover:bg-gray-100 dark:hover:bg-gray-700"
                  onClick={() => {
                    window.print();
                    setShowMenu(false);
                  }}
                >
                  Print
                </button>
              </div>
            )}
          </div>

          {/* Next Chapter */}
          {nextChapterUrl ? (
            <Link href={nextChapterUrl}>
              <Button className="gap-1" size="sm" title={`Chapter ${chapterNumber + 1}`} variant="ghost">
                <span className="hidden text-xs sm:inline">Next</span>
                <ChevronRight className="h-4 w-4" />
              </Button>
            </Link>
          ) : (
            <Button className="gap-1" disabled size="sm" variant="ghost">
              <span className="hidden text-xs sm:inline">Next</span>
              <ChevronRight className="h-4 w-4" />
            </Button>
          )}
        </div>
      </div>

      {/* Settings Modal */}
      <ReaderSettings isOpen={showSettings} onClose={() => setShowSettings(false)} />
    </>
  );
}
