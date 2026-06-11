import { z } from 'zod';

import { COMIC_STATUS, IMAGE_STATUS } from './constants';
import { formatNumberWithDecimal } from './utils';

const rating = z
  .string()
  .refine(
    (value) => /^\d+(\.\d{1})?$/.test(formatNumberWithDecimal(Number(value))),
    'Price must have exactly two decimal places'
  );
// const myrating = z.coerce
//   .number()
//   .int()
//   .min(1, 'Rating must be at least 1')
//   .max(10, 'Rating must be at most 5');

const comicstatus = z.string().refine((value) => COMIC_STATUS.includes(value), {
  path: ['status'],
  message: 'Invalid comic status',
});
const imagestatus = z
  .string()
  .refine((value) => IMAGE_STATUS.includes(value), {
    path: ['status'],
    message: 'Invalid comic image status',
  })
  .optional()
  .nullable();

// Schema for signing users in
export const signInFormSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z.string().min(6, 'Password must be at least 6 characters'),
});

// Schema for signing up a user
export const signUpFormSchema = z
  .object({
    name: z.string().min(3, 'Name must be at least 3 characters'),
    email: z.string().email('Invalid email address'),
    password: z.string().min(6, 'Password must be at least 6 characters'),
    confirmPassword: z
      .string()
      .min(6, 'Confirm password must be at least 6 characters'),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords don't match",
    path: ['confirmPassword'],
  });

// Schema for updating the user profile
export const updateProfileSchema = z.object({
  name: z.string().min(3, 'Name must be at leaast 3 characters'),
  email: z.string().min(3, 'Email must be at leaast 3 characters'),
});

// Schema to update users
export const updateUserSchema = updateProfileSchema.extend({
  id: z.string().min(1, 'ID is required'),
  role: z.string().min(1, 'Role is required'),
});

// Schema for inserting comicImages
export const insertComicImageSchema = z.object({
  link: z.string().min(3, 'Link must be at least 3 characters'),
  image: z
    .string()
    .min(3, 'Image must be at least 3 characters')
    .optional()
    .nullable(),
  checksum: z
    .string()
    .min(3, 'Checksum must be at least 3 characters')
    .optional()
    .nullable(),
  status: imagestatus,
  comic: z.string().min(3, 'Comic must be at least 3 characters'),
});

// Schema for updating comicImages
export const updateComicImageSchema = insertComicImageSchema.extend({
  id: z.string().min(1, 'Id is required'),
});
// Schema for inserting chapterImages
export const insertChapterImageSchema = z.object({
  link: z.string().min(3, 'Link must be at least 3 characters'),
  image: z
    .string()
    .min(3, 'Image must be at least 3 characters')
    .optional()
    .nullable(),
  checksum: z
    .string()
    .min(3, 'Checksum must be at least 3 characters')
    .optional()
    .nullable(),
  status: imagestatus,
  comic: z.string().min(3, 'Comic must be at least 3 characters'),
  chapter: z.string().min(3, 'Chapter must be at least 3 characters'),
});

// Schema for updating chapterImages
export const updateChapterImageSchema = insertChapterImageSchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Schema for inserting genre
export const insertGenreSchema = z.object({
  name: z.string().min(3, 'Name must be at least 3 characters'),
});

// Schema for updating genre
export const updateGenreSchema = insertGenreSchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Schema for inserting category
export const insertCategorySchema = z.object({
  name: z.string().min(3, 'Name must be at least 3 characters'),
});

// Schema for updating category
export const updateCategorySchema = insertCategorySchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Schema for inserting authors
export const insertAuthorSchema = z.object({
  name: z.string().min(1, 'Name must be at least 3 characters'),
});

// Schema for updating authors
export const updateAuthorSchema = insertAuthorSchema.extend({
  id: z.string().min(1, 'Id is required'),
});
// Schema for inserting artists
export const insertArtistSchema = z.object({
  name: z.string().min(1, 'Name must be at least 3 characters'),
});

