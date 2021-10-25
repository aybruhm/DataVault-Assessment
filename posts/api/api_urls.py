from django.urls import path
from posts.api.api_views import PostList

urlpatterns = [
    path('api/', PostList.as_view(), name="api_lists"),
]
