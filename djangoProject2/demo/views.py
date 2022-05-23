from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def post_list(request):
    posts = Post.objects.all()