from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return HttpResponse(f'<h1>This is a App 2 Page</h1>')