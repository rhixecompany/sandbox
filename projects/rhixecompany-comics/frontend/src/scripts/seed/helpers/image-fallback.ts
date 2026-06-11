/**
 * ComicWise Branded Placeholder Configuration
 *
 * Design System:
 * - Background: #1a1a2e (dark charcoal)
 * - Accent: #e94560 (vibrant pink/red)
 * - Text: #ffffff (white)
 *
 * Placeholder URLs use placehold.co with custom text and colors
 * @module image-fallback
 */

/**
 * ComicWise brand color palette
 */
export const COMICWISE_BRAND = {
  bg: "1a1a2e",
  accent: "e94560",
  text: "ffffff",
  size: {
    cover: "300x450",
    chapter: "800x1200",
  },
} as const;

/**
 * Generate branded cover placeholder URL
 *
 * @param title - Comic title to display
 * @returns Placeholder URL with branded styling
 */
export function getCoverFallback(title: string): string {
  const encoded = encodeURIComponent(title || "No Title");
  return `https://placehold.co/${COMICWISE_BRAND.size.cover}/${COMICWISE_BRAND.bg}/${COMICWISE_BRAND.text}?text=${encoded}`;
}

/**
 * Generate branded chapter page placeholder URL
 *
 * @param chapterInfo - Chapter identifier (e.g., "Chapter 1" or "Ch.15")
 * @returns Placeholder URL with branded styling
 */
export function getChapterPageFallback(chapterInfo: string): string {
  const encoded = encodeURIComponent(chapterInfo || "No Chapter");
  return `https://placehold.co/${COMICWISE_BRAND.size.chapter}/${COMICWISE_BRAND.bg}/${COMICWISE_BRAND.text}?text=${encoded}`;
}

/**
 * Generate generic branded placeholder
 *
 * @param text - Text to display
 * @param width - Image width
 * @param height - Image height
 * @returns Branded placeholder URL
 */
export function getPlaceholder(text: string, width = 300, height = 450): string {
  const encoded = encodeURIComponent(text || "Placeholder");
  return `https://placehold.co/${width}x${height}/${COMICWISE_BRAND.bg}/${COMICWISE_BRAND.text}?text=${encoded}`;
}

/**
 * Generate ComicWise branded logo SVG data URL
 * Uses inline SVG with ComicWise branding for embedding
 *
 * @param width - SVG width
 * @param height - SVG height
 * @returns SVG data URL with ComicWise branding
 */
export function getComicWiseLogoPlaceholder(width = 300, height = 450): string {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <rect width="${width}" height="${height}" fill="#${COMICWISE_BRAND.bg}"/>
  <line x1="50" y1="${height / 2 - 40}" x2="${width - 50}" y2="${height / 2 - 40}" stroke="#${COMICWISE_BRAND.accent}" stroke-width="3"/>
  <text x="50%" y="${height / 2 - 10}" dominant-baseline="middle" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="32" font-weight="bold" fill="#${COMICWISE_BRAND.accent}">ComicWise</text>
  <line x1="50" y1="${height / 2 + 10}" x2="${width - 50}" y2="${height / 2 + 10}" stroke="#${COMICWISE_BRAND.accent}" stroke-width="3"/>
  <text x="50%" y="${height / 2 + 45}" dominant-baseline="middle" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#${COMICWISE_BRAND.text}">No Image Available</text>
</svg>`;
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}
