"use client";

import { Suspense } from "react";

import { Star } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

import { ComicCard } from "@/components/comics";
import { BookmarkButton } from "@/components/comics/bookmark-button";
import { ShareButton } from "@/components/comics/share-button";
import { ComicRatingsSection } from "@/components/ratings/comic-ratings-section";
import { RatingButton } from "@/components/ratings/rating-button";
import { Button } from "@/components/ui/button";
import type { Rating } from "@/types/comment-rating";

// Type for the comic data structure from getComicBySlugAction
interface ComicData {
  artist?: { name: string } | null;
  author?: { name: string } | null;
  chapters?: Array<{
    chapterNumber: number;
    createdAt: Date | string;
    id: number;
    title: null | string;
  }>;
  comicToGenre?: Array<{ genre?: { id: number; name: string } }>;
  coverImage: null | string;
  description: null | string;
  id: number;
  rating: { average: number } | null;
  slug: string;
  status: string;
  title: string;
  type?: { name: string } | null;
}

// Type for related comic data
interface RelatedComicData {
  coverImage?: null | string;
  description?: string;
  id: number;
  rating?: null | number | string;
  slug: string;
  status?: string;
  title: string;
  type?: { name: string } | null;
}

// Type for ratings data
interface RatingsData {
  allRatings: Rating[];
  averageRating: number;
  userRating: null | Rating;
}

interface ComicDetailWrapperProps {
  bookmarkStatus: "Completed" | "Dropped" | "On Hold" | "Plan to Read" | "Reading" | null;
  comic: ComicData | null;
  ratingsData: RatingsData;
  relatedComics: RelatedComicData[];
  sessionUserId?: string;
}

