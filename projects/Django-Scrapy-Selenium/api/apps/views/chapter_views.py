from django.conf import settings
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django_htmx.http import trigger_client_event
from django_htmx.middleware import HtmxDetails

from api.apps.filters import ChapterFilter
from api.apps.forms import ChapterForm
from api.apps.forms import ChapterImageForm
from api.apps.forms import CommentForm
from api.apps.models import Chapter
from api.apps.models import ChapterImage
from api.apps.models import Comic
from api.users.decorators import admin_only
from api.users.decorators import user_only


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@user_only
@admin_only
@require_http_methods(["GET"])
def chapter_list_view(
    request: HtmxHttpRequest,
) -> HttpResponse:
    qs = Chapter.objects.prefetch_related("chapteritems").select_related("comic").all()
    chapter_filter = ChapterFilter(request.GET, queryset=qs)
    paginator = Paginator(chapter_filter.qs, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)  # type: ignore  # noqa: PGH003
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    htmx_template_name = "partials/chapters/container.html"
    template_name = "chapters/chapter_list.html"
    context = {"filter": chapter_filter, "object_list": page_obj}
    if request.htmx:
        htmx_template_name += "#container-section"
        return render(request, htmx_template_name, context)
    return render(request, template_name, context)


@require_http_methods(["GET", "POST"])
def chapter_detail_hx_view(
    request: HtmxHttpRequest,
    slug=None,
) -> HttpResponse:
    # if not request.htmx:
    #     raise Http404
    try:
        obj = get_object_or_404(Chapter, slug=slug)
        chapter_type = obj.comic.type
        chapter_author = obj.comic.author
        chapter_artist = obj.comic.artist
        chapterlookups = (
            Q(type__name__iexact=chapter_type)
            | Q(author__name__iexact=chapter_author)
            | Q(artist__name__iexact=chapter_artist)
        )
        comics = (
            Comic.objects.prefetch_related(
                "comicitems",
                "genres",
                "followers",
                "comicchapters",
            )
            .select_related("user", "author", "type", "artist")
            .filter(chapterlookups)
            .distinct()[0:6]
        )
        comments = obj.get_comments_children()
        chapters = obj.comic.get_chapters_children()
        paginator = Paginator(chapters, 1)
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.page(page_number)  # type: ignore  # noqa: PGH003
        except PageNotAnInteger:
            page_obj = paginator.page(1)

        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        page_obj = paginator.get_page(page_number)
        form = CommentForm
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid:
                comment = form.save(commit=False)
                comment.user = request.user
                comment.chapter = obj
                comment.comic = obj.comic
                comment.save()
                form = CommentForm
        context = {
            "items": comics,
            "object": obj,
            "comments": comments,
            "form": form,
            "chapters": chapters,
            "object_list": page_obj,
        }
    except:  # noqa: E722
        obj = None
    if obj is None:
        return HttpResponse("Not found.")
    return render(request, "partials/chapter/detail.html", context)


@require_http_methods(["GET"])
@user_only
def chapter_detail_view(
    request: HtmxHttpRequest,
    slug=None,
) -> HttpResponse:
    hx_url = reverse("chapters:hx_chapter_detail", kwargs={"slug": slug})

    context = {"hx_url": hx_url}
    return render(request, "chapters/detail.html", context)


@user_only
@admin_only
@require_http_methods(["GET", "POST"])
def chapter_create_view(
    request: HtmxHttpRequest,
) -> HttpResponse:
    form = ChapterForm(request.POST or None)
    context = {
        "form": form,
    }
    htmx_template_name = "partials/chapters/create.html"
    template_name = "chapters/add_chapter.html"
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        obj.numpages = obj.get_chapter_images_children().count()
        obj.save()
        success_url = obj.get_edit_url()
        if request.htmx:
            headers = {"HX-Redirect": success_url}
            return HttpResponse("Created", headers=headers)
        return redirect(success_url)
    if request.htmx:
        htmx_template_name += "#form-section"
        return render(request, htmx_template_name, context)
    return render(request, template_name, context)


