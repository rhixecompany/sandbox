/**
 * Notification Types - Shared across components, pages, and wrappers
 */

export interface NotificationData {
  chapterId: null | number;
  comicId: null | number;
  createdAt: Date | string;
  id: number;
  link: null | string;
  message: string;
  read: boolean;
  title: string;
  type: string;
}

export interface NotificationTypeConfig {
  color: string;
  icon: string;
  label: string;
}

export interface NotificationStats {
  totalCount: number;
  unreadCount: number;
}

export type NotificationType = "bookmark" | "comment_reply" | "follow" | "new_chapter" | "rating" | "system";

export const NOTIFICATION_CONFIGS: Record<string, NotificationTypeConfig> = {
  new_chapter: { icon: "📖", color: "bg-blue-100", label: "New Chapter" },
  comment_reply: { icon: "💬", color: "bg-green-100", label: "Comment Reply" },
  system: { icon: "⚙️", color: "bg-gray-100", label: "System" },
  follow: { icon: "👤", color: "bg-purple-100", label: "New Follower" },
  rating: { icon: "⭐", color: "bg-yellow-100", label: "New Rating" },
  bookmark: { icon: "🔖", color: "bg-red-100", label: "Bookmark" },
};
