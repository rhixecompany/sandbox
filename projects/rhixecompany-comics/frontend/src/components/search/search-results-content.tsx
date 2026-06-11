/**
 * Search Results Content Component
 * Server component displaying search results with pagination
 */

import Image from "next/image";
import Link from "next/link";

import { Button } from "@/components/ui/button";

import type { SearchResult } from "@/dal/search-dal";

interface SearchResultsContentProps {
  initialResults: null | SearchResult;
  page: number;
  query: string;
}

export default function SearchResultsContent({ initialResults, query, page }: SearchResultsContentProps) {
  if (!initialResults || initialResults.items.length === 0) {
    return (
      <div className="py-12 text-center">
        <p className="mb-4 text-lg text-muted-foreground">No comics found matching &quot;{query}&quot;</p>
        <p className="text-sm text-muted-foreground">Try searching with different keywords or filters</p>
      </div>
    );
  }

  const totalPages = Math.ceil(initialResults.total / initialResults.pageSize);

  return (
    <div className="space-y-6">
      {/* Results Header */}
      <div className="flex items-center justify-between">
        <p className="text-sm text-muted-foreground">
          Found {initialResults.total} comics matching &quot;{query}&quot;
        </p>
      </div>

      {/* Results Grid */}
      <div className="grid grid-cols-1 gap-4">
        {initialResults.items.map((comic) => (
          <Link
            className="group flex gap-4 rounded-lg border p-4 transition-colors hover:bg-accent"
            href={`/comics/${comic.slug}`}
            key={comic.id}
          >
            {/* Comic Cover */}
            {comic.coverImage && (
              <div className="relative h-32 w-20 flex-shrink-0 overflow-hidden rounded">
                <Image
                  alt={comic.title}
                  className="object-cover transition-transform group-hover:scale-105"
                  fill
                  src={comic.coverImage}
                />
              </div>
            )}

            {/* Comic Info */}
            <div className="min-w-0 flex-1">
              {/* Title */}
              <h3 className="line-clamp-2 text-lg font-semibold transition-colors group-hover:text-primary">
                {comic.title}
              </h3>

              {/* Author & Artist */}
              <div className="space-y-1 text-sm text-muted-foreground">
                {comic.author && <p>by {comic.author.name}</p>}
                {comic.artist && comic.artist.id !== comic.author?.id && <p>art by {comic.artist.name}</p>}
              </div>

              {/* Description */}
              <p className="mt-2 line-clamp-2 text-sm text-muted-foreground">{comic.description}</p>

              {/* Genres */}
              {comic.genres && comic.genres.length > 0 && (
                <div className="mt-3 flex flex-wrap gap-2">
                  {comic.genres.slice(0, 3).map((g) => (
                    <span
                      className="inline-block rounded bg-secondary px-2 py-1 text-xs text-secondary-foreground"
                      key={g.id}
                    >
                      {g.name}
                    </span>
                  ))}
                  {comic.genres.length > 3 && (
                    <span className="inline-block px-2 py-1 text-xs text-muted-foreground">
                      +{comic.genres.length - 3} more
                    </span>
                  )}
                </div>
              )}

              {/* Status */}
              {comic.status && (
                <div className="mt-2">
                  <span className="inline-block rounded bg-blue-100 px-2 py-1 text-xs text-blue-900 dark:bg-blue-900 dark:text-blue-100">
                    {comic.status}
                  </span>
                </div>
              )}
            </div>
          </Link>
        ))}
      </div>

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="mt-8 flex items-center justify-center gap-2">
          {page > 0 && (
            <Link href={`/search?q=${encodeURIComponent(query)}&page=${page - 1}`}>
              <Button variant="outline">Previous</Button>
            </Link>
          )}

          {/* Page Numbers */}
          <div className="flex gap-2">
            {Array.from({ length: totalPages }).map((_, i) => (
              <Link href={`/search?q=${encodeURIComponent(query)}&page=${i}`} key={i}>
                <Button size="sm" variant={i === page ? "default" : "outline"}>
                  {i + 1}
                </Button>
              </Link>
            ))}
          </div>

          {page < totalPages - 1 && (
            <Link href={`/search?q=${encodeURIComponent(query)}&page=${page + 1}`}>
              <Button variant="outline">Next</Button>
            </Link>
          )}
        </div>
      )}
    </div>
  );
}
