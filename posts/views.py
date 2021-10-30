from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post


def home_page(request: HttpResponse) -> HttpResponse:
    context = {

    }
    return render(request, "posts/index.html", context)


def single_post_page(request: HttpRequest, id) -> HttpResponse:
    post = Post.objects.get(id=id)

    context = {
        "post": post
    }
    return render(request, "posts/single-post.html", context)


def create_post_page(request: HttpRequest) -> HttpResponse:
    return render(request, "posts/create-post.html")


def register_user(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "auth/register.html", context)


def login_user(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "auth/login.html", context)
