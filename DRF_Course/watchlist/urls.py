from django.urls import path, include

from watchlist.views import *

urlpatterns=[
    path('list/', movie_list, name='movie-list'),
    path('detail/<int:pk>', movie_details, name='movie-details'),
]