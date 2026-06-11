/**
 * ComicSeeder - seeds comics with relation resolution and image handling
 */

import { asc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { comic, comicImage, comicToGenre } from "@/database/schema";
import { type ComicSeed, comicSeedItemSchema } from "@/schemas/seed/comic.seed";

import { type EntityMeta, extractExtension, extractOriginalName, imageDownloader } from "@/storages/image-downloader";
import { dataLoader } from "../data-loader";
import { stripHtmlTags } from "../helpers/html-utils";
import { getCoverFallback } from "../helpers/image-fallback";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

/**
 * ComicSeeder loads comics from JSON with full relation resolution
 *
 * Handles:
 * - Author/artist/type/genre ID resolution
 * - Cover image download (local strategy) and selection
 * - ComicToGenre junction table population
 * - HTML stripping from descriptions
 * - ComicWise branded fallback for missing covers
 */
export class ComicSeeder extends BaseSeeder<ComicSeed> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("comics", comicSeedItemSchema, cache, options);
    this.dependencies = ["types", "authors", "artists", "genres"];
  }

  protected getDataSources(): string[] {
    return ["comic"];
  }

  /**
   * Pre-populate comic cache from existing database records
   * This ensures chapter seeding can find comics even if they weren't just inserted
   */
  private async preloadComicCache(): Promise<void> {
    try {
      const existingComics = await db.query.comic.findMany();
      for (const comic of existingComics) {
        this.cache.comics.set(comic.slug, comic.id);
      }
      logger.debug(`Pre-loaded ${existingComics.length} existing comics into cache`);
    } catch (error) {
      logger.warn(`Failed to pre-load comic cache: ${error}`);
    }
  }

  /**
   * Override seed to pre-load comic cache before processing
   */
  async seed(): Promise<EntityResult> {
    // Pre-load existing comics into cache
    await this.preloadComicCache();
    // Call parent seed method
    const result = await super.seed();
    // Post-seed: update coverImages from comicImage table
    await this.updateCoverImagesFromComicImages();
    logger.info(`Comic cache after seeding: ${this.cache.comics.size} entries`);
    return result;
  }

  /**
   * After seeding, update comics with no coverImage by fetching the latest image from comicImage table
   * Uses ComicWise branded fallback if no images exist
   */
  private async updateCoverImagesFromComicImages(): Promise<void> {
    try {
      // Find all comics with empty or no coverImage
      const comicsNeedingCover = await db.query.comic.findMany({
        where: (c, { or, isNull }) => or(isNull(c.coverImage), eq(c.coverImage, "")),
      });

      if (comicsNeedingCover.length === 0) {
        logger.debug("All comics have coverImages, skipping coverImage update");
        return;
      }

      logger.info(`Updating coverImages for ${comicsNeedingCover.length} comics`);

      for (const comicRecord of comicsNeedingCover) {
        // Find the first image for this comic (lowest imageOrder)
        const firstImage = await db.query.comicImage.findFirst({
          where: eq(comicImage.comicId, comicRecord.id),
          orderBy: [asc(comicImage.imageOrder)],
        });

        const coverUrl = firstImage ? firstImage.imageUrl : getCoverFallback(comicRecord.title);

        await db.update(comic).set({ coverImage: coverUrl, updatedAt: new Date() }).where(eq(comic.id, comicRecord.id));
        logger.debug(`Updated coverImage for comic ${comicRecord.id} to ${coverUrl}`);
      }
    } catch (error) {
      logger.warn(`Failed to update coverImages from comicImages: ${error}`);
    }
  }

  /**
   * Download cover image to local storage if using local strategy
   */
  private async downloadCoverImage(coverUrl: string, comicId: number, slug: string, title: string): Promise<string> {
    try {
      const entityMeta: EntityMeta = {
        slug,
        isCover: true,
        originalExtension: extractExtension(coverUrl),
        originalName: extractOriginalName(coverUrl),
      };

      const result = await imageDownloader.download(coverUrl, "comics", comicId, { entityMeta });
      if (result.success && result.filePath) {
        return result.filePath;
      }
      return getCoverFallback(title);
    } catch {
      return getCoverFallback(title);
    }
  }

  /** Maps title → all slug variants from JSON (for cross-referencing chapters) */
  private slugAliases = new Map<string, Set<string>>();

  protected async loadData(): Promise<ComicSeed[]> {
    const sources = this.getDataSources();

    if (sources.length === 0) {
      return [];
    }

    const allData: ComicSeed[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ComicSeed>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} comic records from ${source}`);
      } catch (error) {
        logger.warn(`Failed to load ${source}: ${error}`);
      }
    }

    // Collect all slug variants per title before deduplication
    for (const c of allData) {
      if (!this.slugAliases.has(c.title)) {
        this.slugAliases.set(c.title, new Set());
      }
      this.slugAliases.get(c.title)!.add(c.slug);
    }

    // Deduplicate by title (DB has unique constraint on title)
    const seen = new Set<string>();
    const deduplicated = allData.filter((c) => {
      if (seen.has(c.title)) return false;
      seen.add(c.title);
      return true;
    });

    if (deduplicated.length < allData.length) {
      logger.info(
        `Deduplicated comics: ${allData.length} → ${deduplicated.length} (removed ${allData.length - deduplicated.length} duplicates)`
      );
    }

    return deduplicated;
  }

  protected getUniqueField(): string {
    return "slug";
  }

  protected async transformData(raw: ComicSeed): Promise<unknown> {
    // Clean description (strip HTML tags)
    const cleanDescription = raw.description ? stripHtmlTags(raw.description) : null;

    return {
      ...raw,
      description: cleanDescription,
    };
  }

  async insertBatch(data: ComicSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        // Check if comic already exists (by slug or title)
        const existing =
          (await db.query.comic.findFirst({
            where: (comic_table) => eq(comic_table.slug, item.slug),
          })) ??
          (await db.query.comic.findFirst({
            where: (comic_table) => eq(comic_table.title, item.title),
          }));

        if (existing) {
          // Cache by BOTH the JSON slug and the DB slug for chapter matching
          this.cache.comics.set(item.slug, existing.id);
          this.cache.comics.set(existing.slug, existing.id);
          // Also cache all slug aliases from duplicate JSON entries
          const aliases = this.slugAliases.get(item.title);
          if (aliases) {
            for (const alias of aliases) {
              this.cache.comics.set(alias, existing.id);
            }
          }

          // If force overwrite is enabled, update the comic
          if (this.options.forceOverwrite) {
            const typeId = item.type?.name ? this.cache.types.get(item.type.name) : undefined;
            const authorEntry = item.author?.name ? this.cache.authors.get(item.author.name) : undefined;
            const artistEntry = item.artist?.name ? this.cache.artists.get(item.artist.name) : undefined;

            const cleanDescription = item.description ? stripHtmlTags(item.description) : "";
            const newPublicationDate =
              item.updatedAt instanceof Date && !isNaN(item.updatedAt.getTime()) ? item.updatedAt : new Date();
            const newTypeId = typeId ?? null;
            const newAuthorId = authorEntry ? parseInt(authorEntry.id, 10) : null;
            const newArtistId = artistEntry ? parseInt(artistEntry.id, 10) : null;

            // Determine the cover image URL to use
            // Priority: item.coverImage > first image from item.images > fallback
            let newCoverImage = "";
            if (item.coverImage) {
              newCoverImage = item.coverImage;
            } else if (item.images && item.images.length > 0) {
              // Use the first image from the images array as cover
              const firstImage = item.images[0];
              newCoverImage = typeof firstImage === "string" ? firstImage : firstImage.url;
            } else {
              newCoverImage = getCoverFallback(item.title);
            }

            // Smart update: only if data actually changed
            const hasChanges =
              existing.title !== item.title ||
              existing.slug !== item.slug ||
              existing.description !== cleanDescription ||
              existing.coverImage !== newCoverImage ||
              existing.status !== item.status ||
              String(existing.publicationDate) !== String(newPublicationDate) ||
              existing.url !== (item.url || null) ||
              existing.rating !== String(item.rating ?? 0) ||
              existing.typeId !== newTypeId ||
              existing.authorId !== newAuthorId ||
              existing.artistId !== newArtistId ||
              existing.views !== (item.views ?? 0);

            if (hasChanges) {
              await db
                .update(comic)
                .set({
                  title: item.title,
                  slug: item.slug,
                  description: cleanDescription,
                  coverImage: newCoverImage,
                  status: item.status,
                  publicationDate: newPublicationDate,
                  url: item.url || null,
                  rating: String(item.rating ?? 0),
                  typeId: typeId ?? undefined,
                  authorId: authorEntry ? parseInt(authorEntry.id, 10) : undefined,
                  artistId: artistEntry ? parseInt(artistEntry.id, 10) : undefined,
                  views: item.views ?? 0,
                  updatedAt: new Date(),
                })
                .where(eq(comic.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        // Resolve relations from cache
        const typeId = item.type?.name ? this.cache.types.get(item.type.name) : undefined;
        const authorEntry = item.author?.name ? this.cache.authors.get(item.author.name) : undefined;
        const artistEntry = item.artist?.name ? this.cache.artists.get(item.artist.name) : undefined;

        // Handle cover image (download locally or use branded fallback)
        let coverImageUrl = "";
        if (item.coverImage) {
          if (this.options.imageStrategy === "local") {
            // We'll download after insert to get the ID
            coverImageUrl = item.coverImage;
          } else {
            coverImageUrl = item.coverImage;
          }
        } else {
          coverImageUrl = getCoverFallback(item.title);
        }

        // Create comic record (without coverImage for now if local strategy)
        const comicResult = await db
          .insert(comic)
          .values({
            title: item.title,
            slug: item.slug,
            description: item.description ? stripHtmlTags(item.description) : "",
            coverImage: this.options.imageStrategy === "local" ? "" : coverImageUrl,
            status: item.status,
            publicationDate:
              item.updatedAt instanceof Date && !isNaN(item.updatedAt.getTime()) ? item.updatedAt : new Date(),
            url: item.url || null,
            rating: String(item.rating ?? 0),
            typeId: typeId ?? undefined,
            authorId: authorEntry ? parseInt(authorEntry.id, 10) : undefined,
            artistId: artistEntry ? parseInt(artistEntry.id, 10) : undefined,
            views: item.views ?? 0,
            updatedAt: item.updatedAt instanceof Date && !isNaN(item.updatedAt.getTime()) ? item.updatedAt : new Date(),
          })
          .returning();

        if (comicResult.length === 0) {
          throw new Error("Failed to insert comic");
        }

        const comicId = comicResult[0].id;
        this.cache.comics.set(item.slug, comicId);
        // Cache all slug aliases for chapter matching
        const aliases = this.slugAliases.get(item.title);
        if (aliases) {
          for (const alias of aliases) {
            this.cache.comics.set(alias, comicId);
          }
        }

        // Download cover image if using local strategy
        if (this.options.imageStrategy === "local" && item.coverImage) {
          const downloadedCover = await this.downloadCoverImage(item.coverImage, comicId, item.slug, item.title);
          await db.update(comic).set({ coverImage: downloadedCover }).where(eq(comic.id, comicId));
        }

        // Add genre relations
        if (item.genres && item.genres.length > 0) {
          const genreIds = item.genres
            .map((g) => this.cache.genres.get(g.name))
            .filter((id): id is number => id !== undefined);

          if (genreIds.length > 0) {
            await db.insert(comicToGenre).values(
              genreIds.map((genreId) => ({
                comicId,
                genreId,
              }))
            );
          }
        }

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({
          itemIndex: i,
          value: data[i],
          message,
        });
        logger.debug(`Error inserting comic: ${message}`);
      }
    }

    const duration = Date.now() - startTime;

    return {
      entityName: this.entityName,
      inserted,
      updated,
      skipped,
      errors,
      duration,
      success: errors.length === 0,
    };
  }
}
