from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(req):
    # return HttpResponse('<h1>This is Learn Django Page</h1>')
    courseDetails={'courseName': 'Django 5.1'}
    return render(req, 'course/django.html',context=courseDetails)

# we can directly pass the dictionary in context as below

