from django.shortcuts import render, get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from watchlist.models import *
from .serializers import *
from .permissions import *


# Create your views here.

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        watchlist= get_object_or_404(WatchList,pk=pk)

        review_user= self.request.user
        if Review.objects.filter(watchlist=watchlist, review_user=review_user).exists():
            raise ValidationError("You have already reviewed this movie!")

        serializer.save(watchlist=watchlist)


class ReviewList(generics.ListAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk= self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]



class StreamPlatformView(APIView):

    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamDetail(APIView):
    def get(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self,request, pk):
        platform= get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(data=request.data, instance=platform)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class WatchingList(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchDetail(APIView):

    def get(self, request, pk):
        watchlist = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)

    def delete(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)
        movie.delete()
        return Response(
            {
                "Message": "Instance Deleted Successfully"
            },
            status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        movie = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(data=request.data, instance=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




# @api_view(['GET','POST'])
# def movie_list(request):
#     movies = Movie.objects.all()
#     if request.method == 'GET':
#         serializer= MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer= MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#
#     if request.method == 'GET':
#         serializer= MovieSerializer(movie)
#         return Response(serializer.data)
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(
#             {
#                 "Message": "Instance Deleted Successfully"
#              },
#             status=status.HTTP_204_NO_CONTENT)
#
#     elif request.method == 'PUT':
#         serializer= MovieSerializer(data=request.data, instance=movie)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
