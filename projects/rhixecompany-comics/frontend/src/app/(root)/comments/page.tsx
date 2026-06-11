/**
 * User Comments Page
 * Route: /comments
 */

import { redirect } from "next/navigation";

import { getUserCommentsAction } from "@/actions/comment-rating.actions";
import { auth } from "@/auth";
import { CommentsWrapper } from "@/components/comments/comments-wrapper";

export const metadata = {
  title: "My Comments | ComicWise",
  description: "View and manage your comments on ComicWise",
};

export default async function CommentsPage() {
  const session = await auth();

  if (!session?.user) {
    redirect("/sign-in");
  }

  const result = await getUserCommentsAction();
  const comments = result.ok ? (result.data ?? []) : [];

  return <CommentsWrapper comments={comments as CommentsWrapperProps["comments"]} />;
}

interface CommentsWrapperProps {
  comments: Array<{
    chapter: {
      chapterNumber: number | string;
      comic?: {
        slug: string;
        title: string;
      };
    };
    content: string;
    createdAt: Date | string;
    id: number | string;
  }>;
}
