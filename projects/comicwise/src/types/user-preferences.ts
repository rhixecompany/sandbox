/**
 * User Preferences Types
 * Defines types for user settings and preferences
 */

export interface UserPreference {
  // Timestamps
  createdAt: Date;
  // Reading layout
  defaultLayout: "book" | "comic" | "webtoon";
  // Display
  fontSize: number;
  id: number;
  lineHeight: "compact" | "normal" | "relaxed";
  notifyBookmarkUpdates: boolean;
  notifyComments: boolean;
  // Notifications
  notifyNewChapters: boolean;
  pageNavigationStyle: "buttons" | "click" | "swipe";
  // Privacy
  profilePublic: boolean;
  showReadingHistory: boolean;
  // Theme
  theme: "dark" | "light" | "system";
  updatedAt: Date;
  userId: string;
}

export interface UpdateUserPreferenceInput {
  defaultLayout?: "book" | "comic" | "webtoon";
  fontSize?: number;
  lineHeight?: "compact" | "normal" | "relaxed";
  notifyBookmarkUpdates?: boolean;
  notifyComments?: boolean;
  notifyNewChapters?: boolean;
  pageNavigationStyle?: "buttons" | "click" | "swipe";
  profilePublic?: boolean;
  showReadingHistory?: boolean;
  theme?: "dark" | "light" | "system";
}

export const DEFAULT_PREFERENCES: UserPreference = {
  id: 0,
  userId: "",
  theme: "system",
  defaultLayout: "webtoon",
  pageNavigationStyle: "buttons",
  fontSize: 16,
  lineHeight: "normal",
  notifyNewChapters: true,
  notifyComments: true,
  notifyBookmarkUpdates: false,
  profilePublic: false,
  showReadingHistory: false,
  createdAt: new Date(),
  updatedAt: new Date(),
};
