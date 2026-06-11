/**
 * Following Page
 * Display list of users that a user is following
 */

import { getFollowingAction } from "@/actions/follow.actions";
import { auth } from "@/auth";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { FollowButton } from "@/components/users/follow-button";
import { FollowStats } from "@/components/users/follow-stats";

interface FollowWithUser {
  createdAt: Date;
  followerId: string;
  following?: {
    id: string;
    image: null | string;
    name: null | string;
  };
  followingId: string;
}

export default async function FollowingPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const [result, session] = await Promise.all([getFollowingAction(id), auth()]);

  const following = result.ok ? result.data.following : [];
  const total = result.ok ? result.data.total : 0;
  const currentUserId = session?.user?.id;
  const isOwnProfile = currentUserId === id;

  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Following</h1>
      <FollowStats followers={0} following={total} />
      <div className="mt-6 space-y-4">
        {following.length === 0 ? (
          <p className="text-muted-foreground">Not following anyone yet</p>
        ) : (
          following.map((user: FollowWithUser) => {
            const canUnfollow = currentUserId && !isOwnProfile && user.followingId !== currentUserId;

            return (
              <div className="flex items-center justify-between rounded-lg border p-4" key={user.followingId}>
                <div className="flex items-center gap-3">
                  <Avatar>
                    <AvatarImage src={user.following?.image ?? undefined} />
                    <AvatarFallback>{user.following?.name?.[0]?.toUpperCase() ?? "?"}</AvatarFallback>
                  </Avatar>
                  <a className="font-medium hover:underline" href={`/profile/${user.followingId}`}>
                    {user.following?.name ?? "Anonymous"}
                  </a>
                </div>
                {canUnfollow && <FollowButton isFollowing={true} targetUserId={user.followingId} />}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
