from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User

from celery import shared_task

@shared_task
def add(x,y):
    return x + y

@shared_task
def create_user(username:str):
    us= User.objects.create(username=username)
    us.save()
    return f'User {username} Added to UserDB!'

