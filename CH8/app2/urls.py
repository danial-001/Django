from django.urls import path
from django.contrib import admin
from app2.views import app2

urlpatterns = [
    path('app2/',app2)
]