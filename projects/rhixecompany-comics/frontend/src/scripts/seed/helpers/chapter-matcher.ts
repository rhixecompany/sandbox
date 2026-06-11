/**
 * Chapter Matcher - Intelligently matches chapters to comics using multi-level strategy
 * Handles multiple chapter data formats and resolves fuzzy comic references
 */

/**
 * Three-level matching strategy for chapters to comics:
 * 1. Explicit comic.slug (fastest, most reliable)
 * 2. Alternative comicslug field (handles alt data formats)
 * 3. Fuzzy title matching (fallback for poorly formatted data)
 */
export function matchChapterToComic(
  chapter: unknown,
  comicCache: Map<string, number>,
  comicsByNormalizedSlug: Map<string, number>
): null | number {
  // Type guard: ensure chapter is an object with properties
  if (typeof chapter !== "object" || chapter === null) {
    return null;
  }
  const ch = chapter as Record<string, unknown>;

  // Level 1: Try explicit comic.slug first (most common format)
  if (typeof ch.comic === "object" && ch.comic !== null && "slug" in ch.comic) {
    const comic = ch.comic as { slug?: unknown };
    if (typeof comic.slug === "string") {
      const comicId = comicCache.get(comic.slug);
      if (comicId) return comicId;
    }
  }

  // Level 2: Try alternative comicslug field (handles alternate data formats)
  if (typeof ch.comicslug === "string") {
    // First try exact match
    let comicId = comicCache.get(ch.comicslug);
    if (comicId) return comicId;

    // Try normalized version
    const normalized = normalizeSlug(ch.comicslug);
    comicId = comicsByNormalizedSlug.get(normalized);
    if (comicId) return comicId;
  }

  // Level 3: Fuzzy title matching (fallback)
  if (typeof ch.comictitle === "string") {
    const normalized = normalizeSlug(ch.comictitle);

    // Find by normalized title
    const comicId = comicsByNormalizedSlug.get(normalized);
    if (comicId) return comicId;

    // Try partial matching (contains check)
    for (const [key, id] of comicsByNormalizedSlug.entries()) {
      if (key.includes(normalized) || normalized.includes(key)) {
        return id;
      }
    }
  }

  // Also try from comic.title if available
  if (typeof ch.comic === "object" && ch.comic !== null && "title" in ch.comic) {
    const comic = ch.comic as { title?: unknown };
    if (typeof comic.title === "string") {
      const normalized = normalizeSlug(comic.title);
      const comicId = comicsByNormalizedSlug.get(normalized);
      if (comicId) return comicId;

      // Try partial matching
      for (const [key, id] of comicsByNormalizedSlug.entries()) {
        if (key.includes(normalized) || normalized.includes(key)) {
          return id;
        }
      }
    }
  }

  return null;
}

/**
 * Normalize a string to slug format for fuzzy matching
 * Examples:
 *   "The Extra's Academy" → "the-extras-academy"
 *   "Solo Leveling" → "solo-leveling"
 *   "My-Hero--Academia" → "my-hero-academia"
 */
export function normalizeSlug(text: string): string {
  if (!text) return "";

  return (
    text
      .toLowerCase()
      // Replace special characters with nothing (removes apostrophes, etc.)
      .replaceAll(/[^\w\s-]/g, "")
      // Replace whitespace with hyphens
      .replaceAll(/\s+/g, "-")
      // Collapse multiple hyphens
      .replaceAll(/-+/g, "-")
      // Trim hyphens from start/end
      .trim()
      .replaceAll(/^-+|-+$/g, "")
  );
}

/**
 * Extract chapter number from chapter name
 * Examples:
 *   "Chapter 273" → 273
 *   "Ch. 5" → 5
 *   "Prologue" → null (will use 0 as fallback)
 *   "Episode 10" → 10
 */
