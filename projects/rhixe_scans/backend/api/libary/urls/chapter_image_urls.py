from django.urls import path

from api.libary.views import chapter_image_views as views

app_name = "chapterimages"


urlpatterns = [
    path(
        "",
        view=views.chapter_image_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.chapter_image_detail,
        name="detail",
    ),
]
