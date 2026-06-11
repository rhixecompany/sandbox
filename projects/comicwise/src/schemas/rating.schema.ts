/**
 * Rating Validation Schemas
 * Zod schemas for rating CRUD operations
 */

import { z } from "zod";

export const ratingSchema = z.object({
  comicId: z.number().int().positive("Comic ID must be positive"),
  rating: z.number().int().min(1, "Rating must be between 1 and 5").max(5, "Rating must be between 1 and 5"),
  review: z.string().max(1000, "Review must be less than 1000 characters").optional().nullable(),
});

export type RatingInput = z.infer<typeof ratingSchema>;

export const ratingResponseSchema = z.object({
  id: z.number(),
  comicId: z.number(),
  userId: z.string(),
  rating: z.number(),
  review: z.string().nullable(),
  createdAt: z.date(),
  updatedAt: z.date(),
  user: z.object({
    id: z.string(),
    name: z.string().nullable(),
    image: z.string().nullable(),
  }),
});

export type RatingResponse = z.infer<typeof ratingResponseSchema>;

export const ratingStatsSchema = z.object({
  totalCount: z.number(),
  averageScore: z.number(),
  distribution: z.object({
    5: z.number(),
    4: z.number(),
    3: z.number(),
    2: z.number(),
    1: z.number(),
  }),
});

export type RatingStats = z.infer<typeof ratingStatsSchema>;
