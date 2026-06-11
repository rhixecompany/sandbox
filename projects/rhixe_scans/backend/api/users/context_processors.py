from django.conf import settings
from django.db.models import Q

from api.users.models import User


def allauth_settings(request):
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }


def avatar(request):
    if request.user.is_authenticated:
        user = User.objects.get(Q(email=request.user))

        avatar = User.objects.filter(Q(email=user))

        return {
            "avatar": avatar,  # type: ignore  # noqa: PGH003
        }
    return {"NotLoggedIn": User.objects.none()}  # type: ignore  # noqa: PGH003
