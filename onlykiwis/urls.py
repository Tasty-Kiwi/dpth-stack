from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>", views.post, name="post"),
    path("profile/<str:username>", views.profile, name="profile"),

    path("hxml", views.index_hxml, name="index_hxml"),
    path("hxml/post/<int:post_id>", views.post_hxml, name="post_hxml"),
    path("hxml/profile/<str:username>", views.profile_hxml, name="profile_hxml"),
]

