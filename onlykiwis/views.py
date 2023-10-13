from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Comment, User, Post


def index(request):
    posts = Post.objects.order_by("-date")
    return render(request, "onlykiwis/html/index.html", {"posts": posts})


def log_in(request):
    if request.method == "GET":
        context = {}
        return render(request, "onlykiwis/html/login.html", context)

    user = authenticate(
        request, username=request.POST["username"], password=request.POST["password"]
    )
    if user is None:
        return render(
            request,
            "onlykiwis/html/login.html",
            {"error": "Wrong username/password, try again."},
        )

    login(request, user)
    if request.GET.get("next") is not None:
        return redirect(request.GET["next"])

    return redirect("profile", user.username)


def post(request, post_id):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=post_id)
        return render(request, "onlykiwis/html/post.html", {"post": post})

    params = request.POST
    if params["content"] is not None:
        if request.user.is_authenticated:
            new_comment = Comment(
                author=request.user, content=params["content"], date=timezone.now()
            )

            new_comment.save()
            post = get_object_or_404(Post, pk=post_id)
            post.comments.add(new_comment)
            return redirect("post", post_id)

        return redirect("login")

    return render(
        request, "onlykiwis/html/post.html", {"post": post, "error": "Missing Content."}
    )


def post_(request):
    params = request.POST
    if params["title"] is not None and params["subtitle"] is not None:
        if request.user.is_authenticated:
            new_post = Post(
                author=request.user,
                title=params["title"],
                subtitle=params["subtitle"],
                date=timezone.now(),
                content=[""],
            )

            new_post.save()
            return redirect("index")

        return redirect("login")

    return render(
        request, "onlykiwis/html/login.html", {"error": "Missing Title or Subtitle."}
    )


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
