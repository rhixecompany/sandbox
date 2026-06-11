/**
 * Comic Filters Component (Client)
 * URL-driven filters keep state server-synced
 * Includes aria-live regions to announce filter changes to screen readers
 */

"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useDebounce } from "@/hooks/use-debounce";

interface FilterOption {
  id: number;
  name: string;
}

interface ComicFiltersProps {
  defaultQuery: string;
  defaultSort: "latest" | "popular" | "rating";
  genres?: FilterOption[];
  selectedGenreId?: string;
  selectedStatus?: string;
  selectedTypeId?: string;
  types?: FilterOption[];
}

const COMIC_STATUSES = [
  { label: "Ongoing", value: "Ongoing" },
  { label: "Completed", value: "Completed" },
  { label: "Hiatus", value: "Hiatus" },
  { label: "Dropped", value: "Dropped" },
  { label: "Season End", value: "Season End" },
  { label: "Coming Soon", value: "Coming Soon" },
];

export function ComicFilters({
  defaultSort,
  defaultQuery,
  genres = [],
  types = [],
  selectedGenreId,
  selectedStatus,
  selectedTypeId,
}: ComicFiltersProps) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [filterAnnouncement, setFilterAnnouncement] = useState("");
  const [previousFilters, setPreviousFilters] = useState(
    `${defaultQuery}-${defaultSort}-${selectedStatus}-${selectedGenreId}-${selectedTypeId}`
  );
  const [searchInput, setSearchInput] = useState(defaultQuery);
  const debouncedSearch = useDebounce(searchInput, 300);

  useEffect(() => {
    const currentFilters = `${defaultQuery}-${defaultSort}-${selectedStatus}-${selectedGenreId}-${selectedTypeId}`;
    if (currentFilters !== previousFilters) {
      setFilterAnnouncement("Search results updated with new filter selections");
      setPreviousFilters(currentFilters);
    }
  }, [defaultQuery, defaultSort, selectedStatus, selectedGenreId, selectedTypeId, previousFilters]);

  const handleFilterChange = (filters: Record<string, null | string>) => {
    const params = new URLSearchParams(searchParams);
    for (const [key, value] of Object.entries(filters)) {
      if (value === null) {
        params.delete(key);
      } else {
        params.set(key, value);
      }
    }
    params.set("page", "1");
    router.push(`?${params.toString()}`);
  };

  useEffect(() => {
    handleFilterChange({ query: debouncedSearch || null });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [debouncedSearch]);

  const handleSortChange = (sort: "latest" | "popular" | "rating") => {
    handleFilterChange({ sortBy: sort });
  };

  const handleClearFilters = () => {
    router.push("?");
  };

  return (
    <div className="lg:col-span-1">
      {/* Aria-live region to announce filter changes */}
      <div aria-atomic="true" aria-live="polite" className="sr-only" role="status">
        {filterAnnouncement}
      </div>

      <div aria-label="Comic search filters" className="sticky top-4 space-y-6">
        {/* Search Input */}
        <div>
          <label className="mb-2 block text-sm font-semibold" htmlFor="comic-search">
            Search
          </label>
          <Input
            aria-describedby="comic-search-help"
            className="w-full dark:border-border/50 dark:bg-muted/50 dark:placeholder-muted-foreground/50"
            id="comic-search"
            onChange={(e) => setSearchInput(e.target.value)}
            placeholder="Search comics..."
            type="text"
            value={searchInput}
          />
          <span className="sr-only" id="comic-search-help">
            Search by title, synopsis, author, or genre
          </span>
        </div>

        {/* Sort Options */}
        <fieldset>
          <legend className="mb-2 block text-sm font-semibold">Sort By</legend>
          <div className="space-y-1" role="group">
            {[
              { value: "latest" as const, label: "Latest" },
              { value: "popular" as const, label: "Popular" },
              { value: "rating" as const, label: "Top Rated" },
            ].map(({ value, label }) => (
              <button
                aria-label={`Sort by ${label.toLowerCase()}`}
                className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                  defaultSort === value
                    ? "bg-primary text-primary-foreground dark:bg-primary"
                    : "hover:bg-muted dark:hover:bg-muted/50"
                }`}
                key={value}
                onClick={() => handleSortChange(value)}
              >
                {label}
              </button>
            ))}
          </div>
        </fieldset>

        {/* Status Filter */}
        <fieldset>
          <legend className="mb-2 block text-sm font-semibold">Status</legend>
          <div className="space-y-1" role="group">
            <button
              aria-label="Show all comic statuses"
              className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                !selectedStatus
                  ? "bg-primary text-primary-foreground dark:bg-primary"
                  : "hover:bg-muted dark:hover:bg-muted/50"
              }`}
              onClick={() => handleFilterChange({ status: null })}
            >
              All
            </button>
            {COMIC_STATUSES.map(({ value, label }) => (
              <button
                aria-label={`Show only ${label.toLowerCase()} comics`}
                className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                  selectedStatus === value
                    ? "bg-primary text-primary-foreground dark:bg-primary"
                    : "hover:bg-muted dark:hover:bg-muted/50"
                }`}
                key={value}
                onClick={() => handleFilterChange({ status: value })}
              >
                {label}
              </button>
            ))}
          </div>
        </fieldset>

        {/* Genre Filter */}
        {genres.length > 0 && (
          <fieldset>
            <legend className="mb-2 block text-sm font-semibold">Genre</legend>
            <div className="max-h-48 space-y-1 overflow-y-auto" role="group">
              <button
                aria-label="Show comics from all genres"
                className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                  !selectedGenreId
                    ? "bg-primary text-primary-foreground dark:bg-primary"
                    : "hover:bg-muted dark:hover:bg-muted/50"
                }`}
                onClick={() => handleFilterChange({ genreId: null })}
              >
                All Genres
              </button>
              {genres.map((genre) => (
                <button
                  aria-label={`Show only ${genre.name} comics`}
                  className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                    selectedGenreId === String(genre.id)
                      ? "bg-primary text-primary-foreground dark:bg-primary"
                      : "hover:bg-muted dark:hover:bg-muted/50"
                  }`}
                  key={genre.id}
                  onClick={() => handleFilterChange({ genreId: String(genre.id) })}
                >
                  {genre.name}
                </button>
              ))}
            </div>
          </fieldset>
        )}

        {/* Type Filter */}
        {types.length > 0 && (
          <fieldset>
            <legend className="mb-2 block text-sm font-semibold">Type</legend>
            <div className="space-y-1" role="group">
              <button
                aria-label="Show comics of all types"
                className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                  !selectedTypeId
                    ? "bg-primary text-primary-foreground dark:bg-primary"
                    : "hover:bg-muted dark:hover:bg-muted/50"
                }`}
                onClick={() => handleFilterChange({ typeId: null })}
              >
                All Types
              </button>
              {types.map((t) => (
                <button
                  aria-label={`Show only ${t.name} comics`}
                  className={`w-full rounded px-3 py-2 text-left text-sm transition ${
                    selectedTypeId === String(t.id)
                      ? "bg-primary text-primary-foreground dark:bg-primary"
                      : "hover:bg-muted dark:hover:bg-muted/50"
                  }`}
                  key={t.id}
                  onClick={() => handleFilterChange({ typeId: String(t.id) })}
                >
                  {t.name}
                </button>
              ))}
            </div>
          </fieldset>
        )}

        {/* Clear Filters Button */}
        <Button
          aria-label="Clear all filter selections"
          className="w-full dark:border-border/50 dark:hover:bg-accent"
          onClick={handleClearFilters}
          variant="outline"
        >
          Clear Filters
        </Button>
      </div>
    </div>
  );
}
