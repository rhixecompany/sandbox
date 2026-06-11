from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render


def user_function(user):
    # Custom test logic here
    return user.is_active and user.is_authenticated


def admin_function(user):
    # Custom test logic here
    return user.is_authenticated and user.is_superuser


class MessageMixin:
    """
    Make it easy to display notification messages when using Class Based Views.
    """

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)  # type: ignore  # noqa: PGH003
        return super().delete(request, *args, **kwargs)  # type: ignore  # noqa: PGH003

    def form_valid(self, form):
        messages.success(self.request, self.success_message)  # type: ignore  # noqa: PGH003
        return super().form_valid(form)  # type: ignore  # noqa: PGH003


class LoginMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)  # type: ignore  # noqa: PGH003


class AdminLoginMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)  # type: ignore  # noqa: PGH003


def user_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return view_func(request, *args, **kwargs)
        messages.error(request, "You are not authorized to view this page")
        return render(
            request,
            "error.html",
        )

    return wrapper_function


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            return view_func(request, *args, **kwargs)
        messages.error(request, "You are not authorized to view this page")
        return render(
            request,
            "error.html",
        )

    return wrapper_function
