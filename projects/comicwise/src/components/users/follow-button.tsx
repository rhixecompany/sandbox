/**
 * Follow Button Component
 * Toggle follow/unfollow state for users
 */

"use client";

import { useState } from "react";

import { followUserAction, unfollowUserAction } from "@/actions/follow.actions";
import { Button } from "@/components/ui/button";

interface FollowButtonProps {
  isFollowing: boolean;
  onFollowChange?: (isFollowing: boolean) => void;
  targetUserId: string;
}

export function FollowButton({ targetUserId, isFollowing: initialIsFollowing, onFollowChange }: FollowButtonProps) {
  const [isFollowing, setIsFollowing] = useState(initialIsFollowing);
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    setIsLoading(true);
    try {
      const result = isFollowing
        ? await unfollowUserAction({ targetUserId })
        : await followUserAction({ targetUserId });

      if (result.ok) {
        setIsFollowing(!isFollowing);
        onFollowChange?.(!isFollowing);
      }
    } catch (error) {
      console.error("Failed to toggle follow:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Button
      disabled={isLoading}
      onClick={() => void handleClick()}
      size="sm"
      variant={isFollowing ? "outline" : "default"}
    >
      {isLoading ? "Loading..." : isFollowing ? "Following" : "Follow"}
    </Button>
  );
}
