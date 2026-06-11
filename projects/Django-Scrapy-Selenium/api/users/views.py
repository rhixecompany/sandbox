from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django_htmx.middleware import HtmxDetails

from api.apps.filters import UserFilter
from api.users.decorators import admin_only
from api.users.decorators import user_only
from api.users.forms import UserChangeForm
from api.users.forms import UserCreationForm
from api.users.models import User


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@user_only
@admin_only
@require_http_methods(["GET"])
def user_list_view(
    request: HtmxHttpRequest,
) -> HttpResponse:
    qs = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=qs)
    paginator = Paginator(user_filter.qs, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    htmx_template_name = "partials/users/container.html"
    template_name = "users/user_list.html"
    context = {"filter": user_filter, "object_list": page_obj}
    if request.htmx:
        htmx_template_name += "#container-section"
        return render(request, htmx_template_name, context)
    return render(request, template_name, context)


@require_http_methods(["GET"])
def user_detail_hx_view(
    request: HtmxHttpRequest,
    pk=None,
) -> HttpResponse:
    if not request.htmx:
        raise Http404
    try:
        obj = get_object_or_404(User, pk=pk)
    except:  # noqa: E722
        obj = None
    if obj is None:
        return HttpResponse("Not found.")
    comments = obj.get_user_comments_children()
    paginator = Paginator(comments, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    context = {"object": obj, "object_list": page_obj}
    return render(request, "partials/user/detail.html", context)


@require_http_methods(["GET"])
def user_detail_view(request: HtmxHttpRequest, pk=None) -> HttpResponse:
    hx_url = reverse("users:hx_user_detail", kwargs={"pk": pk})

    context = {"hx_url": hx_url}
    return render(request, "users/detail.html", context)


@user_only
@admin_only
@require_http_methods(["GET", "POST"])
def user_create_view(
    request: HtmxHttpRequest,
) -> HttpResponse:
    form = UserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    htmx_template_name = "partials/users/create.html"
    template_name = "users/add_user.html"
    if form.is_valid():
        obj = form.save(commit=False)

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
def user_delete_view(request: HtmxHttpRequest, pk=None) -> HttpResponse:
    try:
        obj = User.objects.get(pk=pk)
    except:  # noqa: E722
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        success_url = reverse("users:user_list")
        if request.htmx:
            headers = {"HX-Redirect": success_url}
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
    context = {"object": obj}
    return render(request, "users/delete.html", context)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_edit_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user

    def get_template_names(self):
        htmx_template_name = "partials/users/update.html"
        template_name = "users/update_user.html"
        if self.request.htmx:
            htmx_template_name += "#form-section"
            return htmx_template_name
        return template_name


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail_user", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()
