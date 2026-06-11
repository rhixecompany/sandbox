/**
 * Image Optimization Utilities
 * Reference: Next.js 16 Image Optimization Best Practices
 *
 * Provides responsive image sizing, blur placeholders, and performance metrics
 */

import type { CSSProperties } from "react";

/**
 * Responsive image sizes for different breakpoints
 * Used with next/image sizes prop for optimal loading
 */
export const RESPONSIVE_IMAGE_SIZES = {
  // Hero/Cover images
  hero: "(max-width: 640px) 100vw, (max-width: 1024px) 90vw, 100vw",

  // Comic cards (3 columns on desktop, 2 on tablet, 1 on mobile)
  comicCard: "(max-width: 640px) 50vw, (max-width: 1024px) 33vw, 25vw",

  // Thumbnail images (small previews)
  thumbnail: "(max-width: 640px) 80px, 100px",

  // Avatar images (user profiles)
  avatar: "(max-width: 640px) 40px, 56px",

  // Chapter preview images
  chapterPreview: "(max-width: 640px) 100vw, (max-width: 1024px) 80vw, 60vw",
};

/**
 * Device-specific widths for comic cover images
 * Next.js will generate images at these widths for optimal bandwidth
 *
 * Supports both 2x and 3x density on high-DPI devices
 */
export const COMIC_COVER_WIDTHS = [
  192, // Mobile @ 1x
  384, // Mobile @ 2x
  576, // Tablet @ 1x
  1152, // Tablet @ 2x
  864, // Desktop @ 1x
  1728, // Desktop @ 2x
];

/**
 * Generates blur data URL for placeholder effect
 * Creates a low-quality placeholder while image loads
 *
 * Usage: <Image src={src} placeholder="blur" blurDataURL={generateBlur()} />
 */
export function generateBlurDataUrl(width: number = 10, height: number = 10): string {
  // Minimal SVG placeholder (very small, fast to render)
  const svg = `
    <svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">
      <rect width="${width}" height="${height}" fill="#e5e7eb"/>
    </svg>
  `;

  return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
}

/**
 * Image aspect ratios for different content types
 * Use with aspect-ratio CSS for proper space reservation
 * Prevents Cumulative Layout Shift (CLS)
 */
export const IMAGE_ASPECT_RATIOS = {
  // Standard manga/comic cover ratio (portrait)
  comicCover: "2/3",

  // Chapter preview/thumbnail
  chapterPreview: "16/9",

  // User avatar
  avatar: "1/1",

  // Banner/hero
  banner: "16/9",

  // Landscape cover
  landscape: "3/2",
};

/**
 * Image loading strategies
 * eager: Load immediately (above the fold)
 * lazy: Load when near viewport (below the fold)
 */
export const IMAGE_LOADING_STRATEGY = {
  EAGER: "eager",
  LAZY: "lazy",
} as const;

/**
 * Determines loading strategy based on position
 * @param isAboveFold - Is image in initial viewport?
 * @returns Loading strategy ("eager" or "lazy")
 */
export function getImageLoadingStrategy(isAboveFold: boolean): string {
  return isAboveFold ? IMAGE_LOADING_STRATEGY.EAGER : IMAGE_LOADING_STRATEGY.LAZY;
}

/**
 * Creates style object with aspect ratio to prevent CLS
 * @param aspectRatio - Aspect ratio string (e.g., "2/3")
 * @returns CSS style object
 */
export function createAspectRatioStyle(aspectRatio: string): CSSProperties {
  return {
    aspectRatio,
    width: "100%",
    overflow: "hidden",
    backgroundColor: "#f3f4f6", // Light gray background during load
  };
}

/**
 * Image optimization presets for common use cases
 * Each preset includes optimal sizes and loading strategy
 */
export const IMAGE_PRESETS = {
  // Comic cover image (above the fold)
  comicCoverFeatured: {
    sizes: RESPONSIVE_IMAGE_SIZES.hero,
    loading: "eager" as const,
    aspectRatio: IMAGE_ASPECT_RATIOS.comicCover,
    priority: true,
  },

  // Comic cover image (in list, lazy load)
  comicCoverCard: {
    sizes: RESPONSIVE_IMAGE_SIZES.comicCard,
    loading: "lazy" as const,
    aspectRatio: IMAGE_ASPECT_RATIOS.comicCover,
    priority: false,
  },

  // Chapter thumbnail
  chapterThumbnail: {
    sizes: RESPONSIVE_IMAGE_SIZES.thumbnail,
    loading: "lazy" as const,
    aspectRatio: IMAGE_ASPECT_RATIOS.chapterPreview,
    priority: false,
  },

  // User avatar
  avatar: {
    sizes: RESPONSIVE_IMAGE_SIZES.avatar,
    loading: "lazy" as const,
    aspectRatio: IMAGE_ASPECT_RATIOS.avatar,
    priority: false,
  },

  // Chapter preview/reader
  chapterPreview: {
    sizes: RESPONSIVE_IMAGE_SIZES.chapterPreview,
    loading: "eager" as const,
    aspectRatio: IMAGE_ASPECT_RATIOS.chapterPreview,
    priority: true,
  },
};

/**
 * Performance optimization guide for images
 * Checklist to ensure images are optimized
 */
export const IMAGE_OPTIMIZATION_CHECKLIST = [
  "✅ Use next/image component (not <img>)",
  "✅ Specify width and height (aspect ratio)",
  "✅ Set sizes prop (responsive sizing)",
  "✅ Use priority={true} for above-the-fold",
  "✅ Use placeholder='blur' with blurDataURL",
  "✅ Use formats: ['image/avif', 'image/webp']",
  "✅ Set loading='lazy' for below-the-fold",
  "✅ Verify image is in remotePatterns",
  "✅ Use alt text (accessibility + SEO)",
  "✅ Monitor LCP (Largest Contentful Paint)",
];

/**
 * Example usage with all optimizations:
 *
 * import Image from 'next/image';
 * import { IMAGE_PRESETS, generateBlurDataUrl } from '@/lib/image-optimization';
 *
 * export function ComicCoverCard({ src, alt }: { src: string; alt: string }) {
 *   const preset = IMAGE_PRESETS.comicCoverCard;
 *
 *   return (
 *     <div style={createAspectRatioStyle(preset.aspectRatio)}>
 *       <Image
 *         src={src}
 *         alt={alt}
 *         fill
 *         sizes={preset.sizes}
 *         loading={preset.loading}
 *         placeholder="blur"
 *         blurDataURL={generateBlurDataUrl(10, 15)}
 *         quality={75}
 *       />
 *     </div>
 *   );
 * }
 */