function ComicDetailsContent({
  comic,
  relatedComics,
  bookmarkStatus,
  sessionUserId,
  ratingsData,
}: ComicDetailWrapperProps) {
  if (!comic) {
    return (
      <div className="min-h-screen bg-background">
        <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
          <div className="py-12 text-center">
            <h3 className="mb-2 text-xl font-semibold">Comic not found</h3>
            <p className="text-muted-foreground">The comic you are looking for does not exist.</p>
          </div>
        </div>
      </div>
    );
  }

  const comicId = comic.id;

  // Extract genre info from eager-loaded data
  const genres = ((comic.comicToGenre as Array<{ genre?: { id: number; name: string } }>) ?? [])
    .map((g) => g.genre)
    .filter((genre): genre is { id: number; name: string } => !!genre);

  // Extract chapters from eager-loaded data
  const chapters =
    (comic.chapters as Array<{
      chapterNumber: number;
      createdAt: Date | string;
      id: number;
      title?: null | string;
    }>) ?? [];

  // First chapter for "Start Reading" link
  const firstChapter = chapters.length > 0 ? chapters[chapters.length - 1] : null;

  return (
    <main className="min-h-screen bg-background">
      {/* Header/Hero Section */}
      <div className="relative bg-linear-to-r from-muted to-muted-foreground/20 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-4">
            {/* Cover Image */}
            <div className="md:col-span-1">
              <div className="relative aspect-2/3 w-full overflow-hidden rounded-lg shadow-lg">
                <Image alt={String(comic.title)} className="object-cover" fill src={String(comic.coverImage)} />
              </div>
            </div>

            {/* Comic Info */}
            <div className="md:col-span-3">
              <div className="space-y-4">
                <div>
                  <h1 className="mb-2 text-4xl font-bold">{String(comic.title)}</h1>
                  <p className="text-lg text-muted-foreground">{String(comic.description)}</p>
                </div>

                {/* Author/Artist */}
                <div className="space-y-2">
                  {comic.author && (
                    <p className="text-sm">
                      <span className="font-semibold">Author:</span> {(comic.author as { name: string }).name}
                    </p>
                  )}
                  {comic.artist && (
                    <p className="text-sm">
                      <span className="font-semibold">Artist:</span> {(comic.artist as { name: string }).name}
                    </p>
                  )}
                </div>

                {/* Rating and Stats */}
                <div className="flex flex-wrap items-center gap-4">
                  <div className="flex items-center gap-2">
                    <Star className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                    <span className="text-lg font-semibold">
                      {comic.rating
                        ? parseFloat(String((comic.rating as { average?: number })?.average ?? 0)).toFixed(1)
                        : "0.0"}
                    </span>
                    <span className="text-sm text-muted-foreground">/ 5</span>
                  </div>

                  <div className="rounded-lg bg-muted px-3 py-1 text-sm font-medium">{String(comic.status)}</div>

                  {Boolean(comic.type) && (
                    <div className="rounded-lg bg-muted px-3 py-1 text-sm font-medium">
                      {(comic.type as { name: string }).name}
                    </div>
                  )}
                </div>

                {/* Genres */}
                {genres.length > 0 && (
                  <div className="flex flex-wrap gap-2">
                    {genres.map((genre) => (
                      <Link
                        className="rounded bg-primary/10 px-3 py-1 text-xs text-primary transition hover:bg-primary/20"
                        href={`/comics?genreId=${genre.id}`}
                        key={genre.id}
                      >
                        {genre.name}
                      </Link>
                    ))}
                  </div>
                )}

                {/* Action Buttons */}
                <div className="flex flex-wrap gap-3 pt-4">
                  {firstChapter ? (
                    <Button asChild size="lg">
                      <Link href={`/comics/${String(comic.slug)}/chapter/${firstChapter.chapterNumber}`}>
                        Start Reading
                      </Link>
                    </Button>
                  ) : (
                    <Button disabled size="lg">
                      No Chapters Available
                    </Button>
                  )}

                  {sessionUserId && <BookmarkButton comicId={comicId} initialStatus={bookmarkStatus} />}

                  <ShareButton title={String(comic.title)} url={`/comics/${String(comic.slug)}`} />
                </div>

                {/* User Rating */}
                {sessionUserId && (
                  <div className="flex items-center gap-2 pt-2">
                    <span className="text-sm font-medium">Your Rating:</span>
                    <RatingButton comicId={comicId} />
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Content Sections */}
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        {/* Ratings Section */}
        <section className="mb-16">
          <h2 className="mb-6 text-2xl font-bold">Ratings & Reviews</h2>
          <ComicRatingsSection
            allRatings={ratingsData.allRatings}
            averageRating={ratingsData.averageRating}
            comicId={comicId}
            isAuthenticated={!!sessionUserId}
            userRating={ratingsData.userRating}
          />
        </section>

        {/* Chapters Section */}
        {chapters.length > 0 && (
          <section className="mb-16" data-testid="chapters-section">
            <h2 className="mb-6 text-2xl font-bold">Chapters ({chapters.length})</h2>
            <div className="max-h-96 space-y-2 overflow-y-auto rounded-lg border p-4">
              {chapters.map((ch) => (
                <Link
                  className="flex items-center justify-between rounded-lg p-3 transition hover:bg-muted"
                  data-testid="chapter-link"
                  href={`/comics/${String(comic.slug)}/chapter/${ch.chapterNumber}`}
                  key={ch.id}
                >
                  <span className="font-medium">Chapter {ch.chapterNumber}</span>
                  {ch.title && <span className="text-sm text-muted-foreground">{ch.title}</span>}
                  <span className="text-xs text-muted-foreground">{new Date(ch.createdAt).toLocaleDateString()}</span>
                </Link>
              ))}
            </div>
          </section>
        )}

        {/* Related Comics Section */}
        {relatedComics && relatedComics.length > 0 && (
          <section>
            <h2 className="mb-6 text-2xl font-bold">You might also like</h2>
            <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-6">
              {relatedComics.map((relComic) => (
                <div key={relComic.id}>
                  <ComicCard
                    comic={{
                      id: relComic.id,
                      slug: relComic.slug,
                      title: relComic.title,
                      coverImage: relComic.coverImage,
                      description: relComic.description,
                      rating: relComic.rating,
                      status: relComic.status,
                    }}
                    type={relComic.type}
                    variant="grid"
                  />
                </div>
              ))}
            </div>
          </section>
        )}
      </div>
    </main>
  );
}

export function ComicDetailWrapper(props: ComicDetailWrapperProps) {
  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-background">
          <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
            <div className="h-96 animate-pulse rounded-lg bg-muted" />
          </div>
        </div>
      }
    >
      <ComicDetailsContent {...props} />
    </Suspense>
  );
}
