from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#each function in views.py is a view
def index(request):
    return HttpResponse("Rango says hey there partner!"+
    '<a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse("Rango says here is an about page." +
    '<a href="/rango/">Return</a>')
