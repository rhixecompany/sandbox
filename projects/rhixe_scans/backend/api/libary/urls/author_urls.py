from django.urls import path

from api.libary.views import author_views as views

app_name = "authors"


urlpatterns = [
    path(
        "",
        view=views.author_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.author_detail,
        name="detail",
    ),
]
