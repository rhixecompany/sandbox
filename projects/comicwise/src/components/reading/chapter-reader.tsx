"use client";

import { useCallback, useEffect, useState } from "react";

import { updateProgressAction } from "@/actions/reading-progress.actions";
import { useReaderStore } from "@/stores/reader-store";

import { ImageViewer } from "./image-viewer";
import { ReaderControls } from "./reader-controls";

interface ChapterReaderProps {
  chapterId: number;
  chapterImages: string[];
  chapterNumber: number;
  chapterTitle: string;
  comicId: number;
  comicSlug: string;
  isBookmarked?: boolean;
  onBookmarkToggle?: () => void;
  totalChapters: number;
}

export function ChapterReader({
  comicSlug,
  chapterNumber,
  chapterTitle,
  chapterImages,
  comicId,
  chapterId,
  totalChapters,
  isBookmarked = false,
  onBookmarkToggle,
}: ChapterReaderProps) {
  const [currentPageIndex, setCurrentPageIndex] = useState(0);
  const [lastSavedPage, setLastSavedPage] = useState(0);
  const { settings } = useReaderStore();
  const [isUpdatingProgress, setIsUpdatingProgress] = useState(false);

  // Update reading progress - debounced
  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentPageIndex !== lastSavedPage && !isUpdatingProgress) {
        setIsUpdatingProgress(true);
        void (async () => {
          const result = await updateProgressAction({
            comicId,
            chapterId,
            pageNumber: currentPageIndex,
            scrollPercentage: ((currentPageIndex + 1) / chapterImages.length) * 100,
          });
          if (result.ok) {
            setLastSavedPage(currentPageIndex);
          }
          setIsUpdatingProgress(false);
        })();
      }
    }, 500); // Debounce for 500ms

    return () => clearTimeout(timer);
  }, [currentPageIndex, lastSavedPage, comicId, chapterId, chapterImages.length, isUpdatingProgress]);

  const handlePageChange = useCallback((index: number) => {
    setCurrentPageIndex(index);
  }, []);

  // Apply reader settings
  const containerStyle: React.CSSProperties = {
    filter: `brightness(${settings.brightness}%) contrast(${settings.contrast}%)`,
  };

  return (
    <div className="flex h-screen flex-col bg-background" style={containerStyle}>
      {/* Chapter Header */}
      <div className="border-b border-border bg-card px-4 py-3">
        <h1 className="text-2xl font-bold">{chapterTitle}</h1>
        <p className="text-sm text-muted-foreground">
          Chapter {chapterNumber} of {totalChapters}
        </p>
      </div>

      {/* Image Viewer */}
      <div className="flex-1 overflow-hidden">
        <ImageViewer
          chapterTitle={chapterTitle}
          currentPageIndex={currentPageIndex}
          images={chapterImages}
          onPageChange={handlePageChange}
        />
      </div>

      {/* Reader Controls */}
      <ReaderControls
        chapterNumber={chapterNumber}
        chapterTitle={chapterTitle}
        comicSlug={comicSlug}
        isBookmarked={isBookmarked}
        onBookmarkToggle={onBookmarkToggle}
        totalChapters={totalChapters}
      />

      {/* Progress Indicator */}
      {isUpdatingProgress && (
        <div className="fixed right-4 bottom-24 rounded bg-primary px-3 py-1 text-xs text-primary-foreground">
          Saving progress...
        </div>
      )}
    </div>
  );
}
