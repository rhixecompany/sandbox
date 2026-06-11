/**
 * CommentList Component
 * Display threaded comments with replies
 */

"use client";

import { useState } from "react";

import { CommentCard } from "./comment-card";

import type { Comment } from "@/types/comment-rating";

interface CommentListProps {
  comments: Comment[];
  currentUserId?: string;
  replies?: Record<number, Comment[]>;
}

export function CommentList({ comments, currentUserId, replies = {} }: CommentListProps) {
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  if (comments.length === 0) {
    return (
      <div className="py-8 text-center text-muted-foreground">
        <p>No comments yet. Be the first to share your thoughts!</p>
      </div>
    );
  }

  const handleCommentUpdated = () => {
    setRefreshTrigger((prev) => prev + 1);
  };

  return (
    <div className="space-y-0 divide-y divide-border" key={refreshTrigger}>
      {comments.map((comment) => (
        <div key={comment.id}>
          {/* Parent Comment */}
          <CommentCard
            comment={comment}
            currentUserId={currentUserId}
            level={0}
            onDeleteSuccess={handleCommentUpdated}
            onReplySuccess={handleCommentUpdated}
          />

          {/* Replies */}
          {replies[comment.id] && replies[comment.id].length > 0 && (
            <div>
              {replies[comment.id].map((reply) => (
                <CommentCard
                  comment={reply}
                  currentUserId={currentUserId}
                  key={reply.id}
                  level={1}
                  onDeleteSuccess={handleCommentUpdated}
                  onReplySuccess={handleCommentUpdated}
                />
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
