/**
 * User Profile View Page
 * Route: /profile
 */

import { redirect } from "next/navigation";
import { Suspense } from "react";

import { getUserProfileAction, getUserProfileStatsAction } from "@/actions/profile.actions";
import { auth } from "@/auth";
import { ProfileWrapper } from "@/components/profile/profile-wrapper";

export const metadata = {
  title: "Profile | ComicWise",
  description: "View and manage your ComicWise profile",
};

function ProfileSkeleton() {
  return (
    <div className="mx-auto max-w-4xl space-y-6 px-4 py-8">
      <div className="h-40 animate-pulse rounded-lg bg-muted" />
      <div className="grid grid-cols-4 gap-4">
        {[1, 2, 3, 4].map((i) => (
          <div className="h-24 animate-pulse rounded-lg bg-muted" key={i} />
        ))}
      </div>
    </div>
  );
}

export default async function ProfilePage() {
  const session = await auth();

  if (!session?.user) {
    redirect("/sign-in");
  }

  const [profileResult, statsResult] = await Promise.all([getUserProfileAction(), getUserProfileStatsAction()]);

  const profile = profileResult.ok ? profileResult.data : { name: null, email: null, image: null };

  const stats = statsResult.ok ? statsResult.data : { bookmarks: 0, ratingsGiven: 0, commentsMade: 0, chaptersRead: 0 };

  return (
    <main className="min-h-screen bg-background">
      <Suspense fallback={<ProfileSkeleton />}>
        <ProfileWrapper profile={profile} stats={stats} />
      </Suspense>
    </main>
  );
}
