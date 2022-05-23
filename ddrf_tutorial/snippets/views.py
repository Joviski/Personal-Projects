from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer, UserTokenSerializer
from rest_framework import mixins, generics, renderers
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.decorators import permission_classes, throttle_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.throttling import UserRateThrottle
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
@throttle_classes((UserRateThrottle,))
def snippet_list(request, format= None):
    if request.method == 'GET':
        paginator= PageNumberPagination()
        paginator.page_size= 2
        snippets = Snippet.objects.filter(owner=request.user)

        if snippets.count() == 0:
            return Response({'message':'You have no snippets.'})

        pagesnippets = paginator.paginate_queryset(snippets,request)
        serializer = SnippetSerializer(pagesnippets, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated,IsOwnerOrReadOnly,])
def snippet_detail(request,pk, format=None):
    snippet = get_object_or_404(Snippet,id=pk)

    if snippet.owner != request.user:
        return Response({'message': "You are not the owner of this snippet."})

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snip_delete= snippet.delete()
        data={}
        if snip_delete:
            data["message"] = f'Snippet {pk} with title {snippet.title} deleted successfully.'
        else:
            data["message"] = f'Delete failed for Snippet {pk}.'
        return Response(data= data, status=status.HTTP_204_NO_CONTENT)



####################################################################
# Class Based Views
# class SnippetList(APIView):
#     def get(self,request, format = None):
#          snippets=Snippet.objects.all()
#          serializer= SnippetSerializer(snippets, many=True)
#          return Response(serializer.data)
#
#     def post(self, request, format = None):
#         serializer= SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class SnippetDetail(APIView):
#     def get(self, request, pk,  format=None):
#         snippet = get_object_or_404(Snippet, id=pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = get_object_or_404(Snippet, id=pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk, format= None):
#         snippet = get_object_or_404(Snippet, id=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

###########################################################
# Using Mixins
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,*args,**kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#################################################################
# Using Generic Views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination
    throttle_classes = [UserRateThrottle,]
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields={'title','owner__username'}

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User
    serializer_class = UserSerializer

#Relationships and hyperlinked APIs
@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
