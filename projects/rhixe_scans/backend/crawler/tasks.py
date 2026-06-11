import time

from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.users.models import User
from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder
from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task(bind=True, name="Get Users Count")
def get_users_count(self, seconds):
    """A pointless Celery task to demonstrate usage."""
    logger.info("A pointless Celery task to demonstrate usage.")
    progress_recorder = ProgressRecorder(self)
    for i in range(seconds):
        time.sleep(1)

        progress_recorder.set_progress(
            i + 1,
            seconds,
            description="Get Users Count description",
        )
    return {
        "users": User.objects.all(),
        "users_count": User.objects.count(),
    }


@shared_task(bind=True, name="Get Comics Count")
def get_comics_count(self, seconds):
    """A pointless Celery task to demonstrate usage."""
    logger.info("A pointless Celery task to demonstrate usage.")
    progress_recorder = ProgressRecorder(self)
    for i in range(seconds):
        time.sleep(1)

        progress_recorder.set_progress(
            i + 1,
            seconds,
            description="Get Comics Count description",
        )
    comics = (
        Comic.objects.prefetch_related(
            "comicitems",
            "comicchapters",
            "genres",
            "followers",
        )
        .select_related("author", "category", "artist", "user")
        .all()
    )
    comic_images = ComicImage.objects.select_related("comic").all()
    chapters = (
        Chapter.objects.prefetch_related("chapteritems").select_related("comic").all()
    )

    chapter_images = ChapterImage.objects.select_related("comic", "chapter").all()
    context = {
        "Comics": comics.values("title", "slug"),
        "Comics_Count": comics.count(),
        "ComicsImage": comic_images.values("image", "url", "comic"),
        "ComicsImage_Count": comic_images.count(),
        "Chapters": chapters.values("name", "slug", "numpages"),
        "Chapters_Count": chapters.count(),
        "ChaptersImage": chapter_images.values("image", "url", "chapter"),
        "ChaptersImage_Count": chapter_images.count(),
    }
    logger.info(context)
    return "Done "


@shared_task(bind=True, name="Crawl task")
def crawl_task(self, seconds):
    """A Celery task to Run Crawl Custom command crawl."""
    logger.info("A Celery task to Run Crawl Custom command crawl")
    call_command("crawls")
    progress_recorder = ProgressRecorder(self)

    for i in range(seconds):
        time.sleep(1)

        progress_recorder.set_progress(
            i + 1,
            seconds,
            description="Crawl task description",
        )

    comics = (
        Comic.objects.prefetch_related(
            "comicitems",
            "comicchapters",
            "genres",
            "followers",
        )
        .select_related("author", "category", "artist", "user")
        .all()
    )
    comic_images = ComicImage.objects.select_related("comic").all()
    chapters = (
        Chapter.objects.prefetch_related("chapteritems").select_related("comic").all()
    )

    chapter_images = ChapterImage.objects.select_related("comic", "chapter").all()
    return {
        "Comics": comics.values("title", "slug"),
        "Comics_Count": comics.count(),
        "ComicsImage": comic_images.values("image", "url", "comic"),
        "ComicsImage_Count": comic_images.count(),
        "Chapters": chapters.values("name", "slug", "numpages"),
        "Chapters_Count": chapters.count(),
        "ChaptersImage": chapter_images.values("image", "url", "chapter"),
        "ChaptersImage_Count": chapter_images.count(),
    }
