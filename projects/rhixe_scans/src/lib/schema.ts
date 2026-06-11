import { z } from 'zod';

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(1),
});

type Schema = z.infer<typeof schema>;

export { schema, type Schema };
const userschema = z
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

type UserSchema = z.infer<typeof userschema>;

export { userschema, type UserSchema };
