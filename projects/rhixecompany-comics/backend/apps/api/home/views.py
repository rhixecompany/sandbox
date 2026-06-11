from django.conf import settings
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from api.apps.filters import SearchFilter
from api.apps.models import Comic


def index(request):
    queryset = (
        Comic.objects.prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .all()
    )
    paginator = Paginator(queryset, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    top = (
        Comic.objects.get_top()
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(rating__gte=10) | Q(rating__lte=9.9))
    )
    feat = (
        Comic.objects.get_feat()
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
        "comics": page_obj,
        "topcomics": top[0:7],
        "featcomics": feat[0:5],
    }
    if request.htmx:
        return render(request, "partials/home/index/container.html", context)
    return render(request, "home/index.html", context)


def comics(request):
    title = request.GET.get("title")
    types = request.GET.getlist("type")
    status = request.GET.get("status")
    updated_at = request.GET.get("updated_at")
    genres = request.GET.getlist("genres")
    titleq = title if title is not None else ""
    statusq = status if status is not None else ""
    typesq = types if types is not None else ""
    genresq = genres if genres is not None else ""
    updated_atq = updated_at if updated_at is not None else ""
    if titleq:
        qs = (
            Comic.objects.search(query=titleq)
            .prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
        )
    elif statusq:
        qs = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .filter(Q(status__icontains=statusq))
        )
    elif typesq:
        qs = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .filter(Q(type__name__in=typesq))
        )
    elif genresq:
        qs = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .filter(Q(genres__name__in=genresq))
        )
    elif updated_atq:
        qs = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .all()
            .order_by(updated_atq)
        )
    else:
        qs = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .all()
        )
    comic_filter = SearchFilter(request.GET, queryset=qs)
    paginator = Paginator(qs, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)

    context = {
        "comics": page_obj,
        "filter": comic_filter,
    }
    if request.htmx:
        return render(request, "partials/home/series/container.html", context)
    return render(request, "home/series.html", context)


def digital(request):
    context = {}
    return render(request, "home/digital.html", context)


def privacy(request):
    context = {}
    return render(request, "home/privacy.html", context)


def terms(request):
    context = {}
    return render(request, "home/terms.html", context)
