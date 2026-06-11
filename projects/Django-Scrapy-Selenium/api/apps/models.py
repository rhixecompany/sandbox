# models.py
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()

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


def panel_location(instance, filename):
    return "{}/{}/{}".format(
        str(instance.comic.slug)
        .replace(" ", "_")
        .replace(":", " ")
        .replace("/", "")
        .replace("\\", ""),
        instance.chapter.slug,
        filename,
    )


def comic_location(instance, filename):
    return "{}/{}".format(
        str(instance.comic.slug)
        .replace(" ", "_")
        .replace(":", " ")
        .replace("/", "")
        .replace("\\", ""),
        filename,
    )


class ComicStatus(models.TextChoices):
    COMPLETED = "Completed"
    ONGOING = "Ongoing"
    HIATUS = "Hiatus"
    DROPPED = "Dropped"
    SEASON_END = "Season End"
    COMING_SOON = "Coming Soon"


class ComicQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query)
        return self.filter(lookups)

    def single_status(self):
        lookups = Q(status=ComicStatus.ONGOING)
        return self.filter(lookups)

    def multi_status(self):
        lookups = (
            Q(status=ComicStatus.ONGOING)
            | Q(status=ComicStatus.COMPLETED)
            | Q(status=ComicStatus.HIATUS)
            | Q(status=ComicStatus.SEASON_END)
        )
        return self.filter(lookups)


class ComicManager(models.Manager):
    def get_queryset(self):
        return ComicQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    def get_top(self):
        return self.get_queryset().single_status()

    def get_feat(self):
        return self.get_queryset().multi_status()


class ChapterQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(name__icontains=query) | Q(slug__icontains=query)
        return self.filter(lookups)


class ChapterManager(models.Manager):
    def get_queryset(self):
        return ChapterQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class TypeStatus(models.TextChoices):
    MANGA = "Manga"
    MANHWA = "Manhwa"
    MANHUA = "Manhua"


class Genre(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Genres"
        verbose_name = "Genre"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"

    def __str__(self):
        return self.name

    def get_author_comics_children(self):
        return self.comicauthor.all()  # type: ignore  # noqa: PGH003


class Artist(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Artists"
        verbose_name = "Artist"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.comicartist.all()  # type: ignore  # noqa: PGH003


class Type(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=6,
        choices=TypeStatus.choices,
    )

    class Meta:
        verbose_name_plural = "Types"
        verbose_name = "Type"

    def __str__(self):
        return self.name

    def get_comics_children(self):
        return self.comictype.all()  # type: ignore  # noqa: PGH003


class Comic(models.Model):
    uuid = models.UUIDField(_("Uuid"), default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=5000, unique=True)
    slug = models.SlugField(
        _("Slug"),
        max_length=5000,
        unique=True,
        blank=True,
        null=True,
    )
    description = models.TextField(_("Description"), blank=True)
    status = models.CharField(
        _("Status"),
        max_length=15,
        choices=ComicStatus.choices,
    )
    rating = models.DecimalField(_("Rating"), max_digits=10, decimal_places=1)
    serialization = models.CharField(
        _("Serialization"),
        max_length=5000,
        blank=True,
    )
    numchapters = models.PositiveIntegerField(
        _("Total Chapters"),
        blank=True,
        default=0,
    )
    spider = models.CharField(_("Spider"), max_length=500, blank=True)
    url = models.URLField(_("Url"), max_length=500, blank=True)
    numitems = models.PositiveSmallIntegerField(_("Total Items"), blank=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="comictype",
    )
    genres = models.ManyToManyField(Genre, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comicauthor",
    )
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comicartist",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="comicuser",
    )
    users = models.ManyToManyField(
        User,
        through="UserItem",
        blank=True,
    )

    objects = ComicManager()

    class Meta:
        verbose_name_plural = "Comics"
        verbose_name = "Comic"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("comics:comic_detail", kwargs={"slug": self.slug})

    def get_hx_url(self) -> str:
        return reverse("comics:hx_comic_detail", kwargs={"slug": self.slug})

    def get_edit_url(self) -> str:
        return reverse("comics:update_comic", kwargs={"slug": self.slug})

    def get_delete_url(self) -> str:
        return reverse("comics:delete_comic", kwargs={"slug": self.slug})

    def get_comic_images_children(self):
        return self.comicitems.all()  # type: ignore  # noqa: PGH003

    def get_chapters_children(self):
        return self.comicchapters.all()  # type: ignore  # noqa: PGH003

    def get_comments_children(self):
        return self.comiccomments.all()  # type: ignore  # noqa: PGH003


class ComicImage(models.Model):
    url = models.URLField(
        _("Url"),
        max_length=5000,
    )

    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicitems",
    )
    image = models.ImageField(
        _("Image"),
        upload_to=comic_location,
        validators=[
            ext_validator,
        ],
        max_length=5000,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_hx_edit_url(self):
        kwargs = {"parent_slug": self.comic.slug, "id": self.pk}
        return reverse("comics:hx_image_update", kwargs=kwargs)

    def get_delete_url(self):
        kwargs = {"parent_slug": self.comic.slug, "id": self.pk}
        return reverse("comics:delete_comic_image", kwargs=kwargs)


class UserItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="followers")
    order = models.PositiveSmallIntegerField(
        _("Order"),
    )

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "UserItems"
        verbose_name = "Useritem"

    def __str__(self):
        return (
            f"Order - {self.order} User - {self.user.email} Comic - {self.comic.title}"
        )


