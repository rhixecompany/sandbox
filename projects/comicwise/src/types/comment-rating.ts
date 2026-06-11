/**
 * Comment and Rating Types
 * Defines types for user comments and ratings
 */

export interface Comment {
  chapterId: number;
  content: string;
  createdAt: Date;
  deletedAt: Date | null;
  id: number;
  parentId: null | number;
  replies?: Comment[];
  updatedAt: Date;
  // Relations (optional)
  user?: {
    email: string;
    id: string;
    image: null | string;
    name: null | string;
  };
  userId: string;
}

export interface Rating {
  comicId: number;
  createdAt: Date;
  id: number;
  rating: number; // 1-5 stars
  review: null | string;
  updatedAt: Date;
  userId: string;
}

export interface CommentWithUser extends Comment {
  replyCount: number;
  user: {
    email: string;
    id: string;
    image: null | string;
    name: null | string;
  };
}

export interface CreateCommentInput {
  chapterId: number;
  content: string;
  parentId?: null | number;
}

export interface UpdateCommentInput {
  content: string;
}

export interface CreateRatingInput {
  comicId: number;
  rating: number; // 1-5
  review?: string;
}
