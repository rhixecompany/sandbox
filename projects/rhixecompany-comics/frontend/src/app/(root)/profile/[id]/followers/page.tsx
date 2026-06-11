/**
 * Followers Page
 * Display list of followers for a user
 */

import { getFollowersAction } from "@/actions/follow.actions";
import { auth } from "@/auth";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { FollowButton } from "@/components/users/follow-button";
import { FollowStats } from "@/components/users/follow-stats";

export default async function FollowersPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const [result, session] = await Promise.all([getFollowersAction(id), auth()]);

  const followers = result.ok ? result.data.followers : [];
  const total = result.ok ? result.data.total : 0;
  const currentUserId = session?.user?.id;
  const isOwnProfile = currentUserId === id;

  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Followers</h1>
      <FollowStats followers={total} following={0} />
      <div className="mt-6 space-y-4">
        {followers.length === 0 ? (
          <p className="text-muted-foreground">No followers yet</p>
        ) : (
          followers.map((follower) => {
            if (
              typeof follower !== "object" ||
              follower === null ||
              typeof follower.followerId !== "string" ||
              typeof follower.follower !== "object" ||
              follower.follower === null
            ) {
              return null;
            }
            const name = typeof follower.follower.name === "string" ? follower.follower.name : "Anonymous";
            const image = typeof follower.follower.image === "string" ? follower.follower.image : undefined;
            const canFollow = currentUserId && !isOwnProfile && follower.followerId !== currentUserId;

            return (
              <div className="flex items-center justify-between rounded-lg border p-4" key={follower.followerId}>
                <div className="flex items-center gap-3">
                  <Avatar>
                    <AvatarImage src={image} />
                    <AvatarFallback>{name[0]?.toUpperCase() ?? "?"}</AvatarFallback>
                  </Avatar>
                  <a className="font-medium hover:underline" href={`/profile/${follower.followerId}`}>
                    {name}
                  </a>
                </div>
                {canFollow && <FollowButton isFollowing={false} targetUserId={follower.followerId} />}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
