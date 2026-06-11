import uuid
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import ImageField
from django.db.models import UUIDField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


def user_image_location(instance, filename):
    return "{}/{}".format(
        str(instance.email)
        .replace(" ", "_")
        .replace(":", " ")
        .replace("/", "")
        .replace("\\", ""),
        filename,
    )


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


class User(AbstractUser):
    """
    Default custom user model for Rhixescans.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = CharField(_("Full Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name of User"), blank=True, max_length=255)
    last_name = CharField(_("Last Name of User"), blank=True, max_length=255)
    image = ImageField(
        _("Image"),
        upload_to=user_image_location,
        validators=[
            ext_validator,
        ],
        blank=True,
        null=True,
    )
    email = EmailField(_("email address"), unique=True)
    username = CharField(_("User Name of User"), blank=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.pk})

    def get_comics(self):
        return self.usercomics.all()  # type: ignore  # noqa: PGH003
