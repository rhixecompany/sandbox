/**
 * Chapter Comments Section
 * Server component that loads and displays comments for a chapter
 */

import { Suspense } from "react";

import { auth } from "@/auth";
import { CommentForm, CommentList } from "@/components/comments";
import { commentDal } from "@/dal/comment-rating-dal";

import type { Comment } from "@/types/comment-rating";

interface ChapterCommentsSectionProps {
  chapterId: number;
}

async function ChapterCommentsContent({ chapterId }: ChapterCommentsSectionProps) {
  const session = await auth();
  const comments = await commentDal.getCommentsByChapterId(chapterId, null, 50, 0);

  // Load replies for each comment
  const repliesMap: Record<number, Comment[]> = {};
  for (const comment of comments) {
    const replies = await commentDal.getReplies(comment.id);
    if (replies.length > 0) {
      repliesMap[comment.id] = replies;
    }
  }

  return (
    <div className="space-y-6">
      {/* Comment Form */}
      {session?.user && (
        <div className="rounded-lg border bg-card p-4">
          <h3 className="mb-3 font-semibold">Share your thoughts</h3>
          <CommentForm chapterId={chapterId} />
        </div>
      )}

      {!session?.user && (
        <div className="rounded-lg bg-muted p-4 text-center text-sm text-muted-foreground">
          <p>Sign in to comment on this chapter</p>
        </div>
      )}

      {/* Comments List */}
      <div>
        <h3 className="mb-3 font-semibold">
          {comments.length} {comments.length === 1 ? "Comment" : "Comments"}
        </h3>
        <CommentList comments={comments} currentUserId={session?.user?.id} replies={repliesMap} />
      </div>
    </div>
  );
}

export function ChapterCommentsSection({ chapterId }: ChapterCommentsSectionProps) {
  return (
    <Suspense fallback={<div className="py-8 text-center text-muted-foreground">Loading comments...</div>}>
      <ChapterCommentsContent chapterId={chapterId} />
    </Suspense>
  );
}
