"use client";
import { create } from "zustand";
import { devtools } from "zustand/middleware";

interface NotificationItem {
  createdAt: Date;
  id: number;
  message: string;
  read: boolean;
  title: string;
}

interface NotificationState {
  addNotification: (item: NotificationItem) => void;
  markAllRead: () => void;
  markRead: (id: number) => void;
  notifications: NotificationItem[];
  setNotifications: (items: NotificationItem[]) => void;
  unreadCount: number;
}

export const useNotificationStore = create<NotificationState>()(
  devtools(
    (set) => ({
      notifications: [],
      unreadCount: 0,
      setNotifications: (notifications) =>
        set({ notifications, unreadCount: notifications.filter((n) => !n.read).length }, false, "setNotifications"),
      markRead: (id) =>
        set(
          (s) => {
            const notifications = s.notifications.map((n) => (n.id === id ? { ...n, read: true } : n));
            return { notifications, unreadCount: notifications.filter((n) => !n.read).length };
          },
          false,
          "markRead"
        ),
      markAllRead: () =>
        set(
          (s) => ({
            notifications: s.notifications.map((n) => ({ ...n, read: true })),
            unreadCount: 0,
          }),
          false,
          "markAllRead"
        ),
      addNotification: (item) =>
        set(
          (s) => ({
            notifications: [item, ...s.notifications],
            unreadCount: item.read ? s.unreadCount : s.unreadCount + 1,
          }),
          false,
          "addNotification"
        ),
    }),
    { name: "NotificationStore" }
  )
);
