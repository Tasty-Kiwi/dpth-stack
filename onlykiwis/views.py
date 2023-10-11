from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import *


# Create your views here.
def index(request):
    posts = Post.objects.order_by("-date")
    return render(request, "onlykiwis/html/index.html", {"posts": posts})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/html/post.html", {"post": post})


def profile(request, username):
    user = get_object_or_404(User, pk=username)
    return render(request, "onlykiwis/html/profile.html", {"user": user})


def index_hxml(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "onlykiwis/hxml/index.xml", context)


def post_hxml(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/hxml/post.xml", {"post": post})


def profile_hxml(request, username):
    user = get_object_or_404(User, pk=username)
    return render(request, "onlykiwis/hxml/profile.xml", {"user": user})
