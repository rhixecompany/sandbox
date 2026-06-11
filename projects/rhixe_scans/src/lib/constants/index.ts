export const APP_NAME = process.env.NEXT_PUBLIC_APP_NAME || 'Rhixe Scans';
export const APP_DESCRIPTION =
  process.env.NEXT_PUBLIC_APP_DESCRIPTION || 'Read Comics';
export const SERVER_URL =
  process.env.NEXT_PUBLIC_SERVER_URL || 'http://localhost:3000';
export const LATEST_COMICS_LIMIT = Number(process.env.LATEST_COMICS_LIMIT) || 4;

export const signInDefaultValues = {
  email: '',
  password: '',
};

export const signUpDefaultValues = {
  name: '',
  email: '',
  password: '',
  confirmPassword: '',
};

export const COMIC_STATUS = process.env.COMIC_STATUS
  ? process.env.COMIC_STATUS.split(', ')
  : ['completed', 'ongoing', 'hiatus', 'dropped', 'season end', 'coming soon'];
export const DEFAULT_STATUS = process.env.DEFAULT_STATUS || 'ongoing';
export const IMAGE_STATUS = process.env.IMAGE_STATUS
  ? process.env.IMAGE_STATUS.split(', ')
  : ['downloaded', 'uptodate', 'cached'];
export const DEFAULT_IMAGE_STATUS =
  process.env.DEFAULT_IMAGE_STATUS || 'downloaded';

export const PAGE_SIZE = Number(process.env.PAGE_SIZE) || 12;

export const comicDefaultValues = {
  title: '',
  slug: '',
  description: '',
  rating: '0',
  numchapters: 0,
  numimages: 0,
  updated_at: '',
  serialization: '',
  status: '',
  link: '',
  category: {},
  has_images: false,
  has_chapters: false,
  author: {},
  artist: {},
  genres: [],
  images: [],
};

export const USER_ROLES = process.env.USER_ROLES
  ? process.env.USER_ROLES.split(', ')
  : ['admin', 'user'];

export const SENDER_EMAIL = process.env.SENDER_EMAIL || 'onboarding@resend.dev';
