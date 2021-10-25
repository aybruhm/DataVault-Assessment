from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def home_page(request: HttpResponse) -> HttpResponse:
    context = {

    }
    return render(request, "posts/index.html", context)


def single_post_page(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request, "posts/single-post.html", context)


def create_post_page(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request, "posts/create-post.html", context)