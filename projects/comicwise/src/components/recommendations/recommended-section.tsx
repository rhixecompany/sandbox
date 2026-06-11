"use client";

import Image from "next/image";
import { Suspense } from "react";

import { auth } from "@/auth";
import { BookmarkButton } from "@/components/comics/bookmark-button";
import { recommendationDal } from "@/dal/recommendation-dal";
interface Comic {
  coverImage: string;
  genres: Array<{ genre: { id: number; name: string }; genreId: number }>;
  id: number;
  rating: null | number | string;
  slug: string;
  title: string;
}

/**
 * Server Component (wrapped for Suspense)
 * Fetch and display recommended comics for the current user
 * Falls back to trending if no personalized recommendations
 */
async function RecommendedSectionContent() {
  let recommendations: Comic[];

  try {
    // Get session on server side
    const session = await auth();
    if (!session?.user?.id) {
      return null; // Not logged in - don't show recommendations
    }

    // Fetch recommendations for this user
    recommendations = (await recommendationDal.getForUser(session.user.id, 6)) as Comic[];

    // Fallback to trending if no personalized recommendations
    if (recommendations.length === 0) {
      recommendations = (await recommendationDal.getTrending(6)) as Comic[];
    }
  } catch (error) {
    console.error("[RecommendedSection] Failed to fetch recommendations:", error);
    // Silent fail - don't break page rendering
    return null;
  }

  if (recommendations.length === 0) {
    return (
      <div className="py-8 text-center">
        <p className="text-muted-foreground">No recommendations available yet</p>
      </div>
    );
  }

  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold">Recommended for You</h2>
      <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
        {recommendations.map((comic) => (
          <RecommendedComicCard comic={comic} key={comic.id} />
        ))}
      </div>
    </section>
  );
}

/**
 * Individual comic card for recommendations
 */
interface RecommendedComicCardProps {
  comic: Comic;
}

function RecommendedComicCard({ comic }: RecommendedComicCardProps) {
  return (
    <div className="group space-y-2">
      {/* Cover Image */}
      <div className="relative aspect-2/3 overflow-hidden rounded-lg bg-muted">
        {comic.coverImage ? (
          <Image
            alt={comic.title}
            className="h-full w-full object-cover transition-transform group-hover:scale-105"
            fill
            src={comic.coverImage}
          />
        ) : (
          <div className="flex h-full w-full items-center justify-center">
            <span className="px-2 text-center text-xs text-muted-foreground">{comic.title}</span>
          </div>
        )}

        {/* Bookmark Button - Overlay on hover */}
        <div className="absolute inset-0 flex items-end justify-center gap-2 bg-black/40 p-2 opacity-0 transition-opacity group-hover:opacity-100">
          <BookmarkButton comicId={comic.id} size="sm" />
        </div>
      </div>

      {/* Title */}
      <div className="space-y-1">
        <h3 className="line-clamp-2 text-sm font-semibold hover:underline">
          <a href={`/comics/${comic.slug}`}>{comic.title}</a>
        </h3>

        {/* Rating */}
        {comic.rating && Number(comic.rating) > 0 && (
          <div className="flex items-center gap-1">
            <div className="flex">
              {[1, 2, 3, 4, 5].map((star) => (
                <span
                  className={`text-xs ${
                    star <= Math.round(Number(comic.rating ?? 0)) ? "text-yellow-400" : "text-muted-foreground"
                  }`}
                  key={star}
                >
                  ★
                </span>
              ))}
            </div>
            <span className="text-xs text-muted-foreground">{(comic.rating as number).toFixed(1)}</span>
          </div>
        )}
      </div>
    </div>
  );
}

/**
 * Public component - Shows recommended comics section with Suspense boundary
 * Safe to use on any page (handles auth check internally)
 */
export function RecommendedSection() {
  return (
    <Suspense fallback={<RecommendedSectionLoadingSkeleton />}>
      <RecommendedSectionContent />
    </Suspense>
  );
}

/**
 * Loading skeleton for recommended section
 */
function RecommendedSectionLoadingSkeleton() {
  return (
    <section className="animate-pulse space-y-4">
      <div className="h-8 w-48 rounded bg-muted" />
      <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
        {Array.from({ length: 6 }).map((_, i) => (
          <div className="space-y-2" key={i}>
            <div className="aspect-2/3 rounded-lg bg-muted" />
            <div className="h-4 w-full rounded bg-muted" />
            <div className="h-3 w-20 rounded bg-muted" />
          </div>
        ))}
      </div>
    </section>
  );
}
