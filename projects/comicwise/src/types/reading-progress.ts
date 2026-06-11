/**
 * Reading Progress Types
 */

export interface ReadingProgress {
  comicId: number;
  completedAt: Date | null;
  createdAt: Date;
  currentChapterId: null | number;
  currentPageNumber: number;
  currentPosition: string;
  deviceLastUsed: null | string;
  lastReadAt: Date | null;
  notesCount: number;
  progressPercent: number | string;
  readingSpeed: null | string;
  startedAt: Date;
  status: string;
  totalChaptersRead: number;
  totalPagesRead: number;
  updatedAt: Date;
  userId: string;
}

export interface ContinueReadingItem {
  chapterId: null | number;
  chapterNumber?: null | number;
  chapterTitle?: null | string;
  comicId: number;
  comicSlug: string;
  comicTitle: string;
  lastReadAt: Date;
  pageNumber: number;
  progressPercent: null | number;
}

export interface ReadingStats {
  averageProgressPercent: number;
  totalChaptersCompleted: number;
  totalChaptersRead: number;
}
