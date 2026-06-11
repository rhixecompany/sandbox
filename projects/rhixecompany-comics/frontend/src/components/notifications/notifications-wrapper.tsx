"use client";

import { Bell, ChevronRight } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface NotificationData {
  chapterId: null | number;
  comicId: null | number;
  createdAt: Date;
  id: number;
  link: null | string;
  message: string;
  read: boolean;
  title: string;
  type: string;
}

interface NotificationItemProps {
  notification: NotificationData;
}

const notificationTypeConfig: Record<string, { color: string; icon: string; label: string }> = {
  new_chapter: { icon: "📖", color: "bg-blue-100", label: "New Chapter" },
  comment_reply: { icon: "💬", color: "bg-green-100", label: "Comment Reply" },
  system: { icon: "⚙️", color: "bg-gray-100", label: "System" },
};

function NotificationItem({ notification: notif }: NotificationItemProps) {
  const config = notificationTypeConfig[notif.type] || {
    icon: "🔔",
    color: "bg-gray-100",
    label: notif.type,
  };

  const formattedDate = new Date(notif.createdAt).toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });

  const content = (
    <div
      className={`rounded-lg border p-4 transition-colors ${
        notif.read ? "border-border bg-background" : "border-primary/50 bg-primary/5"
      }`}
    >
      <div className="flex items-start gap-4">
        <div className="mt-1 text-2xl">{config.icon}</div>
        <div className="min-w-0 flex-1">
          <div className="mb-1 flex items-start justify-between gap-2">
            <h3 className="truncate font-semibold">{notif.title}</h3>
            <span className="text-xs whitespace-nowrap text-muted-foreground">{formattedDate}</span>
          </div>
          <p className="line-clamp-2 text-sm text-muted-foreground">{notif.message}</p>
          {notif.link && (
            <a className="mt-2 inline-flex items-center gap-1 text-xs text-primary hover:underline" href={notif.link}>
              View <ChevronRight className="h-3 w-3" />
            </a>
          )}
        </div>
        {!notif.read && <div className="mt-2 h-2 w-2 shrink-0 rounded-full bg-primary" />}
      </div>
    </div>
  );

  return notif.link ? <a href={notif.link}>{content}</a> : content;
}

interface NotificationsWrapperProps {
  notifications: NotificationData[];
}

export function NotificationsWrapper({ notifications }: NotificationsWrapperProps) {
  const unreadCount = notifications.filter((n) => !n.read).length;

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <section className="border-b border-border bg-linear-to-br from-primary/20 via-background to-primary/10 py-8">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="flex items-center gap-3 text-3xl font-bold md:text-4xl">
                <Bell className="h-8 w-8" />
                Notifications
              </h1>
              <p className="mt-2 text-muted-foreground">Stay updated with new chapters and community interactions</p>
            </div>
          </div>
        </div>
      </section>

      {/* Notifications List */}
      <section className="py-8">
        <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
          {notifications.length === 0 ? (
            <div className="py-12 text-center">
              <Bell className="mx-auto mb-4 h-12 w-12 text-muted-foreground" />
              <p className="mb-2 text-lg font-semibold">No notifications yet</p>
              <p className="mb-6 text-muted-foreground">
                You&apos;ll see notifications here when new chapters are released or you get comments
              </p>
              <Link href="/browse">
                <Button variant="outline">Browse Comics</Button>
              </Link>
            </div>
          ) : (
            <div className="space-y-4">
              {unreadCount > 0 && (
                <div className="flex items-center justify-between rounded-lg border border-primary/20 bg-primary/10 p-4">
                  <div>
                    <p className="font-semibold">
                      You have {unreadCount} unread notification
                      {unreadCount !== 1 ? "s" : ""}
                    </p>
                  </div>
                  <Button size="sm" variant="outline">
                    Mark all as read
                  </Button>
                </div>
              )}

              <div className="space-y-3">
                {notifications.map((notif) => (
                  <NotificationItem key={notif.id} notification={notif} />
                ))}
              </div>
            </div>
          )}
        </div>
      </section>
    </main>
  );
}
