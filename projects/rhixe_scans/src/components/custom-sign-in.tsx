import { signIn } from '@/auth';
import { Button } from '@/components/ui/button';
import { LucideIcon } from 'lucide-react';

interface CustomSignInProps {
  text: string;
  provider: string;
  icon: React.ReactElement<LucideIcon>;
}

const CustomSignIn = ({ text, provider, icon }: CustomSignInProps) => {
  return (
    <form
      action={async () => {
        'use server';
        await signIn(`${provider}`);
      }}
    >
      <Button className='w-full' variant='outline'>
        {icon}

        <span className='sr-only'>{text}</span>
      </Button>
    </form>
  );
};

export { CustomSignIn };
