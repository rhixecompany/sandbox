import json
import logging

from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Genre
from api.libary.serializers import ArtistSerializer
from api.libary.serializers import AuthorSerializer
from api.libary.serializers import CategorySerializer
from api.libary.serializers import ChapterImageSerializer
from api.libary.serializers import ChaptersInfoSerializer
from api.libary.serializers import ComicImageSerializer
from api.libary.serializers import ComicsInfoSerializer
from api.libary.serializers import GenreSerializer
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):  # noqa: PLR0915
        def save_comics():
            # save the data to a JSON file
            base = settings.BASE_DIR
            comic_file = base / "comic.json"
            genre_file = base / "genre.json"
            author_file = base / "author.json"
            artist_file = base / "artist.json"
            category_file = base / "category.json"
            comicimage_file = base / "comicimage.json"

            genres = Genre.objects.all()
            genreserializer = GenreSerializer(genres, many=True)
            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(genre_file, "w") as json_file:  # noqa: PTH123
                json.dump(genreserializer.data, json_file)
                logger.info("Genre JSON created successfully")
            categorys = Category.objects.all()
            categoryserializer = CategorySerializer(categorys, many=True)
            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(category_file, "w") as json_file:  # noqa: PTH123
                json.dump(categoryserializer.data, json_file)
                logger.info("Category JSON created successfully")
            authors = Author.objects.all()
            authorserializer = AuthorSerializer(authors, many=True)
            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(author_file, "w") as json_file:  # noqa: PTH123
                json.dump(authorserializer.data, json_file)
                logger.info("Author JSON created successfully")
            artists = Artist.objects.all()
            artistserializer = ArtistSerializer(artists, many=True)
            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(artist_file, "w") as json_file:  # noqa: PTH123
                json.dump(artistserializer.data, json_file)
                logger.info("Artist JSON created successfully")

            comics = Comic.objects.all()
            comicserializer = ComicsInfoSerializer(comics, many=True)

            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(comic_file, "w") as json_file:  # noqa: PTH123
                json.dump(comicserializer.data, json_file)
                logger.info("Comic JSON created successfully")

            comicimages = ComicImage.objects.all()
            comicimageserializer = ComicImageSerializer(comicimages, many=True)

            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(comicimage_file, "w") as json_file:  # noqa: PTH123
                json.dump(comicimageserializer.data, json_file)
                logger.info("Comic Image JSON created successfully")

        def save_chapters():
            # save the data to a JSON file
            base = settings.BASE_DIR
            chapter_file = base / "chapter.json"
            chapterimage_file = base / "chapterimage.json"

            chapters = Chapter.objects.all()

            chapterserializer = ChaptersInfoSerializer(chapters, many=True)

            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(chapter_file, "w") as json_file:  # noqa: PTH123
                json.dump(chapterserializer.data, json_file)
                logger.info("Chapter JSON created successfully")
            chapterimages = ChapterImage.objects.all()
            chapterimageserializer = ChapterImageSerializer(chapterimages, many=True)

            # Open the JSON file in write mode and dump the Python list to the JSON file
            with open(chapterimage_file, "w") as json_file:  # noqa: PTH123
                json.dump(chapterimageserializer.data, json_file)
                logger.info("Chapterimage JSON created successfully")

        def load():

            save_comics()

            save_chapters()

        def main():
            load()

        main()
