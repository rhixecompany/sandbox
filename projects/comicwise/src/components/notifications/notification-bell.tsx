"use client";

import { formatDistanceToNow } from "date-fns";
import { Bell } from "lucide-react";
import { useSession } from "next-auth/react";
import { useEffect, useState, useTransition } from "react";
import { toast } from "sonner";

import { markAllNotificationsReadAction, markNotificationReadAction } from "@/actions/notification.actions";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { useNotificationStore } from "@/stores/use-notification-store";

export function NotificationBell() {
  const { data: session } = useSession();
  const [isOpen, setIsOpen] = useState(false);
  const [isPending, startTransition] = useTransition();
  const notifications = useNotificationStore((state) => state.notifications);
  const unreadCount = useNotificationStore((state) => state.unreadCount);
  const markRead = useNotificationStore((state) => state.markRead);
  const markAllRead = useNotificationStore((state) => state.markAllRead);

  // Close drawer on Escape key
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) {
        setIsOpen(false);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen]);

  if (!session?.user?.id) return null;

  const handleMarkAsRead = (notificationId: number) => {
    startTransition(async () => {
      try {
        const result = await markNotificationReadAction(notificationId);
        if (result.ok) {
          markRead(notificationId);
        } else {
          toast.error(result.error || "Failed to mark notification as read");
        }
      } catch {
        toast.error("An error occurred");
      }
    });
  };

  const handleClearAll = () => {
    startTransition(async () => {
      try {
        const result = await markAllNotificationsReadAction();
        if (result.ok) {
          markAllRead();
          toast.success("All notifications cleared");
        } else {
          toast.error(result.error || "Failed to clear notifications");
        }
      } catch {
        toast.error("An error occurred");
      }
    });
  };

  return (
    <>
      <div className="relative">
        <Button
          aria-label="Notifications"
          className="relative h-9 w-9 p-0"
          onClick={() => setIsOpen(true)}
          size="sm"
          title={unreadCount > 0 ? `${unreadCount} unread notification(s)` : "No new notifications"}
          variant="ghost"
        >
          <Bell className="h-4 w-4" />
          {unreadCount > 0 && (
            <Badge
              className="absolute -top-2 -right-2 flex h-5 w-5 items-center justify-center rounded-full bg-red-500 p-0 text-xs font-semibold text-white"
              variant="destructive"
            >
              {unreadCount > 9 ? "9+" : unreadCount}
            </Badge>
          )}
        </Button>
      </div>

      <Dialog onOpenChange={setIsOpen} open={isOpen}>
        <DialogContent className="max-w-sm">
          <DialogHeader>
            <DialogTitle>Notifications</DialogTitle>
            <DialogDescription>
              {unreadCount > 0 ? `You have ${unreadCount} unread notification(s)` : "All caught up!"}
            </DialogDescription>
          </DialogHeader>

          <div className="max-h-96 space-y-2 overflow-y-auto">
            {notifications.length === 0 ? (
              <div className="py-8 text-center text-muted-foreground">
                <p>No notifications yet</p>
              </div>
            ) : (
              notifications.map((notification) => (
                <div
                  className={`space-y-1 rounded-lg border p-3 ${!notification.read ? "bg-muted" : "bg-background"}`}
                  key={notification.id}
                >
                  <div className="flex items-start justify-between gap-2">
                    <div className="flex-1">
                      <p className="text-sm font-semibold">{notification.title}</p>
                      <p className="line-clamp-2 text-xs text-muted-foreground">{notification.message}</p>
                      <p className="mt-1 text-xs text-muted-foreground">
                        {formatDistanceToNow(new Date(notification.createdAt), { addSuffix: true })}
                      </p>
                    </div>
                    {!notification.read && (
                      <Button
                        className="h-auto px-2 py-1 text-xs"
                        disabled={isPending}
                        onClick={() => handleMarkAsRead(notification.id)}
                        size="sm"
                        variant="ghost"
                      >
                        Mark read
                      </Button>
                    )}
                  </div>
                </div>
              ))
            )}
          </div>

          {notifications.length > 0 && (
            <div className="border-t pt-3">
              <Button
                className="w-full"
                disabled={isPending || notifications.length === 0}
                onClick={handleClearAll}
                size="sm"
                variant="outline"
              >
                Clear all
              </Button>
            </div>
          )}
        </DialogContent>
      </Dialog>
    </>
  );
}
