from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def learnDjango(request):
    return HttpResponse('Hello Django')

def learnTagsHTML(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learnMaths(request):
    sum=10+20+30+40
    return HttpResponse(sum)

def learnTagsInVariable(request):
    tag='<h1>Hello Django</h1>'
    return HttpResponse(tag)