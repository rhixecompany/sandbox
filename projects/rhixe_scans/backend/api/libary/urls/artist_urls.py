from django.urls import path

from api.libary.views import artist_views as views

app_name = "artists"


urlpatterns = [
    path(
        "",
        view=views.artist_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.artist_detail,
        name="detail",
    ),
]
