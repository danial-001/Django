from django.urls import path
from course.views import introduction

urlpatterns = [
    path('intro/',introduction),
]
