/**
 * ComicDataExtractor - Extracts unique authors, artists, genres, and types
 * from comic.json for seeding entity tables.
 *
 * Since separate author.json, artist.json, genre.json files don't exist,
 * this utility reads comic.json once and extracts embedded entity data.
 */

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import type { ArtistSeed } from "@/schemas/seed/artist.seed";
import type { AuthorSeed } from "@/schemas/seed/author.seed";
import type { GenreSeed } from "@/schemas/seed/genre.seed";

interface RawComicRecord {
  artist?: { name: string } | null | string;
  author?: { name: string } | null | string;
  genres?: Array<{ name: string } | string>;
  type?: { name: string } | string;
}

function slugify(name: string): string {
  return name
    .toLowerCase()
    .replaceAll(/[^\w\s-]/g, "")
    .replaceAll(/\s+/g, "-")
    .replaceAll(/-+/g, "-")
    .replaceAll(/^-|-$/g, "");
}

function extractName(val: { name: string } | null | string | undefined): string | undefined {
  if (!val || val === "_") return undefined;
  if (typeof val === "string") return val === "_" ? undefined : val;
  return val.name === "_" ? undefined : val.name;
}

/** Cached extraction results */
let cachedResult: ExtractedEntities | null = null;

export interface ExtractedEntities {
  artists: ArtistSeed[];
  authors: AuthorSeed[];
  genres: GenreSeed[];
  types: string[];
}

/**
 * Load comic.json and extract unique entities.
 * Results are cached after first call.
 */
export async function extractEntitiesFromComics(): Promise<ExtractedEntities> {
  if (cachedResult) return cachedResult;

  let rawComics: RawComicRecord[];
  try {
    rawComics = await dataLoader.loadWithFallback<RawComicRecord>("comic");
  } catch (error) {
    logger.warn(`Failed to load comic.json for entity extraction: ${error}`);
    return { authors: [], artists: [], genres: [], types: [] };
  }

  const authorSet = new Set<string>();
  const artistSet = new Set<string>();
  const genreSet = new Set<string>();
  const typeSet = new Set<string>();

  for (const comic of rawComics) {
    const authorName = extractName(comic.author);
    if (authorName) authorSet.add(authorName);

    const artistName = extractName(comic.artist);
    if (artistName) artistSet.add(artistName);

    if (comic.type) {
      const typeName = typeof comic.type === "string" ? comic.type : comic.type.name;
      if (typeName && typeName !== "_") typeSet.add(typeName);
    }

    if (comic.genres && Array.isArray(comic.genres)) {
      for (const g of comic.genres) {
        const name = typeof g === "string" ? g : g.name;
        if (name && name !== "_") genreSet.add(name);
      }
    }
  }

  cachedResult = {
    authors: Array.from(authorSet).map((name) => ({ name })),
    artists: Array.from(artistSet).map((name) => ({ name })),
    genres: Array.from(genreSet).map((name) => ({ name, slug: slugify(name) })),
    types: Array.from(typeSet),
  };

  logger.info(
    `Extracted from comic.json: ${cachedResult.authors.length} authors, ` +
      `${cachedResult.artists.length} artists, ${cachedResult.genres.length} genres, ` +
      `${cachedResult.types.length} types`
  );

  return cachedResult;
}

/** Reset cache (useful for testing) */
export function resetExtractionCache(): void {
  cachedResult = null;
}
