from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginfunc, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("users/<int:pk>/", views.users_detail, name="users_detail"),
    path("posts/new/", views.posts_new, name="posts_new"),
    path("posts/<int:pk>/", views.posts_detail, name="posts_detail"),
    path("posts/<int:pk>/delete/", views.posts_delete, name="posts_delete"),
]
