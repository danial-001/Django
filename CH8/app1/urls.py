from django.urls import path
from django.contrib import admin
from app1.views import home, learn_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dj/', learn_django,{'status':'OK'}, name='learn_django'),
    path('dj2/',learn_django),
]