// Schema for updating artists
export const updateArtistSchema = insertArtistSchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Schema for inserting comics
export const insertComicSchema = z.object({
  title: z.string().min(3, 'Title must be at least 3 characters'),
  slug: z.string().min(3, 'Slug must be at least 3 characters'),
  description: z.string().min(3, 'Description must be at least 3 characters'),
  rating: rating,
  status: comicstatus,
  link: z.string().min(3, 'Link must be at least 3 characters'),
  serialization: z
    .string()
    .min(3, 'Serialization must be at least 3 characters'),
  numimages: z
    .number()
    .int()
    .nonnegative('NumImages must be a positive number'),
  numchapters: z
    .number()
    .int()
    .nonnegative('NumChapters must be a positive number'),
  has_images: z.boolean(),
  has_chapters: z.boolean(),
  updated_at: z.string().min(3, 'Update At must be at least 3 characters'),
  images: z.array(insertComicImageSchema),
  genres: z.array(insertGenreSchema),
  category: insertCategorySchema,
  author: insertAuthorSchema,
  artist: insertArtistSchema,
});

// Schema for updating comics
export const updateComicSchema = insertComicSchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Schema for inserting chapters
export const insertChapterSchema = z.object({
  name: z.string().min(3, 'Name must be at least 3 characters'),
  slug: z.string().min(3, 'Slug must be at least 3 characters'),
  title: z.string().optional().nullable(),
  link: z.string().min(3, 'Link must be at least 3 characters'),
  numimages: z
    .number()
    .int()
    .nonnegative('NumImages must be a positive number'),
  has_images: z.boolean(),
  updated_at: z.string().min(3, 'Update At must be at least 3 characters'),
  images: z.array(insertChapterImageSchema),
  comic: z.object({
    title: z.string().min(3, 'Title must be at least 3 characters'),
    slug: z.string().min(3, 'Slug must be at least 3 characters'),
    description: z.string().min(3, 'Description must be at least 3 characters'),
    rating: rating,
    status: comicstatus,
    link: z.string().min(3, 'Link must be at least 3 characters'),
    serialization: z
      .string()
      .min(3, 'Serialization must be at least 3 characters'),
    numimages: z
      .number()
      .int()
      .nonnegative('NumImages must be a positive number'),
    numchapters: z
      .number()
      .int()
      .nonnegative('NumChapters must be a positive number'),
    has_images: z.boolean(),
    has_chapters: z.boolean(),
    updated_at: z.string().min(3, 'Update At must be at least 3 characters'),
    images: z.array(insertComicImageSchema),
    genres: z.array(insertGenreSchema),
    category: insertCategorySchema,
    author: insertAuthorSchema,
    artist: insertArtistSchema,
  }),
});

// Schema for updating chapters
export const updateChapterSchema = insertChapterSchema.extend({
  id: z.string().min(1, 'Id is required'),
});

// Bookmark Schemas
export const bookmarkItemSchema = z.object({
  id: z.string().min(1, 'id is required'),
  title: z.string().min(3, 'Title must be at least 3 characters'),
  slug: z.string().min(3, 'Slug must be at least 3 characters'),
  description: z.string().min(3, 'Description must be at least 3 characters'),
  rating: rating,
  status: comicstatus,
  link: z.string().min(3, 'Link must be at least 3 characters'),
  serialization: z
    .string()
    .min(3, 'Serialization must be at least 3 characters'),
  numimages: z
    .number()
    .int()
    .nonnegative('NumImages must be a positive number'),
  numchapters: z
    .number()
    .int()
    .nonnegative('NumChapters must be a positive number'),
  has_images: z.boolean(),
  has_chapters: z.boolean(),
  updated_at: z.string().min(3, 'Update At must be at least 3 characters'),
  images: z.array(insertComicImageSchema),
  genres: z.array(insertGenreSchema),
  category: insertCategorySchema,
  author: insertAuthorSchema,
  artist: insertArtistSchema,
  qty: z.number().int().nonnegative('Quantity must be a positive number'),
});

export const insertBookmarkSchema = z.object({
  items: z.array(bookmarkItemSchema),
  sessionBookmarkId: z.string().min(1, 'Session bookmark id is required'),
  userId: z.string().optional().nullable(),
});
