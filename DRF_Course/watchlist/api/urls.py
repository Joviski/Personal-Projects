from django.urls import path, include

from watchlist.api.views import *

urlpatterns=[
    path('list/', WatchingList.as_view(), name='movie-list'),
    path('detail/<int:pk>/', WatchDetail.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformView.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamDetail.as_view(), name='stream'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),


]