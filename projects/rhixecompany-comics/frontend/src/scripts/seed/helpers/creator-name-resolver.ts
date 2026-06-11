/**
 * Creator (author/artist) name resolution utilities
 * Handles splitting, normalization, and deduplication
 */

/**
 * Split creator names on "/" separator
 * Example: "Redice Studio/Indestructible" → ["Redice Studio", "Indestructible"]
 * Placeholder "_" is replaced with "Unknown"
 */
export function splitCreators(input: string): string[] {
  if (!input || input.trim() === "" || input === "_") {
    return ["Unknown"];
  }

  return input
    .split("/")
    .map((name) => normalizeCreatorName(name))
    .filter((name) => name !== "");
}

/**
 * Normalize creator name: trim whitespace, replace "_" with "Unknown"
 */
export function normalizeCreatorName(name: string): string {
  const trimmed = name.trim();

  if (trimmed === "" || trimmed === "_") {
    return "Unknown";
  }

  return trimmed;
}

/**
 * Check if a creator is the "Unknown" placeholder
 */
export function isUnknownCreator(name: string): boolean {
  const normalized = normalizeCreatorName(name);
  return normalized === "Unknown";
}

/**
 * Cache interface for creator lookups
 */
export interface CreatorCache {
  get(name: string): { id: string; name: string } | undefined;
  has(name: string): boolean;
  set(name: string, value: { id: string; name: string }): void;
}

/**
 * Lookup or create author in cache and database
 * Returns cached or newly created author record
 *
 * @param name - Creator name to lookup/create
 * @param cache - Creator cache map
 * @param createFn - Function to create record in database if missing
 * @returns Created or cached author record
 */
export async function lookupOrCreateCreator(
  name: string,
  cache: CreatorCache,
  createFn: (name: string) => Promise<{ id: string; name: string }>
): Promise<{ id: string; name: string }> {
  const normalized = normalizeCreatorName(name);

  // Check cache first
  if (cache.has(normalized)) {
    return cache.get(normalized)!;
  }

  // Create in database
  const created = await createFn(normalized);
  cache.set(normalized, created);

  return created;
}
