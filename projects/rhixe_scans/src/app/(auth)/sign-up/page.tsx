import { CustomSignIn } from '@/components/custom-sign-in';
import { Apple } from '@/components/ui/apple';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { Github } from '@/components/ui/github';
import { Google } from '@/components/ui/google';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { signUp } from '@/lib/actions/user.actions';
import { APP_NAME } from '@/lib/constants';
import Image from 'next/image';
import Link from 'next/link';
import { redirect } from 'next/navigation';

import { auth } from '@/auth';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Sign Up',
};

const Page = async () => {
  const session = await auth();
  if (session) redirect('/');
  return (
    <div className='flex min-h-svh flex-col items-center justify-center bg-muted p-6 md:p-10'>
      <div className='w-full max-w-sm md:max-w-3xl'>
        <div className='flex flex-col gap-6'>
          <Card className='overflow-hidden'>
            <CardContent className='grid p-0 md:grid-cols-2'>
              <div className='p-6 md:p-8'>
                <div className='flex flex-col gap-6'>
                  <div className='flex flex-col items-center text-center'>
                    <h1 className='text-2xl font-bold'>Welcome back</h1>
                    <p className='text-balance text-muted-foreground'>
                      Signup for a new account
                    </p>
                  </div>
                  <form
                    action={async (formData) => {
                      'use server';
                      const res = await signUp(formData);
                      if (res.success) {
                        redirect('/sign-in');
                      }
                    }}
                    // action={async (formData) => {
                    //   'use server';
                    //   const res = await signUp(formData);
                    //   if (res.success) {
                    //     redirect('/sign-in');
                    //   }
                    // }}
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
                      <Label htmlFor='name'>Name</Label>
                      <Input
                        name='name'
                        placeholder='Name'
                        type='name'
                        required
                        autoComplete='name'
                      />
                    </div>
                    <div className='grid gap-2 mb-2'>
                      <Label htmlFor='password'>Password</Label>
                      <Input
                        name='password'
                        placeholder='Password'
                        type='password'
                        required
                        autoComplete='current-password'
                      />
                    </div>
                    <div className='grid gap-2 mb-2'>
                      <Label htmlFor='confirmPassword'>ConfirmPassword</Label>
                      <Input
                        name='confirmPassword'
                        placeholder='confirmPassword'
                        type='password'
                        required
                        autoComplete='confirm-password'
                      />
                    </div>
                    <div className='mt-4'>
                      <Button type='submit' className='w-full'>
                        Signup
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
                      text='Signup with Apple'
                      provider='apple'
                      icon={<Apple />}
                    />
                    <CustomSignIn
                      text='Signup with Google'
                      provider='google'
                      icon={<Google />}
                    />
                    <CustomSignIn
                      text='Signup with Github'
                      provider='github'
                      icon={<Github />}
                    />
                  </div>

                  <div className='text-center text-sm'>
                    Already have an account?{' '}
                    <Link
                      href='/sign-in'
                      className='underline underline-offset-4'
                    >
                      Sign in
                    </Link>
                  </div>
                </div>
              </div>
              <div className='relative hidden bg-muted md:block'>
                <Image
                  src='/images/logo.png'
                  width={100}
                  height={100}
                  alt={`${APP_NAME} logo`}
                  priority={true}
                  className='absolute inset-0 h-full w-full object-cover dark:brightness-[0.2] dark:grayscale'
                />
              </div>
            </CardContent>
          </Card>
          <div className='text-balance text-center text-xs text-muted-foreground [&_a]:underline [&_a]:underline-offset-4 hover:[&_a]:text-primary'>
            By clicking continue, you agree to our{' '}
            <a href='#'>Terms of Service</a> and <a href='#'>Privacy Policy</a>.
          </div>
        </div>
      </div>
    </div>
  );
};

export default Page;
