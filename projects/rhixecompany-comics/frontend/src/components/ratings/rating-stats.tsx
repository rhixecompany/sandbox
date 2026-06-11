/**
 * RatingStats Component
 * Display aggregate rating statistics for a comic
 */

"use client";

import { Star } from "lucide-react";

interface RatingStatsProps {
  averageRating: number;
  totalRatings: number;
}

export function RatingStats({ averageRating, totalRatings }: RatingStatsProps) {
  const displayRating = averageRating.toFixed(1);
  const fullStars = Math.floor(averageRating);
  const hasHalfStar = averageRating % 1 >= 0.5;

  return (
    <div className="flex items-center gap-3 rounded-lg border border-border bg-card p-3 dark:border-border dark:bg-card">
      {/* Large Star Display */}
      <div className="flex flex-col items-center gap-1">
        <div className="flex gap-0.5">
          {[1, 2, 3, 4, 5].map((i) => {
            const isFull = i <= fullStars;
            const isHalf = i === fullStars + 1 && hasHalfStar;

            return (
              <div className="relative h-4 w-4" key={i}>
                <Star className="text-muted-foreground" size={16} />
                {(isFull || isHalf) && (
                  <div
                    className="absolute top-0 left-0 h-full overflow-hidden text-yellow-400 dark:text-yellow-300"
                    style={{ width: isHalf ? "50%" : "100%" }}
                  >
                    <Star className="fill-yellow-400 dark:fill-yellow-300" size={16} />
                  </div>
                )}
              </div>
            );
          })}
        </div>
        <span className="text-xs text-muted-foreground">
          {totalRatings} {totalRatings === 1 ? "rating" : "ratings"}
        </span>
      </div>

      {/* Rating Value */}
      <div>
        <p className="text-2xl font-bold">{displayRating}</p>
        <p className="text-xs text-muted-foreground">out of 5</p>
      </div>

      {/* Rating Distribution */}
      <div className="ml-4 hidden flex-col gap-1 sm:flex">
        {[5, 4, 3, 2, 1].map((stars) => (
          <div className="flex items-center gap-2 text-xs" key={stars}>
            <span className="w-12 text-right">{stars}★</span>
            <div className="h-2 w-20 rounded-full bg-muted" />
          </div>
        ))}
      </div>
    </div>
  );
}
