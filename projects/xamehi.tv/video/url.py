<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<slug:slug>/', views.movie, name='movie'),
    path('send_email/', views.sendEmail, name="send_email"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.userAccount, name="account"),
    path('update_profile/', views.updateProfile, name="update_profile"),
    # CRUD PATHS
    path('create_movie/', views.createMovie, name="create_movie"),
    path('update_movie/<slug:slug>/', views.updateMovie, name="update_movie"),
    path('delete_movie/<slug:slug>/', views.deleteMovie, name="delete_movie"),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<slug:slug>/', views.movie, name='movie'),
    path('send_email/', views.sendEmail, name="send_email"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.userAccount, name="account"),
    path('update_profile/', views.updateProfile, name="update_profile"),
    # CRUD PATHS
    path('create_movie/', views.createMovie, name="create_movie"),
    path('update_movie/<slug:slug>/', views.updateMovie, name="update_movie"),
    path('delete_movie/<slug:slug>/', views.deleteMovie, name="delete_movie"),
]
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
