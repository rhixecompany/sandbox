/**
 * Comment Types - Shared across components, pages, and wrappers
 */

export interface CommentData {
  chapter: {
    chapterNumber: number | string;
    comic?: {
      slug: string;
      title: string;
    };
  };
  content: string;
  createdAt: Date | string;
  deletedAt?: Date | null | string;
  id: number | string;
  updatedAt?: Date | string;
}

export interface CommentWithReplies extends CommentData {
  replies?: CommentData[];
  user?: {
    id: string;
    image?: string;
    name: string;
  };
}

export interface CreateCommentData {
  chapterId: number;
  content: string;
  parentId?: number;
}

export interface UpdateCommentData {
  content: string;
}

export interface CommentRatingData {
  comic?: {
    coverImage: null | string;
    id: number;
    slug: string;
    title: string;
  };
  createdAt: Date | string;
  id: number;
  rating: number;
  review?: null | string;
  updatedAt?: Date | string;
}

export interface RatingWithComic {
  comic: {
    coverImage: null | string;
    slug: string;
    title: string;
  } | null;
  createdAt: Date | string;
  id: number;
  rating: number;
  review: null | string;
}

export interface CreateRatingData {
  comicId: number;
  rating: number;
  review?: string;
}

export interface UpdateRatingData {
  rating?: number;
  review?: string;
}
