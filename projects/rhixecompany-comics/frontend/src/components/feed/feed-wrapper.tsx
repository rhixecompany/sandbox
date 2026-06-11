"use client";

import { ActivityFeed } from "@/components/activity/activity-feed";

interface ShareType {
  createdAt: Date;
  id: number;
  message: null | string;
  resourceId: number;
  resourceType: string;
  userId: string;
}

interface ActivityItem {
  createdAt: Date;
  id: number;
  message: string | undefined;
  resourceId: number;
  resourceType: string;
  type: "share";
  userId: string;
  userImage: null | string;
  userName: null | string;
}

interface FeedWrapperProps {
  activities: ActivityItem[];
}

export function FeedWrapper({ activities }: FeedWrapperProps) {
  return (
    <div className="container mx-auto py-8">
      <h1 className="mb-6 text-2xl font-bold">Activity Feed</h1>
      <ActivityFeed activities={activities} />
    </div>
  );
}

export type { ActivityItem, ShareType };
