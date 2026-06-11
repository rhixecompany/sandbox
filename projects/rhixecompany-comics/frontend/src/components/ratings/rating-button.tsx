"use client";

import { Star } from "lucide-react";
import { useState, useTransition } from "react";
import { toast } from "sonner";

import { upsertRatingAction } from "@/actions/comment-rating.actions";
import { Button } from "@/components/ui/button";

interface RatingButtonProps {
  comicId: number;
  onRatingChange?: (rating: number) => void;
  userRating?: number;
}

/**
 * Interactive rating button component
 * Allows users to quickly rate a comic with visual feedback
 */
export function RatingButton({ comicId, userRating = 0, onRatingChange }: RatingButtonProps) {
  const [hoverRating, setHoverRating] = useState(0);
  const [currentRating, setCurrentRating] = useState(userRating);
  const [isPending, startTransition] = useTransition();

  const handleRate = (rating: number) => {
    startTransition(async () => {
      const result = await upsertRatingAction({
        comicId,
        rating,
      });

      if (result.ok) {
        setCurrentRating(rating);
        onRatingChange?.(rating);
        toast.success(`Rated ${rating} out of 5 stars`);
      } else {
        toast.error(result.error);
      }
    });
  };

  return (
    <div aria-label="Rate this comic (1-5 stars)" className="flex gap-1" role="group">
      {[1, 2, 3, 4, 5].map((star) => (
        <Button
          aria-label={`Rate ${star} out of 5 stars`}
          aria-pressed={currentRating === star}
          className="h-auto w-auto p-0 hover:bg-transparent"
          disabled={isPending}
          key={star}
          onClick={() => handleRate(star)}
          onMouseEnter={() => setHoverRating(star)}
          onMouseLeave={() => setHoverRating(0)}
          size="sm"
          variant="ghost"
        >
          <Star
            className={`h-5 w-5 transition-colors ${
              star <= (hoverRating || currentRating)
                ? "fill-yellow-400 text-yellow-400 dark:fill-yellow-300 dark:text-yellow-300"
                : "text-muted-foreground dark:text-muted-foreground/60"
            }`}
          />
        </Button>
      ))}
    </div>
  );
}
