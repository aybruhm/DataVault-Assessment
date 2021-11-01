from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer
from braces.views import CsrfExemptMixin
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from .authentication import CsrfExemptSessionAuthentication


class PostView(CsrfExemptMixin, APIView):
    """
    List all posts, or create a new post.
    """
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (
        AllowAny
    )

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            message = "You have successfully published your story!"
            return Response({"message": message, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
