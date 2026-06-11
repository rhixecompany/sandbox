import csv
import logging

from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Genre
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):  # noqa: C901, PLR0915
        def save_comics():  # noqa: PLR0915
            # save the data to a CSV file
            base = settings.BASE_DIR
            comic_file = str(base / "comic_data.csv")
            genre_file = str(base / "genre_data.csv")
            author_file = str(base / "author_data.csv")
            artist_file = str(base / "artist_data.csv")
            category_file = str(base / "category_data.csv")
            comic_image_file = str(base / "comic_image_data.csv")
            genres_data = Genre.objects.all().values("name")
            genrekeys = genres_data[0].keys()
            authors_data = Author.objects.all().values("name")
            authorkeys = authors_data[0].keys()
            artists_data = Artist.objects.all().values("name")
            artistkeys = artists_data[0].keys()
            categorys_data = Category.objects.all().values("name")
            categorykeys = categorys_data[0].keys()
            mycomics_data = []
            comics = Comic.objects.all()

            mycomicimages_data = []
            comicimages = ComicImage.objects.all()

            for comic in comics:
                if comic.genres.all().count() == 0:
                    item = {
                        "user_id": "ce9d78e6-dcc1-4850-b6a9-5814f821482d",
                        "title": comic.title,
                        "slug": comic.slug,
                        "description": comic.description,
                        "rating": comic.rating,
                        "numchapters": comic.numchapters,
                        "numimages": comic.numimages,
                        "updated_at": comic.updated_at,
                        "serialization": comic.serialization,
                        "status": comic.status,
                        "link": comic.link,
                        "category": comic.category.name,
                        "author": comic.author.name,
                        "artist": comic.artist.name,
                        "genres": ["_"],
                    }
                else:

                    item = {
                        "user_id": "ce9d78e6-dcc1-4850-b6a9-5814f821482d",
                        "title": comic.title,
                        "slug": comic.slug,
                        "description": comic.description,
                        "rating": comic.rating,
                        "numchapters": comic.numchapters,
                        "numimages": comic.numimages,
                        "updated_at": comic.updated_at,
                        "serialization": comic.serialization,
                        "status": comic.status,
                        "link": comic.link,
                        "category": comic.category.name,
                        "author": comic.author.name,
                        "artist": comic.artist.name,
                        "genres": [genre.name for genre in comic.genres.all()],
                    }

                mycomics_data.append(item)

            for comicimage in comicimages:

                item = {
                    "image": comicimage.image.url,
                    "status": comicimage.status,
                    "checksum": comicimage.checksum,
                    "link": comicimage.link,
                    "comic": comicimage.comic.slug,
                }

                mycomicimages_data.append(item)

            comickeys = mycomics_data[0].keys()

            comicimagekeys = mycomicimages_data[0].keys()

            with open(  # noqa: PTH123
                genre_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=genrekeys)
                dict_writer.writeheader()
                dict_writer.writerows(genres_data)
                logger.info("Genre CSV created successfully")
            with open(  # noqa: PTH123
                artist_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=artistkeys)
                dict_writer.writeheader()
                dict_writer.writerows(artists_data)
                logger.info("Artist CSV created successfully")
            with open(  # noqa: PTH123
                author_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=authorkeys)
                dict_writer.writeheader()
                dict_writer.writerows(authors_data)
                logger.info("Author CSV created successfully")
            with open(  # noqa: PTH123
                category_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=categorykeys)
                dict_writer.writeheader()
                dict_writer.writerows(categorys_data)
                logger.info("Category CSV created successfully")
            with open(  # noqa: PTH123
                comic_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=comickeys)
                dict_writer.writeheader()
                for row in mycomics_data:

                    dict_writer.writerow(row)
                logger.info("Comic CSV created successfully")
            with open(  # noqa: PTH123
                comic_image_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=comicimagekeys)
                dict_writer.writeheader()
                dict_writer.writerows(mycomicimages_data)
                logger.info("Comic image CSV created successfully")

        def save_chapters():
            # save the data to a CSV file
            base = settings.BASE_DIR
            chapter_file = str(base / "chapter_data.csv")
            chapter_image_file = str(base / "chapter_image_data.csv")
            mychapters_data = []
            chapters = Chapter.objects.all()
            mychapterimages_data = []
            chapterimages = ChapterImage.objects.all()
            for chapter in chapters:

                item = {
                    "name": chapter.name,
                    "title": chapter.title,
                    "slug": chapter.slug,
                    "numimages": chapter.numimages,
                    "updated_at": chapter.updated_at,
                    "link": chapter.link,
                    "comic": chapter.comic.slug,
                }

                mychapters_data.append(item)
            chapterkeys = mychapters_data[0].keys()

            for chapterimage in chapterimages:
                if chapterimage.image:
                    item = {
                        "image": chapterimage.image.url,
                        "checksum": chapterimage.checksum,
                        "status": chapterimage.status,
                        "link": chapterimage.link,
                        "chapter": chapterimage.chapter.slug,
                        "comic": chapterimage.comic.slug,
                    }
                else:
                    item = {
                        "image": "",
                        "checksum": "",
                        "status": "",
                        "link": chapterimage.link,
                        "chapter": chapterimage.chapter.slug,
                        "comic": chapterimage.comic.slug,
                    }

                mychapterimages_data.append(item)
            chapterimagekeys = mychapterimages_data[0].keys()

            with open(  # noqa: PTH123
                chapter_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=chapterkeys)
                dict_writer.writeheader()
                dict_writer.writerows(mychapters_data)
                logger.info("CSV created successfully")
            with open(  # noqa: PTH123
                chapter_image_file,
                "w",
                newline="",
                encoding="utf-8",
            ) as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=chapterimagekeys)
                dict_writer.writeheader()
                dict_writer.writerows(mychapterimages_data)
                logger.info("CSV created successfully")

        def load():

            save_comics()

            save_chapters()

        def main():
            load()

        main()
