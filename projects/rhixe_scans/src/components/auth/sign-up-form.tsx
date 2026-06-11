import { Apple } from '@/components/ui/apple';
import { Button } from '@/components/ui/button';
import { Github } from '@/components/ui/github';
import { Google } from '@/components/ui/google';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { signUp } from '@/lib/actions/user.actions';
import { redirect } from 'next/navigation';
import { CustomSignIn } from './custom-sign-in';
// import { signUp } from '@/lib/actions/user.actions';
const SignUpForm = () => {
  return (
    <>
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
    </>
  );
};

export default SignUpForm;
