import {
  bookmarkItemSchema,
  insertBookmarkSchema,
  insertChapterImageSchema,
  insertChapterSchema,
  insertComicImageSchema,
  insertComicSchema,
  signUpFormSchema,
} from '@/lib/validators';
import { z } from 'zod';

export type Comic = z.infer<typeof insertComicSchema> & {
  id?: string;
  createdAt: Date;
  updatedAt: Date;
};
export type ComicImage = z.infer<typeof insertComicImageSchema> & {
  id?: string;
};
export type Chapter = z.infer<typeof insertChapterSchema> & {
  id?: string;
  createdAt: Date;
  updatedAt: Date;
};
export type ChapterImage = z.infer<typeof insertChapterImageSchema> & {
  id?: string;
};
export type User = z.infer<typeof signUpFormSchema> & {
  id?: string;
};

export type Bookmark = z.infer<typeof insertBookmarkSchema>;
export type BookmarkItem = z.infer<typeof bookmarkItemSchema>;

const loginschema = z.object({
  email: z.string().email(),
  password: z.string().min(1),
});

type loginSchema = z.infer<typeof loginschema>;

export { loginschema, type loginSchema };

const signupschema = z
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

type signupSchema = z.infer<typeof signupschema>;

export { signupschema, type signupSchema };
