from django.urls import path

from api.libary.views import genre_views as views

app_name = "genres"


urlpatterns = [
    path(
        "",
        view=views.genre_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.genre_detail,
        name="detail",
    ),
]
