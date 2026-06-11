/**
 * Bookmark Types
 */

export interface BookmarkCardData {
  authorName: string;
  comicId: number;
  comicSlug: string;
  comicTitle: string;
  coverImage?: string;
  createdAt: Date;
  lastReadChapter?: number;
  lastReadDate?: Date;
  progressPercent: number;
  status: "Completed" | "Dropped" | "On Hold" | "Plan to Read" | "Reading";
  updatedAt: Date;
}

export interface BookmarkFilter {
  search?: string;
  sortBy?: "added" | "progress" | "recent" | "title";
  status?: string;
  view?: "grid" | "list";
}

export interface BookmarksListResult {
  bookmarks: BookmarkCardData[];
  hasMore: boolean;
  nextCursor?: string;
  total: number;
}
