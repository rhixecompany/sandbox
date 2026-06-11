"use client";

/**
 * Comic Ratings Section
 * Client component that displays ratings data passed as props
 */

import type { Rating } from "@/types/comment-rating";

import { ComicRatingsDisplay } from "./comic-ratings-display";

interface ComicRatingsSectionProps {
  allRatings: Rating[];
  averageRating: number;
  comicId: number;
  isAuthenticated: boolean;
  userRating: null | Rating;
}

export function ComicRatingsSection({
  comicId,
  averageRating,
  allRatings,
  userRating,
  isAuthenticated,
}: ComicRatingsSectionProps) {
  return (
    <ComicRatingsDisplay
      allRatings={allRatings}
      averageRating={averageRating}
      comicId={comicId}
      isAuthenticated={isAuthenticated}
      userRating={userRating}
    />
  );
}
