from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.
    """

    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _("Updated"),
        auto_now=True,
    )
    is_deleted = models.BooleanField(_("Is deleted"), default=False, db_index=True)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()


class QuerySet(models.QuerySet):
    def comic_query_search(self, titlequery: str | None, slugquery: str | None):
        if titlequery is None or titlequery == "":
            return self.none()
        if slugquery is None or slugquery == "":
            return self.none()
        lookups = Q(title__exact=titlequery) | Q(slug__exact=slugquery)
        return self.filter(lookups)

    def chapter_query_search(self, slugquery: str | None):
        if slugquery is None or slugquery == "":
            return self.none()
        lookups = Q(slug__exact=slugquery)
        return self.filter(lookups)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).filter(is_deleted=False)

    def get_comic_search(self, titlequery: str | None, slugquery: str | None):
        return self.get_queryset().comic_query_search(
            titlequery=titlequery,
            slugquery=slugquery,
        )

    def get_chapter_search(self, slugquery: str | None):
        return self.get_queryset().chapter_query_search(
            slugquery=slugquery,
        )
