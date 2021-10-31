from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import Post
from .forms import User, UserCreateForm

URL = "http://127.0.0.1:8000"


def home_page(request: HttpResponse) -> HttpResponse:

    context = {
        "url": URL
    }
    return render(request, "posts/index.html", context)


def single_post_page(request: HttpRequest, id) -> HttpResponse:
    post = Post.objects.get(id=id)

    context = {
        "post": post,
        "url": URL
    }
    return render(request, "posts/single-post.html", context)


@login_required
def create_post_page(request: HttpRequest) -> HttpResponse:
    # messages.success(
    #     request,
    #     'You have successfully published your story! \
    #             Our Editorial Team are looking into it.'
    # )
    context = {
        "url": URL
    }
    return render(request, "posts/create-post.html", context)


def register_user(request: HttpRequest) -> HttpResponse:
    form = UserCreateForm()

    if request.method == "POST":
        form = UserCreateForm(request.POST)

        print(form.is_valid)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("posts:login")

    context = {"form": form}
    return render(request, "auth/register.html", context)


def login_user(request: HttpRequest) -> HttpResponse:
    username = request.POST.get("username")
    password = request.POST.get("password")

    if request.method == "POST":

        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            messages.success(
                request, f"Welcome {username}, you are logged in.")
            return redirect('posts:home_page')

    context = {}
    return render(request, "auth/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('posts:home_page')
