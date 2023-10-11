from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.
def index(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "onlykiwis/html/index.html", context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/html/post.html", {"post": post})


def index_hxml(request):
    context = {"posts": Post.objects.order_by("-date")}
    return render(request, "onlykiwis/hxml/index.xml", context)

def post_hxml(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "onlykiwis/hxml/post.xml", {"post": post})
