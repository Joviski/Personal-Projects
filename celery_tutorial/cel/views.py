from django.shortcuts import HttpResponse
from .models import *

# Create your views here.

def list(request):
    return HttpResponse('Task Print')
