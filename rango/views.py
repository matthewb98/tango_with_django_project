from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#each function in views.py is a view
def index(request):
    return HttpResponse("Rango says hey there partner!")
