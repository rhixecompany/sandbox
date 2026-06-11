/**
 * Notifications Page
 * Route: /notifications
 */

import { redirect } from "next/navigation";

import { getNotificationsAction } from "@/actions/notification.actions";
import { auth } from "@/auth";
import { NotificationsWrapper } from "@/components/notifications/notifications-wrapper";

export const metadata = {
  title: "Notifications - ComicWise",
  description: "View your notifications about new chapters and comments",
};

export default async function NotificationsPage() {
  const session = await auth();

  if (!session?.user?.id) {
    redirect("/sign-in");
  }

  const result = await getNotificationsAction();
  const notifications = result.ok ? result.data : [];

  return <NotificationsWrapper notifications={notifications} />;
}
