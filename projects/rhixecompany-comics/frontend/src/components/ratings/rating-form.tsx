/**
 * RatingForm Component
 * Form for rating a comic with optional review
 */

"use client";

import { Star } from "lucide-react";
import { useState, useTransition } from "react";

import { deleteRatingAction, upsertRatingAction } from "@/actions/comment-rating.actions";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

import type { Rating } from "@/types/comment-rating";

interface RatingFormProps {
  comicId: number;
  existingRating?: Rating;
  onSuccess?: (rating: null | Rating) => void;
}

export function RatingForm({ comicId, existingRating, onSuccess }: RatingFormProps) {
  const [rating, setRating] = useState(existingRating?.rating || 0);
  const [review, setReview] = useState(existingRating?.review || "");
  const [error, setError] = useState<null | string>(null);
  const [isPending, startTransition] = useTransition();

  const maxReviewCharacters = 1000;
  const hasRating = rating > 0;

  const handleRatingSubmit = async () => {
    setError(null);

    if (!hasRating) {
      setError("Please select a rating");
      return;
    }

    if (review.length > maxReviewCharacters) {
      setError(`Review must be less than ${maxReviewCharacters} characters`);
      return;
    }

    startTransition(async () => {
      try {
        const result = await upsertRatingAction({
          comicId,
          rating,
          review: review.trim() || undefined,
        });

        if (result.ok) {
          onSuccess?.(result.data);
        } else {
          setError(result.error);
        }
      } catch {
        setError("An error occurred while saving your rating");
      }
    });
  };

  const handleDelete = async () => {
    if (!existingRating) return;
    if (!confirm("Remove your rating?")) return;

    setError(null);
    startTransition(async () => {
      try {
        const result = await deleteRatingAction(existingRating.id);
        if (result.ok) {
          setRating(0);
          setReview("");
          onSuccess?.(null);
        } else {
          setError(result.error);
        }
      } catch {
        setError("An error occurred while deleting your rating");
      }
    });
  };

  return (
    <div className="space-y-4 rounded-lg border bg-card p-4">
      <div>
        <h3 className="mb-3 font-semibold">Rate this comic</h3>

        {/* Star Rating */}
        <div className="mb-4 flex gap-1">
          {[1, 2, 3, 4, 5].map((value) => (
            <button
              className="p-1 transition-colors"
              disabled={isPending}
              key={value}
              onClick={() => {
                setRating(value);
                setError(null);
              }}
              type="button"
            >
              <Star
                className={`${value <= rating ? "fill-yellow-400 text-yellow-400" : "text-muted-foreground"}`}
                size={24}
              />
            </button>
          ))}
        </div>

        {/* Rating Label */}
        {hasRating && <p className="mb-3 text-xs text-muted-foreground">{rating} out of 5 stars</p>}

        {/* Review Text */}
        <div className="relative">
          <Textarea
            className="min-h-20 resize-none"
            disabled={isPending}
            maxLength={maxReviewCharacters}
            onChange={(e) => {
              setReview(e.target.value);
              setError(null);
            }}
            placeholder="Share your thoughts about this comic (optional)"
            value={review}
          />
          <div className="absolute right-2 bottom-2 text-xs text-muted-foreground">
            {review.length}/{maxReviewCharacters}
          </div>
        </div>
      </div>

      {/* Error Message */}
      {error && <div className="rounded bg-destructive/10 p-2 text-sm text-destructive">{error}</div>}

      {/* Action Buttons */}
      <div className="flex justify-between gap-2">
        <div>
          {existingRating && (
            <Button disabled={isPending} onClick={() => void handleDelete()} size="sm" variant="destructive">
              Remove Rating
            </Button>
          )}
        </div>
        <Button className="min-w-[100px]" disabled={isPending || !hasRating} onClick={() => void handleRatingSubmit()}>
          {isPending ? "Saving..." : "Save Rating"}
        </Button>
      </div>
    </div>
  );
}
