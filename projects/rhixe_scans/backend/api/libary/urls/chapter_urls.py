from django.urls import path

from api.libary.views import chapter_views as views

app_name = "chapters"

urlpatterns = [
    path(
        "",
        view=views.chapter_list,
        name="list",
    ),
    path(
        "<str:slug>/",
        view=views.chapter_detail,
        name="detail",
    ),
]
