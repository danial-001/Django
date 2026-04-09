from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def user_fees(req):
    return HttpResponse('<h1>This is Fees Page</h1>')
