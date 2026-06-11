from django.conf import settings
from django.db.models import Q
from django.http import HttpRequest

from api.apps.models import UserItem
from api.users.models import User


def allauth_settings(request: HttpRequest) -> dict[str, str]:
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }


def avatar(request: HttpRequest) -> dict[str, str]:
    if request.user.is_authenticated:
        user = User.objects.get(Q(email=request.user))

        avatar = User.objects.filter(Q(email=user))

        return {
            "avatar": avatar,
        }
    return {"NotLoggedIn": User.objects.none()}


def load(request: HttpRequest) -> dict[str, str]:
    if request.user.is_authenticated:
        queryset = UserItem.objects.prefetch_related("comic").all()

        return {
            "items": queryset,
        }

    return {"NotLoggedIn": User.objects.none()}
