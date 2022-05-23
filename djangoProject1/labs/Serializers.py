from rest_framework import serializers
from .models import *

class LabSerializers(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['name','lab_ID','lab_deadline']

class Equipserializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields= '__all__'