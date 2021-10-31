from django.urls import path
from posts import views

app_name = "posts"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("single-post/<str:id>/", views.single_post_page, name="single_post"),
    path("create-post/", views.create_post_page, name="create_post"),

    # Auth URLs
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout")
]
