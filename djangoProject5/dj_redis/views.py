from django.shortcuts import HttpResponse
from django.core.cache import cache

from .models import *
# Create your views here.

def list(request,id):
    x:str
    if cache.get(id):
        test = cache.get(id)
        x= "Listed From Cache"
    else:
        test= Test.objects.get(id=id)
        cache.set(id, test)
        x= "Listed From DB"

    return HttpResponse(f'{test.id} --> {test.name}: {x}')


