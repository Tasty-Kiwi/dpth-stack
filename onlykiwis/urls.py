from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.log_in, name="login"),
    path("post", views.post_, name="post"),
    path("post/<int:post_id>", views.post, name="post"),
    path("@<str:username>", views.profile, name="profile"),
    path("hxml", views.index_hxml, name="index_hxml"),
    path("hxml/login", views.login_hxml, name="login_hxml"),
    path("hxml/post/<int:post_id>", views.post_hxml, name="post_hxml"),
    path("hxml/@<str:username>", views.profile_hxml, name="profile_hxml"),
]
