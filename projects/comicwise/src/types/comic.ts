/**
 * Comic Types - Shared across components, pages, and wrappers
 */

// Basic comic summary for grid/list views
export interface ComicSummary {
  coverImage: null | string;
  description: null | string;
  id: number;
  rating: null | number | string;
  slug: string;
  status: string;
  title: string;
}

// Comic with type information
export interface ComicWithType extends ComicSummary {
  type?: { name: string } | null;
}

// Full comic detail with relationships
export interface ComicDetail {
  artist?: { id: number; name: string } | null;
  author?: { id: number; name: string } | null;
  chapters?: Array<{
    chapterNumber: number;
    createdAt: Date | string;
    id: number;
    title: null | string;
    url?: null | string;
  }>;
  comicToGenre?: Array<{ genre?: { id: number; name: string } }>;
  coverImage: null | string;
  description: null | string;
  genres?: Array<{ id: number; name: string }>;
  id: number;
  rating: { average: number; count?: number } | null;
  slug: string;
  status: string;
  synopsis?: null | string;
  title: string;
  type?: { id: number; name: string } | null;
}

// Chapter information
export interface ChapterInfo {
  chapterNumber: number;
  createdAt: Date | string;
  id: number;
  title: null | string;
  url?: null | string;
}

// Genre for comic
export interface GenreInfo {
  description?: null | string;
  id: number;
  name: string;
  slug?: string;
}

// Author/Artist
export interface PersonInfo {
  bio?: null | string;
  id: number;
  name: string;
}

// Related comic (for recommendations)
export interface RelatedComic {
  coverImage: null | string;
  description?: string;
  id: number;
  rating: null | number | string;
  slug: string;
  status?: string;
  title: string;
  type?: { name: string } | null;
}

// Filter options for comic listing
export interface ComicFilterOptions {
  genreId?: number;
  limit?: number;
  offset?: number;
  orderBy?: "latest" | "popular" | "rating" | "title";
  query?: string;
  status?: string;
  typeId?: number;
}
