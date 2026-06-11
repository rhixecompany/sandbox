/**
 * Activity Feed Page
 * Route: /feed
 */

import { getFeedSharesAction } from "@/actions/share.actions";
import { auth } from "@/auth";
import { FeedWrapper } from "@/components/feed/feed-wrapper";

export const metadata = {
  title: "Activity Feed | ComicWise",
  description: "See what people you follow are reading and sharing",
};

export default async function FeedPage() {
  const session = await auth();

  if (!session?.user?.id) {
    return (
      <div className="container mx-auto py-8">
        <h1 className="mb-6 text-2xl font-bold">Activity Feed</h1>
        <p className="text-muted-foreground">Please sign in to see your feed.</p>
      </div>
    );
  }

  const result = await getFeedSharesAction(session.user.id);
  const shares = result.ok ? result.data.shares : [];

  const activities = shares.map((share) => ({
    id: share.id,
    type: "share" as const,
    userId: share.userId,
    userName: null,
    userImage: null,
    resourceType: share.resourceType,
    resourceId: share.resourceId,
    message: share.message ?? undefined,
    createdAt: share.createdAt,
  }));

  return <FeedWrapper activities={activities} />;
}
