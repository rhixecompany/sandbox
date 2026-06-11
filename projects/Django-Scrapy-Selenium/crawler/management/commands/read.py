import json
import logging

from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates transactions for testing"

    def handle(self, *args, **options):
        def read_json():
            base = settings.BASE_DIR
            comics_file = str(base / "comics.json")
            with open(comics_file) as comic_file:  # noqa: PTH123
                comics_data = json.load(comic_file)
                comics = []
                for item in comics_data:
                    comics.append(item)  # noqa: PERF402
            context = {
                "comics": comics[0:1],
                "comicscount": len(comics),
            }
            logger.info(
                context,
            )
            chapters_file = str(base / "chapters.json")
            with open(chapters_file) as chapter_file:  # noqa: PTH123
                chapters_data = json.load(chapter_file)
                chapters = []
                for citem in chapters_data:
                    chapters.append(citem)  # noqa: PERF402
            context1 = {
                "chapters": chapters[0:1],
                "chapterscount": len(chapters),
            }
            logger.info(
                context1,
            )

        read_json()
