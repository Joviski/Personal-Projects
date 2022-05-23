from django.shortcuts import render
from .models import *
from .Serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

def home(request):
    obj = Currency.objects.all()

    context = {
        'obj': obj
    }

    return render(request,'home.html',context)

@api_view(['POST',])
def LabsCreateView(request):
    if(request.method == 'POST'):
        serializer=LabSerializers(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def EquipmentCreateView(request):
    if (request.method == 'POST'):
        serializer = Equipserializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentListCreate(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = Equipserializers
    search_fields = ['name','id','brand']

class EquipmentControl(RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = Equipserializers
    lookup_field = 'id'
