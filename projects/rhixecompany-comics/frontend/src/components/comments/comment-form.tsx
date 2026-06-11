/**
 * CommentForm Component
 * Form for creating and editing comments
 */

"use client";

import { useState, useTransition } from "react";

import { createCommentAction, replyToCommentAction, updateCommentAction } from "@/actions/comment-rating.actions";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

import type { Comment } from "@/types/comment-rating";

interface CommentFormProps {
  chapterId: number;
  existingComment?: Comment;
  initialValue?: string;
  isReply?: boolean;
  onCancel?: () => void;
  onSuccess?: (comment: Comment) => void;
  parentId?: number;
}

export function CommentForm({
  chapterId,
  parentId,
  onSuccess,
  onCancel,
  initialValue = "",
  isReply = false,
  existingComment,
}: CommentFormProps) {
  const [content, setContent] = useState(initialValue);
  const [error, setError] = useState<null | string>(null);
  const [isPending, startTransition] = useTransition();

  const isEditing = !!existingComment;
  const characterCount = content.length;
  const maxCharacters = 5000;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!content.trim()) {
      setError("Comment cannot be empty");
      return;
    }

    if (content.length > maxCharacters) {
      setError(`Comment must be less than ${maxCharacters} characters`);
      return;
    }

    startTransition(async () => {
      try {
        let result;

        if (isEditing && existingComment) {
          result = await updateCommentAction(existingComment.id, {
            content: content.trim(),
          });
        } else if (parentId) {
          result = await replyToCommentAction(parentId, {
            content: content.trim(),
            chapterId,
          });
        } else {
          result = await createCommentAction({
            content: content.trim(),
            chapterId,
          });
        }

        if (result.ok) {
          setContent("");
          onSuccess?.(result.data);
        } else {
          setError(result.error);
        }
      } catch {
        setError("An error occurred while saving your comment");
      }
    });
  };

  const buttonText = isEditing ? "Update Comment" : isReply ? "Post Reply" : "Post Comment";
  const placeholder = isReply
    ? "Write a reply..."
    : isEditing
      ? "Edit your comment..."
      : "Share your thoughts about this chapter...";

  return (
    <form
      className="space-y-3"
      onSubmit={(e) => {
        void handleSubmit(e);
      }}
    >
      <div className="relative">
        <Textarea
          className="min-h-24 resize-none"
          disabled={isPending}
          maxLength={maxCharacters}
          onChange={(e) => {
            setContent(e.target.value);
            setError(null);
          }}
          placeholder={placeholder}
          value={content}
        />
        <div className="absolute right-2 bottom-2 text-xs text-muted-foreground">
          {characterCount}/{maxCharacters}
        </div>
      </div>

      {error && <div className="rounded bg-destructive/10 p-2 text-sm text-destructive">{error}</div>}

      <div className="flex justify-between gap-2">
        <div>
          {onCancel && (
            <Button disabled={isPending} onClick={onCancel} type="button" variant="ghost">
              Cancel
            </Button>
          )}
        </div>
        <Button className="min-w-[120px]" disabled={isPending || !content.trim()} type="submit">
          {isPending ? "Posting..." : buttonText}
        </Button>
      </div>
    </form>
  );
}
