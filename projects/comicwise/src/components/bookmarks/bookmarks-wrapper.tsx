"use client";

import { BookMarked } from "lucide-react";
import { useCallback, useState, useTransition } from "react";

import { getBookmarksAction, getBookmarkStatsAction, removeBookmarkAction } from "@/actions/bookmark.actions";
import { BookmarkCard } from "@/components/bookmarks/bookmark-card";
import { BookmarksFilter } from "@/components/bookmarks/bookmarks-filter";
import { StatusEditor } from "@/components/bookmarks/status-editor";
import { EmptyState } from "@/components/comics/empty-state";
import { Button } from "@/components/ui/button";
import { usePagination } from "@/hooks/use-pagination";

import type { BookmarkStatus } from "@/schemas/bookmark-schema";
import type { BookmarkCardData } from "@/types/bookmark";

interface BookmarkState {
  bookmarks: BookmarkCardData[];
  isLoading: boolean;
  page: number;
  search: string;
  sort: "date" | "progress" | "title";
  status: "All" | BookmarkStatus;
  total: number;
  view: "grid" | "list";
}

interface BookmarkStats {
  completed: number;
  dropped: number;
  onHold: number;
  planToRead: number;
  reading: number;
}

interface BookmarksWrapperProps {
  initialBookmarks: BookmarkCardData[];
  initialStats: BookmarkStats;
  isAuthenticated: boolean;
}

function BookmarksListSkeleton({ view }: { view: "grid" | "list" }) {
  return (
    <div className={view === "grid" ? "grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4" : "space-y-4"}>
      {Array.from({ length: view === "grid" ? 12 : 5 }).map((_, i) => (
        <div
          className={`${view === "grid" ? "aspect-2/3 w-full" : "h-32"} animate-pulse rounded-lg bg-muted`}
          key={i}
        />
      ))}
    </div>
  );
}

