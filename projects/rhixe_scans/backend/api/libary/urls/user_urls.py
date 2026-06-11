from django.urls import path

from api.libary.views import user_views as views

app_name = "users"

urlpatterns = [
    path(
        "",
        view=views.user_list,
        name="list",
    ),
    path(
        "<int:id>/",
        view=views.user_detail,
        name="detail",
    ),
    path(
        "login/",
        view=views.user_obtain_token,
        name="login",
    ),
    path("register/", views.registeruser, name="register"),
]
