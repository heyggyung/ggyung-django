from django.db import models
from django.conf import settings 
# from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=20)
    is_publish = models.BooleanField (default=False)

    def __str__(self):
        return self.title
# class Article(models.Model):
#     pass

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
