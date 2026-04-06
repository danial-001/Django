from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def introduction(request):
    return HttpResponse('<h1> Course Introduction Page</h1>')
