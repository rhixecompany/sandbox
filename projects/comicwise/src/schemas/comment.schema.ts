/**
 * Comment Validation Schemas
 * Zod schemas for comment CRUD operations
 */

import { z } from "zod";

export const createCommentSchema = z.object({
  chapterId: z.number().int().positive("Chapter ID must be positive"),
  content: z
    .string()
    .min(1, "Comment cannot be empty")
    .max(2000, "Comment must be less than 2000 characters")
    .refine((val) => val.trim().length > 0, "Comment cannot be only whitespace"),
  parentId: z.number().int().optional().nullable(),
});

export type CreateCommentInput = z.infer<typeof createCommentSchema>;

export const updateCommentSchema = z.object({
  content: z
    .string()
    .min(1, "Comment cannot be empty")
    .max(2000, "Comment must be less than 2000 characters")
    .refine((val) => val.trim().length > 0, "Comment cannot be only whitespace"),
});

export type UpdateCommentInput = z.infer<typeof updateCommentSchema>;

export const commentResponseSchema = z.object({
  id: z.number(),
  chapterId: z.number(),
  userId: z.string(),
  content: z.string(),
  parentId: z.number().nullable(),
  createdAt: z.date(),
  updatedAt: z.date(),
  deletedAt: z.date().nullable(),
  user: z.object({
    id: z.string(),
    name: z.string().nullable(),
    image: z.string().nullable(),
  }),
  replies: z.array(z.any()).optional(),
});

export type CommentResponse = z.infer<typeof commentResponseSchema>;
