/**
 * User Ratings Page
 * Route: /ratings
 */

import { redirect } from "next/navigation";

import { getUserRatingsAction } from "@/actions/comment-rating.actions";
import { auth } from "@/auth";
import { RatingsWrapper } from "@/components/ratings/ratings-wrapper";

export const metadata = {
  title: "My Ratings | ComicWise",
  description: "View comics you've rated on ComicWise",
};

export default async function RatingsPage() {
  const session = await auth();

  if (!session?.user) {
    redirect("/sign-in");
  }

  const result = await getUserRatingsAction();
  const ratings = result.ok ? (result.data ?? []) : [];

  return <RatingsWrapper ratings={ratings} />;
}
