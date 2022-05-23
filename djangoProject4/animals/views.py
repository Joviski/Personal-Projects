from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from .models import *
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

class AnimalView(View):
    def get(self, request,r):
        query= get_object_or_404(Animal,name=r)
        context={
            "name":query.name,
            "species":query.species.name,
            "last_feed_time":query.last_feed_time
        }
        return JsonResponse({"context":context})


    @csrf_exempt
    def post(self, request):

        x= Animal.objects.create(name=request.POST['name'],
                              species=request.POST['species'],
                              last_feed_time=timezone.now()
                              )
        return JsonResponse({"x":x})
# Create your views here.
class AnimalhungerView(View):
    def get(self, request):
        query= Animal.objects.all()
        count=0
        for i in query:
            if timezone.now().day - i.last_feed_time.day >= 2:
                count+=1
        return HttpResponse(count)
