import random

from django.utils.text import slugify


def slugify_instance_title(instance, save=False, new_slug=None):  # noqa: FBT002
    slug = new_slug if new_slug is not None else slugify(instance.title)
    Klass = instance.__class__  # noqa: N806
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)  # noqa: S311
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def slugify_instance_name(instance, save=False, new_slug=None):  # noqa: FBT002
    if new_slug is not None:
        slug = new_slug
    else:
        comictitle = instance.comic.title
        chaptername = instance.name
        new_name = f"{comictitle} {chaptername}"
        slug = slugify(new_name)
    Klass = instance.__class__  # noqa: N806
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        # auto generate new slug
        rand_int = random.randint(300_000, 500_000)  # noqa: S311
        slug = f"{slug}-{rand_int}"
        return slugify_instance_name(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def delete_instance_image(instance):
    file = instance.image
    print(f"Removing {file}")  # noqa: T201
    file.delete()
    return instance
