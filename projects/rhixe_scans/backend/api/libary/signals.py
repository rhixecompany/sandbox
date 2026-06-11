# from django.core.cache import cache  # noqa: ERA001
# from django.db.models.signals import post_delete  # noqa: ERA001
# import logging  # noqa: ERA001

from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save

# from django.dispatch import receiver  # noqa: ERA001
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from app.api.libary.signals_helpers import delete_instance_image
from app.api.libary.signals_helpers import slugify_instance_name
from app.api.libary.signals_helpers import slugify_instance_title

# logger = logging.getLogger(__name__)  # noqa: ERA001

# @receiver([post_save, post_delete], sender=Comic)
# def invalidate_comic_cache(sender, instance, **kwargs):
#     """
#     Invalidate comic list caches when a comic is created, updated, or deleted
#     """
#     logger.info("Clearing comic cache")  # noqa: ERA001

#     # Clear comic list caches
#     cache.delete_pattern("*comic_list*")  # type: ignore  # noqa: ERA001, PGH003


# @receiver([post_save, post_delete], sender=Chapter)
# def invalidate_chapter_cache(sender, instance, **kwargs):
#     """
#     Invalidate chapter list caches when a chapter is created, updated, or deleted
#     """
#     logger.info("Clearing chapter cache")  # noqa: ERA001

#     # Clear chapter list caches
#     cache.delete_pattern("*chapter_list*")  # type: ignore  # noqa: ERA001, PGH003


# @receiver([post_save, post_delete], sender=ComicImage)
# def invalidate_comic_image_cache(sender, instance, **kwargs):
#     """
#     Invalidate comic_image list caches when a comic_image is created, updated, or deleted  # noqa: E501
#     """
#     logger.info("Clearing comic_image cache")  # noqa: ERA001

#     # Clear comic_image list caches
#     cache.delete_pattern("*comic_image_list*")  # type: ignore  # noqa: ERA001, PGH003


# @receiver([post_save, post_delete], sender=ChapterImage)
# def invalidate_chapter_image_cache(sender, instance, **kwargs):
#     """
#     Invalidate chapter_image list caches when a chapter_image is created, updated, or deleted  # noqa: E501
#     """
#     logger.info("Clearing chapter_image cache")  # noqa: ERA001

#     # Clear chapter_image list caches
#     cache.delete_pattern("*chapter_image_list*")  # type: ignore  # noqa: E501, ERA001, PGH003


def comic_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(comic_pre_save, sender=Comic, dispatch_uid="comic_pre_save")


def comic_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(comic_post_save, sender=Comic, dispatch_uid="comic_post_save")


def comic_image_pre_delete(sender, instance, *args, **kwargs):
    if instance.image:
        delete_instance_image(instance)


pre_delete.connect(
    comic_image_pre_delete,
    sender=ComicImage,
    dispatch_uid="comic_image_pre_save",
)


def chapter_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_name(instance, save=False)


pre_save.connect(chapter_pre_save, sender=Chapter, dispatch_uid="chapter_pre_save")


def chapter_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_name(instance, save=True)


post_save.connect(chapter_post_save, sender=Chapter, dispatch_uid="chapter_post_save")


def chapter_image_pre_delete(sender, instance, *args, **kwargs):
    if instance.image:
        delete_instance_image(instance)


pre_delete.connect(
    chapter_image_pre_delete,
    sender=ChapterImage,
    dispatch_uid="chapter_image_pre_save",
)
