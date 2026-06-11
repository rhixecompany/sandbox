import json
import logging

from api.libary.models import Artist  # noqa: F401
from api.libary.models import Author  # noqa: F401
from api.libary.models import Category  # noqa: F401
from api.libary.models import Chapter
from api.libary.models import ChapterImage  # noqa: F401
from api.libary.models import Comic  # noqa: F401
from api.libary.models import ComicImage  # noqa: F401
from api.libary.models import Genre  # noqa: F401
from django.conf import settings
from django.contrib.auth import get_user_model  # noqa: F401
from django.core.management.base import BaseCommand
from django.db.models import Q  # noqa: F401

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):
        def save_chapters(chapters_data):
            for item in chapters_data:
                images = item.get("images")
                comicslug = item["comicslug"]  # noqa: F841
                comictitle = item["comictitle"]
                name = item["chaptername"]
                title = item.get("chaptertitle", "")
                slug = item["chapterslug"]
                link = item["url"]  # noqa: F841
                spider = item["spider"]  # noqa: F841
                updated_at = item.get("updated_at")  # noqa: F841
                numimages = len(images)  # noqa: F841
                if (
                    comictitle == "The Indomitable Martial King"
                    or comictitle.lower() == "The Indomitable Martial King"
                ):
                    chapter = Chapter.objects.get_search(  # type: ignore  # noqa: PGH003
                        slug,
                    )
                    if chapter.exists():
                        msg3 = f"{chapter.first().chapter_id} - {chapter.first().slug} - {chapter.first().comic.title} Exists"  # type: ignore  # noqa: E501, PGH003
                        logger.error(
                            msg3,
                        )
                    else:
                        logger.info(name)

        base = settings.BASE_DIR
        # comics_file = str(base / "comics.json")  # noqa: ERA001
        # with open(comics_file, encoding="utf-8") as comic_file:  # noqa: E501, PTH123, RUF100
        #     comics_data = json.load(comic_file)  # noqa: ERA001
        #     save_comics(comics_data=comics_data)  # noqa: ERA001
        chapters_file = str(base / "chapters.json")
        with open(chapters_file, encoding="utf-8") as chapter_file:  # noqa: PTH123
            chapters_data = json.load(chapter_file)
            save_chapters(chapters_data=chapters_data)
