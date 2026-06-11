export interface Genre {
  id: number;
  name: string;
  slug: string;
}

export interface Author {
  id: number;
  name: string;
  slug: string;
}

export interface Artist {
  id: number;
  name: string;
  slug: string;
}

export interface Type {
  id: number;
  name: string;
  slug: string;
}

export interface ComicImage {
  id: number;
  image: string;
  alt_text: string;
  is_primary: boolean;
}

export interface ChapterImage {
  id: number;
  image: string;
  page_number: number;
  alt_text?: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface ComicListEntry {
  id: number;
  title: string;
  slug: string;
  status: string;
  rating: number;
  numchapters: number;
  updated_at: string;
  type_name: string;
  author_name: string;
  thumbnail: string;
}

export interface Chapter {
  id: number;
  title: string;
  slug: string;
  chapter_number: number;
  volume_number: number | null;
  date_published: string;
  comic: number;
}

export interface ComicDetail {
  id: number;
  title: string;
  slug: string;
  description: string;
  status: string;
  rating: number;
  numchapters: number;
  updated_at: string;
  created_at: string;
  type_name: string;
  author_name: string;
  artist_name: string;
  genres: Genre[];
  chapters: Chapter[];
  images: ComicImage[];
  thumbnail: string;
}

export interface ChapterDetail {
  id: number;
  title: string;
  slug: string;
  chapter_number: number;
  volume_number: number | null;
  date_published: string;
  comic: number;
  comic_slug: string;
  comic_title: string;
  images: ChapterImage[];
  previous_chapter: Chapter | null;
  next_chapter: Chapter | null;
}
