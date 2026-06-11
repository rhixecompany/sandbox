"""User model and profile."""
from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name of User"), blank=True, max_length=255)
    last_name = CharField(_("Last Name of User"), blank=True, max_length=255)
    image = ImageField(_("Image"), upload_to="users/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("api:user-detail", kwargs={"pk": self.pk})
