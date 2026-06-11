/**
 * Comment and Rating Server Actions
 * Protected server actions for comment and rating mutations
 */

"use server";

import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { commentDal, ratingDal } from "@/dal/comment-rating-dal";

import type { ActionResult } from "@/types/actions-types";
import type { Comment, CreateCommentInput, CreateRatingInput, Rating } from "@/types/comment-rating";

/**
 * Create a new comment
 */
export async function createCommentAction(input: unknown): Promise<ActionResult<Comment>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in to comment" };
  }

  try {
    const commentInput = input as CreateCommentInput;

    if (!commentInput.content || commentInput.content.trim().length === 0) {
      return { ok: false, error: "Comment cannot be empty" };
    }

    if (commentInput.content.length > 5000) {
      return { ok: false, error: "Comment is too long (max 5000 characters)" };
    }

    if (!commentInput.chapterId) {
      return { ok: false, error: "Invalid chapter ID" };
    }

    const newComment = await commentDal.create({
      ...commentInput,
      userId: session.user.id,
    });

    revalidatePath(`/chapter/${commentInput.chapterId}`);
    return { ok: true, data: newComment };
  } catch (error) {
    console.error("[createCommentAction]", error);
    return { ok: false, error: "Failed to create comment" };
  }
}

/**
 * Update an existing comment
 */
export async function updateCommentAction(commentId: number | string, input: unknown): Promise<ActionResult<Comment>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  try {
    const updateData = input as { content: string };

    if (!updateData.content || updateData.content.trim().length === 0) {
      return { ok: false, error: "Comment cannot be empty" };
    }

    if (updateData.content.length > 5000) {
      return { ok: false, error: "Comment is too long (max 5000 characters)" };
    }

    // Fetch the comment to verify ownership
    const existingComment = await commentDal.getById(commentId);
    if (!existingComment) {
      return { ok: false, error: "Comment not found" };
    }

    if (existingComment.userId !== session.user.id) {
      return { ok: false, error: "You can only edit your own comments" };
    }

    const updated = await commentDal.update(commentId, updateData);
    if (!updated) {
      return { ok: false, error: "Failed to update comment" };
    }

    revalidatePath(`/chapter/${existingComment.chapterId}`);
    return { ok: true, data: updated };
  } catch (error) {
    console.error("[updateCommentAction]", error);
    return { ok: false, error: "Failed to update comment" };
  }
}

/**
 * Delete a comment
 */
export async function deleteCommentAction(commentId: number | string): Promise<ActionResult<null>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  try {
    const existingComment = await commentDal.getById(commentId);
    if (!existingComment) {
      return { ok: false, error: "Comment not found" };
    }

    if (existingComment.userId !== session.user.id) {
      return { ok: false, error: "You can only delete your own comments" };
    }

    await commentDal.delete(commentId);
    revalidatePath(`/chapter/${existingComment.chapterId}`);
    return { ok: true, data: null };
  } catch (error) {
    console.error("[deleteCommentAction]", error);
    return { ok: false, error: "Failed to delete comment" };
  }
}

/**
 * Reply to a comment
 */
export async function replyToCommentAction(parentId: number | string, input: unknown): Promise<ActionResult<Comment>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in to reply" };
  }

  try {
    const replyInput = input as CreateCommentInput;

    if (!replyInput.content || replyInput.content.trim().length === 0) {
      return { ok: false, error: "Reply cannot be empty" };
    }

    if (replyInput.content.length > 5000) {
      return { ok: false, error: "Reply is too long (max 5000 characters)" };
    }

    // Verify parent comment exists
    const parentComment = await commentDal.getById(parentId);
    if (!parentComment) {
      return { ok: false, error: "Parent comment not found" };
    }

    const reply = await commentDal.create({
      content: replyInput.content,
      chapterId: parentComment.chapterId,
      parentId: Number(parentId),
      userId: session.user.id,
    });

    revalidatePath(`/chapter/${parentComment.chapterId}`);
    return { ok: true, data: reply };
  } catch (error) {
    console.error("[replyToCommentAction]", error);
    return { ok: false, error: "Failed to reply to comment" };
  }
}

/**
 * Create or update a rating
 */
