from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts_images/", null=True, blank=True)
    content = RichTextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title