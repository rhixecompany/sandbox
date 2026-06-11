import json
import logging

from api.libary.models import Chapter
from api.libary.models import Comic
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Q

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generates comics for apps"

    def handle(self, *args, **options):
        def save_comics(comics_data):
            alltitle = [comic.get("title") for comic in comics_data]
            newcomics = []
            for item in comics_data:
                title = item["title"]
                if Comic.objects.filter(
                    Q(title__in=alltitle),
                ) and not Comic.objects.filter(Q(title__iexact=title)):
                    newcomics.append(item)
                else:
                    msg = f"{title} Doesn`t Exists"
                    logger.error(msg)

            return newcomics

        def load():
            base = settings.BASE_DIR
            comics_file = str(base / "comicsdata1.json")

            with open(comics_file, encoding="utf-8") as comic_file:  # noqa: PTH123
                comics_data = json.load(comic_file)
                comics = save_comics(comics_data=comics_data)
                logger.info({"comics": comics})

        load()
