from django.urls import resolve
from django.urls import reverse

from api.users.models import User


def test_detail(user: User):
    assert reverse("users:detail_user", kwargs={"pk": user.pk}) == f"/users/{user.pk}/"
    assert resolve(f"/users/{user.pk}/").view_name == "users:detail_user"


def test_update():
    assert reverse("users:update_user") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:update_user"


def test_redirect():
    assert reverse("users:redirect_user") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect_user"
