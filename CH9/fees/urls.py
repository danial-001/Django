from django.urls import path, include
from fees.views import user_fees

urlpatterns = [
    path('fee/', user_fees),
]