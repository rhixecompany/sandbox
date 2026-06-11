from django.urls import path

from api.libary.views import comic_image_views as views

app_name = "comicimages"

urlpatterns = [
    path(
        "",
        view=views.comic_image_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.comic_image_detail,
        name="detail",
    ),
]
