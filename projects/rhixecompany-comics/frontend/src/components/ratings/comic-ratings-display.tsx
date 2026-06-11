"use client";

/**
 * Comic Ratings Display
 * Client component that displays ratings without fetching data
 */

import type { Rating } from "@/types/comment-rating";

import { RatingForm, RatingStats } from "@/components/ratings";

interface ComicRatingsDisplayProps {
  allRatings: Rating[];
  averageRating: number;
  comicId: number;
  isAuthenticated: boolean;
  userRating: null | Rating;
}

export function ComicRatingsDisplay({
  comicId,
  averageRating,
  allRatings,
  userRating,
  isAuthenticated,
}: ComicRatingsDisplayProps) {
  return (
    <div className="space-y-6">
      {/* Rating Stats */}
      {allRatings.length > 0 && <RatingStats averageRating={averageRating} totalRatings={allRatings.length} />}

      {/* Rating Form */}
      {isAuthenticated ? (
        <RatingForm comicId={comicId} existingRating={userRating ?? undefined} />
      ) : (
        <div className="rounded-lg bg-muted p-4 text-center text-sm text-muted-foreground">
          <p>Sign in to rate this comic</p>
        </div>
      )}

      {/* Top Ratings Preview */}
      {allRatings.length > 0 && (
        <div className="border-t pt-4">
          <h3 className="mb-3 font-semibold">Top Ratings</h3>
          <div className="max-h-96 space-y-3 overflow-y-auto">
            {allRatings
              .sort((a, b) => {
                if (a.review && !b.review) return -1;
                if (!a.review && b.review) return 1;
                return new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime();
              })
              .slice(0, 5)
              .map((rating) => (
                <div className="rounded-lg bg-muted/30 p-3 text-sm" key={rating.id}>
                  <div className="mb-2 flex items-center justify-between">
                    <div className="flex gap-1">
                      {([0, 1, 2, 3, 4] as const).map((i) => (
                        <span
                          className={i < rating.rating ? "text-lg text-yellow-400" : "text-muted-foreground text-lg"}
                          key={i}
                        >
                          ★
                        </span>
                      ))}
                    </div>
                    <span className="text-xs text-muted-foreground">
                      {new Date(rating.createdAt).toLocaleDateString()}
                    </span>
                  </div>
                  {rating.review && <p className="text-xs text-foreground">{rating.review}</p>}
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
}
