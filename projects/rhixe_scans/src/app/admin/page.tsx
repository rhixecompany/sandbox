// import DeleteDialog from '@/components/shared/delete-dialog';
// import Pagination from '@/components/shared/pagination';
import { Button } from '@/components/ui/button';
import {
  Table,
  // TableBody,
  // TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
// import { deleteComic, getAllComics } from '@/lib/actions/comic.actions';
// import { requireAdmin } from '@/lib/auth-guard';
// import { formatId } from '@/lib/utils';
import LoadingPage from '@/app/loading';
import Link from 'next/link';
import { Suspense } from 'react';

const AdmincomicsPage = async (props: {
  searchParams: Promise<{
    page: string;
    query: string;
    category: string;
  }>;
}) => {
  // await requireAdmin();

  const searchParams = await props.searchParams;

  const page = Number(searchParams.page) || 1;
  const searchText = searchParams.query || '';
  const category = searchParams.category || '';
  console.log({ page, category });

  // const comics = await getAllComics({
  //   query: searchText,
  //   page,
  //   category,
  // });

  return (
    <>
      <Suspense key={searchText + page} fallback={<LoadingPage />}>
        <div className='space-y-2'>
          <div className='flex-between'>
            <div className='flex items-center gap-3'>
              <h1 className='h2-bold'>comics</h1>
              {searchText && (
                <div>
                  Filtered by <i>&quot;{searchText}&quot;</i>{' '}
                  <Link href='/admin/comics'>
                    <Button variant='outline' size='sm'>
                      Remove Filter
                    </Button>
                  </Link>
                </div>
              )}
            </div>
            <Button asChild variant='default'>
              <Link href='/admin/comics/create'>Create comic</Link>
            </Button>
          </div>

          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>TITLE</TableHead>
                <TableHead className='text-right'>STATUS</TableHead>

                <TableHead>RATING</TableHead>
                <TableHead className='w-[100px]'>ACTIONS</TableHead>
              </TableRow>
            </TableHeader>
            {/* <TableBody>
          {comics.data.map((comic) => (
            <TableRow key={comic.id}>
              <TableCell>{formatId(comic.id)}</TableCell>
              <TableCell>{comic.title}</TableCell>

              <TableCell>{comic.status}</TableCell>

              <TableCell>{comic.rating}</TableCell>
              <TableCell className="flex gap-1">
                <Button asChild variant="outline" size="sm">
                  <Link href={`/admin/comics/${comic.id}`}>Edit</Link>
                </Button>
                <DeleteDialog id={comic.id} action={deleteComic} />
              </TableCell>
            </TableRow>
          ))}
        </TableBody> */}
          </Table>
          {/* {comics.totalPages > 1 && (
        <Pagination page={page} totalPages={comics.totalPages} />
      )} */}
        </div>
      </Suspense>
    </>
  );
};

export default AdmincomicsPage;
