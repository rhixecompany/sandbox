/**
 * CommentCard Component
 * Display a single comment with user info and actions
 */

"use client";

import { formatDistanceToNow } from "date-fns";
import Image from "next/image";
import { useState } from "react";

import { deleteCommentAction } from "@/actions/comment-rating.actions";
import { Button } from "@/components/ui/button";

import { CommentForm } from "./comment-form";

import type { Comment } from "@/types/comment-rating";

interface CommentCardProps {
  comment: Comment;
  currentUserId?: string;
  level?: number;
  onDeleteSuccess?: () => void;
  onReplySuccess?: () => void;
}

export function CommentCard({ comment, currentUserId, level = 0, onReplySuccess, onDeleteSuccess }: CommentCardProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [isReplying, setIsReplying] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const isOwner = currentUserId === comment.userId;

  const handleDelete = async () => {
    if (!confirm("Are you sure you want to delete this comment?")) return;

    setIsDeleting(true);
    try {
      const result = await deleteCommentAction(comment.id);
      if (result.ok) {
        onDeleteSuccess?.();
      }
    } finally {
      setIsDeleting(false);
    }
  };

  const paddingLeft = level > 0 ? `${Math.min(level * 3, 12)}rem` : "0";
  const borderLeft = level > 0 ? "border-l-2 border-muted" : "";

  if (comment.deletedAt) {
    return (
      <div className={`py-3 ${borderLeft}`} style={{ paddingLeft }}>
        <p className="text-sm text-muted-foreground italic">This comment has been deleted.</p>
      </div>
    );
  }

  return (
    <div className={`space-y-3 py-3 ${borderLeft}`} style={{ paddingLeft }}>
      {/* Header */}
      <div className="flex items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          {comment.user?.image && (
            <Image
              alt={comment.user.name || "User"}
              className="rounded-full"
              height={32}
              src={comment.user.image}
              width={32}
            />
          )}
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium">{comment.user?.name || "Anonymous User"}</p>
            <p className="text-xs text-muted-foreground">
              {formatDistanceToNow(new Date(comment.createdAt), {
                addSuffix: true,
              })}
              {comment.updatedAt !== comment.createdAt && " (edited)"}
            </p>
          </div>
        </div>

        {isOwner && (
          <div className="flex gap-1">
            <Button className="h-6 px-2 text-xs" onClick={() => setIsEditing(!isEditing)} size="sm" variant="ghost">
              {isEditing ? "Cancel" : "Edit"}
            </Button>
            <Button
              className="h-6 px-2 text-xs text-destructive hover:text-destructive"
              disabled={isDeleting}
              onClick={() => void handleDelete()}
              size="sm"
              variant="ghost"
            >
              {isDeleting ? "Deleting..." : "Delete"}
            </Button>
          </div>
        )}
      </div>

      {/* Content */}
      {!isEditing && <p className="text-sm break-words whitespace-pre-wrap">{comment.content}</p>}

      {/* Edit Form */}
      {isEditing && (
        <CommentForm
          chapterId={comment.chapterId}
          existingComment={comment}
          initialValue={comment.content}
          onCancel={() => setIsEditing(false)}
          onSuccess={() => {
            setIsEditing(false);
            onReplySuccess?.();
          }}
        />
      )}

      {/* Reply Section */}
      {!isEditing && level < 3 && (
        <div>
          {isReplying ? (
            <CommentForm
              chapterId={comment.chapterId}
              isReply
              onCancel={() => setIsReplying(false)}
              onSuccess={() => {
                setIsReplying(false);
                onReplySuccess?.();
              }}
              parentId={comment.id}
            />
          ) : (
            <Button className="h-6 px-2 text-xs" onClick={() => setIsReplying(true)} size="sm" variant="ghost">
              Reply
            </Button>
          )}
        </div>
      )}
    </div>
  );
}
