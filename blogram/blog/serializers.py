from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True,read_only=True)
    class Meta:
        model = Comment
        fields= ['comment','image','uploader','uploaded_dt','updated_dt','likes','posts']
