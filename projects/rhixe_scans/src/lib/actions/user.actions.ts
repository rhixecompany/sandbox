import db from '@/lib/db';
import { executeAction } from '@/lib/executeAction';
import { userschema } from '@/lib/schema';

const signUp = async (formData: FormData) => {
  return executeAction({
    actionFn: async () => {
      const email = formData.get('email');
      const name = formData.get('name');
      const password = formData.get('password');
      const confirmPassword = formData.get('confirmPassword');
      const validatedData = userschema.parse({
        email,
        name,
        password,
        confirmPassword,
      });
      await db.user.create({
        data: {
          email: validatedData.email.toLocaleLowerCase(),
          name: validatedData.name,
          password: validatedData.password,
        },
      });
    },
    successMessage: 'Signed up successfully',
  });
};

export { signUp };
