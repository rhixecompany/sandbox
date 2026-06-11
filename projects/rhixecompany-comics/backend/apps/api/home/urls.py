from django.urls import path

from api.home import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("series/", view=views.comics, name="series"),
    path(
        "digital/",
        view=views.digital,
        name="digital",
    ),
    path(
        "privacy/",
        view=views.privacy,
        name="privacy",
    ),
    path(
        "terms/",
        view=views.terms,
        name="terms",
    ),
]
