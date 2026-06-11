from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save

from api.apps.models import Chapter
from api.apps.models import ChapterImage
from api.apps.models import Comic
from api.apps.models import ComicImage
from api.apps.utils import delete_instance_image
from api.apps.utils import slugify_instance_name
from api.apps.utils import slugify_instance_title


def comic_pre_save(sender, instance, *args, **kwargs):

    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(comic_pre_save, sender=Comic)


def comic_post_save(sender, instance, created, *args, **kwargs):

    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(comic_post_save, sender=Comic)


def comic_image_pre_delete(sender, instance, *args, **kwargs):

    if instance.image:
        delete_instance_image(instance)


pre_delete.connect(comic_image_pre_delete, sender=ComicImage)


def chapter_pre_save(sender, instance, *args, **kwargs):

    if instance.slug is None:
        slugify_instance_name(instance, save=False)


pre_save.connect(chapter_pre_save, sender=Chapter)


def chapter_post_save(sender, instance, created, *args, **kwargs):

    if created:
        slugify_instance_name(instance, save=True)


post_save.connect(chapter_post_save, sender=Chapter)


def chapter_image_pre_delete(sender, instance, *args, **kwargs):

    if instance.image:
        delete_instance_image(instance)


pre_delete.connect(chapter_image_pre_delete, sender=ChapterImage)
