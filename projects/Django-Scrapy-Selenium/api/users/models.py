from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import CharField
from django.db.models import ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image


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
    Default custom user model for My Banking Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
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

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 100 or img.width > 100:  # noqa: PLR2004
                print(f"saving {self.image.path}")  # noqa: T201
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def get_absolute_url(self) -> str:
        return reverse("users:detail_user", kwargs={"pk": self.pk})

    def get_edit_url(self) -> str:
        return reverse("users:update_user")

    def get_hx_url(self) -> str:
        return reverse("users:hx_user_detail", kwargs={"pk": self.pk})

    def get_delete_url(self) -> str:
        return reverse("users:delete_user", kwargs={"pk": self.pk})

    def get_user_comics_children(self):
        return self.comicuser.all()

    def get_user_comments_children(self):
        return self.usercomments.all()
