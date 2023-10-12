from django.shortcuts import render, redirect, get_object_or_404
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate

from .models import User, Post


def index(request):
    posts = Post.objects.order_by("-date")
    return render(request, "onlykiwis/html/index.html", {"posts": posts})

def login(request):
    if request.method == "GET":
        context = {}
        return render(request, "onlykiwis/html/login.html", context)
    
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        return redirect(f"@{user.get_username()}")

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/html/post.html", {"post": post})


def profile(request, username):
    profile = get_object_or_404(User, pk=username)
    return render(request, "onlykiwis/html/profile.html", {"profile": profile})


def index_hxml(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "onlykiwis/hxml/index.xml", context)

def login_hxml(request):
    csrf_token = get_token(request)
    context = {"csrf_token": csrf_token}
    return render(request, "onlykiwis/hxml/login.xml", context)


def post_hxml(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/hxml/post.xml", {"post": post})


def profile_hxml(request, username):
    profile = get_object_or_404(User, pk=username)
    return render(request, "onlykiwis/hxml/profile.xml", {"profile": profile})
