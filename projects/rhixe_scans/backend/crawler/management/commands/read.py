import json
import logging

from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):
        def save_comics(comics_data):
            for item in comics_data:
                images = item.get("images")
                title = item["title"]
                slug = item["slug"]
                description = item.get("description")
                rating = item["rating"]
                status = item["status"]
                url = item["url"]
                spider = item["spider"]
                updated_at = item["updated_at"]
                numchapters = item["numchapters"]
                numitems = len(images)
                serialization = item["serialization"]
                ca = item.get("type")
                author = item.get("author")
                artist = item.get("artist")
                genres = item.get("genres")
                comic_data = {
                    "images": images,
                    "title": title,
                    "slug": slug,
                    "description": description,
                    "rating": rating,
                    "status": status,
                    "url": url,
                    "spider": spider,
                    "updated_at": updated_at,
                    "numchapters": numchapters,
                    "numitems": numitems,
                    "serialization": serialization,
                    "category": ca,
                    "author": author,
                    "artist": artist,
                    "genres": genres,
                }
                logger.info(comic_data)

        def save_chapters(chapters_data):
            for item in chapters_data[0:10]:
                chapterimages = item.get("images")
                comicslug = item["comicslug"]
                comictitle = item["comictitle"]
                name = item["chaptername"]
                title = item.get("chaptertitle", "")
                slug = item["chapterslug"]
                url = item["url"]
                spider = item["spider"]
                updated_at = item.get("updated_at")
                numpages = len(chapterimages)
                if chapterimages:
                    chapter_data = {
                        "images": chapterimages,
                        "title": title,
                        "slug": slug,
                        "name": name,
                        "url": url,
                        "spider": spider,
                        "updated_at": updated_at,
                        "numpages": numpages,
                        "comic_title": comictitle,
                        "comic_slug": comicslug,
                    }
                    logger.info(chapter_data)

        base = settings.BASE_DIR
        comics_file = str(base / "comics.json")
        with open(comics_file, encoding="utf-8") as comic_file:  # noqa: PTH123
            comics_data = json.load(comic_file)
            save_comics(comics_data=comics_data)
        chapters_file = str(base / "chapters.json")
        with open(chapters_file, encoding="utf-8") as chapter_file:  # noqa: PTH123
            chapters_data = json.load(chapter_file)
            save_chapters(chapters_data=chapters_data)
