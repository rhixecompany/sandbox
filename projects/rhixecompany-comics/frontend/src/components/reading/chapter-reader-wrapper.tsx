"use client";

import { ChapterReader } from "@/components/reading/chapter-reader";

interface ChapterReaderWrapperProps {
  chapterId: number;
  chapterImages: string[];
  chapterNumber: number;
  chapterTitle: string;
  comicId: number;
  comicSlug: string;
  isBookmarked: boolean;
  onBookmarkToggle: () => void;
  totalChapters: number;
}

export function ChapterReaderWrapper(props: ChapterReaderWrapperProps) {
  return (
    <ChapterReader
      chapterId={props.chapterId}
      chapterImages={props.chapterImages}
      chapterNumber={props.chapterNumber}
      chapterTitle={props.chapterTitle}
      comicId={props.comicId}
      comicSlug={props.comicSlug}
      isBookmarked={props.isBookmarked}
      onBookmarkToggle={props.onBookmarkToggle}
      totalChapters={props.totalChapters}
    />
  );
}
