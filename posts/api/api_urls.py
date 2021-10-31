from django.urls import path
from posts.api.api_views import PostView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/', csrf_exempt(PostView.as_view()), name="api_lists"),
]
