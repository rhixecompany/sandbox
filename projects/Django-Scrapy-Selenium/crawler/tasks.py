import time

from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder
from django.core.management import call_command

from api.apps.models import Comic

logger = get_task_logger(__name__)


@shared_task(bind=True, name="My task")
def my_task(self, seconds):
    call_command("crawls")
    logger.info("Done   Downloading")
    progress_recorder = ProgressRecorder(self)

    for i in range(seconds):
        time.sleep(1)

        progress_recorder.set_progress(
            i + 1,
            seconds,
            description="my progress description",
        )

    return Comic.objects.all().count()