@user_only
@admin_only
@require_http_methods(["GET", "POST"])
def chapter_update_view(
    request: HtmxHttpRequest,
    slug=None,
) -> HttpResponse:
    obj = get_object_or_404(Chapter, slug=slug)
    form = ChapterForm(request.POST or None, instance=obj)
    htmx_template_name = "partials/chapters/update.html"
    template_name = "chapters/update_chapter.html"
    new_chapter_image_url = reverse(
        "chapters:hx_image_create",
        kwargs={"parent_slug": obj.slug},
    )
    context = {
        "form": form,
        "object": obj,
        "new_chapter_image_url": new_chapter_image_url,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.numpages = obj.get_chapter_images_children().count()
        obj.save()
        success_url = obj.get_edit_url()
        if request.htmx:
            headers = {"HX-Redirect": success_url}
            return HttpResponse("Created", headers=headers)
        return redirect(success_url)
    if request.htmx:
        htmx_template_name += "#form-section"
        return render(request, htmx_template_name, context)
    return render(request, template_name, context)


@user_only
@admin_only
@require_http_methods(["GET", "DELETE"])
def chapter_delete_view(
    request: HtmxHttpRequest,
    slug=None,
) -> HttpResponse:
    try:
        obj = (
            Chapter.objects.prefetch_related("chapteritems")
            .select_related("comic")
            .get(slug=slug)
        )
    except:  # noqa: E722
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "DELETE":
        obj.delete()
        success_url = reverse("chapters:chapter_list")
        if request.htmx:
            response = HttpResponse("")
            return trigger_client_event(
                response,
                "chapter-deleted",
            )
        return redirect(success_url)
    context = {"object": obj}
    return render(request, "chapters/delete.html", context)


@user_only
@admin_only
@require_http_methods(["GET", "POST"])
def chapter_images_update_hx_view(
    request: HtmxHttpRequest,
    parent_slug=None,
    id=None,  # noqa: A002
) -> HttpResponse:
    if not request.htmx:
        raise Http404
    try:
        parent_obj = (
            Chapter.objects.prefetch_related("chapteritems")
            .select_related("comic")
            .get(slug=parent_slug)
        )
    except:  # noqa: E722
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not found.")
    instance = None
    if id is not None:
        try:
            instance = ChapterImage.objects.select_related("comic", "chapter").get(
                chapter=parent_obj,
                id=id,
            )
        except:  # noqa: E722
            instance = None
    form = ChapterImageForm(
        request.POST or None,
        request.FILES or None,
        instance=instance,
    )
    url = reverse("chapters:hx_image_create", kwargs={"parent_slug": parent_obj.slug})
    chapter_url = parent_obj.get_edit_url()
    if instance:
        url = instance.get_hx_edit_url()
    context = {"url": url, "chapter_url": chapter_url, "object": instance, "form": form}
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.chapter = parent_obj
        new_obj.comic = parent_obj.comic
        new_obj.save()
        context["object"] = new_obj
        return render(request, "partials/chapters/images-inline.html", context)

    return render(request, "partials/chapters/images-inline-form.html", context)


@user_only
@admin_only
@require_http_methods(["GET", "DELETE"])
def chapter_images_delete_view(
    request: HtmxHttpRequest,
    parent_slug=None,
    id=None,  # noqa: A002
) -> HttpResponse:
    try:
        obj = ChapterImage.objects.select_related("comic", "chapter").get(
            chapter__slug=parent_slug,
            id=id,
        )
    except:  # noqa: E722
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "DELETE":
        obj.delete()
        success_url = reverse("chapters:update_chapter", kwargs={"slug": parent_slug})
        if request.htmx:
            response = HttpResponse("")
            return trigger_client_event(
                response,
                "chapter-image-deleted",
            )
        return redirect(success_url)
    context = {"object": obj}
    return render(request, "chapters/delete.html", context)