export function BookmarksWrapper({ initialBookmarks, initialStats, isAuthenticated }: BookmarksWrapperProps) {
  const [state, setState] = useState<BookmarkState>({
    bookmarks: initialBookmarks,
    total: initialBookmarks.length,
    isLoading: false,
    view: "grid",
    status: "All",
    search: "",
    sort: "date",
    page: 1,
  });

  const [stats, setStats] = useState<BookmarkStats>(initialStats);

  const [isPending, startTransition] = useTransition();
  const [statusEditorOpen, setStatusEditorOpen] = useState(false);
  const [editingBookmark, _setEditingBookmark] = useState<BookmarkCardData | null>(null);

  // Open status editor
  const _handleOpenStatusEditor = useCallback((bookmark: BookmarkCardData) => {
    _setEditingBookmark(bookmark);
    setStatusEditorOpen(true);
  }, []);

  // Fetch bookmarks from server
  const loadBookmarks = useCallback(
    async (
      status: "All" | BookmarkStatus,
      search: string,
      sort: "date" | "progress" | "title",
      page: number,
      viewMode: "grid" | "list"
    ) => {
      setState((prev) => ({ ...prev, isLoading: true }));

      const filter = {
        status: status === "All" ? undefined : status,
        search: search || undefined,
        sortBy: sort,
        page,
        limit: viewMode === "grid" ? 20 : 10,
      };

      const result = await getBookmarksAction(filter);
      if (result.ok) {
        const rawBookmarks = (result.data.bookmarks ?? []) as Array<{
          comic?: { coverImage?: string; slug?: string; title?: string };
          comicId: number;
          createdAt: Date | string;
          status: string;
          updatedAt: Date | string;
        }>;
        const transformed: BookmarkCardData[] = rawBookmarks.map((b) => ({
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

        setState((prev: BookmarkState) => ({
          ...prev,
          bookmarks: transformed,
          total: result.data.total,
          isLoading: false,
        }));
      }
    },
    []
  );

  // Load stats
  const loadStats = useCallback(async () => {
    const result = await getBookmarkStatsAction();
    if (result.ok) {
      setStats(result.data);
    }
  }, []);

  // Handle status change
  const handleStatusChange = useCallback(
    (newStatus: "All" | BookmarkStatus) => {
      setState((prev) => ({ ...prev, status: newStatus, page: 1 }));
      void loadBookmarks(newStatus, state.search, state.sort, 1, state.view);
    },
    [loadBookmarks, state.search, state.sort, state.view]
  );

  // Handle search
  const handleSearch = useCallback(
    (query: string) => {
      setState((prev) => ({ ...prev, search: query, page: 1 }));
      void loadBookmarks(state.status, query, state.sort, 1, state.view);
    },
    [loadBookmarks, state.status, state.sort, state.view]
  );

  // Handle sort change
  const handleSort = useCallback(
    (newSort: "date" | "progress" | "title") => {
      setState((prev) => ({ ...prev, sort: newSort, page: 1 }));
      void loadBookmarks(state.status, state.search, newSort, 1, state.view);
    },
    [loadBookmarks, state.status, state.search, state.view]
  );

  // Handle remove bookmark
  const handleRemoveBookmark = useCallback(
    (comicId: number) => {
      startTransition(async () => {
        const result = await removeBookmarkAction(comicId);
        if (result.ok) {
          setState((prev) => ({
            ...prev,
            bookmarks: prev.bookmarks.filter((b) => b.comicId !== comicId),
          }));
          await loadStats();
          await loadBookmarks(state.status, state.search, state.sort, state.page, state.view);
        }
      });
    },
    [loadStats, loadBookmarks, state.status, state.search, state.sort, state.page, state.view]
  );

  // Handle status change from StatusEditor
  const handleStatusChangeComplete = useCallback(
    async (_newStatus: BookmarkStatus) => {
      await loadStats();
      await loadBookmarks(state.status, state.search, state.sort, state.page, state.view);
    },
    [loadStats, loadBookmarks, state.status, state.search, state.sort, state.page, state.view]
  );

  // Calculate pagination
  const itemsPerPage = state.view === "grid" ? 20 : 10;
  const totalPages = Math.ceil(state.total / itemsPerPage);
  const displayStart = (state.page - 1) * itemsPerPage + 1;
  const displayEnd = Math.min(state.page * itemsPerPage, state.total);

  // Pagination hook
  const { pages, showLeftEllipsis, showRightEllipsis } = usePagination({
    currentPage: state.page,
    paginationItemsToDisplay: 5,
    totalPages,
  });

  // Not authenticated state
  if (!isAuthenticated) {
    return (
      <main className="min-h-screen bg-background">
        <div className="mx-auto max-w-7xl px-4 py-12 text-center sm:px-6 lg:px-8">
          <EmptyState
            action={{ href: "/sign-in", label: "Sign In" }}
            description="Please sign in to view your bookmarks"
            icon={<BookMarked className="h-12 w-12" />}
            title="Sign in to view bookmarks"
          />
        </div>
      </main>
    );
  }

  // Empty state
  if (!state.isLoading && state.bookmarks.length === 0 && state.total === 0) {
    return (
      <main className="min-h-screen bg-background">
        <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
          <EmptyState
            action={{ href: "/comics", label: "Browse Comics" }}
            description="Start bookmarking comics to keep track of your reading progress"
            icon={<BookMarked className="h-12 w-12" />}
            title="No bookmarks yet"
          />
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-background">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="mb-2 text-3xl font-bold">My Bookmarks</h1>
          <p className="text-muted-foreground">Track and manage your reading list</p>
        </div>

        {/* Stats */}
        <div className="mb-8 grid grid-cols-5 gap-4">
          <div className="rounded-lg bg-muted p-4">
            <div className="text-2xl font-bold">{stats.reading}</div>
            <div className="text-sm text-muted-foreground">Reading</div>
          </div>
          <div className="rounded-lg bg-muted p-4">
            <div className="text-2xl font-bold">{stats.completed}</div>
            <div className="text-sm text-muted-foreground">Completed</div>
          </div>
          <div className="rounded-lg bg-muted p-4">
            <div className="text-2xl font-bold">{stats.planToRead}</div>
            <div className="text-sm text-muted-foreground">Plan to Read</div>
          </div>
          <div className="rounded-lg bg-muted p-4">
            <div className="text-2xl font-bold">{stats.onHold}</div>
            <div className="text-sm text-muted-foreground">On Hold</div>
          </div>
          <div className="rounded-lg bg-muted p-4">
            <div className="text-2xl font-bold">{stats.dropped}</div>
            <div className="text-sm text-muted-foreground">Dropped</div>
          </div>
        </div>

        {/* Filters */}
        <div className="mb-8">
          <BookmarksFilter
            activeFilters={{
              search: state.search || undefined,
              status: state.status === "All" ? undefined : state.status,
              sortBy: state.sort === "date" ? "recent" : state.sort,
              view: state.view,
            }}
            onFilterChange={(filter) => {
              handleSearch(filter.search || "");
              handleStatusChange(filter.status ? (filter.status as BookmarkStatus) : "All");
              const sortMap: Record<string, "date" | "progress" | "title"> = {
                recent: "date",
                added: "date",
                progress: "progress",
                title: "title",
              };
              handleSort(sortMap[filter.sortBy || "recent"] || "date");
              setState((prev) => ({ ...prev, view: filter.view ?? prev.view }));
            }}
            onViewModeChange={(mode) => setState((prev) => ({ ...prev, view: mode }))}
            viewMode={state.view}
          />
        </div>

        {/* Results info */}
        {state.total > 0 && (
          <div className="mb-4 text-sm text-muted-foreground">
            Showing {displayStart} to {displayEnd} of {state.total} bookmarks
          </div>
        )}

        {/* Loading state */}
        {state.isLoading && <BookmarksListSkeleton view={state.view} />}

        {/* Bookmarks grid/list */}
        {!state.isLoading && state.bookmarks.length > 0 && (
          <div className={state.view === "grid" ? "grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4" : "space-y-4"}>
            {state.bookmarks.map((bm) => (
              <BookmarkCard
                bookmark={bm}
                isListView={state.view === "list"}
                key={bm.comicId}
                onRemove={handleRemoveBookmark}
              />
            ))}
          </div>
        )}

        {/* Status Editor Modal */}
        {editingBookmark && (
          <StatusEditor
            comicId={editingBookmark.comicId}
            comicTitle={editingBookmark.comicTitle}
            currentStatus={editingBookmark.status}
            isOpen={statusEditorOpen}
            onOpenChange={setStatusEditorOpen}
            onStatusChange={() => {
              void handleStatusChangeComplete(editingBookmark?.status);
            }}
          />
        )}

        {/* Pagination */}
        {totalPages > 1 && (
          <div className="mt-8 flex items-center justify-center gap-2">
            <Button
              disabled={state.page === 1 || isPending}
              onClick={() => setState((prev) => ({ ...prev, page: Math.max(1, prev.page - 1) }))}
              size="sm"
              variant="outline"
            >
              Previous
            </Button>

            {showLeftEllipsis && (
              <>
                <Button
                  className="h-8 w-8 p-0"
                  onClick={() => setState((prev) => ({ ...prev, page: 1 }))}
                  size="sm"
                  variant="outline"
                >
                  1
                </Button>
                <span className="px-2">...</span>
              </>
            )}

            {pages.map((page) => (
              <Button
                className="h-8 w-8 p-0"
                key={page}
                onClick={() => setState((prev) => ({ ...prev, page }))}
                size="sm"
                variant={state.page === page ? "default" : "outline"}
              >
                {page}
              </Button>
            ))}

            {showRightEllipsis && (
              <>
                <span className="px-2">...</span>
                <Button
                  className="h-8 w-8 p-0"
                  onClick={() => setState((prev) => ({ ...prev, page: totalPages }))}
                  size="sm"
                  variant="outline"
                >
                  {totalPages}
                </Button>
              </>
            )}

            <Button
              disabled={state.page === totalPages || isPending}
              onClick={() => setState((prev) => ({ ...prev, page: Math.min(totalPages, prev.page + 1) }))}
              size="sm"
              variant="outline"
            >
              Next
            </Button>
          </div>
        )}
      </div>
    </main>
  );
}
