/**
 * Bookmarks Page
 * Route: /bookmarks
 */

// Note: Auth redirect is handled by middleware

import { getBookmarksAction, getBookmarkStatsAction } from "@/actions/bookmark.actions";
import { auth } from "@/auth";
import { BookmarksWrapper } from "@/components/bookmarks/bookmarks-wrapper";

import type { BookmarkCardData } from "@/types/bookmark";

interface BookmarkStats {
  completed: number;
  dropped: number;
  onHold: number;
  planToRead: number;
  reading: number;
}

export const metadata = {
  title: "My Bookmarks | ComicWise",
  description: "Track your favorite comics and manage your reading list",
};

export default async function BookmarksPage() {
  const session = await auth();
  const isAuthenticated = !!session?.user;

  // Fetch initial data server-side
  const [bookmarksResult, statsResult] = await Promise.all([
    getBookmarksAction({ limit: 20, page: 1, sortBy: "date" }),
    isAuthenticated ? getBookmarkStatsAction() : Promise.resolve({ ok: true as const, data: null }),
  ]);

  // Transform bookmarks to expected format
  let initialBookmarks: BookmarkCardData[] = [];
  if (bookmarksResult.ok && bookmarksResult.data?.bookmarks) {
    const rawBookmarks = bookmarksResult.data.bookmarks as Array<{
      comic?: { coverImage?: string; slug?: string; title?: string };
      comicId: number;
      createdAt: Date | string;
      status: string;
      updatedAt: Date | string;
    }>;

    initialBookmarks = rawBookmarks.map((b) => ({
      comicId: b.comicId,
      comicSlug: b.comic?.slug ?? "",
      comicTitle: b.comic?.title ?? "",
      authorName: "Unknown",
      coverImage: b.comic?.coverImage,
      status: b.status as BookmarkCardData["status"],
      progressPercent: 0,
      createdAt: new Date(b.createdAt),
      updatedAt: new Date(b.updatedAt),
    }));
  }

  const initialStats: BookmarkStats =
    statsResult.ok && statsResult.data
      ? statsResult.data
      : { reading: 0, completed: 0, planToRead: 0, onHold: 0, dropped: 0 };

  return (
    <BookmarksWrapper
      initialBookmarks={initialBookmarks}
      initialStats={initialStats}
      isAuthenticated={isAuthenticated}
    />
  );
}
