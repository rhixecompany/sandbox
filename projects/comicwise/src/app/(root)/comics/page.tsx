/**
 * Comics Listing Page
 * Route: /comics
 */

import { Suspense } from "react";

import { ComicListSkeleton } from "@/components/comics";
import ComicsWrapper from "@/components/comics/comics-wrapper";
import { genreDal, typeDal } from "@/dal";

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Browse Comics | ComicWise",
  description: "Discover and read your favorite manga, manhwa, webtoons, and comics.",
};

interface PageProps {
  searchParams: Promise<{
    genreId?: string;
    page?: string;
    query?: string;
    sortBy?: "latest" | "popular" | "rating";
    status?: string;
    typeId?: string;
  }>;
}

export default async function ComicsPage({ searchParams }: PageProps) {
  const params = await searchParams;
  const query = params.query || "";
  const sortBy = (params.sortBy as "latest" | "popular" | "rating") || "latest";
  const page = parseInt(params.page || "1", 10);
  const genreId = params.genreId ? parseInt(params.genreId, 10) : undefined;
  const status = params.status || undefined;
  const typeId = params.typeId ? parseInt(params.typeId, 10) : undefined;

  const [genres, types] = await Promise.all([genreDal.list(), typeDal.list()]);

  return (
    <Suspense fallback={<ComicListSkeleton />}>
      <ComicsWrapper
        genreId={genreId}
        genres={genres}
        page={page}
        query={query}
        sortBy={sortBy}
        status={status}
        typeId={typeId}
        types={types}
      />
    </Suspense>
  );
}
