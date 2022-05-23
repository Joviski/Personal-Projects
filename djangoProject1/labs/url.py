from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('',home ,name='home'),
    path('labs/create/',LabsCreateView,name='Labs_Create'),
    path('equipment/create/',EquipmentCreateView,name='Equipment_Create'),
    path('equipment/listcreate/',EquipmentListCreate.as_view(),name='Equipment_list_Create'),
    path('equipment/control/<int:id>/',EquipmentControl.as_view(),name='Equipment_Control'),
]