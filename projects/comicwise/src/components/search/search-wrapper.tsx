"use client";

import { Suspense } from "react";

import { AdvancedSearchForm } from "@/components/search/advanced-search-form";
import { SearchResults } from "@/components/search/search-results";

import type { SearchResults as SearchResultsType } from "@/schemas/search.schema";

interface SearchWrapperProps {
  authors: Array<{ id: string; name: string }>;
  genres: Array<{ id: string; name: string }>;
  isLoading?: boolean;
  results: null | SearchResultsType;
}

export function SearchWrapper({ authors, genres, results, isLoading = false }: SearchWrapperProps) {
  return (
    <div className="min-h-screen bg-linear-to-br from-gray-50 to-white dark:bg-linear-to-br dark:from-background dark:to-background/95">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {/* Page Header */}
        <div className="mb-8">
          <h1 className="mb-2 text-4xl font-bold dark:text-foreground">Advanced Search</h1>
          <p className="text-lg text-gray-600 dark:text-muted-foreground">
            Find your next favorite manga or comic with our advanced search filters
          </p>
        </div>

        {/* Search Layout: Form on left, results on right */}
        <div className="grid gap-6 lg:grid-cols-3">
          {/* Sidebar: Search Form */}
          <div className="lg:col-span-1">
            <Suspense
              fallback={
                <div className="space-y-4">
                  <div className="h-10 animate-pulse rounded bg-muted" />
                  <div className="h-10 animate-pulse rounded bg-muted" />
                  <div className="h-10 animate-pulse rounded bg-muted" />
                </div>
              }
            >
              <AdvancedSearchForm authors={authors} genres={genres} />
            </Suspense>
          </div>

          {/* Main: Search Results */}
          <div className="lg:col-span-2">
            <Suspense fallback={<div>Loading search results...</div>}>
              <SearchResults isLoading={isLoading} results={results} />
            </Suspense>
          </div>
        </div>
      </div>
    </div>
  );
}
