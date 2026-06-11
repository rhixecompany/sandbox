from django.urls import path

from api.home import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("series/", view=views.series, name="series"),
    path("bookmarks/", view=views.bookmarks, name="bookmarks"),
    path("privacy/", view=views.privacy, name="privacy-policy"),
    path("dmca/", view=views.dmca, name="dmca"),
    path("terms/", view=views.terms, name="terms-of-service"),
]
