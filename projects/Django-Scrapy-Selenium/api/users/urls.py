from django.urls import path

from api.users import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=views.user_redirect_view, name="redirect_user"),
    path("~update/", view=views.user_update_view, name="update_user"),
    path("<int:pk>/", view=views.user_detail_view, name="detail_user"),
    path(
        "",
        view=views.user_list_view,
        name="user_list",
    ),
    path(
        "add/",
        view=views.user_create_view,
        name="add_user",
    ),
    path(
        "hx/<int:pk>/",
        view=views.user_detail_hx_view,
        name="hx_user_detail",
    ),
    path(
        "<int:pk>/delete/",
        view=views.user_delete_view,
        name="delete_user",
    ),
]
