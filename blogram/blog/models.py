from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    image = models.ImageField()
    uploader = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    uploaded_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    uploaded_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Comment Posted"
