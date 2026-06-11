import { Input } from '@/components/ui/input';
import { Search, X } from 'lucide-react';
// import {
//   Select,
//   SelectContent,
//   SelectItem,
//   SelectTrigger,
//   SelectValue,
// } from '@/components/ui/select';
// import { getAllCategories } from '@/lib/actions/comic.actions';

const SearchMobile = async () => {
  // const categories = await getAllCategories();

  return (
    <>
      <div id='searchform' className='flex-1 hidden'>
        <div className='relative'>
          <Search className='absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-white/70' />
          <Input
            name='q'
            type='text'
            className='flex h-10 rounded-md border-input px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50 w-full border-0 bg-purple-800/50 pl-9 text-white placeholder:text-white/70 focus-visible:ring-1 focus-visible:ring-purple-400'
            placeholder='Search comics...'
          />
        </div>
      </div>
      <button className='hidden items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 w-10 text-white hover:bg-purple-800/50'>
        <X className='h-5 w-5' />
      </button>
      <button className='inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 w-10 text-white hover:bg-purple-800/50'>
        <Search className='h-5 w-5' />
      </button>
    </>
  );
};

export default SearchMobile;
