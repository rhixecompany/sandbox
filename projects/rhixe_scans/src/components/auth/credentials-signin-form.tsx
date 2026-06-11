import { Button } from '@/components/ui/button';

import { Apple } from '@/components/ui/apple';
import { Github } from '@/components/ui/github';
import { Google } from '@/components/ui/google';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';

import { signIn } from '@/auth';
import { executeAction } from '@/lib/executeAction';
import Link from 'next/link';
import { CustomSignIn } from './custom-sign-in';
const CredentialsSignInForm = () => {
  return (
    <>
      <form
        action={async (formData) => {
          'use server';
          await executeAction({
            actionFn: async () => {
              await signIn('credentials', formData);
            },
          });
        }}
      >
        <div className='grid gap-2 mb-2'>
          <Label htmlFor='email'>Email</Label>
          <Input
            name='email'
            placeholder='Email'
            type='email'
            required
            autoComplete='email'
          />
        </div>
        <div className='grid gap-2 mb-2'>
          <div className='flex items-center'>
            <Label htmlFor='password'>Password</Label>
            <Link
              href='#'
              className='ml-auto text-sm underline-offset-2 hover:underline'
            >
              Forgot your password?
            </Link>
          </div>
          <Input
            name='password'
            placeholder='Password'
            type='password'
            required
            autoComplete='current-password'
          />
        </div>
        <div className='mt-4'>
          <Button type='submit' className='w-full'>
            Login
          </Button>
        </div>
      </form>
      <div className='relative text-center text-sm after:absolute after:inset-0 after:top-1/2 after:z-0 after:flex after:items-center after:border-t after:border-border'>
        <span className='relative z-10 bg-background px-2 text-muted-foreground'>
          Or continue with
        </span>
      </div>
      <div className='grid grid-cols-3 gap-4'>
        <CustomSignIn
          text='Login with Apple'
          provider='apple'
          icon={<Apple />}
        />
        <CustomSignIn
          text='Login with Google'
          provider='google'
          icon={<Google />}
        />
        <CustomSignIn
          text='Login with Github'
          provider='github'
          icon={<Github />}
        />
      </div>
    </>
  );
};

export default CredentialsSignInForm;