class Chapter(models.Model):
    uuid = models.UUIDField(_("Uuid"), default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=500)
    title = models.CharField(_("Title"), max_length=5000, blank=True)
    slug = models.SlugField(
        _("Slug"),
        max_length=5000,
        unique=True,
        blank=True,
        null=True,
    )
    spider = models.CharField(_("Spider"), max_length=500, blank=True)
    url = models.URLField(_("Url"), max_length=500, blank=True)
    updated_at = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    numpages = models.PositiveSmallIntegerField(_("Total Pages"), blank=True, default=0)
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name="comicchapters",
    )

    objects = ChapterManager()

    class Meta:
        verbose_name_plural = "Chapters"
        verbose_name = "Chapter"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("chapters:chapter_detail", kwargs={"slug": self.slug})

    def get_hx_url(self) -> str:
        return reverse("chapters:hx_chapter_detail", kwargs={"slug": self.slug})

    def get_edit_url(self) -> str:
        return reverse("chapters:update_chapter", kwargs={"slug": self.slug})

    def get_delete_url(self) -> str:
        return reverse("chapters:delete_chapter", kwargs={"slug": self.slug})

    def get_chapter_images_children(self):
        return self.chapteritems.all()  # type: ignore  # noqa: PGH003

    def get_comments_children(self):
        return self.chaptercomments.all()  # type: ignore  # noqa: PGH003

    def get_hx_comic_edit_url(self):
        kwargs = {"parent_slug": self.comic.slug, "id": self.pk}
        return reverse("comics:hx_chapter_update", kwargs=kwargs)

    def get_hx_comic_delete_url(self):
        kwargs = {"parent_slug": self.comic.slug, "id": self.pk}
        return reverse("comics:delete_comic_chapter", kwargs=kwargs)


class ChapterImage(models.Model):
    url = models.URLField(
        _("Url"),
        max_length=5000,
    )

    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="chapteritems",
    )
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    image = models.ImageField(
        _("Image"),
        upload_to=panel_location,
        validators=[ext_validator],
        max_length=5000,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_hx_edit_url(self):
        kwargs = {"parent_slug": self.chapter.slug, "id": self.pk}
        return reverse("chapters:hx_image_update", kwargs=kwargs)

    def get_delete_url(self):
        kwargs = {"parent_slug": self.chapter.slug, "id": self.pk}
        return reverse("chapters:delete_chapter_image", kwargs=kwargs)


class Comment(models.Model):
    text = RichTextUploadingField(
        "Text",
        null=True,
        config_name="default",
    )  # type: ignore  # noqa: PGH003
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="chaptercomments",
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
    timestamp = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
        ordering = ["-updated"]

    def __str__(self):
        return self.text

    def get_chapter_children(self):
        return self.chaptercomments.all()  # type: ignore  # noqa: PGH003

    def get_comic_children(self):
        return self.comiccomments.all()  # type: ignore  # noqa: PGH003
