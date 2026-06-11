from django.urls import path

from api.libary.views import category_views as views

app_name = "categorys"


urlpatterns = [
    path(
        "",
        view=views.category_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.category_detail,
        name="detail",
    ),
]
