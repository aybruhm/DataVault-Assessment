from django.urls import path
from posts import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("single-post/", views.single_post_page, name="single_post"),
    path("create-post/", views.create_post_page, name="create-post")
]
