from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def learn_django(request, **kwargs):
    status = kwargs.get('status','N/A')
    print(status)
    return HttpResponse(f'<h1>This is a Learn Django Page {status}</h1>')

