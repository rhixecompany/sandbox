from api.apps.models import Chapter, ChapterImage, Comic, ComicImage
from api.apps.utils import delete_instance_image, slugify_instance_name, slugify_instance_title
from django.db.models.signals import post_save, pre_delete, pre_save


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