export function extractChapterNumber(name: string): null | number {
  if (!name) return null;

  // Match patterns like "Chapter 123", "Ch. 5", "Episode 10", "#5"
  const match = name.match(/(?:chapter|ch|episode|ep|#)\s*\.?\s*(\d+)/i);
  if (match?.[1]) {
    return parseInt(match[1], 10);
  }

  // Try to find any number at the start
  const numMatch = name.match(/^(\d+)/);
  if (numMatch?.[1]) {
    return parseInt(numMatch[1], 10);
  }

  return null;
}

/**
 * Parse date from multiple possible field names and formats
 * Handles:
 *   - "August 14th 2025" (human-readable)
 *   - "2025-01-19" (ISO format)
 *   - Unix timestamps
 *   - Multiple field names: updatedAt, updated_at, releaseDate, release_date
 */
export function parseDate(dateValue: unknown): Date | null {
  if (!dateValue) return null;

  // Handle Date objects
  if (dateValue instanceof Date) {
    return isValidDate(dateValue) ? dateValue : null;
  }

  // Handle string dates
  if (typeof dateValue === "string") {
    const cleaned = dateValue.trim();
    if (!cleaned) return null;

    try {
      const date = new Date(cleaned);
      return isValidDate(date) ? date : null;
    } catch {
      return null;
    }
  }

  // Handle numeric timestamps
  if (typeof dateValue === "number") {
    const date = new Date(dateValue);
    return isValidDate(date) ? date : null;
  }

  return null;
}

/**
 * Check if a date is valid (not NaN)
 */
function isValidDate(date: Date): boolean {
  return !isNaN(date.getTime());
}

/**
 * Extract images from chapter data
 * Handles both formats:
 *   - images: [{ url: "..." }] (standard format)
 *   - image_urls: ["..."] (alternative format)
 */
export function extractImageUrls(chapter: unknown): string[] {
  const urls: string[] = [];

  // Type guard for chapter
  if (typeof chapter !== "object" || chapter === null) {
    return urls;
  }
  const ch = chapter as Record<string, unknown>;

  // Format 1: images array with url property
  if (Array.isArray(ch.images)) {
    for (const img of ch.images) {
      if (
        typeof img === "object" &&
        img !== null &&
        "url" in img &&
        typeof (img as Record<string, unknown>).url === "string"
      ) {
        urls.push((img as Record<string, unknown>).url as string);
      }
    }
  }

  // Format 2: image_urls array with direct strings
  if (Array.isArray(ch.image_urls)) {
    for (const url of ch.image_urls) {
      if (typeof url === "string") {
        urls.push(url);
      }
    }
  }

  return urls;
}

/**
 * Extract chapter title with fallback chain
 */
export function getChapterTitle(chapter: unknown): string {
  // Type guard for chapter
  if (typeof chapter !== "object" || chapter === null) {
    return "Untitled Chapter";
  }
  const ch = chapter as Record<string, unknown>;

  return (
    (typeof ch.title === "string" ? ch.title : undefined) || // Standard title field
    (typeof ch.chaptertitle === "string" ? ch.chaptertitle : undefined) || // Alternative format
    (typeof ch.name === "string" ? ch.name : undefined) || // Fallback to name
    (typeof ch.chaptername === "string" ? ch.chaptername : undefined) || // Alternative format
    "Untitled Chapter"
  );
}

/**
 * Extract chapter name/number with fallback chain
 */
export function getChapterName(chapter: unknown): string {
  // Type guard for chapter
  if (typeof chapter !== "object" || chapter === null) {
    return "Unknown";
  }
  const ch = chapter as Record<string, unknown>;

  return (
    (typeof ch.name === "string" ? ch.name : undefined) ||
    (typeof ch.chaptername === "string" ? ch.chaptername : undefined) ||
    "Unknown"
  );
}

/**
 * Extract chapter URL with fallback
 */
export function getChapterUrl(chapter: unknown): null | string {
  // Type guard for chapter
  if (typeof chapter !== "object" || chapter === null) {
    return null;
  }
  const ch = chapter as Record<string, unknown>;

  return typeof ch.url === "string" ? ch.url : null;
}
