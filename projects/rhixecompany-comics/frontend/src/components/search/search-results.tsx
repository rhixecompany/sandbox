"use client";

import { Grid3x3, List } from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useState } from "react";

import { BookmarkButton } from "@/components/comics/bookmark-button";
import { ComicCard } from "@/components/comics/comic-card";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { useKeyboardNavigation } from "@/hooks/use-keyboard-navigation";

import type { SearchResults } from "@/schemas/search.schema";

interface SearchResultsProps {
  isLoading?: boolean;
  results: null | SearchResults;
}

export function SearchResults({ results, isLoading = false }: SearchResultsProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [viewMode, setViewMode] = useState<"grid" | "list">((searchParams.get("view") as "grid" | "list") || "grid");
  const [selectedIndex, setSelectedIndex] = useState(-1);

  const columns = viewMode === "grid" ? 3 : 1; // Grid has 3 columns on desktop
  const totalItems = results?.results.length ?? 0;

  const handleNavigate = useCallback(
    (index: number) => {
      if (results?.results[index]) {
        router.push(`/comics/${results.results[index].slug}`);
      }
    },
    [results, router]
  );

  useKeyboardNavigation({
    onArrowDown: () =>
      setSelectedIndex((prev) => {
        const newIndex = prev + columns;
        return Math.min(newIndex, totalItems - 1);
      }),
    onArrowUp: () =>
      setSelectedIndex((prev) => {
        const newIndex = prev - columns;
        return Math.max(newIndex, 0);
      }),
    onArrowRight: () =>
      setSelectedIndex((prev) => {
        const newIndex = prev + 1;
        return Math.min(newIndex, totalItems - 1);
      }),
    onArrowLeft: () =>
      setSelectedIndex((prev) => {
        const newIndex = prev - 1;
        return Math.max(newIndex, 0);
      }),
    onEnter: () => {
      if (selectedIndex >= 0 && selectedIndex < totalItems) {
        handleNavigate(selectedIndex);
      }
    },
    onEscape: () => setSelectedIndex(-1),
  });

  // Handle view mode change with URL persistence
  const handleViewModeChange = (newMode: "grid" | "list") => {
    setViewMode(newMode);
    const params = new URLSearchParams(searchParams);
    params.set("view", newMode);
    router.push(`/search?${params.toString()}`);
  };

  if (isLoading) {
    return (
      <div className={viewMode === "grid" ? "grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3" : "space-y-4"}>
        {Array.from({ length: 12 }).map((_, i) => (
          <div key={i}>
            {viewMode === "grid" ? (
              <Skeleton className="h-80 w-full rounded-lg" />
            ) : (
              <div className="space-y-2">
                <Skeleton className="h-6 w-full" />
                <Skeleton className="h-4 w-2/3" />
                <Skeleton className="h-4 w-1/2" />
              </div>
            )}
          </div>
        ))}
      </div>
    );
  }

  if (!results || results.results.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-12 text-center dark:text-foreground">
        <p className="mb-4 text-lg text-muted-foreground">No comics found. Try adjusting your search filters.</p>
        <Button
          className="dark:border-border/50 dark:text-foreground dark:hover:bg-accent/50"
          onClick={() => router.push("/search")}
          variant="outline"
        >
          Clear Filters
        </Button>
      </div>
    );
  }

  // Validate page number is within bounds
  const isPageOutOfBounds = results.page > results.pageCount && results.pageCount > 0;

  const handlePageChange = (newPage: number) => {
    const params = new URLSearchParams(searchParams);
    // Clamp page to valid range
    const clampedPage = Math.max(1, Math.min(newPage, results.pageCount || 1));
    params.set("page", String(clampedPage));
    router.push(`/search?${params.toString()}`);
  };

  return (
    <div className="space-y-6" data-testid="search-results">
      {/* Results Header */}
      <div className="flex items-center justify-between rounded-lg border px-4 py-3 md:px-6 dark:border-border/50">
        <div className="space-y-1">
          <p className="font-semibold dark:text-foreground">
            {isPageOutOfBounds
              ? `Page ${results.pageCount} of ${results.pageCount}`
              : `Page ${results.page} of ${results.pageCount}`}{" "}
            ({results.total} comics)
          </p>
          {isPageOutOfBounds && (
            <p className="text-xs text-amber-600 dark:text-amber-500">
              Page {searchParams.get("page")} not found, showing page {results.pageCount}
            </p>
          )}
        </div>

        {/* View Mode Toggle */}
        <div className="flex gap-2">
          <Button
            className={
              viewMode === "grid"
                ? "dark:bg-primary"
                : "dark:border-border/50 dark:text-foreground dark:hover:bg-accent/50"
            }
            onClick={() => handleViewModeChange("grid")}
            size="sm"
            title="Grid view"
            variant={viewMode === "grid" ? "default" : "outline"}
          >
            <Grid3x3 className="h-4 w-4" />
          </Button>
          <Button
            className={
              viewMode === "list"
                ? "dark:bg-primary"
                : "dark:border-border/50 dark:text-foreground dark:hover:bg-accent/50"
            }
            onClick={() => handleViewModeChange("list")}
            size="sm"
            title="List view"
            variant={viewMode === "list" ? "default" : "outline"}
          >
            <List className="h-4 w-4" />
          </Button>
        </div>
      </div>

      {/* Results Grid/List */}
      {viewMode === "grid" ? (
        <div className="grid auto-rows-max grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          {results.results.map((comic, index) => (
            <div
              className={`group relative rounded-lg transition-all ${
                selectedIndex === index ? "ring-2 ring-primary ring-offset-2 ring-offset-background" : ""
              }`}
              data-testid="search-result-item"
              key={comic.id}
            >
              <ComicCard
                comic={{
                  id: comic.id,
                  title: comic.title,
                  slug: comic.slug,
                  coverImage: comic.coverImage,
                  description: comic.synopsis ?? undefined,
                  rating: comic.rating,
                  status: comic.status,
                }}
              />
              <div className="absolute inset-0 flex items-center justify-center rounded-lg bg-black/20 opacity-0 transition-opacity group-hover:opacity-100 dark:bg-black/40">
                <BookmarkButton comicId={comic.id} initialStatus={null} />
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="space-y-3">
          {results.results.map((comic) => (
            <Link
              className="group flex gap-4 rounded-lg border p-4 transition-colors hover:bg-accent dark:border-border/50 dark:bg-card/50 dark:hover:bg-accent/50"
              data-testid="search-result-item"
              href={`/comics/${comic.slug}`}
              key={comic.id}
            >
              {/* Cover Image */}
              {comic.coverImage && (
                <div className="relative h-24 w-16 shrink-0 overflow-hidden rounded border dark:border-border/50">
                  <Image
                    alt={comic.title}
                    className="h-full w-full object-cover transition-transform group-hover:scale-105"
                    height={24}
                    src={comic.coverImage}
                    width={24}
                  />
                </div>
              )}

              {/* Comic Info */}
              <div className="min-w-0 flex-1 space-y-2">
                <h3 className="line-clamp-2 font-semibold transition-colors group-hover:text-primary dark:text-foreground">
                  {comic.title}
                </h3>

                {comic.author && <p className="text-sm text-muted-foreground">by {comic.author.name}</p>}

                {comic.synopsis && <p className="line-clamp-2 text-sm text-muted-foreground">{comic.synopsis}</p>}

                <div className="flex items-center gap-4 pt-2">
                  <div className="flex items-center gap-1">
                    <span className="text-sm font-medium dark:text-foreground">{comic.rating.toFixed(1)}★</span>
                  </div>
                  <div className="text-xs dark:text-foreground/70">{comic.status}</div>
                </div>
              </div>

              {/* Bookmark Button */}
              <div className="shrink-0">
                <BookmarkButton comicId={comic.id} initialStatus={null} />
              </div>
            </Link>
          ))}
        </div>
      )}

      {/* Pagination */}
      {results.pageCount > 1 && (
        <div className="flex items-center justify-center gap-2 rounded-lg border p-4 dark:border-border/50">
          <Button
            className="dark:border-border/50 dark:text-foreground dark:disabled:opacity-50"
            disabled={results.page <= 1}
            onClick={() => handlePageChange(results.page - 1)}
            variant="outline"
          >
            Previous
          </Button>

          <div className="text-sm font-medium dark:text-foreground">
            {results.page} / {results.pageCount}
          </div>

          <Button
            className="dark:border-border/50 dark:text-foreground dark:disabled:opacity-50"
            disabled={results.page >= results.pageCount}
            onClick={() => handlePageChange(results.page + 1)}
            variant="outline"
          >
            Next
          </Button>
        </div>
      )}
    </div>
  );
}
