/**
 * Profile Types - Shared across components, pages, and wrappers
 */

export interface UserProfile {
  bio?: null | string;
  createdAt?: Date | string;
  email: null | string;
  id?: string;
  image: null | string;
  name: null | string;
  role?: string;
}

export interface UserStats {
  bookmarks: number;
  chaptersRead: number;
  commentsMade: number;
  followers?: number;
  following?: number;
  ratingsGiven: number;
}

export interface ProfileWrapperProps {
  profile: UserProfile;
  stats: UserStats;
}

export interface EditProfileData {
  bio?: string;
  image?: string;
  name?: string;
}

export interface ChangePasswordData {
  confirmPassword: string;
  currentPassword: string;
  newPassword: string;
}
