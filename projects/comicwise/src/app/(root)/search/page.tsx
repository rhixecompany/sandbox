/**
 * Advanced Search Page
 * Route: /search
 */

import { getSearchFiltersAction } from "@/actions/search-filters.actions";
import { SearchWrapper } from "@/components/search/search-wrapper";

interface SearchPageProps {
  searchParams: Promise<{
    authors?: string | string[];
    genres?: string | string[];
    maxRating?: string;
    minRating?: string;
    page?: string;
    q?: string;
    sortBy?: string;
    status?: string;
  }>;
}

export async function generateMetadata({ searchParams }: SearchPageProps) {
  const params = await searchParams;
  const query = typeof params.q === "string" ? params.q : "";

  return {
    title: query ? `Search Results for "${query}" | ComicWise` : "Advanced Search | ComicWise",
    description: query
      ? `Search results for "${query}" in ComicWise manga and comic reader`
      : "Advanced search for comics with filters by genre, author, rating, and status",
  };
}

export default async function SearchPage(_props: SearchPageProps) {
  let genresData: Array<{ id: string; name: string }> = [];
  let authorsData: Array<{ id: string; name: string }> = [];

  try {
    const result = await getSearchFiltersAction();
    if (result.ok && result.data) {
      genresData = result.data.genres;
      authorsData = result.data.authors;
    }
  } catch (error) {
    console.error("Failed to load search filters:", error);
  }

  return <SearchWrapper authors={authorsData} genres={genresData} results={null} />;
}