export async function upsertRatingAction(input: unknown): Promise<ActionResult<Rating>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in to rate" };
  }

  try {
    const ratingInput = input as CreateRatingInput;

    if (!ratingInput.comicId) {
      return { ok: false, error: "Invalid comic ID" };
    }

    if (!ratingInput.rating || ratingInput.rating < 1 || ratingInput.rating > 5) {
      return { ok: false, error: "Rating must be between 1 and 5" };
    }

    if (ratingInput.review && ratingInput.review.length > 1000) {
      return { ok: false, error: "Review is too long (max 1000 characters)" };
    }

    const newRating = await ratingDal.upsertRating(session.user.id, ratingInput);
    revalidatePath(`/comic/${ratingInput.comicId}`);
    return { ok: true, data: newRating };
  } catch (error) {
    console.error("[upsertRatingAction]", error);
    return { ok: false, error: "Failed to save rating" };
  }
}

/**
 * Delete a rating
 */
export async function deleteRatingAction(ratingId: number | string): Promise<ActionResult<null>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  try {
    const existingRating = await ratingDal.getById(ratingId);
    if (!existingRating) {
      return { ok: false, error: "Rating not found" };
    }

    if (existingRating.userId !== session.user.id) {
      return { ok: false, error: "You can only delete your own ratings" };
    }

    await ratingDal.delete(ratingId);
    revalidatePath(`/comic/${existingRating.comicId}`);
    return { ok: true, data: null };
  } catch (error) {
    console.error("[deleteRatingAction]", error);
    return { ok: false, error: "Failed to delete rating" };
  }
}

/**
 * Get average rating for a comic
 */
export async function getComicAverageRatingAction(
  comicId: number
): Promise<{ data: number; ok: true } | { error: string; ok: false }> {
  try {
    const average = await ratingDal.getAverageRating(comicId);
    return { ok: true, data: average };
  } catch (error) {
    console.error("[getComicAverageRatingAction]", error);
    return { ok: false, error: "Failed to fetch average rating" };
  }
}

/**
 * Get all comments for a chapter with nested replies
 */
export async function getChapterCommentsAction(chapterId: number) {
  try {
    const comments = await commentDal.getChapterComments(chapterId);
    return { ok: true, data: comments };
  } catch (error) {
    console.error("[getChapterCommentsAction]", error);
    return { ok: false, error: "Failed to fetch comments" };
  }
}

/**
 * Get user's comments
 */
export async function getUserCommentsAction() {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const comments = await commentDal.getUserComments(session.user.id);
    return { ok: true, data: comments };
  } catch (error) {
    console.error("[getUserCommentsAction]", error);
    return { ok: false, error: "Failed to fetch user comments" };
  }
}

/**
 * Get comic rating statistics
 */
export async function getComicRatingStatsAction(comicId: number) {
  try {
    const stats = await ratingDal.getComicRatingStats(comicId);
    return { ok: true, data: stats };
  } catch (error) {
    console.error("[getComicRatingStatsAction]", error);
    return { ok: false, error: "Failed to fetch rating stats" };
  }
}

/**
 * Get comic ratings with pagination
 */
export async function getComicRatingsAction(comicId: number, page = 1, pageSize = 20) {
  try {
    const ratings = await ratingDal.getComicRatings(comicId, pageSize, (page - 1) * pageSize);
    return { ok: true, data: ratings };
  } catch (error) {
    console.error("[getComicRatingsAction]", error);
    return { ok: false, error: "Failed to fetch ratings" };
  }
}

/**
 * Get user's ratings for all comics
 */
export async function getUserRatingsAction() {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const ratings = await ratingDal.getUserRatings(session.user.id);
    return { ok: true, data: ratings };
  } catch (error) {
    console.error("[getUserRatingsAction]", error);
    return { ok: false, error: "Failed to fetch user ratings" };
  }
}

/**
 * Get user's rating for a specific comic
 */
export async function getUserComicRatingAction(comicId: number) {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: true as const, data: null };
    }

    const rating = await ratingDal.getUserComicRating(session.user.id, comicId);
    return { ok: true, data: rating };
  } catch (error) {
    console.error("[getUserComicRatingAction]", error);
    return { ok: false, error: "Failed to fetch user rating" };
  }
}

/**
 * Get top-rated comics
 */
export async function getTopRatedComicsAction(limit = 10) {
  try {
    const comics = await ratingDal.getTopRatedComics(limit);
    return { ok: true, data: comics };
  } catch (error) {
    console.error("[getTopRatedComicsAction]", error);
    return { ok: false, error: "Failed to fetch top-rated comics" };
  }
}
