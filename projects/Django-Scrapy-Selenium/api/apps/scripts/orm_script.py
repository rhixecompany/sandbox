from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import now

from api.apps.models import Comic


def run():
    mdate = now() - timedelta(weeks=8)
    wdate = now() - timedelta(weeks=4)
    ydate = now() - timedelta(weeks=48)
    mon = (
        Comic.objects.get_feat()  # type: ignore  # noqa: PGH003
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=mdate))
    )
    week = (
        Comic.objects.get_feat()  # type: ignore  # noqa: PGH003
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=wdate))
    )
    allc = (
        Comic.objects.get_feat()  # type: ignore  # noqa: PGH003
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=ydate))
    )
    top = (
        Comic.objects.get_top()  # type: ignore  # noqa: PGH003
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(rating__gte=9.9) | Q(rating__lte=9.8))
    )
    feat = (
        Comic.objects.get_feat()  # type: ignore  # noqa: PGH003
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(rating__gte=9.9) | Q(rating__lte=9.8))
    )
    context = {
        "topcomics": top[0:7],
        "featcomics": feat[0:5],
        "moncomics": mon[0:10],
        "weekcomics": week[0:10],
        "allcomics": allc[0:10],
    }
    context1 = {
        "data": context,
        "topcomics_count": top.count(),
        "featcomics_count": feat.count(),
        "moncomics_count": mon.count(),
        "weekcomics_count": week.count(),
        "allcomics_count": allc.count(),
    }
    print(context1)  # noqa: T201
