import { Suspense } from "react";

import { ComicCard, ComicFilters, ComicListSkeleton, ComicPaginationControls } from "@/components/comics";
import { comicDal } from "@/dal/comic-dal";

interface ComicsWrapperProps {
  genreId?: number;
  genres?: Array<{ id: number; name: string }>;
  page?: number;
  query?: string;
  sortBy?: "latest" | "popular" | "rating";
  status?: string;
  typeId?: number;
  types?: Array<{ id: number; name: string }>;
}

async function ComicListContent({
  query,
  sortBy = "latest",
  page = 1,
  genreId,
  status,
  typeId,
}: {
  genreId?: number;
  page?: number;
  query?: string;
  sortBy?: "latest" | "popular" | "rating";
  status?: string;
  typeId?: number;
}) {
  const limit = 20;
  const offset = (Math.max(1, page) - 1) * limit;

  const options = {
    query: query || undefined,
    status,
    genreId,
    typeId,
    orderBy: sortBy as "latest" | "popular" | "rating" | "title",
    limit,
    offset,
  };

  const [comics, totalCount] = await Promise.all([comicDal.list(options), comicDal.count(options)]);

  const totalPages = Math.max(1, Math.ceil(totalCount / limit));

  if (comics.length === 0) {
    return (
      <div className="lg:col-span-3">
        <div className="py-12 text-center">
          <h3 className="mb-2 text-xl font-semibold">No comics found</h3>
          <p className="text-muted-foreground">Try adjusting your search or filters</p>
        </div>
      </div>
    );
  }

  return (
    <div className="lg:col-span-3">
      <div className="mb-6 flex items-center justify-between">
        <p className="text-sm text-muted-foreground">
          Showing {comics.length} of {totalCount} comics{query ? ` matching "${query}"` : ""}
        </p>
      </div>

      <div className="mb-8 grid grid-cols-2 gap-6 sm:grid-cols-3">
        {comics.map((comic) => (
          <div key={comic.id}>
            <ComicCard
              comic={{
                id: comic.id,
                slug: comic.slug,
                title: comic.title,
                coverImage: comic.coverImage || null,
                description: comic.description,
                rating: comic.rating || null,
                status: comic.status,
              }}
              type={(comic as Record<string, unknown>).type as { name: string } | null}
              variant="grid"
            />
          </div>
        ))}
      </div>

      {totalPages > 1 && <ComicPaginationControls page={page} query={query ?? ""} totalPages={totalPages} />}
    </div>
  );
}

export default function ComicsWrapper({
  query = "",
  sortBy = "latest",
  page = 1,
  genreId,
  status,
  typeId,
}: ComicsWrapperProps) {
  return (
    <main className="min-h-screen bg-background">
      <div className="border-b bg-white">
        <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <h1 className="mb-2 text-4xl font-bold">Browse Comics</h1>
          <p className="text-muted-foreground">Discover and read your favorite manga, manhwa, and more</p>
        </div>
      </div>

      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-4">
          <Suspense
            fallback={
              <div className="space-y-4">
                <div className="h-10 animate-pulse rounded bg-muted" />
                <div className="h-10 animate-pulse rounded bg-muted" />
                <div className="h-10 animate-pulse rounded bg-muted" />
              </div>
            }
          >
            <ComicFilters
              defaultQuery={query}
              defaultSort={sortBy}
              genres={[]}
              selectedGenreId={genreId?.toString()}
              selectedStatus={status}
              selectedTypeId={typeId?.toString()}
              types={[]}
            />
          </Suspense>

          <Suspense fallback={<ComicListSkeleton />}>
            <ComicListContent
              genreId={genreId}
              page={page}
              query={query}
              sortBy={sortBy}
              status={status}
              typeId={typeId}
            />
          </Suspense>
        </div>
      </div>
    </main>
  );
}
