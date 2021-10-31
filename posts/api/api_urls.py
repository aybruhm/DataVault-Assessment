from django.urls import path
from posts.api.api_views import PostList
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/', csrf_exempt(PostList.as_view()), name="api_lists"),
]
