from django.http import HttpResponse
import random

def index(request):
    return HttpResponse('index')
