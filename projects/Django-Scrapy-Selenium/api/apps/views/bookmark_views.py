from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.utils.timezone import timedelta
from django.views.decorators.http import require_http_methods
from django_htmx.http import trigger_client_event
from render_block import render_block_to_string

from api.apps.models import Comic
from api.apps.models import ComicStatus
from api.apps.models import UserItem
from api.apps.validators import get_max_order
from api.apps.validators import reorder
from api.users.decorators import user_function


@require_http_methods(["GET"])
@user_passes_test(user_function)
def bookmarks(request):
    comics = UserItem.objects.prefetch_related("comic").all()
    paginator = Paginator(comics, 2)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    monthly = Q(updated_at__gte=(now() - timedelta(days=31)).date()) & Q(
        status=ComicStatus.ONGOING  # noqa: COM812
    ) | Q(status=ComicStatus.SEASON_END)
    weekly = Q(updated_at__gte=(now() - timedelta(days=7)).date()) & Q(
        status=ComicStatus.ONGOING  # noqa: COM812
    ) | Q(status=ComicStatus.SEASON_END)

    monqueryset = (
        Comic.objects.prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(monthly)
        .order_by("-updated_at")[0:10]
    )
    weeklyqueryset = (
        Comic.objects.prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(weekly)
        .order_by("-updated_at")[0:10]
    )
    allqueryset = (
        Comic.objects.prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .all()
        .order_by("-updated_at")[0:10]
    )
    context = {
        "comics": page_obj,
        "moncomics": monqueryset,
        "weeklycomics": weeklyqueryset,
        "allcomics": allqueryset,
    }
    if request.htmx:
        html = render_block_to_string(
            "partials/bookmark/grid.html",
            "bookmarkcomics",
            context,  # type: ignore  # noqa: PGH003
        )
        return HttpResponse(html)
    return render(request, "bookmark/list.html", context)


@user_passes_test(user_function)
def load(request):
    queryset = UserItem.objects.prefetch_related("comic").all()

    context = {
        "items": queryset,
    }

    html = render_block_to_string("partials/bookmarks.html", "comicbookmark", context)  # type: ignore  # noqa: PGH003
    return HttpResponse(html)


@require_http_methods(["GET", "POST"])
@user_passes_test(user_function)
def add_bookmark(request):
    title = request.POST.get("comictitle")

    # add comic
    comic = Comic.objects.get_or_create(title__iexact=title)[0]

    if not UserItem.objects.filter(comic=comic, user=request.user).exists():
        UserItem.objects.create(
            comic=comic,
            user=request.user,
            order=get_max_order(request.user),
        )

    context = {"user": request.user, "comic": comic}
    if request.htmx:
        html = render_block_to_string(
            "partials/comic/bookmark.html",
            "comicbookmark",
            context,  # type: ignore  # noqa: PGH003
        )
        response = HttpResponse(html)

        return trigger_client_event(response, "comic_bookmark")
    return render(request, "partials/comic/bookmark.html", context)


@require_http_methods(["GET", "DELETE"])
@user_passes_test(user_function)
def delete_bookmark(request, comic_id):
    # remove the comic from the user's list
    UserItem.objects.get(comic=comic_id).delete()
    reorder(request.user)
    comic = Comic.objects.get(id=comic_id)

    context = {"user": request.user, "comic": comic}
    if request.htmx:
        html = render_block_to_string(
            "partials/comic/bookmark.html",
            "comicbookmark",
            context,  # type: ignore  # noqa: PGH003
        )
        response = HttpResponse(html)
        return trigger_client_event(response, "comic_bookmark")
    return render(request, "partials/comic/bookmark.html", context)


@require_http_methods(["POST", "GET"])
@user_passes_test(user_function)
def sort(request):
    comic_pks_order = request.POST.getlist("comic_order")
    comics = []
    updated_comics = []

    # fetch user's comics in advance (rather than once per loop)
    usercomics = UserItem.objects.prefetch_related("comic").filter(user=request.user)

    for idx, comic_pk in enumerate(comic_pks_order, start=1):
        # find instance w/ the correct PK
        usercomic = next(u for u in usercomics if u.comic.pk == int(comic_pk))

        # add changed movies only to an updated_comics list
        if usercomic.order != idx:
            usercomic.order = idx
            updated_comics.append(usercomic)

        comics.append(usercomic)

    # bulk_update changed UserComics's 'order' field
    UserItem.objects.bulk_update(updated_comics, ["order"])

    paginator = Paginator(comics, 20)
    page_number = len(comic_pks_order) / 20
    page_obj = paginator.get_page(page_number)
    context = {"comics": comics, "page_obj": page_obj}
    if request.htmx:
        html = render_block_to_string(
            "partials/bookmark/grid.html",
            "bookmarkcomics",
            context,  # type: ignore  # noqa: PGH003
        )
        return HttpResponse(html)
    return render(request, "bookmark/list.html", context)
