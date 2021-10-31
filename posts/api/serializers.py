from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "author", "image", "content", "date_created"]


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.IntegerField()
    image = serializers.ImageField()
    content = serializers.CharField(max_length=200)
