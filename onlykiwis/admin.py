from django import forms
from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["_username", "display_name", "bio", "date"]
    list_filter = ["date"]
    sortable_by = ["date"]

    @admin.display(description="Username/ID")
    def _username(self, obj):
        return f"@{obj.username}"


@admin.display(description="Author username")
def author_username(obj):
    return f"@{obj.author.username}"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", author_username, "title", "subtitle", "date", "likes"]
    list_filter = ["date"]
    sortable_by = ["date", "likes"]


class OriginPost(forms.ModelChoiceField):
    def label_from_instance(self, member):
        return "%s" % member


class CommentForm(forms.ModelForm):
    fields = ["author", "content", "date", "likes", "origin"]

    origin = OriginPost(queryset=Post.objects.all(), widget=forms.Select)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", author_username, "content", "date", "likes"]
    list_filter = ["date"]
    sortable_by = ["date", "likes"]
    form = CommentForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        Post.objects.get(pk=form["origin"].value()).comments.add(obj)
