import uuid
from typing import ClassVar

from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import UUIDField

# from django.db.models import Q  # noqa: ERA001
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from api.libary.constants import ComicStatus
from api.libary.constants import ImageStatus
from api.libary.managers import ActiveManager
from api.libary.managers import StandardMetadata
from api.users.models import User

ext_validator = FileExtensionValidator(
    [
        "ico",
        "jpg",
        "svg",
        "jpeg",
        "png",
        "gif",
        "bmp",
        "webp",
        "tiff",
        "ttf",
        "eot",
        "woff",
        "woff2",
    ],
)


def chapter_image_location(instance, filename):
    return "{}/{}/{}".format(
        str(instance.comic.slug)
        .replace(" ", "_")
        .replace(":", " ")
        .replace("/", "")
        .replace("\\", ""),
        instance.chapter.slug,
        filename,
    )


def comic_image_location(instance, filename):
    return "{}/{}".format(
        str(instance.comic.slug)
        .replace(" ", "_")
        .replace(":", " ")
        .replace("/", "")
        .replace("\\", ""),
        filename,
    )


class Genre(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Genres"
        verbose_name = "Genre"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.genrecomics.all()  # type: ignore  # noqa: PGH003


class Author(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.authorcomics.all()  # type: ignore  # noqa: PGH003


class Artist(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Artists"
        verbose_name = "Artist"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.artistcomics.all()  # type: ignore  # noqa: PGH003


class Category(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.categorycomics.all()  # type: ignore  # noqa: PGH003


class Website(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Websites"
        verbose_name = "Website"

    def __str__(self):
        return self.name

    def get_spider_comics_children(self):
        return self.websitecomics.all()  # type: ignore  # noqa: PGH003

    def get_spider_chapters_children(self):
        return self.websitechapters.all()  # type: ignore  # noqa: PGH003


class Comic(StandardMetadata):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=5000, unique=True)
    slug = models.SlugField(_("Slug"), max_length=5000, blank=True, unique=True)
    description = CKEditor5Field("Description", config_name="extends")
    status = models.CharField(_("Status"), max_length=15, choices=ComicStatus.choices)
    rating = models.DecimalField(_("Rating"), max_digits=10, decimal_places=1)
    updated_at = models.DateTimeField(
        _("Updated At"),
    )
    link = models.URLField(
        default="",
    )
    numchapters = models.PositiveSmallIntegerField(
        _("Total Chapters"),
        null=True,
        blank=True,
    )
    numimages = models.PositiveSmallIntegerField(
        _("Total Images"),
        null=True,
        blank=True,
    )
    serialization = models.CharField(  # noqa: DJ001
        _("Serialization"),
        max_length=5000,
        blank=True,
        null=True,
    )
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE,
        related_name="websitecomics",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categorycomics",
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="authorcomics",
        null=True,
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="artistcomics",
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usercomic",
        null=True,
        blank=True,
    )
    genres = models.ManyToManyField(
        Genre,
        blank=True,
        related_name="genrecomics",
    )
    users = models.ManyToManyField(
        User,
        through="UserComic",
        blank=True,
    )

    objects: ClassVar[ActiveManager] = ActiveManager()

    class Meta:
        verbose_name_plural = "Comics"
        verbose_name = "Comic"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        """Get URL for comic's detail view.

        Returns:
            str: URL for comic detail.

        """
        return reverse("comics:detail", kwargs={"slug": self.slug})

    @property
    def has_chapters(self):
        return self.numchapters > 0

    @property
    def has_images(self):
        return self.numimages > 1

    def get_images(self):
        return self.comicimages.all()  # type: ignore  # noqa: PGH003

    def get_chapters(self):
        return self.comicchapters.all()  # type: ignore  # noqa: PGH003

    def get_comments(self):
        return self.comiccomments.all()  # type: ignore  # noqa: PGH003

    def get_users(self):
        return self.comicusers.all()  # type: ignore  # noqa: PGH003


class Chapter(StandardMetadata):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    website = models.ForeignKey(
        Website,
        on_delete=models.CASCADE,
        related_name="websitechapters",
        null=True,
        blank=True,
    )
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicchapters",
    )
    name = models.CharField(_("Name"), max_length=500)
    slug = models.SlugField(
        _("Slug"),
        max_length=5000,
        unique=True,
        blank=True,
    )
    title = models.CharField(_("Title"), max_length=5000, blank=True)
    updated_at = models.DateTimeField(
        _("Updated At"),
    )
    link = models.URLField(
        default="",
    )
    numimages = models.PositiveSmallIntegerField(
        _("Total Images"),
        null=True,
        blank=True,
    )

    objects: ClassVar[ActiveManager] = ActiveManager()

    class Meta:
        verbose_name_plural = "Chapters"
        verbose_name = "Chapter"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        """Get URL for chapter's detail view.

        Returns:
            str: URL for chapter detail.

        """
        return reverse("chapters:detail", kwargs={"slug": self.slug})

    @property
    def has_images(self):
        return self.numimages > 0

    def get_images(self):
        return self.chapterimages.all()  # type: ignore  # noqa: PGH003

    def get_comments(self):
        return self.chaptercomments.all()  # type: ignore  # noqa: PGH003


class UserComic(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercomics")
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicusers",
    )

    class Meta:
        verbose_name_plural = "UserComics"
        verbose_name = "UserComic"

    def __str__(self):
        return f"{self.user.email} - {self.comic.title}"


class ComicImage(StandardMetadata):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(
        default="",
    )
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicimages",
    )
    image = models.ImageField(
        upload_to=comic_image_location,
        validators=[
            ext_validator,
        ],
        blank=True,
        null=True,
    )
    status = models.CharField(  # noqa: DJ001
        max_length=13,
        choices=ImageStatus.choices,
        blank=True,
        null=True,
    )
    checksum = models.CharField(max_length=500, blank=True, null=True)  # noqa: DJ001
    objects: ClassVar[ActiveManager] = ActiveManager()

    class Meta:
        verbose_name_plural = "ComicImages"
        verbose_name = "ComicImage"

    def __str__(self):
        return f"{self.link}"

    def get_absolute_url(self) -> str:
        """Get URL for comicimage's detail view.

        Returns:
            str: URL for comicimage detail.

        """
        return reverse("comicimages:detail", kwargs={"id": self.pk})


class ChapterImage(StandardMetadata):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(
        default="",
    )
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="chapterimages",
    )
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicchapterimages",
    )
    image = models.ImageField(
        upload_to=chapter_image_location,
        validators=[
            ext_validator,
        ],
        blank=True,
        null=True,
    )
    status = models.CharField(  # noqa: DJ001
        max_length=13,
        choices=ImageStatus.choices,
        blank=True,
        null=True,
    )
    checksum = models.CharField(max_length=500, blank=True, null=True)  # noqa: DJ001
    objects: ClassVar[ActiveManager] = ActiveManager()

    class Meta:
        verbose_name_plural = "ChapterImages"
        verbose_name = "ChapterImage"

    def __str__(self):
        return f"{self.link}"

    def get_absolute_url(self) -> str:
        """Get URL for chapterimage's detail view.

        Returns:
            str: URL for chapterimage detail.

        """
        return reverse("chapterimages:detail", kwargs={"id": self.pk})


class Comment(StandardMetadata):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = CKEditor5Field("Text", config_name="extends")
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="chaptercomments",
        blank=True,
        null=True,
    )
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comiccomments",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usercomments",
    )
    objects: ClassVar[ActiveManager] = ActiveManager()

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"

    def __str__(self):
        return self.text

    def get_chapter_children(self):
        return self.chaptercomments.all()  # type: ignore  # noqa: PGH003

    def get_comic_children(self):
        return self.comiccomments.all()  # type: ignore  # noqa: PGH003
