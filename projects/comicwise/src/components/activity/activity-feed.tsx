/**
 * Activity Feed Component
 * Displays a timeline of user activities (shares, comments, ratings)
 */

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

interface ActivityItem {
  createdAt: Date;
  id: number;
  message?: string;
  resourceId: number;
  resourceType: string;
  type: "bookmark" | "comment" | "rating" | "share";
  userId: string;
  userImage: null | string;
  userName: null | string;
}

interface ActivityFeedProps {
  activities: ActivityItem[];
}

function getActivityMessage(activity: ActivityItem): string {
  switch (activity.type) {
    case "share":
      return `shared a ${activity.resourceType}`;
    case "comment":
      return `commented on ${activity.resourceType}`;
    case "rating":
      return `rated ${activity.resourceType}`;
    case "bookmark":
      return `bookmarked ${activity.resourceType}`;
    default:
      return "performed an action";
  }
}

export function ActivityFeed({ activities }: ActivityFeedProps) {
  if (activities.length === 0) {
    return (
      <div className="py-8 text-center text-muted-foreground">
        No activity yet. Follow users to see their activity here.
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {activities.map((activity) => (
        <div className="flex gap-3 rounded-lg border bg-card p-4" key={activity.id}>
          <Avatar>
            <AvatarImage src={activity.userImage ?? undefined} />
            <AvatarFallback>{activity.userName?.[0]?.toUpperCase() ?? "?"}</AvatarFallback>
          </Avatar>
          <div className="flex-1 space-y-1">
            <p className="text-sm">
              <span className="font-semibold">{activity.userName ?? "Anonymous"}</span>{" "}
              <span className="text-muted-foreground">{getActivityMessage(activity)}</span>
            </p>
            {activity.message && <p className="text-sm text-muted-foreground">{activity.message}</p>}
            <p className="text-xs text-muted-foreground">{new Date(activity.createdAt).toLocaleDateString()}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
